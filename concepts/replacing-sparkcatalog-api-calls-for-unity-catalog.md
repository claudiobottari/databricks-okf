---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 316d8d224c560aa548ce2323784e0b4f98fe4db876b835e815dcb7f968d5891c
  pageDirectory: concepts
  sources:
    - update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - replacing-sparkcatalog-api-calls-for-unity-catalog
    - RSACFUC
  citations:
    - file: update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md
title: Replacing spark.catalog API Calls for Unity Catalog
description: Workarounds for spark.catalog.tableExists, listTables, and setDefaultCatalog using SQL equivalents when running on shared clusters with Unity Catalog.
tags:
  - databricks
  - spark
  - unity-catalog
  - migration
timestamp: "2026-06-19T23:16:47.742Z"
---

# Replacing spark.catalog API Calls for [Unity Catalog](/concepts/unity-catalog.md)

**Replacing spark.catalog API Calls for Unity Catalog** refers to the modifications required when upgrading legacy Databricks workspaces to [Unity Catalog](/concepts/unity-catalog.md), where certain `spark.catalog` methods (such as `tableExists`, `listTables`, and `setDefaultCatalog`) behave differently on shared clusters and may need to be replaced with SQL-based alternatives. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Overview

When you upgrade legacy workspaces to [Unity Catalog](/concepts/unity-catalog.md), job notebooks that use `spark.catalog.X` on a [Shared Cluster](/concepts/no-isolation-shared-clusters.md) may require code changes. The `spark.catalog` API behaves differently under [Unity Catalog](/concepts/unity-catalog.md)'s security model, and some methods may not work as expected on shared cluster access mode. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Required Databricks Runtime Version

The recommended approach is to use **Databricks Runtime 14.2 or above**, which provides better compatibility with `spark.catalog` APIs on shared clusters in [Unity Catalog](/concepts/unity-catalog.md) environments. If a Databricks Runtime upgrade is not possible, you must use SQL-based workarounds for affected methods. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

## Replacing Specific spark.catalog Methods

### tableExists

Instead of `spark.catalog.tableExists(tablename)`, use a SQL `DESCRIBE TABLE` call wrapped in a try-except block: ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

```python
def tableExistsSql(tablename):
    try:
        spark.sql(f"DESCRIBE TABLE {tablename};")
    except Exception as e:
        return False
    return True

tableExistsSql("catalog.schema.my_table")
```

### listTables

Instead of `spark.catalog.listTables()`, use the SQL `SHOW TABLES` command, which also supports restricting by database or pattern matching. ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

### setDefaultCatalog

Instead of `spark.catalog.setDefaultCatalog(catalog_name)`, use the SQL command: ^[update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md]

```python
spark.sql("USE CATALOG <catalog_name>")
```

## Related Changes

When upgrading jobs for [Unity Catalog](/concepts/unity-catalog.md), you may also need to address other compatibility issues on shared clusters:

- Replacing sc.parallelize with json.loads – For reading JSON data.
- Replacing sc.emptyRDD for Empty DataFrames – For creating empty DataFrames.
- Replacing input_file_name with _metadata – The `input_file_name()` function is not supported in [Unity Catalog](/concepts/unity-catalog.md) on shared clusters; use `_metadata.file_name` or `_metadata.file_path` instead.
- Migrating DBFS Operations to Volumes – Direct file operations on DBFS via FUSE are not supported; use `dbutils`, `spark`, or [Unity Catalog](/concepts/unity-catalog.md) Volumes.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Shared Cluster Access Mode
- Databricks Runtime 14.2
- Data Governance in Unity Catalog
- [Job Migration to Unity Catalog](/concepts/upgrading-jobs-to-unity-catalog.md)

## Sources

- update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md

# Citations

1. [update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws.md](/references/update-jobs-when-you-upgrade-legacy-workspaces-to-unity-catalog-databricks-on-aws-0f91bc02.md)
