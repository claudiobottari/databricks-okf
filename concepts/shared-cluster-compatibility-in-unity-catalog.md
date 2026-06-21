---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7abfbbd818ad03bbd1250adc51d86d399853ced213b0c453e495d5aac12220b
  pageDirectory: concepts
  sources:
    - update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-cluster-compatibility-in-unity-catalog
    - SCCIUC
    - Shared cluster restrictions in Unity Catalog
  citations:
    - file: update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
title: Shared Cluster Compatibility in Unity Catalog
description: Certain Spark APIs like spark.catalog, sc.parallelize, sc.emptyRDD, and input_file_name() are unsupported or behave differently on shared clusters when using Unity Catalog.
tags:
  - databricks
  - unity-catalog
  - shared-cluster
  - spark
timestamp: "2026-06-19T23:16:48.416Z"
---

# Shared Cluster Compatibility in [Unity Catalog](/concepts/unity-catalog.md)

**Shared Cluster Compatibility in Unity Catalog** refers to the limitations and required code changes when running jobs on shared clusters after upgrading a legacy workspace to [Unity Catalog](/concepts/unity-catalog.md). Certain Spark operations that worked in legacy workspaces—particularly those relying on the SparkContext (`sc`) or direct filesystem access via DBFS FUSE—are not supported or behave differently on shared clusters in [Unity Catalog](/concepts/unity-catalog.md). Understanding these incompatibilities is essential for a smooth migration. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Requirements

Many of the workarounds for shared cluster incompatibilities require **Databricks Runtime 14.2 or above**. If an upgrade is not possible, alternative SQL-based workarounds are available. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Detailed Scenarios and Workarounds

### Spark Catalog Methods (`spark.catalog.X`)

Methods such as `spark.catalog.tableExists`, `spark.catalog.listTables`, and `spark.catalog.setDefaultCatalog` are not supported on shared clusters when using [Unity Catalog](/concepts/unity-catalog.md). ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

**Workarounds:**

- Replace `tableExists` with a SQL `DESCRIBE TABLE` wrapped in a try/except block.
- Replace `listTables` with `spark.sql("SHOW TABLES ...")`.
- Replace `setDefaultCatalog` with `spark.sql("USE CATALOG <catalog_name>")`.

```python
# Instead of spark.catalog.tableExists("catalog.schema.table")
def tableExistsSql(tablename):
    try:
        spark.sql(f"DESCRIBE TABLE {tablename};")
    except Exception:
        return False
    return True

# Instead of spark.catalog.setDefaultCatalog("my_catalog")
spark.sql("USE CATALOG my_catalog")
```

### `sc.parallelize` with `spark.read.json()`

Using `sc.parallelize` to create an RDD of JSON strings and then reading it with `spark.read.json()` is not supported on shared clusters. The recommended replacement is to parse the JSON strings with `json.loads` and build a DataFrame using `spark.createDataFrame`. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

```python
# Before (not supported)
json_content1 = "{'json_col1': 'hello', 'json_col2': 32}"
json_content2 = "{'json_col1': 'hello', 'json_col2': 'world'}"
df = spark.read.json(sc.parallelize([json_content1, json_content2]))

# After
import json
from pyspark.sql import Row

json_data = [json.loads(response.text)]
rows = [Row(**d) for d in json_data]
df = spark.createDataFrame(rows)
```

### Empty RDD to Create Empty DataFrame

Creating an empty DataFrame using `sc.emptyRDD[Row]` is not supported on shared clusters. Use an empty `ArrayList` or an empty Python list instead. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

**Scala workaround:**
```scala
import org.apache.spark.sql.types._
val schema = StructType(StructField("k", StringType, true) :: StructField("v", IntegerType, false) :: Nil)
spark.createDataFrame(new java.util.ArrayList[Row](), schema)
```

**Python workaround:**
```python
from pyspark.sql.types import StructType, StructField, StringType
schema = StructType([StructField("k", StringType(), True)])
spark.createDataFrame([], schema)
```

### `input_file_name()` Function

`input_file_name()` is not supported in [Unity Catalog](/concepts/unity-catalog.md) for shared clusters. Use the `_metadata` column instead. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

```python
# Get file name
df.withColumn("RECORD_FILE_NAME", col("_metadata.file_name"))

# Get full file path
df.withColumn("RECORD_FILE_PATH", col("_metadata.file_path"))
```

Both options work with `spark.read`.

### DBFS Data Operations

When using DBFS with a shared cluster through the FUSE service (e.g., `/dbfs/test/sample_file.csv`), the cluster cannot reach the filesystem and generates a file-not-found error. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

**Solutions:**

1. Use a Unity Catalog Volume instead of DBFS (preferred).
2. Update the code to use `dbutils` or `spark` APIs, which use the direct-to-storage access path and are granted access to DBFS from shared clusters.

```bash
# Fails on shared cluster:
with open('/dbfs/test/sample_file.csv', 'r') as file:
ls -ltr /dbfs/test
cat /dbfs/test/sample_file.csv
```

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution that introduces these compatibility changes.
- Shared Cluster Architecture – Explains how shared clusters differ from single-user clusters.
- [Upgrading a Job to Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md) – A guided workflow for updating jobs.
- DBFS FUSE – The filesystem interface that is restricted in shared clusters.
- SparkContext (sc) – The entry point that is limited on shared clusters under [Unity Catalog](/concepts/unity-catalog.md).

## Sources

- update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md](/references/update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws-0f91bc02.md)
