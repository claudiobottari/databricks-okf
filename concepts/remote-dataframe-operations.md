---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94426667ece2418b8df2a01b0160380f84740a14be756c83db85975baff9363a
  pageDirectory: concepts
  sources:
    - code-examples-for-databricks-connect-for-python-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - remote-dataframe-operations
    - RDO
    - DataFrame operations
    - DataFrame actions
    - DataFrame transformations
  citations:
    - file: code-examples-for-databricks-connect-for-python-databricks-on-aws.md
title: Remote DataFrame Operations
description: The ability to create, manipulate, and persist DataFrames on a remote Databricks cluster using local Python code through Databricks Connect
tags:
  - databricks
  - python
  - dataframe
  - remote-execution
timestamp: "2026-06-18T10:59:02.153Z"
---

# Remote DataFrame Operations

**Remote DataFrame Operations** refer to reading, transforming, and writing [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) from external applications — such as local IDE scripts, notebook servers, or custom applications — by connecting to a remote Databricks cluster. This capability is provided by [Databricks Connect](/concepts/databricks-connect.md), which enables a client to submit Spark jobs that execute on a Databricks cluster while the client code runs locally. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Overview

Databricks Connect for Python (Databricks Runtime 13.3 LTS and above) allows developers to use familiar development tools and still leverage the compute and data resources of a Databricks cluster. The client application sends Spark commands to a remote cluster, which runs them against the [Unity Catalog](/concepts/unity-catalog.md) or workspace data. All standard DataFrame APIs — `read`, `write`, `createDataFrame`, `sql`, `show`, etc. — work transparently. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## How It Works

The client uses the `DatabricksSession` class (or falls back to a regular `SparkSession`) to establish a connection. Authentication is handled through the Databricks Connect client setup, often via the `SPARK_REMOTE` environment variable or default credentials. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

Once connected, all DataFrame operations are executed remotely on the cluster. The client receives only the results (e.g., row data for `show()` or schema information), not the raw data in transit for processing. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Code Examples

### Reading a Table

The simplest remote operation is reading a table from the cluster’s [Metastore](/concepts/metastore.md):

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.read.table("samples.nyctaxi.trips")
df.show(5)
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Creating a DataFrame and Saving as a Table

A typical remote workflow involves creating an in‑memory DataFrame, saving it as a table, querying it, and cleaning up:

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
from pyspark.sql.types import *
from datetime import date

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()

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
spark.sql('USE default')
spark.sql('DROP TABLE IF EXISTS zzz_demo_temps_table')
temps.write.saveAsTable('zzz_demo_temps_table')

df_temps = spark.sql("""
    SELECT * FROM zzz_demo_temps_table
    WHERE AirportCode != 'BLI' AND Date > '2021-04-01'
    GROUP BY AirportCode, Date, TempHighF, TempLowF
    ORDER BY TempHighF DESC
""")
df_temps.show()
# +-----------+----------+---------+--------+
# |AirportCode|      Date|TempHighF|TempLowF|
# +-----------+----------+---------+--------+
# |        PDX|2021-04-03|       64|      45|
# |        PDX|2021-04-02|       61|      41|
# |        SEA|2021-04-03|       57|      43|
# |        SEA|2021-04-02|       54|      39|
# +-----------+----------+---------+--------+

spark.sql('DROP TABLE zzz_demo_temps_table')
```

^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

### Portable Code Using SparkSession

When writing code that must also run in environments where `DatabricksSession` is not available, you can use a fallback pattern:

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

## Supported Operations

All standard PySpark DataFrame APIs are supported when using Databricks Connect, including:

- `read.table()`, `read.load()`, `read.format()`
- `write.saveAsTable()`, `write.mode().save()`
- `spark.sql()` for arbitrary SQL queries
- DataFrame transformations (`select`, `filter`, `groupBy`, `join`, etc.)
- Actions (`show()`, `collect()`, `count()`, etc.)

Operations that require direct access to cluster‑local resources (e.g., `dbutils` in the same process) may need additional handling, but the Spark DataFrame operations themselves are fully remote. ^[code-examples-for-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- [Databricks Connect](/concepts/databricks-connect.md) — The framework enabling remote DataFrame operations
- SparkSession — The entry point for Spark functionality
- [DatabricksSession](/concepts/databrickssession.md) — The Databricks-specific session for remote connections
- [Unity Catalog](/concepts/unity-catalog.md) — The metadata layer where tables are managed
- PySpark — The Python API for Apache Spark

## Sources

- code-examples-for-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [code-examples-for-databricks-connect-for-python-databricks-on-aws.md](/references/code-examples-for-databricks-connect-for-python-databricks-on-aws-43e94551.md)
