---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55e128992e770a4f95f26614d3db38026c0d0f95b3f2ea84ca8bd02fce0e0c66
  pageDirectory: concepts
  sources:
    - upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata-upgrade-scope
    - MUS
  citations:
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
title: Metadata upgrade scope
description: "The set of feature table metadata upgraded to Unity Catalog: primary keys, time series columns, comments, tags, and notebook/job lineage."
tags:
  - databricks
  - metadata
  - migration
timestamp: "2026-06-19T23:18:10.397Z"
---

# Metadata Upgrade Scope

**Metadata upgrade scope** refers to the specific set of [Feature Table](/concepts/feature-table.md) metadata that is transferred from a workspace [Feature Table](/concepts/feature-table.md) to a [Unity Catalog](/concepts/unity-catalog.md) table when using the `upgrade_workspace_table` API in [Databricks Feature Store](/concepts/databricks-feature-store.md). Understanding this scope is essential for planning migrations and anticipating potential conflicts.

## Upgraded Metadata

When upgrading a workspace [Feature Table](/concepts/feature-table.md) to [Unity Catalog](/concepts/unity-catalog.md), the following metadata is automatically transferred to the target [Unity Catalog](/concepts/unity-catalog.md) table: ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

- **Primary keys** — The column(s) designated as primary keys for the [Feature Table](/concepts/feature-table.md)
- **Time series columns** — Columns used for time-based lookups and point-in-time queries
- **Table and column comments (descriptions)** — Human-readable descriptions attached to the table or individual columns
- **Table and column tags** — Metadata tags used for classification and governance
- **Notebook and job lineage** — Information about which notebooks and jobs produce or consume the [Feature Table](/concepts/feature-table.md)

## Metadata Conflict Handling

If the target [Unity Catalog](/concepts/unity-catalog.md) table already has existing table or column comments that differ from the source workspace table, the upgrade method skips upgrading comments and logs a warning instead of failing. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

For all other metadata types (primary keys, time series columns, tags, and lineage), a mismatch between the target table and source table causes an error and prevents the upgrade from proceeding. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

### Overwriting Existing Metadata

To bypass the error and overwrite any existing metadata on the target [Unity Catalog](/concepts/unity-catalog.md) table, pass `overwrite = True` to the API: ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

```python
upgrade_client.upgrade_workspace_table(
  source_workspace_table='recommender_system.customer_features',
  target_uc_table='ml.recommender_system.customer_features',
  overwrite=True
)
```

## Prerequisites

Before calling the upgrade API, you must first upgrade the underlying workspace Delta table to [Unity Catalog](/concepts/unity-catalog.md). The metadata upgrade only handles the [Feature Store](/concepts/feature-store.md) metadata layer; the underlying data must already be accessible in [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Version Limitations

Upgrading tags and time series columns is not supported in Databricks Runtime 13.2 ML and below. Databricks recommends always using the latest version of `databricks-feature-engineering` for this operation, regardless of the Databricks Runtime version you are using. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Post-Upgrade Considerations

After upgrading, producers and consumers of the [Feature Table](/concepts/feature-table.md) must be notified to start using the new table name in [Unity Catalog](/concepts/unity-catalog.md). If the target table in [Unity Catalog](/concepts/unity-catalog.md) was upgraded using `CREATE TABLE AS SELECT` or a similar method that cloned the source table, updates to the source table are not automatically synchronized in the target table. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The workspace-level [Feature Store](/concepts/feature-store.md) that stores [Feature Tables](/concepts/feature-table.md)
- [Unity Catalog](/concepts/unity-catalog.md) — The governance catalog that serves as the target for upgrades
- UpgradeClient — The API client used to perform metadata upgrades
- Delta Table Upgrade to Unity Catalog — The prerequisite step for upgrading the underlying data
- Feature Table Lineage — Notebook and job lineage that is preserved during upgrade

## Sources

- upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
