---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27f7f27ff15eeb36448e919d38ab006c9f5bf81d4c2e0c5daede55d1f3d330a9
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-table-crud-operations
    - DCTCO
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect Table CRUD Operations
description: Common patterns for reading, creating, querying, and dropping tables on a Databricks cluster through a remote Databricks Connect session.
tags:
  - databricks
  - python
  - sql
  - operations
timestamp: "2026-06-19T14:15:08.085Z"
---

Here is the wiki page for "Databricks Connect Table CRUD Operations".

---

## Databricks Connect Table CRUD Operations

**Databricks Connect Table CRUD Operations** covers the core Create, Read, Update, and Delete operations you can perform on Databricks tables from a remote Python client using [Databricks Connect](/concepts/databricks-connect.md). These operations allow you to manage table data directly from external IDEs, notebook servers, or custom applications without working inside a Databricks notebook.

## Overview

Databricks Connect for Python enables you to connect a remote Spark session to a Databricks cluster. Using this session, you can perform standard table operations: reading existing tables, creating new tables, writing data into them, and deleting them. All operations execute on the remote Databricks cluster via the Databricks Connect connection. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Prerequisites

Before performing table CRUD operations, you must:

1. [Set up the Databricks Connect client](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install)
2. Initialize a `DatabricksSession` using `DatabricksSession.builder.getOrCreate()`
3. Ensure you have appropriate permissions on the cluster to create, read, write, and drop tables ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Read Operations

Reading a table is performed using `spark.read.table()`. The returned DataFrame can then be displayed or queried further using standard Spark SQL or DataFrame operations.

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Reading with SQL Queries

You can read table data using `spark.sql()` with SELECT statements: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
df_temps = spark.sql(
    "SELECT * FROM zzz_demo_temps_table "
    "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' "
    "GROUP BY AirportCode, Date, TempHighF, TempLowF "
    "ORDER BY TempHighF DESC"
)
df_temps.show()
```

## Create Operations

To create a table, you first build a PySpark DataFrame, then save it as a table using `DataFrame.write.saveAsTable()`.

### Creating a Table with a Defined Schema

You can define a schema using `StructType` and `StructField`, populate it with data, and save it as a new table: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

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
  ['BLI', date(2021, 4, 3), 52, 43],
  ['BLI', date(2021, 4, 2), 50, 38],
  ['BLI', date(2021, 4, 1), 52, 41],
  ['PDX', date(2021, 4, 3), 64, 45],
  ['PDX', date(2021, 4, 2), 61, 41],
  ['PDX', date(2021, 4, 1), 66, 39],
  ['SEA', date(2021, 4, 3), 57, 43],
  ['SEA', date(2021, 4, 2), 54, 39],
  ['SEA', date(2021, 4, 1), 56, 41]
]

temps = spark.createDataFrame(data, schema)
temps.write.saveAsTable('zzz_demo_temps_table')
```

### Selecting the Database Schema

Before creating the table, use `spark.sql('USE default')` to switch to the desired database schema. The table will be created in that schema. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Update Operations

To update a table's data, you use standard Spark SQL or [DataFrame operations](/concepts/remote-dataframe-operations.md). After performing transformations, you can write the updated data back to the table using `DataFrame.write.mode("overwrite").saveAsTable()`. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
# Example: Filter rows and write back
df_filtered = spark.table("zzz_demo_temps_table").filter("TempHighF > 55")
df_filtered.write.mode("overwrite").saveAsTable("zzz_demo_temps_table")
```

## Delete Operations

Tables can be deleted using the `DROP TABLE` SQL statement: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
spark.sql("DROP TABLE IF EXISTS zzz_demo_temps_table")
```

It is a best practice to drop the table before attempting to recreate it with the same name to avoid conflicts: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
spark.sql('DROP TABLE IF EXISTS zzz_demo_temps_table')
temps.write.saveAsTable('zzz_demo_temps_table')
```

## Complete CRUD Example

The following complete example demonstrates the full CRUD lifecycle — creating, reading querying, and deleting a table:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from pyspark.sql.types import *
from datetime import date

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()

# Schema definition
schema = StructType([
  StructField('AirportCode', StringType(), False),
  StructField('Date', DateType(), False),
  StructField('TempHighF', IntegerType(), False),
  StructField('TempLowF', IntegerType(), False)
])

data = [
  ['BLI', date(2021, 4, 3), 52, 43],
  ['BLI', date(2021, 4, 2), 50, 38],
  ['BLI', date(2021, 4, 1), 52, 41],
  ['PDX', date(2021, 4, 3), 64, 45],
  ['PDX', date(2021, 4, 2), 61, 41],
  ['PDX', date(2021, 4, 1), 66, 39],
  ['SEA', date(2021, 4, 3), 57, 43],
  ['SEA', date(2021, 4, 2), 54, 39],
  ['SEA', date(2021, 4, 1), 56, 41]
]

temps = spark.createDataFrame(data, schema)

# CREATE
spark.sql('USE default')
spark.sql('DROP TABLE IF EXISTS zzz_demo_temps_table')
temps.write.saveAsTable('zzz_demo_temps_table')

# READ
df_temps = spark.sql(
    "SELECT * FROM zzz_demo_temps_table "
    "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' "
    "GROUP BY AirportCode, Date, TempHighF, TempLowF "
    "ORDER BY TempHighF DESC"
)
df_temps.show()

# DELETE
spark.sql('DROP TABLE zzz_demo_temps_table')
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Portable Approach Using `SparkSession`

For code that must run in environments where `DatabricksSession` is unavailable (such as directly on a cluster), use a portable pattern that falls back to `SparkSession`: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

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

- [Databricks Connect](/concepts/databricks-connect.md) — The client library for remote Spark session connections
- Spark SQL — The query engine used for SQL-based CRUD operations
- [PySpark DataFrame](/concepts/pysparklyr-package.md) — The primary data structure for CRUD operations
- [Databricks Session](/concepts/databrickssession.md) — The session object that connects to the cluster
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Databricks tables

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
