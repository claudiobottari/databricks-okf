---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16e440c24ada01a39f7ade25056fd16c29a4975ecaae7791c1b8d8d22c1aadd0
  pageDirectory: concepts
  sources:
    - upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prerequisites-for-upgrading-feature-tables-to-unity-catalog
    - PFUFTTUC
  citations:
    - file: upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md
title: Prerequisites for upgrading feature tables to Unity Catalog
description: The underlying workspace Delta table must be upgraded to Unity Catalog before calling upgrade_workspace_table, and users must notify producers/consumers of the new table name.
tags:
  - databricks
  - prerequisites
  - migration
timestamp: "2026-06-19T23:18:31.914Z"
---

# Prerequisites for upgrading [Feature Tables](/concepts/feature-table.md) to [Unity Catalog](/concepts/unity-catalog.md)

Upgrading a workspace [Feature Table](/concepts/feature-table.md) to [Unity Catalog](/concepts/unity-catalog.md) requires meeting several prerequisites before migrating the metadata. This page outlines the conditions that must be in place for the upgrade to succeed.

## 1. Upgrade the underlying Delta table

The most important prerequisite is that the workspace Delta table underlying the [Feature Table](/concepts/feature-table.md) must already be present in [Unity Catalog](/concepts/unity-catalog.md). The upgrade process does **not** move the data or the table schema; it only migrates the feature‑table metadata (primary keys, time series columns, comments, tags, lineage). You must first follow the standard procedure to [upgrade tables and views to [Unity Catalog](/concepts/unity-catalog.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate). ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

If the data is moved using `CREATE TABLE AS SELECT` or a similar cloning approach, updates to the source workspace table will **not** be automatically synchronized to the [Unity Catalog](/concepts/unity-catalog.md) target. Producers and consumers must be notified to switch to the new table name after the upgrade. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## 2. Use the latest version of `databricks-feature-engineering`

Databricks recommends always using the latest version of the `databricks-feature-engineering` library, regardless of the Databricks Runtime version you are running. Install it with `%pip install databricks-feature-engineering --upgrade` and call `dbutils.library.restartPython()` afterward. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

If you are using version **0.1.2 or below**, the `upgrade_workspace_table` method will throw an error and the upgrade will not run. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## 3. Runtime compatibility for tags and time series columns

Upgrading **tags** and **time series columns** is **not supported** in Databricks Runtime **13.2 ML and below**. If you are running on an older runtime, these metadata items will not be migrated. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## 4. Metadata matches between source and target

When the `upgrade_workspace_table` method is called, it checks for metadata consistency between the workspace source table and the [Unity Catalog](/concepts/unity-catalog.md) target table:

- If **table or column comments** differ, the upgrade **skips** upgrading comments and logs a warning (no error).
- For all other metadata (primary keys, time series columns, tags), a mismatch causes an error and the upgrade fails.

To bypass such errors and **overwrite** the existing metadata on the [Unity Catalog](/concepts/unity-catalog.md) table, pass `overwrite=True` to the API. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## 5. Notification to producers and consumers

After the upgrade, producers and consumers must start using the new [Unity Catalog](/concepts/unity-catalog.md) table name. If the target table was cloned from the source (e.g., `CREATE TABLE AS SELECT`), updates to the source table are not automatically reflected in the target. Communicate the change to all downstream users. ^[upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md)
- Upgrade tables and views to Unity Catalog
- [Feature Engineering client](/concepts/featureengineeringclient-api.md)
- [Feature table metadata](/concepts/feature-table.md)
- [Databricks Runtime ML compatibility](/concepts/databricks-runtime-compatibility.md)

## Sources

- upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-workspace-feature-table-to-unity-catalog-databricks-on-aws-057725bd.md)
