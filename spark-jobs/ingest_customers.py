from pyspark.sql import SparkSession

spark = SparkSession.builder \
        .appName("ingest_customers") \
        .getOrCreate()

df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres-prod:5432/prod-postgre") \
    .option("dbtable", "customers") \
    .option("user", "adminproduser") \
    .option("password", "adminprodpassword") \
    .option("driver", "org.postgresql.Driver") \
    .load()

df.show()

spark.sql("CREATE NAMESPACE IF NOT EXISTS demo.sales")

df.writeTo("demo.sales.customers").createOrReplace()