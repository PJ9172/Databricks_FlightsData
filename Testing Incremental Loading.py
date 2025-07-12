# Databricks notebook source
# MAGIC %md
# MAGIC **INCREMENTAL DATA INJECTION (Testing)**

# COMMAND ----------

# MAGIC %md
# MAGIC creating readStream which read data from rawdata folder. (csv file)

# COMMAND ----------

df = spark.readStream.format("cloudfiles")\
        .option("cloudFiles.format", "csv")\
        .option("cloudFiles.schemaLocation", "/Volumes/flight/bronze/bronzevolume/bookings/checkpoint")\
        .option("cloudFiles.schemaEvolutionMode", "rescue")\
        .load("/Volumes/flight/rawdata/bookings/")

# COMMAND ----------

# MAGIC %md
# MAGIC loads data in bronzevolume 

# COMMAND ----------

df.writeStream.format("delta")\
        .outputMode("append")\
        .trigger(once=True)\
        .option("checkpointLocation", "/Volumes/flight/bronze/bronzevolume/bookings/checkpoint")\
        .option("path", "/Volumes/flight/bronze/bronzevolume/bookings/data/")\
        .start()

# COMMAND ----------

# MAGIC %md
# MAGIC reading the loaded data in delta formate

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from delta.`/Volumes/flight/bronze/bronzevolume/bookings/data`

# COMMAND ----------


# Now upload the another csv file in raw data for testing and re-run and check the difference in number of rows.

# COMMAND ----------

# MAGIC %md
# MAGIC Now we have to do this operation dynamically.
# MAGIC not for single booking.