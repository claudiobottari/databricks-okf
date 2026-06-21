---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d21a643d07bfc75ed53f09dd96301c54863255cbd448c984822b37c41b82cd1a
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-only-mode
    - UCOM
    - Unity Catalog Volume
    - Unity Catalog volume
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Unity Catalog Only Mode
description: A workspace admin setting that disables direct access to the legacy Hive metastore, forcing all queries to go through Unity Catalog.
tags:
  - unity-catalog
  - workspace-settings
  - data-governance
timestamp: "2026-06-19T10:13:36.288Z"
---

# Unity Catalog Only Mode

**Unity Catalog Only Mode** is a Spark configuration setting that disables direct access to the legacy Hive [Metastore](/concepts/metastore.md) for a specific compute cluster, forcing all table operations to go through [Unity Catalog](/concepts/unity-catalog.md). It is used as a gradual migration tool before permanently disabling Hive [Metastore](/concepts/metastore.md) access at the workspace level. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Purpose

During a Unity Catalog migration, you may want to reduce reliance on the legacy Hive [Metastore](/concepts/metastore.md) incrementally. Unity Catalog Only Mode allows you to test and enforce Unity Catalog usage on individual clusters before disabling the [Metastore](/concepts/metastore.md) for the entire workspace. This helps prevent regressions and ensures that all downstream jobs work correctly with Unity Catalog. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Enabling Unity Catalog Only Mode

To enable Unity Catalog Only Mode on a compute cluster, set the following Spark configurations:

```
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When Unity Catalog Only Mode is enabled, the cluster can no longer use `hive_metastore` as the default catalog, so you must specify an initial catalog that the cluster can use. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Effects

Once Unity Catalog Only Mode is active on a cluster:

- All SQL commands and DataFrame operations that attempt to access the `hive_metastore` catalog will fail.
- The cluster will not have access to tables registered in the legacy Hive [Metastore](/concepts/metastore.md) unless they are federated via [Hive Metastore Federation](/concepts/hive-metastore-federation.md).
- The `hive_metastore` catalog will not appear in the Catalog Explorer browser pane for queries running on that cluster.

These effects are similar to the workspace-level setting that disables legacy access, but scoped to a single cluster. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Use Cases

- **Incremental migration**: Enable on a few test or non-critical clusters first, validate that all workloads work with Unity Catalog, then roll out to more clusters.
- **Compliance enforcement**: Prevent users of a specific cluster from accidentally querying ungoverned Hive [Metastore](/concepts/metastore.md) tables.
- **Pre-deployment testing**: Ensure that jobs upgraded to Databricks Runtime 13.3 LTS or above work correctly without relying on the legacy [Metastore](/concepts/metastore.md).

Note that jobs running on Databricks Runtime versions below 13.3 will fail when Unity Catalog Only Mode is enabled. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Relationship to Workspace-Level Disablement

The workspace admin setting **Disable legacy access** disables the Hive [Metastore](/concepts/metastore.md) for all clusters and workloads at once. Unity Catalog Only Mode provides a more controlled, cluster-by-cluster alternative. Databricks recommends that you complete incremental testing with Unity Catalog Only Mode before permanently disabling the legacy [Metastore](/concepts/metastore.md) at the workspace level. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Disable access to Hive metastore](/concepts/disabling-direct-access-to-the-legacy-hive-metastore.md) – Workspace-level setting to fully disable legacy [Metastore](/concepts/metastore.md).
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) – Govern Hive [Metastore](/concepts/metastore.md) tables under Unity Catalog without migration.
- [Unity Catalog migration](/concepts/unity-catalog-migration-path.md) – Process of moving tables and views from Hive [Metastore](/concepts/metastore.md) to Unity Catalog.
- Spark configuration – How to set cluster-level properties.
- Default catalog – The catalog used when no catalog is explicitly specified in queries.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
