---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2010ec938d4a3eb08dc8ae3d5bd4cec64e203f818e8c6c7752cf61cd980d3835
  pageDirectory: concepts
  sources:
    - work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-catalog-configuration-in-unity-catalog
    - DCCIUC
    - Default Catalog Configuration
  citations:
    - file: work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md
title: Default Catalog Configuration in Unity Catalog
description: When a workspace is enabled for Unity Catalog, a default catalog is configured; automatic enablement sets the workspace catalog as default, while manual enablement sets `hive_metastore` as default, affecting how unqualified queries resolve.
tags:
  - databricks
  - unity-catalog
  - configuration
timestamp: "2026-06-19T23:26:17.076Z"
---

# Default Catalog Configuration in [Unity Catalog](/concepts/unity-catalog.md)

The **default catalog** is a workspace-level setting in [Unity Catalog](/concepts/unity-catalog.md) that determines which catalog is used when you omit the top-level catalog name in data operations. When a workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md), a default catalog is automatically configured, and any [Three-Level Namespace](/concepts/three-level-namespace.md) references that omit the catalog component (for example, `schema.table` instead of `catalog.schema.table`) resolve to this default catalog. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Initial Default Catalog Configuration

The initial default catalog depends on how the workspace was enabled for [Unity Catalog](/concepts/unity-catalog.md):

- **Automatic enablement**: If your workspace was enabled for [Unity Catalog](/concepts/unity-catalog.md) automatically, the *workspace catalog* was set as the default catalog. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]
- **Manual enablement**: If your workspace was enabled for [Unity Catalog](/concepts/unity-catalog.md) manually, the `hive_metastore` catalog was set as the default catalog. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Transitioning from the Hive [Metastore](/concepts/metastore.md)

If you are transitioning from the legacy Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md) within an existing workspace, it makes sense to use `hive_metastore` as the default catalog. This avoids impacting existing code that references the Hive [Metastore](/concepts/metastore.md) unless you have fully migrated off it. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

For example, with `hive_metastore` set as the default catalog, the legacy three-level notation `hive_metastore.sales.sales_raw` can be shortened to `sales.sales_raw` in queries, since the catalog component is inferred. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Managing the Default Catalog

To learn how to get and switch the default catalog, see Manage the default catalog. ^[work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The account-level [Metastore](/concepts/metastore.md) governing data access and governance.
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — The legacy per-workspace [Metastore](/concepts/metastore.md) that appears as the `hive_metastore` catalog.
- [Three-Level Namespace](/concepts/three-level-namespace.md) — The `catalog.schema.table` notation used in [Unity Catalog](/concepts/unity-catalog.md).
- [Workspace Catalog](/concepts/workspace-catalog-binding.md) — The default catalog for workspaces automatically enabled for [Unity Catalog](/concepts/unity-catalog.md).
- Manage the default catalog — Documentation for viewing and changing the default catalog setting.

## Sources

- work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md

# Citations

1. [work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws.md](/references/work-with-the-legacy-hive-metastore-alongside-unity-catalog-databricks-on-aws-c5d018d3.md)
