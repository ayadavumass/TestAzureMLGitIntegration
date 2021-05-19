# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

import sys

print("Hello, world!")
print("Driver arguments = " + repr(sys.argv))
print("Python version = " + sys.version)

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HelloWorld").getOrCreate()
print("Spark version = " + spark.version)
spark.stop()
