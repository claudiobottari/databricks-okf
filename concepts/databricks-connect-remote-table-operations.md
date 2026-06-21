---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c14699ed3414f602abb9ba5d9b8f17897c129632d024701dbb55d7a9d10157e3
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-connect-remote-table-operations
    - DCRTO
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Databricks Connect remote table operations
description: The ability to read, create, query, and manage tables on a remote Databricks cluster using standard Spark DataFrame and SQL APIs through Databricks Connect.
tags:
  - databricks
  - sql
  - dataframe
  - table-operations
timestamp: "2026-06-19T09:15:08.365Z"
---

# Databricks Connect Remote Table Operations

**Databricks Connect remote table operations** refer to the ability to read, create, query, and manage tables on a remote Databricks cluster from a local Python environment using the Databricks Connect client. This enables developers to work with Databricks tables using their preferred IDEs, notebook servers, or custom applications while the actual data processing executes on the remote cluster. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

Databricks Connect for Python provides a `DatabricksSession` class that establishes a connection to a remote Databricks cluster. Once connected, you can perform standard Spark DataFrame operations and SQL queries against tables stored in the cluster's [Metastore](/concepts/metastore.md). All computation runs on the remote cluster, while the client handles API calls and result retrieval. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Reading Tables

The most basic remote table operation is reading an existing table. Using `spark.read.table()`, you can load any table accessible to the cluster and then apply transformations or display results locally. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

## Creating and Managing Tables

Databricks Connect supports full table lifecycle operations, including creation, population, querying, and deletion. The typical workflow involves:

1. Creating a local Spark DataFrame with your data.
2. Writing the DataFrame to a table on the remote cluster using `write.saveAsTable()`.
3. Querying the table using `spark.sql()`.
4. Cleaning up by dropping the table when no longer needed. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Example: Full Table Lifecycle

The following example demonstrates creating a table from in-memory data, querying it, and then deleting it: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from pyspark.sql.types import *
from datetime import date

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()

# Define schema and data
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

# Create table on remote cluster
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

## SQL Queries on Remote Tables

You can execute arbitrary SQL statements against tables on the remote cluster using `spark.sql()`. This includes `SELECT`, `INSERT`, `CREATE`, `ALTER`, and `DROP` operations. The SQL executes entirely on the remote cluster, and results are returned to the local client as a [PySpark DataFrame](/concepts/pysparklyr-package.md). ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Portable Code Pattern

For code that needs to work both with and without Databricks Connect, you can use a fallback pattern that attempts to import `DatabricksSession` and falls back to `SparkSession` if unavailable: ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

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

## Requirements

- Databricks Connect for Databricks Runtime 13.3 LTS and above. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]
- The Databricks Connect client must be [set up](https://docs.databricks.com/aws/en/dev-tools/databricks-connect/python/install) before use. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]
- Default authentication is assumed in the examples; alternative authentication methods can be configured. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The overall framework for connecting local environments to Databricks clusters.
- [DatabricksSession](/concepts/databrickssession.md) — The entry point for Databricks Connect operations.
- [PySpark DataFrame](/concepts/pysparklyr-package.md) — The data structure used for representing and manipulating table data.
- Spark SQL — The query engine used for remote table operations.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Runtime versions that support Databricks Connect.

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
