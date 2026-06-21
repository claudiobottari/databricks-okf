---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: deaf4a2a9837d3f1a9dee3d906cec943bf40cd35253a215c85f93342db63585f
  pageDirectory: concepts
  sources:
    - disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-only-mode-spark-configuration
    - UCOMSC
  citations:
    - file: disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md
title: Unity Catalog Only Mode Spark Configuration
description: Spark settings spark.databricks.unityCatalogOnlyMode and spark.databricks.sql.initial.catalog.namespace to enforce Unity Catalog exclusively on a cluster.
tags:
  - databricks
  - spark-config
  - unity-catalog
  - compute
timestamp: "2026-06-19T18:31:56.327Z"
---

# Unity Catalog-Only Mode (Spark Configuration)

**Unity Catalog-Only Mode** is a Spark configuration that disables direct access to the legacy Hive [Metastore](/concepts/metastore.md) on a per‑cluster basis. When enabled, the cluster cannot read or write tables registered in the Hive [Metastore](/concepts/metastore.md) (whether the workspace-local [Metastore](/concepts/metastore.md), an external Hive [Metastore](/concepts/metastore.md), or AWS Glue). This mode forces all data access to go through Unity Catalog, helping organizations transition away from the legacy [Metastore](/concepts/metastore.md) gradually. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Configuration

To enable Unity Catalog-Only Mode on a cluster, set the following Spark properties:

```properties
spark.databricks.unityCatalogOnlyMode true
spark.databricks.sql.initial.catalog.namespace <catalog-name>
```

Replace `<catalog-name>` with the name of an existing Unity Catalog catalog that should serve as the default catalog for the cluster. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Requirement for an Initial Catalog

When Unity Catalog-Only Mode is active, the cluster can no longer use `hive_metastore` as the default catalog. Therefore, you must explicitly set an initial catalog using `spark.databricks.sql.initial.catalog.namespace`. This ensures that SQL queries and DataFrame operations have a valid default namespace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Use Case: Gradual Migration

Unity Catalog-Only Mode is useful during a [Unity Catalog migration](/concepts/unity-catalog-migration-path.md) when you want to reduce reliance on the Hive [Metastore](/concepts/metastore.md) incrementally. By enabling the mode on individual compute clusters, you can test and validate that workloads work correctly with Unity Catalog before disabling the Hive [Metastore](/concepts/metastore.md) globally for the entire workspace. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Workspace‑Level Alternative

As an alternative to the per‑cluster configuration, workspace admins can disable all direct access to the Hive [Metastore](/concepts/metastore.md) for the entire workspace via the **Disable legacy access** workspace admin setting. The per‑cluster approach provides a more controlled, gradual migration path. ^[disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Federation](/concepts/hive-metastore-federation.md) — Govern Hive [Metastore](/concepts/metastore.md) tables through Unity Catalog without migrating them.
- Disable Legacy Access (Workspace Setting) — Global disablement of Hive [Metastore](/concepts/metastore.md) access.
- Fallback (HMS Federation) — How fallback behavior is affected when Unity Catalog-Only Mode is enabled.
- Default Catalog — Configuration of a default catalog in Unity Catalog.

## Sources

- disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md

# Citations

1. [disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws.md](/references/disable-access-to-the-hive-metastore-used-by-your-databricks-workspace-databricks-on-aws-167baf61.md)
