---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f8a83dc9c00e91e0e121b2d2caa454cc8b1057e7e15a4ea9cbd92e3aed83625
  pageDirectory: concepts
  sources:
    - upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - upgrade_workspace_table-method
    - UpgradeClient.upgrade_workspace_table
  citations:
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 5
      end: 6
    - file: 37-38
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 8
      end: 9
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 12
      end: 18
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 20
      end: 24
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 26
      end: 30
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 28
      end: 28
    - file: inferred from the source's mention of the older behavior
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 31
      end: 35
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 39
      end: 40
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
      start: 41
      end: 43
title: upgrade_workspace_table method
description: API method that migrates metadata (primary keys, time series columns, comments, tags, lineage) from a workspace feature table to a target Unity Catalog table.
tags:
  - databricks
  - api
  - migration
timestamp: "2026-06-19T23:18:01.822Z"
---

# upgrade_workspace_table method

The **`upgrade_workspace_table` method** migrates the metadata of an existing workspace [Feature Table](/concepts/feature-table.md) from the legacy workspace-level [Feature Store](/concepts/feature-store.md) to [Unity Catalog](/concepts/unity-catalog.md). It is part of the `UpgradeClient` class in the `databricks-feature-engineering` library. The method does **not** move the underlying Delta table data; instead, it upgrades only the [Feature Table](/concepts/feature-table.md) metadata so that it points to a [Unity Catalog](/concepts/unity-catalog.md) table that must already exist. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

Before calling `upgrade_workspace_table`, you must first upgrade the underlying workspace Delta table to [Unity Catalog](/concepts/unity-catalog.md). This is a prerequisite step described in the Databricks guide on [Upgrade tables and views to [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate). Without this step, the API will fail. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:5-6,37-38]

## Usage

Instantiate an `UpgradeClient` and call the method with the source workspace table name and the target [Unity Catalog](/concepts/unity-catalog.md) table name. Databricks recommends always using the latest version of `databricks-feature-engineering` for this operation, regardless of the Databricks Runtime version. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:8-9]

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

^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:12-18]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `source_workspace_table` | `str` | Fully qualified name of the existing workspace [Feature Table](/concepts/feature-table.md) (e.g., `database.table`). |
| `target_uc_table` | `str` | Fully qualified three-level name of the target [Unity Catalog](/concepts/unity-catalog.md) table (e.g., `catalog.schema.table`). |
| `overwrite` | `bool` | Optional. When `True`, overwrites any existing metadata on the target [Unity Catalog](/concepts/unity-catalog.md) table, bypassing mismatch errors. Defaults to `False`. |

## Metadata upgraded

The method upgrades the following metadata from the workspace [Feature Table](/concepts/feature-table.md) to the [Unity Catalog](/concepts/unity-catalog.md) table:

- Primary keys
- Time series columns
- Table and column comments (descriptions)
- Table and column tags
- Notebook and job lineage

^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:20-24]

## Behavior with comments and metadata mismatches

If the target [Unity Catalog](/concepts/unity-catalog.md) table already has table or column comments that differ from the source workspace table, the upgrade method **skips** upgrading those comments and logs a warning. For all other metadata (primary keys, tags, lineage, etc.), a mismatch between the target and source causes an error and prevents the upgrade. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:26-30]

### Version‑specific comment handling

- **Version 0.1.2 or below** of `databricks-feature-engineering`: If a comment mismatch is detected, the method throws an error and the upgrade does **not** run. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:28]
- **Version 0.1.3+**: Comment mismatches are handled gracefully by skipping the conflicting comments and continuing with the upgrade. ^[inferred from the source's mention of the older behavior]

## Overwrite flag

To bypass errors caused by any metadata mismatch (including comments) and overwrite existing metadata on the target [Unity Catalog](/concepts/unity-catalog.md) table, pass `overwrite=True`:

```python
upgrade_client.upgrade_workspace_table(
  source_workspace_table='recommender_system.customer_features',
  target_uc_table='ml.recommender_system.customer_features',
  overwrite=True
)
```

^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:31-35]

## Runtime limitations

Upgrading **tags** and **time series columns** is **not supported** in Databricks Runtime 13.2 ML and below. Users on those runtimes must upgrade to a more recent runtime to migrate those metadata elements. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:39-40]

## Post‑upgrade considerations

After the upgrade, producers and consumers of the [Feature Table](/concepts/feature-table.md) must be notified to start using the new [Unity Catalog](/concepts/unity-catalog.md) table name. The workspace table and the [Unity Catalog](/concepts/unity-catalog.md) table are **not automatically synchronized**; updates to the source table are not propagated to the target table if the target table was created via `CREATE TABLE AS SELECT` or a similar clone operation. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:41-43]

## Related concepts

- UpgradeClient – The class that provides `upgrade_workspace_table`.
- [databricks-feature-engineering](/concepts/databricks-feature-engineering-client.md) – The Python library containing `UpgradeClient`.
- [Feature Store](/concepts/feature-store.md) – The legacy workspace-level [Feature Store](/concepts/feature-store.md).
- [Unity Catalog](/concepts/unity-catalog.md) – The target catalog system for upgraded [Feature Tables](/concepts/feature-table.md).
- [Delta table](/concepts/delta-lake-table.md) – The underlying storage format that must be upgraded first.
- Upgrade tables and views to Unity Catalog – The prerequisite Delta upgrade process.

## Sources

- upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
2. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:5-6](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
3. 37-38
4. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:8-9](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
5. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:12-18](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
6. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:20-24](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
7. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:26-30](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
8. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:28-28](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
9. inferred from the source's mention of the older behavior
10. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:31-35](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
11. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:39-40](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
12. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md:41-43](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
