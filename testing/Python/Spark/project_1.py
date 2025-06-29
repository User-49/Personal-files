from pyspark.sql import SparkSession
import os, sys

os.environ["PYSPARK_PYTHON"] =sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder.master("local[1]").appName("testApp").getOrCreate()
print(spark)

