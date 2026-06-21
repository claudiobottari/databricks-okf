---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2eb7ca48614d935b5116d8acebb56cd650fa4f4e38d2518f8a733b3ef7f137a
  pageDirectory: concepts
  sources:
    - update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rdd-to-dataframe-migration-pattern
    - RTDMP
  citations:
    - file: update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
title: RDD to DataFrame Migration Pattern
description: Replacing sc.parallelize with spark.read.json() pattern by using json.loads and spark.createDataFrame for Unity Catalog shared clusters.
tags:
  - databricks
  - spark
  - python
  - migration
timestamp: "2026-06-19T23:17:07.270Z"
---

# RDD to DataFrame Migration Pattern

The **RDD to DataFrame Migration Pattern** describes the code changes required when migrating Apache Spark jobs from using Resilient Distributed Datasets (RDDs) to using DataFrames, particularly when upgrading legacy workspaces to [Unity Catalog](/concepts/unity-catalog.md) on Databricks. This migration is necessary because certain RDD-based operations are not supported on shared clusters running with [Unity Catalog](/concepts/unity-catalog.md). ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Common Migration Scenarios

### Replacing `sc.parallelize` with `createDataFrame`

When a job notebook uses `sc.parallelize` in combination with `spark.read.json()` on a shared cluster, this pattern is not supported under [Unity Catalog](/concepts/unity-catalog.md). The recommended replacement is to use `json.loads` to parse JSON strings into dictionaries, then create a DataFrame directly using `spark.createDataFrame()`. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

**Before (RDD-based):**

```python
json_content1 = "{'json_col1': 'hello', 'json_col2': 32}"
json_content2 = "{'json_col1': 'hello', 'json_col2': 'world'}"
json_list = []
json_list.append(json_content1)
json_list.append(json_content2)
df = spark.read.json(sc.parallelize(json_list))
display(df)
```

**After (DataFrame-based):**

```python
from pyspark.sql import Row
import json

# Sample JSON data as a list of dictionaries (similar to JSON objects)
json_data_str = response.text
json_data = [json.loads(json_data_str)]

# Convert dictionaries to Row objects
rows = [Row(**json_dict) for json_dict in json_data]

# Create DataFrame from list of Row objects
df = spark.createDataFrame(rows)
df.display()
```

^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

### Creating Empty DataFrames Without `sc.emptyRDD()`

The pattern of using `sc.emptyRDD()` to create an empty DataFrame is not supported on shared clusters under [Unity Catalog](/concepts/unity-catalog.md). Instead, create the empty DataFrame directly by passing an empty list to `spark.createDataFrame()` with the desired schema. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

**Before (Scala, RDD-based):**

```scala
val schema = StructType(
  StructField("k", StringType, true) ::
  StructField("v", IntegerType, false) :: Nil)
spark.createDataFrame(sc.emptyRDD[Row], schema)
```

**After (Scala, DataFrame-based):**

```scala
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}
val schema = StructType(
  StructField("k", StringType, true) ::
  StructField("v", IntegerType, false) :: Nil)
spark.createDataFrame(new java.util.ArrayList[Row](), schema)
```

**After (Python, DataFrame-based):**

```python
from pyspark.sql.types import StructType, StructField, StringType
schema = StructType([StructField("k", StringType(), True)])
spark.createDataFrame([], schema)
```

^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

### Replacing `input_file_name()` with Metadata Columns

The `input_file_name()` function is not supported on shared clusters under [Unity Catalog](/concepts/unity-catalog.md). The recommended migration is to use the `_metadata` column, which is available when using `spark.read` and provides equivalent file-level information. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

**To get the file name:**

```python
.withColumn("RECORD_FILE_NAME", col("_metadata.file_name"))
```

**To get the full file path:**

```python
.withColumn("RECORD_FILE_PATH", col("_metadata.file_path"))
```

Both options work with `spark.read`. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- RDD – The original Spark abstraction being migrated away from.
- DataFrame – The target abstraction for the migration.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that necessitates certain migration patterns.
- Spark SQL – The API used in DataFrame-based approaches.
- Shared Clusters – The cluster type where RDD-based patterns are unsupported with [Unity Catalog](/concepts/unity-catalog.md).

## Sources

- update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md](/references/update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws-0f91bc02.md)
