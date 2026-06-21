---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02d7e0d623960b85bc5134b24f8eeec2ea0daeb9a104e5a3d0653e87f30fc5da
  pageDirectory: concepts
  sources:
    - update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata-column-access-in-unity-catalog
    - MCAIUC
  citations:
    - file: update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
title: Metadata Column Access in Unity Catalog
description: Using _metadata.file_name and _metadata.file_path as an alternative to input_file_name() for shared clusters in Unity Catalog.
tags:
  - databricks
  - spark
  - unity-catalog
  - file-metadata
timestamp: "2026-06-19T23:16:57.529Z"
---

## Metadata Column Access in [Unity Catalog](/concepts/unity-catalog.md)

**Metadata column access** in [Unity Catalog](/concepts/unity-catalog.md) refers to the ability to read file-level metadata—such as the source file name and path—when querying data. On shared clusters in [Unity Catalog](/concepts/unity-catalog.md), the traditional `input_file_name()` function is not supported. Instead, users must use the `_metadata` virtual columns provided by Databricks. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

### Limitation of `input_file_name()`

The `input_file_name()` function, which returns the path of the file a row was read from, is unavailable on Shared Clusters when using [Unity Catalog](/concepts/unity-catalog.md). Attempting to use it will result in an error or incorrect behavior. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

### Alternative: `_metadata` Columns

To retrieve the file name and path on a [Unity Catalog](/concepts/unity-catalog.md) shared cluster, use the `_metadata` virtual columns:

- **File name**: Use `col("_metadata.file_name")`
- **Full file path**: Use `col("_metadata.file_path")`

These columns work with `spark.read` operations and provide the same information that `input_file_name()` would, without the compatibility issue. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

Example usage in a DataFrame transformation:

```python
from pyspark.sql.functions import col

df.withColumn("RECORD_FILE_NAME", col("_metadata.file_name"))
df.withColumn("RECORD_FILE_PATH", col("_metadata.file_path"))
```

^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution for Databricks workspaces.
- Shared Clusters – Multi-user clusters used in [Unity Catalog](/concepts/unity-catalog.md).
- [Job Upgrade for Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md) – Guidance for updating existing jobs after workspace upgrade.
- input_file_name() Function – The older, unsupported function for file metadata.
- _metadata Virtual Columns – The supported alternative for accessing file metadata.

### Sources

- update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md](/references/update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws-0f91bc02.md)
