---
title: PySpark shell | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/spark-shell
ingestedAt: "2026-06-18T08:06:22.384Z"
---

note

This article covers Databricks Connect for Databricks Runtime 14.0 and above.

Databricks Connect for Python ships with a `pyspark` binary which is a PySpark REPL (a Spark shell) configured to use Databricks Connect.

## Start the shell[​](#start-the-shell "Direct link to Start the shell")

To start the Spark shell and to connect it to your running cluster, run the following command from your activated Python virtual environment.

note

When started with no additional parameters, the shell picks up default credentials from the environment (for example, the `DATABRICKS_` environment variables or the `DEFAULT` configuration profile) to connect to the Databricks cluster. For information about configuring a connection, see [Compute configuration for Databricks Connect](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/cluster-config).

The Spark shell appears, for example:

Output

    Python 3.10 ...[Clang ...] on darwinType "help", "copyright", "credits" or "license" for more information.Welcome to      ____              __      / __/__  ___ _____/ /__   _\ \/ _ \/ _ `/ __/  '_/   /__ / .__/\_,_/_/ /_/\_\   version 13.x.dev0      /_/Using Python version 3.10 ...Client connected to the Spark Connect server at sc://...:.../;token=...;x-databricks-cluster-id=...SparkSession available as 'spark'.>>>

Once the shell starts up, the `spark` object is available to run Apache Spark commands on the Databricks cluster. Run a simple PySpark command, such as `spark.range(1,10).show()`. If there are no errors, you have successfully connected.

## Use the shell[​](#use-the-shell "Direct link to Use the shell")

Refer to [Interactive Analysis with the Spark Shell](https://spark.apache.org/docs/latest/quick-start.html#interactive-analysis-with-the-spark-shell) for information about how to use the Spark shell with Python to run commands on your compute.

Use the built-in `spark` variable to represent the `SparkSession` on your running cluster, for example:

    >>> df = spark.read.table("samples.nyctaxi.trips")>>> df.show(5)+--------------------+---------------------+-------------+-----------+----------+-----------+|tpep_pickup_datetime|tpep_dropoff_datetime|trip_distance|fare_amount|pickup_zip|dropoff_zip|+--------------------+---------------------+-------------+-----------+----------+-----------+| 2016-02-14 16:52:13|  2016-02-14 17:16:04|         4.94|       19.0|     10282|      10171|| 2016-02-04 18:44:19|  2016-02-04 18:46:00|         0.28|        3.5|     10110|      10110|| 2016-02-17 17:13:57|  2016-02-17 17:17:55|          0.7|        5.0|     10103|      10023|| 2016-02-18 10:36:07|  2016-02-18 10:41:45|          0.8|        6.0|     10022|      10017|| 2016-02-22 14:14:41|  2016-02-22 14:31:52|         4.51|       17.0|     10110|      10282|+--------------------+---------------------+-------------+-----------+----------+-----------+only showing top 5 rows

All Python code runs locally, while all PySpark code involving DataFrame operations runs on the cluster in the remote Databricks workspace and run responses are sent back to the local caller.

## Stop the shell[​](#stop-the-shell "Direct link to Stop the shell")

To stop the Spark shell, press `Ctrl + d` or `Ctrl + z`, or run the command `quit()` or `exit()`.
