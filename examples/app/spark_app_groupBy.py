from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("spark_app_groupBy")

sc = SparkContext(conf=conf)

datas = sc.parallelize([1, 2, 3, 4, 5]).groupBy(
    lambda val: val % 2 == 0).collect()

sc.stop()

print datas
