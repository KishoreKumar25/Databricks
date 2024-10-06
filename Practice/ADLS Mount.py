# Databricks notebook source
# MAGIC %fs

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets'))

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

dbutils.help()

# COMMAND ----------

display(dbutils.fs.ls('/databricks-datasets'))

# COMMAND ----------


