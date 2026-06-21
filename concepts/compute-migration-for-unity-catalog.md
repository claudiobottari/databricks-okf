---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43c08a7ab59fbf94038400646a07dbe558274d30e3a0e5a1a4f0b4d813b4c282
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compute-migration-for-unity-catalog
    - CMFUC
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
title: Compute Migration for Unity Catalog
description: The requirement to upgrade all-purpose and job compute resources to Databricks Runtime 13.3 LTS or above and supported access modes for Unity Catalog compatibility.
tags:
  - databricks
  - unity-catalog
  - compute
  - runtime
timestamp: "2026-06-19T23:17:53.836Z"
---

# Compute Migration for [Unity Catalog](/concepts/unity-catalog.md)

**Compute Migration for Unity Catalog** refers to the process of upgrading existing compute resources (all-purpose clusters and job compute) to Databricks Runtime version 13.3 LTS or above and switching to Unity Catalog–compatible [access modes](/concepts/standard-access-mode.md). This migration is a required step when upgrading a workspace that previously did not use [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Overview

During a [Unity Catalog](/concepts/unity-catalog.md) upgrade, all compute resources that run in legacy Databricks Runtime versions or in legacy access modes must be updated. Databricks recommends that every compute resource used with [Unity Catalog](/concepts/unity-catalog.md) run on [Databricks Runtime 13.3 LTS](/concepts/databricks-runtime-133-lts.md) or later and use a supported access mode (e.g., single-user or shared, but not no-isolation shared). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Locating Compute Resources to Migrate

You can manually review compute on the workspace’s **Compute** page. In the **All-purpose compute** and **Job compute** sections, sort or filter by the Databricks Runtime version to identify clusters running versions below 13.3 LTS. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

For a programmatic approach, query the `system.compute.clusters` table. You must be a Databricks account admin or have been granted `USE` and `SELECT` permissions on the `compute` system schema to access this system table. The following query returns all compute resources (both all-purpose and job compute) running on Databricks Runtime versions below 13.3 LTS:

```sql
SELECT
  workspace_id,
  cluster_id,
  dbr_version
FROM system.compute.clusters
WHERE
  TRY_CAST(SPLIT(dbr_version, '\\.')[0] AS INT) < 13
  OR (
    TRY_CAST(SPLIT(dbr_version, '\\.')[0] AS INT) = 13
    AND TRY_CAST(SPLIT(dbr_version, '\\.')[1] AS INT) < 3
  );
```

^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Migrating Compute to Supported Access Modes

After upgrading the Databricks Runtime version, you must also verify that compute resources do not use the no-isolation shared access mode. To identify compute in `'NONE'` or `'NO_ISOLATION'` data security modes, query the same system table:

```sql
SELECT
  workspace_id,
  cluster_id,
  dbr_version,
  data_security_mode
FROM system.compute.clusters
WHERE data_security_mode IN ('NONE','NO_ISOLATION')
LIMIT 100;
```

^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

Upgrade such compute to a supported access mode (e.g., single-user, shared, or user isolation). See [access modes](/concepts/standard-access-mode.md) for full documentation.

## Post-Migration Steps

After all compute has been upgraded and is using [Unity Catalog](/concepts/unity-catalog.md) access modes, workspace admins can disable no-isolation shared compute resources to prevent creation of new legacy clusters. This is done through account-level settings. See [Enable admin protection for no isolation shared clusters](/concepts/no-isolation-shared-clusters.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Access modes (compute)](/concepts/standard-access-mode-compute.md)
- [Hive metastore migration to Unity Catalog](/concepts/hive-metastore-federation-to-unity-catalog.md)
- System tables
- [DBFS disablement](/concepts/databricks-connect-service-disabling.md)

## Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
