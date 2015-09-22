from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from decimal import Decimal
from datetime import datetime, date
from pyspark.sql import StructType, StructField, ByteType, ShortType, IntegerType, LongType, FloatType, DoubleType, DecimalType, StringType, BooleanType, TimestampType, DateType, ArrayType, MapType, StructType

conf = SparkConf().setAppName("spark_sql_datatype")

sc = SparkContext(conf=conf)

hc = HiveContext(sc)

source = sc.parallelize([(int("127"), int("32767"), int("2147483647"), long(
    "9223372036854775807"), float("1.1"), float("2.2"), Decimal("3.3"), "str", bool(0), datetime(2015, 9, 22, 9, 39, 45), date(2015, 9, 22), [1, 2, 3], {"key": "value"}, [1, 2.0, "3.0"])])

schema = StructType([StructField("byte", ByteType(), False), StructField("short", ShortType(), False), StructField(
    "int", IntegerType(), False), StructField("long", LongType(), False), StructField("float", FloatType(), False), StructField("double", DoubleType(), False), StructField("decimal", DecimalType(), False), StructField("string", StringType(), False), StructField("boolean", BooleanType(), False), StructField("timestamp", TimestampType(), False), StructField("date", DateType(), False), StructField("array", ArrayType(IntegerType()), False), StructField("map", MapType(StringType(), StringType(), False)), StructField("struct", StructType([StructField("first", IntegerType(), False), StructField("second", FloatType(), False), StructField("third", StringType(), False)]), False)])

table = hc.applySchema(source, schema)

table.registerAsTable("temp_table")

rows = hc.sql("select * from temp_table").collect()

sc.stop()

for row in rows:
    print row