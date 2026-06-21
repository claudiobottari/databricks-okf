---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: edfb22d107fec16ce24e37bfa1fde02bbaba14e1908422dbfa6683245293fb7d
  pageDirectory: concepts
  sources:
    - user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-pyspark-udf-function-types
    - SPUFT
  citations:
    - file: user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md
title: Supported PySpark UDF Function Types
description: Databricks Connect supports a wide range of PySpark UDF functions including scalar UDFs, pandas UDFs, UDTFs, mapInPandas/mapInArrow, grouped apply functions, and streaming foreach/foreachBatch.
tags:
  - databricks-connect
  - udf
  - pyspark
  - api-reference
timestamp: "2026-06-19T23:23:01.116Z"
---

# Supported PySpark UDF Function Types

**Supported PySpark UDF Function Types** refers to the categories of user-defined functions (UDFs) that can be used with [Databricks Connect for Python](/concepts/databricks-connect-for-python.md). When a DataFrame operation includes UDFs, they are serialized by [Databricks Connect](/concepts/databricks-connect.md) and sent to the server as part of the request. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Overview

[Databricks Connect for Python](/concepts/databricks-connect-for-python.md) supports multiple types of user-defined functions, including traditional scalar UDFs, pandas UDFs, user-defined table functions (UDTFs), and various grouped and streaming apply functions. These functions allow users to extend PySpark's capabilities with custom Python logic that executes on the Databricks compute cluster. ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Supported UDF Types

### PySpark User-Defined Functions

The following PySpark UDF types are supported:

- `pyspark.sql.functions.udf` — Standard scalar UDFs that operate on individual rows and return a single value per row.
- `pyspark.sql.functions.pandas_udf` — Vectorized UDFs that operate on pandas Series or DataFrames for improved performance.
- `pyspark.sql.functions.udtf` — User-defined table functions that return multiple rows and columns from a single input.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### DataFrame Map Functions

- `pyspark.sql.DataFrame.mapInPandas` — Applies a function that takes an iterator of pandas DataFrames and returns an iterator of pandas DataFrames.
- `pyspark.sql.DataFrame.mapInArrow` — Similar to `mapInPandas` but uses Apache Arrow format for data transfer.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Grouped Apply Functions

- `pyspark.sql.GroupedData.applyInPandas` — Applies a function to each group of a grouped DataFrame using pandas DataFrames.
- `pyspark.sql.GroupedData.applyInArrow` — Applies a function to each group using Apache Arrow format.
- `pyspark.sql.PandasCogroupedOps.applyInPandas` — Applies a function to co-grouped pandas DataFrames.
- `pyspark.sql.PandasCogroupedOps.applyInArrow` — Applies a function to co-grouped data using Arrow format.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

### Streaming Functions

- `pyspark.sql.streaming.DataStreamWriter.foreach` — Applies a function to each row in a streaming DataFrame.
- `pyspark.sql.streaming.DataStreamWriter.foreachBatch` — Applies a function to each micro-batch in a streaming DataFrame.
- `pyspark.sql.streaming.StatefulProcessor` — Defines stateful processing logic for streaming applications.

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Defining a UDF

To create a UDF in [Databricks Connect for Python](/concepts/databricks-connect-for-python.md), use the `@udf` decorator with a specified return type. The following example defines a UDF that squares values:

```python
from pyspark.sql.functions import col, udf
from pyspark.sql.types import IntegerType
from databricks.connect import [[databrickssession|DatabricksSession]]

@udf(returnType=IntegerType())
def double(x):
    return x * x

spark = [[databrickssession|DatabricksSession]].builder.getOrCreate()
df = spark.range(1, 2)
df = df.withColumn("doubled", double(col("id")))
df.show()
```

^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Requirements

Because the user-defined function is serialized and deserialized, the Python version of the client must match the Python version on the Databricks compute. For supported versions, see the [Version Support Matrix for Databricks Connect](/concepts/version-compatibility-for-databricks-connect.md). ^[user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md]

## Related Concepts

- User-Defined Functions (UDFs) — General overview of UDFs in Databricks.
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) — Vectorized UDFs for improved performance.
- User-Defined Table Functions (UDTFs) — Functions that return multiple rows and columns.
- [Databricks Connect for Python](/concepts/databricks-connect-for-python.md) — The client library that enables UDF execution on remote clusters.
- Streaming UDFs — UDFs used in structured streaming pipelines.

## Sources

- user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md

# Citations

1. [user-defined-functions-in-databricks-connect-for-python-databricks-on-aws.md](/references/user-defined-functions-in-databricks-connect-for-python-databricks-on-aws-d446d035.md)
