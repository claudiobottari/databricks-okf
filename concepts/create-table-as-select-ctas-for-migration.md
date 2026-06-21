---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4a203290c7e9fd276b855ef45cd63cf11facac62a07971929f99d8469bf1b1f
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-table-as-select-ctas-for-migration
    - CTAS(FM
    - CREATE TABLE ... AS SELECT
    - CREATE TABLE AS SELECT (CTAS)
    - CTAS (CREATE TABLE AS SELECT)
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: CREATE TABLE AS SELECT (CTAS) for Migration
description: Alternative method to create Unity Catalog managed tables by querying Hive tables with SELECT, allowing column/row filtering during migration.
tags:
  - unity-catalog
  - migration
  - sql-commands
timestamp: "2026-06-19T23:19:13.515Z"
---

# CREATE TABLE AS SELECT (CTAS) for Migration

**CREATE TABLE AS SELECT (CTAS)** is a SQL command used to migrate tables from the Hive [Metastore](/concepts/metastore.md) to managed tables in [Unity Catalog](/concepts/unity-catalog.md) on Databricks. It creates a new managed table by querying an existing table and copying its data. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Overview

CTAS is one of several migration options available when upgrading Hive tables to [Unity Catalog](/concepts/unity-catalog.md). It is particularly useful when you cannot use or prefer not to use `CREATE TABLE CLONE` for migration. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

The command creates a **managed table** in [Unity Catalog](/concepts/unity-catalog.md), meaning [Unity Catalog](/concepts/unity-catalog.md) fully manages the table's lifecycle, file layout, storage, and performance optimization. Managed tables always use the [Delta Lake](/concepts/delta-lake.md) format. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Basic Syntax

The standard CTAS syntax for migration is:

```sql
CREATE TABLE <uc-catalog>.<new-schema>.<new-table>
AS SELECT * FROM hive_metastore.<source-schema>.<source-table>;
```

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

Placeholder values:
- `<uc-catalog>`: The [Unity Catalog](/concepts/unity-catalog.md) catalog for the new table
- `<new-schema>`: The [Unity Catalog](/concepts/unity-catalog.md) schema for the new table
- `<new-table>`: A name for the [Unity Catalog](/concepts/unity-catalog.md) table
- `<source-schema>`: The schema for the Hive table (e.g., `default`)
- `<source-table>`: The name of the Hive table

## Selective Migration

If you want to migrate only a subset of columns or rows, modify the `SELECT` statement accordingly. For example, you can include a `WHERE` clause to filter rows or specify particular columns instead of using `SELECT *`. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Requirements

To use CTAS for migration, you need: ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

**Compute requirements:**
- A compute resource that supports [Unity Catalog](/concepts/unity-catalog.md) (SQL warehouses or compute resources using standard or dedicated access mode)

**Unity Catalog permission requirements:**
- `USE CATALOG` and `USE SCHEMA` privileges on the target [Catalog and Schema](/concepts/catalog-and-schema.md)
- `CREATE TABLE` privilege on the target schema, or ownership of the catalog or schema
- If using [Standard Access Mode](/concepts/standard-access-mode.md), table access control privileges on the Hive [Metastore](/concepts/metastore.md)

## Comparison with Other Migration Methods

### CTAS vs. CREATE TABLE CLONE

CTAS is an alternative to `CREATE TABLE CLONE` for creating [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md). While `CLONE` is specifically designed for Delta format tables and preserves the Delta log structure, CTAS copies data through a query operation. The choice between the two depends on the specific migration scenario. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### CTAS vs. SYNC

`SYNC` creates [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md), whereas CTAS creates managed tables. Managed tables are generally preferred when you don't need direct access to data using non-Databricks compute. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Migration Steps

1. Create the new [Unity Catalog](/concepts/unity-catalog.md) table by running the CTAS query
2. Grant account-level users or groups access to the new table using [Unity Catalog Privilege Management](/concepts/unity-catalog-privilege-management.md)
3. (Optional) Add a deprecation comment to the original Hive table pointing users to the new [Unity Catalog](/concepts/unity-catalog.md) table
4. Update existing queries and workloads to reference the new table
5. Test for dependencies by revoking access to the old table before dropping it

## Limitations

- Table history is not migrated. Any tables created with CTAS in [Unity Catalog](/concepts/unity-catalog.md) are treated as new tables. You cannot perform [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) or other operations that rely on pre-migration history. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Hive to Unity Catalog Migration](/concepts/hive-metastore-to-unity-catalog-migration.md) — The overall process of upgrading tables from the Hive [Metastore](/concepts/metastore.md)
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) — Another method for creating [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md)
- SYNC Command — Used to create [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) from Hive tables
- [Managed Tables vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) — Understanding the differences between [Table Types in Unity Catalog](/concepts/table-types-in-unity-catalog.md)
- [Catalog Explorer Upgrade Wizard](/concepts/catalog-explorer-upgrade-wizard.md) — A UI-based tool for upgrading Hive schemas

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
