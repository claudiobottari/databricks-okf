---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fee0f266fdfc37d8b5f76f0d1c3432bf2631c7c945cd69baa51f6b5014b71c11
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - creating-and-saving-dataframes-as-tables-with-databricks-connect
    - saving DataFrames as tables with Databricks Connect and Creating
    - CASDATWDC
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Creating and saving DataFrames as tables with Databricks Connect
description: Pattern for creating in-memory DataFrames, saving them as persistent tables on a Databricks cluster, querying them, and cleaning up
tags:
  - databricks
  - python
  - data-management
timestamp: "2026-06-18T14:37:32.984Z"
---

---
title: Creating and Saving DataFrames as Tables with Databricks Connect
summary: How to create an in-memory PySpark DataFrame and save it as a managed table on a Databricks cluster using Databricks Connect for Python.
sources:
  - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
kind: howto
createdAt: "2026-06-18T08:06:16.367Z"
updatedAt: "2026-06-18T08:06:16.367Z"
tags:
  - databricks-connect
  - dataframe
  - table
  - pyspark
aliases:
  - creating-and-saving-dataframes-as-tables-with-databricks-connect
  - CASDTWDBC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Creating and Saving DataFrames as Tables with Databricks Connect

**Creating and Saving DataFrames as Tables with Databricks Connect** refers to the workflow of building an in-memory PySpark DataFrame on the client side and persistently writing it as a managed SQL table to a Databricks cluster using [Databricks Connect](/concepts/databricks-connect.md) for Python. This pattern allows you to develop and test DataFrame transformations locally and then push the results into the cluster for sharing, querying, or downstream ETL pipelines.

## Overview

Databricks Connect enables a remote client (e.g., your IDE or notebook server) to connect to a Databricks cluster and execute Spark commands. The client creates a [DatabricksSession](/concepts/databrickssession.md) (or falls back to a standard SparkSession), which communicates with the cluster. You can then create a DataFrame in the client’s memory from local data, persist it as a table on the cluster, query it, and clean up when finished. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Prerequisites

Before following this guide, you must [set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install). The examples below assume default authentication is configured. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Step-by-Step Example

The following steps walk through a complete example that creates a DataFrame of airport temperature data, saves it as a table named `zzz_demo_temps_table` in the `default` schema, queries it, and then deletes the table. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### 1. Create a [DatabricksSession](/concepts/databrickssession.md)

Use `DatabricksSession.builder.getOrCreate()` to obtain a Spark session connected to your cluster. This object provides the entry point for all Spark operations. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
```

### 2. Define a Schema and Build Local Data

Define a StructType schema that matches the structure of your data, then create a list of rows. The example below uses airport codes, dates, and high/low temperatures. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from pyspark.sql.types import *
from datetime import date

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
```

### 3. Create an In-Memory DataFrame

Use `spark.createDataFrame(data, schema)` to create the DataFrame in the client’s memory. The data is not yet on the cluster. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
temps = spark.createDataFrame(data, schema)
```

### 4. Prepare the Target Schema and Drop an Existing Table

Switch to the desired schema (e.g., `default`) and optionally drop any pre‑existing table with the same name to avoid conflicts. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
spark.sql('USE default')
spark.sql('DROP TABLE IF EXISTS zzz_demo_temps_table')
```

### 5. Save the DataFrame as a Table

Call `temps.write.saveAsTable('zzz_demo_temps_table')` to persist the DataFrame’s contents as a managed table on the Databricks cluster. The table is created in the `default` schema (or the current schema). ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
temps.write.saveAsTable('zzz_demo_temps_table')
```

### 6. Query the Table

You can now run a SQL query against the saved table using `spark.sql()`. The query results are returned as a new DataFrame. The example below filters, groups, and orders the data. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
df_temps = spark.sql(
  "SELECT * FROM zzz_demo_temps_table "
  "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' "
  "GROUP BY AirportCode, Date, TempHighF, TempLowF "
  "ORDER BY TempHighF DESC"
)
df_temps.show()
```

The output (5 rows) shows PDX and SEA entries with their temperatures. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### 7. Clean Up

Delete the table from the cluster when it is no longer needed. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
spark.sql('DROP TABLE zzz_demo_temps_table')
```

## Reading an Existing Table

You can also read a table from the cluster without creating one. Use `spark.read.table("table_name")` and then display or process the data. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

## Using [DatabricksSession](/concepts/databrickssession.md) or SparkSession Portably

If your code needs to run both inside Databricks (where `DatabricksSession` may not be available) and in a Databricks Connect client, you can write a fallback function that imports `DatabricksSession` and falls back to `SparkSession.builder.getOrCreate()` if the import fails. The `SPARK_REMOTE` environment variable is used for authentication in that case. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

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

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) – Overview and setup guides.
- [DatabricksSession](/concepts/databrickssession.md) – The client-side session object for remote Spark execution.
- [PySpark DataFrame](/concepts/pysparklyr-package.md) – Core data structure for structured data.
- saveAsTable – Method to write a DataFrame as a managed table.
- SQL table – Managed or external tables on the Databricks cluster.
- StructType – Spark schema definition.
- ETL – Extract, transform, load pipelines that commonly use this pattern.

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
