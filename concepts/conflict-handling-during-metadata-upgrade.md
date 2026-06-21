---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c663dddcacc0694aabfe6808bdf13eb31c3b707a3a6db2e871db20482b8fbde
  pageDirectory: concepts
  sources:
    - upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conflict-handling-during-metadata-upgrade
    - CHDMU
  citations:
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
title: Conflict handling during metadata upgrade
description: "Behavior when source and target table metadata differs: comments are skipped with a warning (or cause an error in older versions), other mismatches cause errors unless overwrite=True is passed."
tags:
  - databricks
  - error-handling
  - migration
timestamp: "2026-06-19T23:18:30.085Z"
---

# Conflict Handling During Metadata Upgrade

**Conflict handling during metadata upgrade** refers to how the [Databricks Feature Store](/concepts/databricks-feature-store.md) API manages discrepancies between source workspace [Feature Table](/concepts/feature-table.md) metadata and target [Unity Catalog](/concepts/unity-catalog.md) table metadata when using `upgrade_workspace_table`. The upgrade process transfers metadata such as primary keys, time series columns, comments, tags, and lineage from a workspace [Feature Table](/concepts/feature-table.md) to a [Unity Catalog](/concepts/unity-catalog.md) table. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Metadata Upgrade Process

To upgrade a workspace [Feature Table](/concepts/feature-table.md) to [Unity Catalog](/concepts/unity-catalog.md), you first upgrade the underlying Delta table, then use the `UpgradeClient.upgrade_workspace_table()` API to migrate the [Feature Table](/concepts/feature-table.md) metadata. The following metadata is transferred: ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

- Primary keys
- Time series columns
- Table and column comments (descriptions)
- Table and column tags
- Notebook and job lineage

The API is part of the `databricks-feature-engineering` library. Databricks recommends always using the latest version of this library for the upgrade operation. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Conflict Types and Handling

The upgrade API handles conflicts differently depending on the type of metadata and the library version in use.

### Comments (Descriptions)

If the target [Unity Catalog](/concepts/unity-catalog.md) table has existing table or column comments that differ from the source workspace [Feature Table](/concepts/feature-table.md), the upgrade method **skips upgrading comments** and logs a warning. The upgrade proceeds for other metadata. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Other Metadata (Primary Keys, Time Series Columns, Tags, Lineage)

For all other metadata (primary keys, time series columns, tags, and lineage), a mismatch between the target table and source table causes an **error** and prevents the upgrade from running. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Library Version Compatibility

- **Version 0.1.2 and below**: If comments differ, an error is thrown and the upgrade does not run. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]
- **Version 0.1.3 and above**: Comments are skipped with a warning, and the upgrade continues. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Overwriting Existing Metadata

To bypass the error and overwrite any existing metadata on the target [Unity Catalog](/concepts/unity-catalog.md) table, pass `overwrite=True` to the `upgrade_workspace_table()` API. This forces the upgrade to replace the target table's metadata with the source table's metadata, regardless of conflicts. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Example with Overwrite

```python
from databricks.feature_engineering import UpgradeClient

upgrade_client = UpgradeClient()
upgrade_client.upgrade_workspace_table(
  source_workspace_table='recommender_system.customer_features',
  target_uc_table='ml.recommender_system.customer_features',
  overwrite=True
)
```

^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before calling the upgrade API, you must first upgrade the underlying workspace Delta table to [Unity Catalog](/concepts/unity-catalog.md). Follow the instructions for upgrading tables and views to [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Additional Considerations

- Upgrading tags and time series columns is not supported in Databricks Runtime 13.2 ML and below. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]
- Notify producers and consumers of the upgraded [Feature Table](/concepts/feature-table.md) to start using the new table name in [Unity Catalog](/concepts/unity-catalog.md). If the target table was upgraded using `CREATE TABLE AS SELECT` or a similar method that cloned the source table, updates to the source table are not automatically synchronized in the target table. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The workspace-level [Feature Store](/concepts/feature-store.md) that stores [Feature Tables](/concepts/feature-table.md) with metadata.
- [Unity Catalog](/concepts/unity-catalog.md) — The target catalog for upgrading [Feature Table](/concepts/feature-table.md) metadata.
- [Delta Table Upgrade](/concepts/delta-table-repair.md) — The prerequisite step for upgrading the underlying data.
- UpgradeClient — The API client used for [Feature Table](/concepts/feature-table.md) metadata upgrades.
- [Databricks Feature Engineering Library](/concepts/databricks-feature-engineering-client.md) — The Python library containing the upgrade functionality.

## Sources

- upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
