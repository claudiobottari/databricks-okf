---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adb89aa8df67be27fcc671697a3478c29689d3ec91988d6ab1e75ccdff8bc408
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reading-tables-with-databricks-connect
    - RTWDC
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Reading tables with Databricks Connect
description: Using spark.read.table() to query and display tables on a remote Databricks cluster from a local environment
tags:
  - databricks
  - python
  - data-access
timestamp: "2026-06-18T14:37:25.273Z"
---

#Reading tables with Databricks Connect

**Reading tables with Databricks Connect** refers to using the Databricks Connect client library to query a table stored in a Databricks cluster from a local IDE, notebook server, or custom Python application. This allows you to leverage the compute power of a remote Spark cluster while writing code in your local development environment. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

Databricks Connect for Python enables you to create a `SparkSession` (via `DatabricksSession`) that communicates with a configured Databricks cluster. Once the session is established, standard PySpark DataFrame APIs such as `spark.read.table()` are executed remotely on the cluster, and results are returned to the local client. This pattern is especially useful for interactive development and testing before deploying to production. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Prerequisites

Before reading a table, you must:

- [Set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install) for your environment.
- Have appropriate authentication configured (e.g., a Databricks token or OAuth). The examples below assume default authentication is in place. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Basic example

The following code reads the table `samples.nyctaxi.trips` and displays its first 5 rows:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

`DatabricksSession.builder.getOrCreate()` returns a SparkSession that is connected to the remote Databricks cluster. The call to `spark.read.table("samples.nyctaxi.trips")` reads the entire table as a DataFrame, and `df.show(5)` materializes the first five rows locally for display. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Reading tables in a portable way

If your code must run in environments where the `DatabricksSession` class is not available (e.g., on a cluster without the Databricks Connect library), you can fall back to the standard `SparkSession` builder. The following example uses the `SPARK_REMOTE` environment variable for authentication and reads the same table:

```python
from pyspark.sql import SparkSession, DataFrame

def get_spark() -> SparkSession:
    try:
        from databricks.connect import [[databrickssession|DatabricksSession]]
        return [[databrickssession|DatabricksSession]].builder.getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()

def get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")

get_taxis(get_spark()).show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

This pattern ensures that the same table-reading code works both in a Databricks Connect environment and in a standard Spark environment, making it easier to share logic between development and production. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related concepts

- [Databricks Connect](/concepts/databricks-connect.md) – The overall client library for connecting local code to Databricks clusters.
- SparkSession – The entry point for reading data and executing SQL in Spark.
- DataFrame – The primary data abstraction used with `spark.read.table()`.
- PySpark – The Python API for Apache Spark used in these examples.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Often used with Databricks Connect for ML workloads.

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
