---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 506ab121d60d7d4ba097d2f749813fa761ab70c9696b3e1394d845e5958fdce9
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-tables-in-unity-catalog
    - MTIUC
    - Path-based tables in Unity Catalog
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: Managed Tables in Unity Catalog
description: Tables whose lifecycle, file layout, storage location, and performance optimization are fully managed by Unity Catalog; always use Delta format and reside in reserved managed storage.
tags:
  - unity-catalog
  - tables
  - data-governance
timestamp: "2026-06-19T23:18:33.109Z"
---

# Managed Tables in [Unity Catalog](/concepts/unity-catalog.md)

A **managed table** in [Unity Catalog](/concepts/unity-catalog.md) is a table whose data lifecycle, file layout, and storage are fully managed by [Unity Catalog](/concepts/unity-catalog.md). Managed tables are the preferred way to create tables in [Unity Catalog](/concepts/unity-catalog.md) because the system handles their lifecycle, optimizes performance automatically, and enforces the use of the [Delta Lake](/concepts/delta-lake.md) table format. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Key characteristics

- **Lifecycle management**: [Unity Catalog](/concepts/unity-catalog.md) governs the table's data, including creation, updates, and deletion. When a managed table is dropped, its underlying data is removed. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **File layout and storage**: The physical location of the data is determined by a [Managed storage location](/concepts/managed-storage-location.md) that you reserve specifically for [Unity Catalog](/concepts/unity-catalog.md). Data is stored in a cloud storage bucket (e.g., S3) that only [Unity Catalog](/concepts/unity-catalog.md) accesses; users and workloads interact with the table through the catalog. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Automatic performance optimization**: [Unity Catalog](/concepts/unity-catalog.md) applies built‑in optimizations (such as compaction, indexing, and statistics collection) to improve query performance without manual intervention. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Delta format only**: All managed tables are stored as [Delta tables](/concepts/delta-lake-table.md), ensuring ACID transactions, schema enforcement, and time‑travel capabilities. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Migration from Hive to managed tables

When migrating existing [Hive metastore](/concepts/built-in-hive-metastore.md) tables to [Unity Catalog](/concepts/unity-catalog.md) as managed tables, you must copy the data into Unity Catalog’s managed storage. Two supported methods are: ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) ([Deep Clone](/concepts/deep-clone.md)): Creates a new managed table that is an independent copy of the source Hive table. Unlike shallow clones, deep clones do not reference the source data after creation. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- CREATE TABLE AS SELECT (CTAS): Builds a new managed table by running a `SELECT` query against the Hive table. This allows filtering or transformation during migration. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

Because managed tables must reside in Unity Catalog’s reserved managed storage, you cannot simply “sync” metadata—data must be physically copied. Tools like `SYNC` or the [Catalog Explorer Upgrade Wizard](/concepts/catalog-explorer-upgrade-wizard.md) create external tables by referencing the existing data in place; they do not create managed tables. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related concepts

- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) — Alternative table type where data lifecycle is not managed by [Unity Catalog](/concepts/unity-catalog.md).
- [Managed storage location](/concepts/managed-storage-location.md) — Cloud storage bucket designated for [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md).
- [Delta Lake](/concepts/delta-lake.md) — The required underlying format for managed tables.
- [Hive metastore](/concepts/built-in-hive-metastore.md) — The legacy workspace‑local [Metastore](/concepts/metastore.md) from which tables can be migrated.
- [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md) — Privileges required to create and manage tables (e.g., `CREATE TABLE`, `USE CATALOG`).

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
