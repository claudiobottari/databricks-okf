---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2719ad93ab96d1feb72c1345dea59bcdad5f43f10de04bfa63db4c23ec2f3556
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbfs-migration-to-unity-catalog-volumes
    - DMTUCV
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
title: DBFS Migration to Unity Catalog Volumes
description: The process of migrating raw files, notebooks, scripts, and init scripts from DBFS root and mounts to governed Unity Catalog volumes and workspace files.
tags:
  - databricks
  - unity-catalog
  - dbfs
  - migration
timestamp: "2026-06-19T23:18:14.398Z"
---

# DBFS Migration to [Unity Catalog](/concepts/unity-catalog.md) Volumes

**DBFS Migration to [Unity Catalog](/concepts/unity-catalog.md) Volumes** is the process of moving files stored in the Databricks File System (DBFS) — including raw data files, build artifacts, notebooks, and init scripts — to Unity Catalog Volumes as part of upgrading a workspace to [Unity Catalog](/concepts/unity-catalog.md). Databricks recommends migrating away from DBFS to ensure all data and workflows are governed by [Unity Catalog](/concepts/unity-catalog.md)'s security and access control model. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Overview

As part of a [Unity Catalog](/concepts/unity-catalog.md) upgrade](/en/data-governance/unity-catalog/upgrade/), disabling access to DBFS ensures that all data assets are governed by [Unity Catalog](/concepts/unity-catalog.md). The migration involves three main categories of assets: raw files stored in DBFS root or mounts, workspace assets such as notebooks and scripts, and compute-scoped init scripts. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

The [DBFS scanner scripts](https://github.com/databrickslabs/sandbox/tree/main/dbfs-scanner) by Databricks Labs can help scan current DBFS usage and decide whether to register assets in place using an [External location](/concepts/external-location.md), migrate to [Unity Catalog](/concepts/unity-catalog.md), or archive them. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Migrating Raw Files

Raw files stored in DBFS root (such as under `/FileStore` or other DBFS root directories) or in cloud storage mounted to DBFS (under `/mnt/...`) should be migrated to [Unity Catalog](/concepts/unity-catalog.md) volumes and accessed via [external locations](/concepts/external-location.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 1: Set Up an [External location](/concepts/external-location.md)

Create a [Unity Catalog](/concepts/unity-catalog.md) [External location](/concepts/external-location.md) for the cloud storage container or path where the files currently reside. This can be done using [Catalog Explorer](/concepts/catalog-explorer.md), SQL commands, Terraform, or the Databricks CLI. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 2: Create a Volume

[Unity Catalog](/concepts/unity-catalog.md) volumes provide a governed way to organize files. Databricks recommends using volumes for all non-tabular data. Create an external volume in a schema that refers to a subpath of your [External location](/concepts/external-location.md). For example: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```sql
USE CATALOG main;
USE SCHEMA data;
CREATE VOLUME IF NOT EXISTS raw_files
LOCATION 'my_data_loc/csv-files/';
```

All files under that path become accessible through the [External location](/concepts/external-location.md) and governed by [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 3: Copy Files from DBFS Root

If files were previously stored in DBFS root, copy them to the cloud storage path using `dbutils.fs.cp`: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```python
dbutils.fs.cp(
  "dbfs:/FileStore/tables/data.csv",
  "/Volumes/main/data/raw_files/data.csv"
)
```

For large numbers of files or files larger than a few GB, consider using the Databricks CLI `fs cp` command or a distributed copy using Apache Spark to parallelize the move. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 4: Verify Migrated Files

After migration, list and read files from volumes using standard commands: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```python
# List files in the volume
dbutils.fs.ls("/Volumes/main/data/raw_files/")

# Read a CSV file into a DataFrame
df = spark.read.option("header", True).csv(
  "/Volumes/main/data/raw_files/2024-01-01-data.csv"
)
```

This requires appropriate [Unity Catalog](/concepts/unity-catalog.md) permissions on the volume or [External location](/concepts/external-location.md). [Unity Catalog](/concepts/unity-catalog.md) enforces that the principal reading the file has `READ` permission on the volume or [External location](/concepts/external-location.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Step 5: Clean Up DBFS Mounts

After verification, unmount old DBFS mount points to prevent confusion or accidental use: ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

```python
dbutils.fs.unmount("/mnt/oldpath")
```

Consider locking down or deleting data in DBFS root if it has been moved, because leaving copies can lead to inconsistent updates or security risks. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Migrating Workspace Assets from DBFS

Workspace assets such as notebooks, code files, or reference scripts stored on DBFS should be migrated to appropriate [Unity Catalog](/concepts/unity-catalog.md) or workspace locations. DBFS does not provide per-file access control and should not be used for source code or notebooks. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

- **Notebooks**: If stored as HTML or DBC files in `/FileStore`, import them into the Databricks workspace using the UI or CLI. Store notebooks as workspace objects or in [Git folders](/concepts/databricks-git-folders-for-cicd.md) and use Git for version control. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Job scripts**: Move Python scripts or JAR files referenced in Databricks jobs (e.g., `dbfs:/mnt/scripts/my_etl.py`) to workspace files and manage them in a Git folder. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Build artifacts and libraries**: Store JAR files and Python wheels in [Unity Catalog](/concepts/unity-catalog.md) volumes. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]
- **Compute-scoped init scripts**: Store init scripts previously stored in DBFS (e.g., `dbfs:/databricks/init/...`) in [Unity Catalog](/concepts/unity-catalog.md) volumes. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Disabling DBFS After Migration

After completing the migration of all data and workflows that rely on DBFS root or mounts, and upgrading all jobs and clusters to [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) or above, workspace admins can disable DBFS in existing workspaces. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Unity Catalog Volumes — Governed storage for non-tabular data
- [External locations](/concepts/external-location.md) — Cloud storage paths registered in [Unity Catalog](/concepts/unity-catalog.md)
- [Unity Catalog upgrade](/concepts/unity-catalog-upgrade-process.md) — Full process for migrating a workspace to [Unity Catalog](/concepts/unity-catalog.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Alternative approach for table migration
- Workspace files — Storage for notebooks and code files
- [Git folders](/concepts/databricks-git-folders-for-cicd.md) — Version-controlled workspace file management

## Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
