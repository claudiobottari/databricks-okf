---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c573f3e37aa17dcf887ffdd0c4a86008e8d7e177d1495f4104074fc7d4c15f2
  pageDirectory: concepts
  sources:
    - update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - upgrading-jobs-to-unity-catalog
    - UJTUC
    - Upgrading a Job to Unity Catalog
    - Upgrading to Unity Catalog
    - upgrading to Unity Catalog
    - Job Migration to Unity Catalog
    - Job Upgrade for Unity Catalog
    - Job Upgrade to Unity Catalog
    - Updating jobs to work with Unity Catalog
    - Upgrade to Unity Catalog
  citations:
    - file: update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
title: Upgrading Jobs to Unity Catalog
description: Migration patterns for updating existing Databricks job notebooks to work with Unity Catalog after upgrading from legacy workspaces.
tags:
  - databricks
  - unity-catalog
  - migration
  - data-governance
timestamp: "2026-06-19T23:17:47.743Z"
---

# Upgrading Jobs to [Unity Catalog](/concepts/unity-catalog.md)

When you upgrade legacy workspaces to [Unity Catalog](/concepts/unity-catalog.md), existing jobs may need to be updated to reference upgraded tables and filepaths. The main table on this page lists typical scenarios and suggestions for updating your jobs. Scenarios that require code examples link to the Detailed scenarios section. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Overview of Scenarios

The upgrade process involves converting legacy [Hive Metastore](/concepts/built-in-hive-metastore.md) references to [Unity Catalog](/concepts/unity-catalog.md)-managed tables and file paths. Common scenarios include:
- Updating Spark SQL table references
- Migrating DBFS file paths to Unity Catalog Volumes
- Adjusting DataFrame creation patterns
- Handling File Metadata operations

## Detailed Scenarios

The following scenarios require code examples and specific workarounds when upgrading jobs to [Unity Catalog](/concepts/unity-catalog.md).

### Job Notebooks Use `spark.catalog.X` on a Shared Cluster

Use Databricks Runtime 14.2 or above. If a Databricks Runtime upgrade is not possible, use the following workarounds:

Instead of `tableExists`, use:

```python
def tableExistsSql(tablename):
    try:
        spark.sql(f"DESCRIBE TABLE {tablename};")
    except Exception as e:
        return False
    return True
tableExistsSql("jakob.jakob.my_table")
```

Instead of `listTables`, use `SHOW TABLES` (which also supports restricting by database or pattern matching):

For `setDefaultCatalog`, run:
```python
spark.sql("USE CATALOG <catalog_name>")
```

### Job Notebooks Use `sc.parallelize` and `spark.read.json()` on a Shared Cluster

Use `json.loads` instead.

**Before:**
```python
json_content1 = "{'json_col1': 'hello', 'json_col2': 32}"
json_content2 = "{'json_col1': 'hello', 'json_col2': 'world'}"
json_list = []
json_list.append(json_content1)
json_list.append(json_content2)
df = spark.read.json(sc.parallelize(json_list))
display(df)
```

**After:**
```python
from pyspark.sql import Row
import json
json_data_str = response.text
json_data = [json.loads(json_data_str)]
rows = [Row(**json_dict) for json_dict in json_data]
df = spark.createDataFrame(rows)
df.display()
```

### Job Notebooks Create Empty DataFrames Using `sc.emptyRDD()` on a Shared Cluster

**Before (Scala):**
```scala
val schema = StructType(
  StructField("k", StringType, true) ::
  StructField("v", IntegerType, false) :: Nil)
spark.createDataFrame(sc.emptyRDD[Row], schema)
```

**After (Scala):**
```scala
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}
val schema = StructType(
  StructField("k", StringType, true) ::
  StructField("v", IntegerType, false) :: Nil)
spark.createDataFrame(new java.util.ArrayList[Row](), schema)
```

**After (Python):**
```python
from pyspark.sql.types import StructType, StructField, StringType
schema = StructType([StructField("k", StringType(), True)])
spark.createDataFrame([], schema)
```

### Job Notebooks Use `input_file_name()` on a Shared Cluster

`input_file_name()` is not supported in [Unity Catalog](/concepts/unity-catalog.md) for shared clusters.

To get the file name:
```python
.withColumn("RECORD_FILE_NAME", col("_metadata.file_name"))
```

To get the full file path:
```python
.withColumn("RECORD_FILE_PATH", col("_metadata.file_path"))
```

Both options work with `spark.read`.

### Job Notebooks Perform Data Operations on DBFS on a Shared Cluster

When using DBFS with a shared cluster through the FUSE service, the cluster cannot reach the filesystem and generates a file-not-found error.

The following examples fail on a shared cluster:
```bash
with open('/dbfs/test/sample_file.csv', 'r') as file:
ls -ltr /dbfs/test
cat /dbfs/test/sample_file.csv
```

Use one of the following solutions:
- Use a [Databricks Unity Catalog Volume](/concepts/databricks-utilities-with-unity-catalog-volumes.md) instead of DBFS (preferred)
- Update the code to use `dbutils` or `spark`, which use the direct-to-storage access path and are granted access to DBFS from shared clusters

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) - The data governance platform for Databricks
- Legacy Workspace Upgrade - The process of moving from legacy workspaces to [Unity Catalog](/concepts/unity-catalog.md)
- [Hive Metastore](/concepts/built-in-hive-metastore.md) - The legacy metadata store being replaced by [Unity Catalog](/concepts/unity-catalog.md)
- Unity Catalog Volumes - A file management option for [Unity Catalog](/concepts/unity-catalog.md)
- DBFS - Databricks File System
- Shared Clusters - Compute resources that support multiple users
- Databricks Runtime - The runtime environment for Databricks jobs

## Sources

- update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md](/references/update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws-0f91bc02.md)
