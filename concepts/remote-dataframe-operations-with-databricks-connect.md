---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cb5d73fa58ee4b47506364e94df9e038d9b84bf315c6ae894c2f0078f4c43ad
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-dataframe-operations-with-databricks-connect
    - RDOWDC
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Remote DataFrame Operations with Databricks Connect
description: Using Databricks Connect to read tables, create DataFrames, write to tables, and run SQL queries on a remote Databricks cluster from a local environment.
tags:
  - databricks
  - python
  - dataframe
  - sql
timestamp: "2026-06-19T17:45:21.332Z"
---

# Remote DataFrame Operations with Databricks Connect

**Remote DataFrame Operations with Databricks Connect** refers to the ability to execute Apache Spark DataFrame operations on a remote Databricks cluster from a local development environment, such as an IDE, notebook server, or custom application. Databricks Connect enables this by providing a client library that forwards Spark commands to a configured Databricks cluster for execution. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

Databricks Connect for Python allows developers to write Spark code locally and have it execute remotely on a Databricks cluster. This approach combines the flexibility of local development tools with the computational power of a Databricks cluster. The client library provides a `DatabricksSession` class that mirrors the standard `SparkSession` API, making it straightforward to port existing Spark code. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Prerequisites

Before using Databricks Connect, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install). The examples assume default authentication is configured for the client setup. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Reading a Table

The simplest remote DataFrame operation is reading a table from the Databricks cluster. The following example queries the `samples.nyctaxi.trips` table and displays the first 5 rows: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

## Creating and Managing DataFrames

Databricks Connect supports creating DataFrames locally and saving them as tables on the remote cluster. The following example demonstrates a complete workflow: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

1. Creates an in-memory DataFrame with airport temperature data.
2. Creates a table named `zzz_demo_temps_table` in the `default` schema (dropping it first if it already exists).
3. Saves the DataFrame contents to the table.
4. Runs a `SELECT` query on the table.
5. Displays the results.
6. Cleans up by dropping the table.

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from pyspark.sql.types import *
from datetime import date

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()

# Create a Spark DataFrame
schema = StructType([
  StructField('AirportCode', StringType(), False),
  StructField('Date', DateType(), False),
  StructField('TempHighF', IntegerType(), False),
  StructField('TempLowF', IntegerType(), False)
])

data = [
  [ 'BLI', date(2021, 4, 3), 52, 43],
  [ 'BLI', date(2021, 4, 2), 50, 38],
  [ 'BLI', date(2021, 4, 1), 52, 41],
  [ 'PDX', date(2021, 4, 3), 64, 45],
  [ 'PDX', date(2021, 4, 2), 61, 41],
  [ 'PDX', date(2021, 4, 1), 66, 39],
  [ 'SEA', date(2021, 4, 3), 57, 43],
  [ 'SEA', date(2021, 4, 2), 54, 39],
  [ 'SEA', date(2021, 4, 1), 56, 41]
]

temps = spark.createDataFrame(data, schema)

# Create and populate table on the remote cluster
spark.sql('USE default')
spark.sql('DROP TABLE IF EXISTS zzz_demo_temps_table')
temps.write.saveAsTable('zzz_demo_temps_table')

# Query the remote table
df_temps = spark.sql("""
  SELECT * FROM zzz_demo_temps_table 
  WHERE AirportCode != 'BLI' AND Date > '2021-04-01' 
  GROUP BY AirportCode, Date, TempHighF, TempLowF 
  ORDER BY TempHighF DESC
""")
df_temps.show()

# Clean up
spark.sql('DROP TABLE zzz_demo_temps_table')
```

## Portable Code Between Environments

When writing code that must work both with Databricks Connect and in environments where `DatabricksSession` is unavailable (such as a Databricks notebook), you can use a fallback pattern. The following example attempts to use `DatabricksSession` first and falls back to `SparkSession` if the import fails: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

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

This pattern uses the `SPARK_REMOTE` environment variable for authentication when running outside a Databricks environment. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Supported Operations

All standard [PySpark DataFrame](/concepts/pysparklyr.md) operations are supported when using Databricks Connect, including:

- Reading and writing tables
- Creating DataFrames from local data
- Running SQL queries
- Applying transformations and actions
- Managing schemas and tables

## Additional Resources

Databricks provides example applications in the [Databricks Connect GitHub repository](https://github.com/databricks-demos/dbconnect-examples), including: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

- A simple ETL application
- An interactive data application based on Plotly
- An interactive data application based on Plotly and PySpark AI

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The overall framework for connecting local environments to Databricks clusters
- [DatabricksSession](/concepts/databrickssession.md) — The client class used to establish remote connections
- [PySpark DataFrame](/concepts/pysparklyr.md) — The core data structure for Spark operations
- [Remote Development with Databricks](/concepts/interactive-development-with-databricks-connect.md) — Broader patterns for developing against Databricks remotely
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Runtime environment that supports Databricks Connect

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
