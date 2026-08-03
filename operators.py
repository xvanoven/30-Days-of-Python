"""
Databricks-ready workflow for the 30 Days of Python project.
This script can run in Databricks notebooks or as a local Python script.
"""

from __future__ import annotations

import os

try:
    from pyspark.sql import functions as F
    from pyspark.sql import SparkSession

    SPARK_AVAILABLE = True
except ImportError:  # pragma: no cover - handled gracefully in local environments
    F = None
    SparkSession = None
    SPARK_AVAILABLE = False


def get_spark():
    """Create a Spark session when PySpark is available."""
    if SparkSession is None:
        return None

    return SparkSession.builder.appName("30-days-python-databricks").getOrCreate()


def build_sample_dataframe(spark):
    """Create a small DataFrame that resembles a Databricks analytics workflow."""
    data = [
        (1, "Alicia", 31),
        (2, "Ben", 24),
        (3, "Carla", 29),
    ]
    df = spark.createDataFrame(data, ["id", "name", "age"])
    return df.withColumn("age_group", F.when(F.col("age") >= 30, "adult").otherwise("young"))


def write_to_table(df, table_name: str) -> None:
    """Persist the DataFrame as a Delta table when running in Databricks."""
    if df is None:
        return
    df.write.mode("overwrite").saveAsTable(table_name)


def main() -> None:
    print("Starting Databricks-style workflow...")
    spark = get_spark()

    if spark is None:
        print("PySpark is not available in this environment. Showing a local demo instead.")
        demo_data = [
            {"id": 1, "name": "Alicia", "age": 31},
            {"id": 2, "name": "Ben", "age": 24},
        ]
        for row in demo_data:
            print(row)
        return

    df = build_sample_dataframe(spark)
    print("Sample data preview:")
    df.show()

    table_name = os.getenv("DATABRICKS_TABLE_NAME", "default.python_learning_demo")
    write_to_table(df, table_name)
    print(f"Data written to table: {table_name}")

    summary = df.groupBy("age_group").count()
    print("Age group summary:")
    summary.show()


if __name__ == "__main__":
    main()

