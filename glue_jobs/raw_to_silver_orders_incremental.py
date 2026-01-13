import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql.functions import lit

args = getResolvedOptions(sys.argv, ['ingest_date'])
ingest_date = args['ingest_date']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

bucket = "surya-project2"

raw_path = f"s3://{bucket}/raw/orders/ingest_date={ingest_date}/"
silver_path = f"s3://{bucket}/silver/orders/"

df = spark.read.option("header", "true").csv(raw_path)
df = df.withColumn("ingest_date", lit(ingest_date))

df.write.mode("append") \
    .partitionBy("ingest_date") \
    .parquet(silver_path)

print(f"Orders loaded successfully for {ingest_date}")
