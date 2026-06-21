---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2681c2cca9449d4c18211d48320af5073934d0af9cc7d1740a7222d76ab17ce3
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cluster-level-hms-access-control
    - CHAC
    - cluster-level-hive-metastore-access-control
    - CHMAC
    - Enable Hive Metastore Table Access Control on a Cluster
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Cluster-Level HMS Access Control
description: The ability to disable Hive metastore access on a per-cluster basis using Spark configurations (spark.databricks.unityCatalogOnlyMode and spark.databricks.sql.initial.catalog.namespace).
tags:
  - unity-catalog
  - compute-clusters
  - spark-configuration
timestamp: "2026-06-19T10:13:41.410Z"
---

# Cluster-Level HMS Access Control

**Cluster-Level HMS Access Control** refers to the ability to disable direct access to the legacy Hive [Metastore](/concepts/metastore.md) on a per-cluster basis within a Databricks workspace, providing a gradual migration path away from Hive [Metastore](/concepts/metastore.md) dependency toward Unity Catalog governance. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Overview

When migrating to [Unity Catalog](/concepts/unity-catalog.md), organizations may want to reduce reliance on the legacy Hive [Metastore](/concepts/metastore.md) incrementally rather than disabling access for the entire workspace at once. Cluster-level HMS access control allows administrators to enforce Unity Catalog-only mode on individual compute clusters, forcing jobs and queries on those clusters to use Unity Catalog catalogs instead of the `hive_metastore` catalog.^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Configuration

To disable direct Hive [Metastore](/concepts/metastore.md) access on a specific cluster, set the following Spark configurations on the cluster:^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

```
spark.databricks.unityCatalogOnlyMode true
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your [Metastore](/concepts/metastore.md). When you enable Unity Catalog-only mode, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog.^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Use Cases

Cluster-level HMS access control is particularly useful during a Unity Catalog migration when you want to:^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

- Test that workloads function correctly with Unity Catalog before disabling the legacy [Metastore](/concepts/metastore.md) workspace-wide.
- Gradually migrate teams or applications off the Hive [Metastore](/concepts/metastore.md) one cluster at a time.
- Maintain backward compatibility for some clusters while enforcing new governance standards on others.

## Requirements

Before enabling Unity Catalog-only mode on a cluster, jobs running on that cluster must be upgraded to Databricks Runtime 13.3 LTS or above. Clusters running older runtime versions will fail when Unity Catalog-only mode is enabled.^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Comparison with Workspace-Level Control

Cluster-level access control complements the workspace-level **Disable legacy access** admin setting. While the workspace setting disables Hive [Metastore](/concepts/metastore.md) access for all clusters and workloads at once, the cluster-level approach allows a staged, controlled rollout.^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

| Approach | Scope | Use Case |
|----------|-------|----------|
| Spark configuration per cluster | Individual compute resources | Gradual migration, testing |
| Workspace admin setting | Entire workspace | Final lockdown after migration completion |

## Important Considerations

- After disabling Hive [Metastore](/concepts/metastore.md) access on a cluster, the **Legacy** heading and `hive_metastore` catalog disappear from Catalog Explorer for that cluster's workloads. SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- Disabling legacy access does not prevent users from using cluster-level credentials, such as instance profiles or service principals, that are available on a cluster. Databricks recommends removing such credentials from clusters.^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]
- _No Isolation shared_ clusters do not respect the legacy Hive [Metastore](/concepts/metastore.md) disablement setting. To prevent users from creating and using such clusters, enable the **Enforce User Isolation** setting for the workspace.^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Migration](/concepts/unity-catalog-migration-path.md) — The broader process of moving from Hive [Metastore](/concepts/metastore.md) to Unity Catalog
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Governing Hive [Metastore](/concepts/metastore.md) tables through Unity Catalog without moving data
- [Workspace-Level HMS Access Control](/concepts/databricks-workspace-level-table-access-control-setting.md) — Disabling legacy access for an entire workspace
- [Default Catalog Configuration](/concepts/default-catalog-configuration-in-unity-catalog.md) — Setting a Unity Catalog catalog as the default for clusters
- Enforce User Isolation — Cluster setting that prevents shared cluster bypass of HMS controls

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
