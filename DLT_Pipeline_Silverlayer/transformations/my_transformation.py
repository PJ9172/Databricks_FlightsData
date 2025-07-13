from pyspark.sql.functions import *
from pyspark.sql.types import *
import dlt

#booking data
@dlt.table (
    name  = "staging_booking"
)

def staging_booking():
    df = spark.readStream.format("delta")\
                .load("/Volumes/flight/bronze/bronzevolume/bookings/data/")
    return df

@dlt.view(
    name = "transform_booking"
)

def transform_booking():
    df = spark.readStream.table("staging_booking")
    df = df.withColumn("amount",col("amount").cast(DoubleType()))\
            .withColumn("modifiedDate",current_timestamp())\
            .withColumn("booking_date",col("booking_date").cast(DateType()))\
            .drop("_rescued_data")
    return df


rule = {
    "rule1" : "booking_id IS NOT NULL",
    "rule2" : "passenger_id IS NOT NULL"
}

@dlt.table (
    name = "silver_booking"
)
@dlt.expect_all_or_drop(rule)
def silver_booking():
    df = dlt.readStream("transform_booking")      #we can read the data this way also
    return df

##############################################################
#flight data

@dlt.view(
  name="trans_flight"
)
def trans_flight():
  df = spark.readStream.format("delta")\
            .load("/Volumes/flight/bronze/bronzevolume/flights/data/")  
  df = df.withColumn("flight_date",to_date(col("flight_date")))\
        .drop("_rescued_data")\
        .withColumn("modifiedDate",current_timestamp())
  return df

dlt.create_streaming_table("silver_flights")

dlt.create_auto_cdc_flow(
  target = "silver_flights",
  source = "trans_flight",
  keys = ["flight_id"],
  sequence_by = col("modifiedDate"),
  stored_as_scd_type = 1
)


################################################################
#customer data

@dlt.view(
  name="trans_customers"
)
def trans_customers():
  df = spark.readStream.format("delta")\
            .load("/Volumes/flight/bronze/bronzevolume/customers/data/")  
  df = df.drop("_rescued_data")\
        .withColumn("modifiedDate",current_timestamp())
  return df

dlt.create_streaming_table("silver_customers")

dlt.create_auto_cdc_flow(
  target = "silver_customers",
  source = "trans_customers",
  keys = ["passenger_id"],
  sequence_by = col("modifiedDate"),
  stored_as_scd_type = 1
)


#####################################################################
#airport data

@dlt.view(
  name="trans_airports"
)
def trans_airports():
  df = spark.readStream.format("delta")\
            .load("/Volumes/flight/bronze/bronzevolume/airports/data/")  
  df = df.drop("_rescued_data")\
        .withColumn("modifiedDate",current_timestamp())
  return df

dlt.create_streaming_table("silver_airports")

dlt.create_auto_cdc_flow(
  target = "silver_airports",
  source = "trans_airports",
  keys = ["airport_id"],
  sequence_by = col("modifiedDate"),
  stored_as_scd_type = 1
)

#####################################################################
# Silver Business View

@dlt.table(
  name = "silver_business_view"
)
def silver_business_view():
  df = dlt.readStream("silver_booking")\
          .join(dlt.readStream("silver_flights"),on="flight_id")\
          .join(dlt.readStream("silver_customers"),on="passenger_id")\
          .join(dlt.readStream("silver_airports"),on="airport_id")\
          .drop("modifiedDate")
  return df