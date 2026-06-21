---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55c108979cd0d8935d690842e507859a009c190a3eb9232dd827755797e0b74d
  pageDirectory: concepts
  sources:
    - upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-upgrade-to-unity-catalog
    - FTUTUC
    - Delta Table Upgrade to Unity Catalog
    - Delta table upgrade to Unity Catalog
  citations:
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
title: Feature table upgrade to Unity Catalog
description: Two-step process of first upgrading the underlying Delta table to Unity Catalog, then migrating feature table metadata using upgrade_workspace_table.
tags:
  - databricks
  - migration
  - workflow
timestamp: "2026-06-19T23:18:08.938Z"
---

# [Feature Table](/concepts/feature-table.md) Upgrade to [Unity Catalog](/concepts/unity-catalog.md)

**Feature table upgrade to Unity Catalog** refers to the process of migrating a workspace-level [Feature Table](/concepts/feature-table.md) (managed by the legacy workspace [Feature Store](/concepts/feature-store.md)) to a Unity Catalog–managed [Feature Table](/concepts/feature-table.md). The upgrade requires two sequential steps: first, promoting the underlying [Delta Table](/concepts/delta-lake-table.md) to [Unity Catalog](/concepts/unity-catalog.md), and then using the `UpgradeClient` API to transfer the feature table’s metadata to the new [Unity Catalog](/concepts/unity-catalog.md) location. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Prerequisites and Workflow

Before calling any upgrade API, you must upgrade the underlying workspace Delta table to [Unity Catalog](/concepts/unity-catalog.md) by following the standard migration instructions for tables and views. After the Delta table and its data are available in a [Unity Catalog](/concepts/unity-catalog.md) schema ([Three-Level Namespace](/concepts/three-level-namespace.md): `catalog.schema.table`), you can proceed with the [Feature Table](/concepts/feature-table.md) metadata upgrade. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

Databricks recommends always using the latest version of `databricks-feature-engineering` for the metadata upgrade, regardless of the Databricks Runtime version you are using. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Metadata Upgrade with `UpgradeClient`

The `databricks.feature_engineering` library provides an `UpgradeClient` class with an `upgrade_workspace_table` method. This method copies the workspace feature table’s metadata to a target table already registered in [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering --upgrade
dbutils.library.restartPython()

from databricks.feature_engineering import UpgradeClient

upgrade_client = UpgradeClient()

upgrade_client.upgrade_workspace_table(
  source_workspace_table='recommender_system.customer_features',
  target_uc_table='ml.recommender_system.customer_features'
)
```

### Metadata That Is Upgraded

The following metadata is transferred from the workspace [Feature Table](/concepts/feature-table.md) to the [Unity Catalog](/concepts/unity-catalog.md) target: ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

- Primary keys
- Time series columns
- Table and column comments (descriptions)
- Table and column tags
- Notebook and job lineage

### Handling Metadata Conflicts

If the target [Unity Catalog](/concepts/unity-catalog.md) table already has table or column comments that differ from the source workspace table, the API (in version 0.1.2 and above of `databricks-feature-engineering`) skips upgrading the comments and logs a warning. In version 0.1.2 or below, a conflict causes an error and the upgrade does not run. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

For all other metadata (primary keys, time series columns, tags, lineage), a mismatch between the source and target tables causes an error and prevents the upgrade. To bypass this error and overwrite any existing metadata on the target [Unity Catalog](/concepts/unity-catalog.md) table, pass `overwrite=True` to the API: ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

```python
upgrade_client.upgrade_workspace_table(
  source_workspace_table='recommender_system.customer_features',
  target_uc_table='ml.recommender_system.customer_features',
  overwrite=True
)
```

## Important Notes

- **Delta table upgrade must be done first.** Calling the metadata upgrade before the underlying Delta table is available in [Unity Catalog](/concepts/unity-catalog.md) will fail. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]
- **Runtime limitations.** Upgrading tags and time series columns is not supported in [Databricks Runtime 13.2 ML](/concepts/databricks-runtime-ml.md) and below. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]
- **Consumer notification.** After the upgrade, notify producers and consumers of the [Feature Table](/concepts/feature-table.md) to use the new [Unity Catalog](/concepts/unity-catalog.md) table name in all downstream code. If the target [Unity Catalog](/concepts/unity-catalog.md) table was created using `CREATE TABLE AS SELECT` or a similar cloning approach, updates made to the source workspace table are not automatically synchronized to the target table. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer to which [Feature Tables](/concepts/feature-table.md) are migrated.
- [Feature Store](/concepts/feature-store.md) – The workspace-level feature management system being replaced.
- [Delta Table](/concepts/delta-lake-table.md) – The storage format underlying [Feature Tables](/concepts/feature-table.md).
- [databricks-feature-engineering](/concepts/databricks-feature-engineering-client.md) – The Python library providing `UpgradeClient`.
- UpgradeClient – The API class for metadata migration.
- [Workspace Feature Table](/concepts/databricks-workspace-feature-store-legacy.md) – A [Feature Table](/concepts/feature-table.md) that resides in the workspace catalog (legacy).

## Sources

- upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
