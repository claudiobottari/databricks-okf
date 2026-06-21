---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22b9eb8f576cb9c2fa615935143deb2374aee9912032bc740ac83d3326f8619e
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cluster-level-hive-metastore-disablement
    - CHMD
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Cluster-Level Hive Metastore Disablement
description: Gradually disabling direct Hive metastore access on individual compute clusters via Spark configurations during Unity Catalog migration.
tags:
  - databricks
  - spark-config
  - hive-metastore
  - compute
timestamp: "2026-06-19T18:31:24.102Z"
---

# Cluster-Level Hive [Metastore](/concepts/metastore.md) Disablement

**Cluster-Level Hive [Metastore](/concepts/metastore.md) Disablement** refers to the practice of [Disabling Direct Access to the Legacy Hive Metastore](/concepts/disabling-direct-access-to-the-legacy-hive-metastore.md) on a per-compute-cluster basis using Spark configurations. This approach allows an incremental reduction of reliance on the Hive [Metastore](/concepts/metastore.md) during a migration to [Unity Catalog](/concepts/unity-catalog.md), as opposed to disabling access for the entire workspace at once. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Configuration

To disable direct Hive [Metastore](/concepts/metastore.md) access for an individual cluster, set the following Spark configuration properties on the cluster:

```properties
spark.databricks.unityCatalogOnlyMode true
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When Unity Catalog–only mode is enabled, the cluster can no longer use `hive_metastore` as the default catalog, so an initial catalog must be specified. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Requirements

Before disabling the Hive [Metastore](/concepts/metastore.md) at the cluster level, ensure that:

- All tables registered in the legacy [Metastore](/concepts/metastore.md) that the cluster needs to query have been migrated to Unity Catalog, or the cluster does not require access to those tables.
- The cluster is running Databricks Runtime 13.3 LTS or above. Jobs running on lower versions will fail when Hive [Metastore](/concepts/metastore.md) access is disabled. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Limitations

- **No Isolation shared clusters** do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting, including cluster-level configurations. To prevent users from creating and using such clusters, enable the *Enforce User Isolation* setting for the workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- Disabling legacy access does not prevent users from using cluster-level credentials (such as instance profiles or service principals) that are available on the cluster. Databricks recommends removing such credentials from clusters after migrating. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Use During Migration

Cluster-level disablement is useful during a gradual [Unity Catalog Migration](/concepts/unity-catalog-migration-path.md). It allows teams to test and verify that their workloads function correctly without the Hive [Metastore](/concepts/metastore.md) before committing to a workspace-wide disablement. After all clusters are migrated, administrators can use the **Disable legacy access** workspace admin setting to enforce the restriction for the entire workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- Workspace-Level Hive Metastore Disablement – Disable access for all clusters at once via the workspace admin setting.
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – Govern Hive [Metastore](/concepts/metastore.md) tables under Unity Catalog without migrating them.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution that replaces the legacy Hive [Metastore](/concepts/metastore.md).
- Default Catalog – The catalog used as the default when no catalog is specified; `hive_metastore` can no longer serve as default in Unity Catalog–only mode.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The browser pane where the `hive_metastore` catalog disappears after disablement.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
