---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f4d3fe354138dce07385cf84596cfb0ad329342b5a2b7b3d0e30d14c412c57aa
  pageDirectory: concepts
  sources:
    - update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbfs-access-patterns-for-shared-clusters
    - DAPFSC
  citations:
    - file: update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
title: DBFS Access Patterns for Shared Clusters
description: DBFS FUSE paths fail on shared clusters in Unity Catalog; alternatives include using dbutils, spark readers, or Unity Catalog Volumes.
tags:
  - databricks
  - dbfs
  - unity-catalog
  - storage
timestamp: "2026-06-19T23:17:20.501Z"
---

# DBFS Access Patterns for Shared Clusters

**DBFS Access Patterns for Shared Clusters** describes the methods and limitations of accessing files stored in the Databricks File System (DBFS) when running jobs on shared clusters, particularly after upgrading workspaces to [Unity Catalog](/concepts/unity-catalog.md). Shared clusters have restricted access to DBFS through certain interfaces, requiring specific patterns to avoid file-not-found errors.

## Overview

When using DBFS with a shared cluster through the FUSE service, the cluster cannot reach the filesystem and generates a file-not-found error. This limitation affects legacy code that relies on direct filesystem operations, such as reading files with Python's `open()` or shell commands like `ls` and `cat` on the `/dbfs` mount point. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Affected Operations

The following operations fail on a shared cluster when trying to access DBFS:

```python
# Fails on shared cluster
with open('/dbfs/test/sample_file.csv', 'r') as file:
    ...
```

```bash
# Fails on shared cluster
ls -ltr /dbfs/test
cat /dbfs/test/sample_file.csv
```

^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Recommended Solutions

### Preferred: Use [Unity Catalog](/concepts/unity-catalog.md) Volumes

The recommended approach is to use a [Databricks Unity Catalog Volume](/concepts/databricks-utilities-with-unity-catalog-volumes.md) instead of DBFS. Volumes are fully supported on shared clusters and integrate with [Unity Catalog](/concepts/unity-catalog.md)'s governance model. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

### Alternative: Use `dbutils` or `spark` APIs

Update code to use `dbutils` or `spark` APIs, which use the direct-to-storage access path and are granted access to DBFS from shared clusters. These interfaces bypass the FUSE layer and communicate directly with cloud storage. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

#### Examples

Reading a file with `dbutils`:

```python
file_content = dbutils.fs.head("dbfs:/test/sample_file.csv")
```

Reading data into a DataFrame with Spark:

```python
df = spark.read.csv("dbfs:/test/sample_file.csv")
```

## Related Issues on Shared Clusters

Several other operations may also require changes when upgrading to [Unity Catalog](/concepts/unity-catalog.md) and running on shared clusters:

- **`spark.catalog.X` methods** (`tableExists`, `listTables`, `setDefaultCatalog`) — Use SQL alternatives like `DESCRIBE TABLE`, `SHOW TABLES`, and `USE CATALOG`. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]
- **`sc.parallelize` with `spark.read.json()`** — Replace with `json.loads` and `spark.createDataFrame`. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]
- **`sc.emptyRDD()` for empty DataFrames** — Use `new java.util.ArrayList[Row]()` (Scala) or `[]` (Python) instead. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]
- **`input_file_name()`** — Not supported on shared clusters with [Unity Catalog](/concepts/unity-catalog.md); use `col("_metadata.file_name")` or `col("_metadata.file_path")` instead. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution that changes how DBFS and other storage is accessed.
- Databricks File System (DBFS) — The distributed filesystem mounted to Databricks workspaces.
- Shared Clusters — Compute clusters where code runs in a shared isolation environment.
- [Job Upgrade to Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md) — Overall process for updating jobs when upgrading legacy workspaces.

## Sources

- update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md](/references/update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws-0f91bc02.md)
