# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE CATALOG flight;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA flight.gold;
# MAGIC CREATE SCHEMA flight.silver;
# MAGIC CREATE SCHEMA flight.bronze;
# MAGIC CREATE SCHEMA flight.rawdata;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME flight.rawdata.airports;
# MAGIC CREATE VOLUME flight.rawdata.bookings;
# MAGIC CREATE VOLUME flight.rawdata.customers;
# MAGIC CREATE VOLUME flight.rawdata.flights;

# COMMAND ----------

# MAGIC %md
# MAGIC After creating volume upload the .csv files

# COMMAND ----------

# MAGIC %md
# MAGIC After that creating one volume in each layer schemas

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME flight.gold.goldVolume;
# MAGIC CREATE VOLUME flight.silver.silverVolume;
# MAGIC CREATE VOLUME flight.bronze.bronzeVolume;

# COMMAND ----------

