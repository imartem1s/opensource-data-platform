from datetime import datetime
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG(
    dag_id="ingest_customers_to_iceberg",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    ingest_task = SparkSubmitOperator(
        task_id="ingest_customers",
        application="/home/iceberg/spark-jobs/ingest_customers.py",
        conn_id="spark_local",
        jars=",".join([
            "/home/iceberg/jars/postgresql-42.7.13.jar",
            "/home/iceberg/jars/iceberg-spark-runtime-3.5_2.12-1.9.1.jar",
            "/home/iceberg/jars/iceberg-aws-bundle-1.9.1.jar",
        ]),
        conf={
            "spark.sql.extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
            "spark.sql.catalog.demo": "org.apache.iceberg.spark.SparkCatalog",
            "spark.sql.catalog.demo.type": "rest",
            "spark.sql.catalog.demo.uri": "http://rest:8181",
            "spark.sql.catalog.demo.io-impl": "org.apache.iceberg.aws.s3.S3FileIO",
            "spark.sql.catalog.demo.s3.endpoint": "http://minio:9000",
            "spark.sql.catalog.demo.warehouse": "s3://warehouse/",
            "spark.sql.catalog.demo.client.region": "us-east-1",
            "spark.sql.catalog.demo.s3.access-key-id": "rootuser",
            "spark.sql.catalog.demo.s3.secret-access-key": "rootpassword",
            "spark.sql.catalog.demo.s3.path-style-access": "true",
        },
    )