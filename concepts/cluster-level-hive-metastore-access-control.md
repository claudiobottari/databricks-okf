---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea3840b701086ec654c241e28da10c69f98b3930414a8484e993b7f87ebada03
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cluster-level-hive-metastore-access-control
    - CHMAC
    - Enable Hive Metastore Table Access Control on a Cluster
  citations:
    - file: disable-hms.md
title: Cluster-level Hive Metastore Access Control
description: Using Spark configurations (spark.databricks.unityCatalogOnlyMode and spark.databricks.sql.initial.catalog.namespace) to disable Hive metastore access on individual compute clusters
tags:
  - databricks
  - spark-config
  - hive-metastore
timestamp: "2026-06-19T15:11:47.109Z"
---

# Cluster-level Hive [Metastore](/concepts/metastore.md) Access Control

**Cluster-level Hive [Metastore](/concepts/metastore.md) Access Control** refers to the ability to disable direct access to the legacy Hive [Metastore](/concepts/metastore.md) on a per-cluster basis using Spark configuration settings, rather than applying a workspace-wide policy. This approach is useful during a gradual migration to [Unity Catalog](/concepts/unity-catalog.md) when organizations want to incrementally reduce reliance on the Hive [Metastore](/concepts/metastore.md).[^disable-hms.md]

## Overview

Even after migrating data to Unity Catalog, Databricks compute clusters continue to connect to the [Hive Metastore](/concepts/built-in-hive-metastore.md) by default unless explicitly disabled. Cluster-level access control allows administrators to disable this connection on individual clusters, enabling a phased migration strategy where some clusters run in Unity Catalog-only mode while others still access Hive [Metastore](/concepts/metastore.md) tables.[^disable-hms.md]

This granular approach is particularly valuable when you want to identify and resolve issues with specific workloads before disabling the Hive [Metastore](/concepts/metastore.md) workspace-wide.[^disable-hms.md]

## Configuration

To disable direct Hive [Metastore](/concepts/metastore.md) access for an individual cluster, set the following Spark configurations on the cluster:

```python
spark.databricks.unityCatalogOnlyMode True
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of a [Unity Catalog](/concepts/unity-catalog.md) catalog that exists in your [Metastore](/concepts/metastore.md). When Unity Catalog-only mode is enabled, you must specify an initial catalog because the cluster can no longer use `hive_metastore` as the default catalog.[^disable-hms.md]

## Behavior After Configuration

Once these Spark configurations are applied to a cluster:

- Jobs running against tables registered in the Hive [Metastore](/concepts/metastore.md) will fail.
- Fallback to the Hive [Metastore](/concepts/metastore.md) is disabled.
- The **Legacy** heading and `hive_metastore` catalog disappear from [Catalog Explorer](/concepts/catalog-explorer.md).
- SQL commands attempting to show the contents of the `hive_metastore` catalog will fail.[^disable-hms.md]

## Usage During Migration

Cluster-level access control supports a gradual migration strategy during [Unity Catalog Migration](/concepts/unity-catalog-migration-path.md). Organizations can:

1. Identify clusters that can safely operate in Unity Catalog-only mode.
2. Apply the Spark configuration to those clusters.
3. Monitor for any failed jobs or dependencies on Hive [Metastore](/concepts/metastore.md) tables.
4. Migrate remaining tables or adjust workloads before applying a workspace-wide disable.[^disable-hms.md]

## Comparison with Workspace-Level Control

| Feature | Cluster-Level | Workspace-Level |
|---------|---------------|-----------------|
| Scope | Individual clusters | Entire workspace |
| Configuration Method | Spark configurations | Workspace admin setting (Disable legacy access) |
| Use Case | Gradual migration, testing | Final lockdown after migration complete |
| Effect on Running Jobs | Continues until terminated | Continues until terminated; restarts fail on Runtime < 13.3 |

^[disable-hms.md]

## Prerequisites

Before enabling Unity Catalog-only mode on a cluster:

- Jobs must run on Databricks Runtime 13.3 LTS or above. Clusters running older runtimes will fail.
- Tables registered in the legacy Hive [Metastore](/concepts/metastore.md) should already be migrated to Unity Catalog, or you must be prepared for related jobs to fail.[^disable-hms.md]

## Limitations

Cluster-level configuration does not prevent users from using cluster-level credentials (such as instance profiles or service principals) that are available on a cluster. Databricks recommends removing such credentials from clusters.[^disable-hms.md]

Additionally, _No Isolation shared_ clusters do not respect this setting. To prevent users from creating such clusters, enable the **Enforce User Isolation** workspace setting.[^disable-hms.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that replaces the Hive [Metastore](/concepts/metastore.md).
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Allows Unity Catalog to govern tables registered in a Hive [Metastore](/concepts/metastore.md).
- [Disable Legacy Access Workspace Setting](/concepts/disable-legacy-hive-metastore-access-workspace-setting.md) — The workspace-level equivalent of this control.
- Spark Configuration — How to configure cluster settings on Databricks.
- Default Catalog — The catalog used when no catalog is specified in queries.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. disable-hms.md
