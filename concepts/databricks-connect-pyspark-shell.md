---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5dc0a25855016f6c5842f4080a0cad073e74dc25ca9bd8e46f984f8fa0fa514c
  pageDirectory: concepts
  sources:
    - pyspark-shell-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-pyspark-shell
    - DCPS
  citations:
    - file: pyspark-shell-databricks-on-aws.md
title: Databricks Connect PySpark Shell
description: A PySpark REPL (Spark shell) bundled with Databricks Connect for Python that connects to a remote Databricks cluster for interactive analysis.
tags:
  - databricks
  - pyspark
  - spark-shell
  - interactive-analysis
timestamp: "2026-06-19T20:00:01.625Z"
---

# Databricks Connect PySpark Shell

The **Databricks Connect PySpark Shell** is a PySpark REPL (Read-Eval-Print Loop) that ships with Databricks Connect for Python. It provides an interactive Spark shell configured to connect to a remote Databricks cluster, allowing users to run PySpark commands interactively from their local development environment. ^[pyspark-shell-databricks-on-aws.md]

## Overview

The PySpark shell is a command-line interface that enables interactive analysis against a Databricks cluster. It is available as part of Databricks Connect for Databricks Runtime 14.0 and above. The shell uses the `pyspark` binary, which is pre-configured to work with [Databricks Connect](/concepts/databricks-connect.md). ^[pyspark-shell-databricks-on-aws.md]

## Starting the Shell

To start the PySpark shell and connect it to a running Databricks cluster, run the following command from an activated Python virtual environment:

```bash
pyspark
```

When started with no additional parameters, the shell automatically picks up default credentials from the environment. This includes `DATABRICKS_` environment variables or the `DEFAULT` configuration profile. For information about configuring a connection, see [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md). ^[pyspark-shell-databricks-on-aws.md]

Upon successful startup, the shell displays output similar to the following:

```
Python 3.10 ...[Clang ...] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 13.x.dev0
      /_/

Using Python version 3.10 ...
Client connected to the Spark Connect server at sc://...:.../;token=...;x-databricks-cluster-id=...
SparkSession available as 'spark'.
>>>
```

Once the shell starts, the `spark` object is available to run Apache Spark commands on the Databricks cluster. A simple test command such as `spark.range(1,10).show()` can verify the connection. ^[pyspark-shell-databricks-on-aws.md]

## Using the Shell

The PySpark shell provides a built-in `spark` variable that represents the `SparkSession` on the running cluster. Users can execute PySpark DataFrame operations interactively. For example:

```python
>>> df = spark.read.table("samples.nyctaxi.trips")
>>> df.show(5)
+--------------------+---------------------+-------------+-----------+----------+-----------+
|tpep_pickup_datetime|tpep_dropoff_datetime|trip_distance|fare_amount|pickup_zip|dropoff_zip|
+--------------------+---------------------+-------------+-----------+----------+-----------+
| 2016-02-14 16:52:13|  2016-02-14 17:16:04|         4.94|       19.0|     10282|      10171|
| 2016-02-04 18:44:19|  2016-02-04 18:46:00|         0.28|        3.5|     10110|      10110|
| 2016-02-17 17:13:57|  2016-02-17 17:17:55|          0.7|        5.0|     10103|      10023|
| 2016-02-18 10:36:07|  2016-02-18 10:41:45|          0.8|        6.0|     10022|      10017|
| 2016-02-22 14:14:41|  2016-02-22 14:31:52|         4.51|       17.0|     10110|      10282|
+--------------------+---------------------+-------------+-----------+----------+-----------+
only showing top 5 rows
```

All Python code runs locally, while all PySpark code involving DataFrame operations runs on the cluster in the remote Databricks workspace. Results are sent back to the local caller. ^[pyspark-shell-databricks-on-aws.md]

For more information about using the Spark shell with Python, refer to Interactive Analysis with the Spark Shell. ^[pyspark-shell-databricks-on-aws.md]

## Stopping the Shell

To stop the PySpark shell, use any of the following methods:

- Press `Ctrl + d` or `Ctrl + z`
- Run the command `quit()` or `exit()`

^[pyspark-shell-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The client library that enables remote connection to Databricks clusters
- SparkSession — The entry point for programming Spark with the DataFrame API
- [PySpark DataFrame](/concepts/pysparklyr.md) — The primary data structure for structured data processing
- [Compute configuration for Databricks Connect](/concepts/compute-configuration-for-databricks-connect.md) — How to configure cluster connections
- Interactive Analysis with the Spark Shell — General guide for using the Spark shell

## Sources

- pyspark-shell-databricks-on-aws.md

# Citations

1. [pyspark-shell-databricks-on-aws.md](/references/pyspark-shell-databricks-on-aws-b2b40482.md)
