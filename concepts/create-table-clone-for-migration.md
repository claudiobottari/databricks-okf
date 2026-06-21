---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b915dae0a24a933bdf79fc2d02ba1db7909a7d4fc446f3bc53ab40683704b2b
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-table-clone-for-migration
    - CTCFM
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: CREATE TABLE CLONE for Migration
description: Method using DEEP CLONE to copy managed Delta tables from Hive metastore to Unity Catalog managed tables; table history and time travel are not preserved.
tags:
  - unity-catalog
  - migration
  - delta-table
timestamp: "2026-06-19T23:19:06.961Z"
---

# CREATE TABLE CLONE for Migration

**CREATE TABLE CLONE for Migration** is a method for upgrading [Hive metastore](/concepts/built-in-hive-metastore.md) managed Delta tables to managed tables in [Unity Catalog](/concepts/unity-catalog.md) using the `CREATE TABLE CLONE` SQL command. This approach is specifically designed for copying Delta tables from the legacy workspace-local Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md) as fully managed tables that [Unity Catalog](/concepts/unity-catalog.md) controls for lifecycle, file layout, performance optimization, and storage.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Overview

[Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) are the preferred table type because [Unity Catalog](/concepts/unity-catalog.md) fully manages their lifecycle, file layout, and storage, and automatically optimizes their performance.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md] Managed tables always use the [Delta Lake](/concepts/delta-lake.md) table format and reside in a [Managed storage location](/concepts/managed-storage-location.md) reserved for [Unity Catalog](/concepts/unity-catalog.md). Because Hive managed tables stored in workspace storage (often called DBFS root) cannot be converted to [Unity Catalog](/concepts/unity-catalog.md) external tables using methods like `SYNC`, `CREATE TABLE CLONE` provides the only viable path for migrating those tables to [Unity Catalog](/concepts/unity-catalog.md).^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Requirements

To use `CREATE TABLE CLONE` for migration, you must meet the following requirements:

- **Data format**: The source Hive tables must be in Delta format.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Compute**: A compute resource that supports [Unity Catalog](/concepts/unity-catalog.md), such as SQL warehouses or compute resources using standard or dedicated access mode.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Unity Catalog privileges**: `USE CATALOG` and `USE SCHEMA` privileges on the destination [Catalog and Schema](/concepts/catalog-and-schema.md), along with `CREATE TABLE` on the schema, or ownership of the catalog or schema.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Hive table access**: If using [Standard Access Mode Compute](/concepts/standard-access-mode-compute.md), you need legacy table access control privileges on the source Hive tables.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Migration Process

The core SQL command for migrating a managed Hive Delta table to a [Unity Catalog](/concepts/unity-catalog.md) managed table is as follows:^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

```sql
CREATE OR REPLACE TABLE <uc-catalog>.<uc-schema>.<new-table>
[[deep-clone|Deep Clone]] hive_metastore.<source-schema>.<source-table>;
```

You must use **deep clones** when cloning tables from the legacy Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md).^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Limitations

Table history is not migrated when you run `CREATE TABLE CLONE`.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md] Any tables in the Hive [Metastore](/concepts/metastore.md) that you clone to [Unity Catalog](/concepts/unity-catalog.md) are treated as new tables, meaning you cannot perform [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) or other operations that rely on pre-migration history.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Post-Migration Steps

After cloning the table, Databricks recommends completing the following steps:^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

1. **Grant access**: Grant account-level users or groups access to the new [Unity Catalog](/concepts/unity-catalog.md) table using [Unity Catalog Privilege Management](/concepts/unity-catalog-privilege-management.md).
2. **Add deprecation comments**: Add a comment to the original Hive table pointing users to the new [Unity Catalog](/concepts/unity-catalog.md) table. If the comment uses the format `This table is deprecated. Please use catalog.default.table instead of hive_metastore.schema.table.`, Databricks notebooks and SQL query editors will display the deprecated table name with strikethrough text, show a warning, and provide a quick fix link to [Genie Code](/concepts/genie-code.md) for updating references.
3. **Update workloads**: Modify existing queries and workloads to use the new [Unity Catalog](/concepts/unity-catalog.md) table. [Genie Code](/concepts/genie-code.md) can help identify and replace references to deprecated Hive tables.
4. **Test before dropping**: Before dropping the old table, test for dependencies by revoking access to it and re-running related queries and workloads.

## Comparison with Other Migration Methods

- **CREATE TABLE CLONE** is the recommended method for migrating Hive managed Delta tables to [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md).^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- Use CREATE TABLE AS SELECT (CTAS) as an alternative if you cannot use or prefer not to use `CREATE TABLE CLONE`.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- For migrating external tables, use [SYNC for Unity Catalog Migration](/concepts/sync-command-for-hive-to-unity-catalog-migration.md) or the [Catalog Explorer Upgrade Wizard](/concepts/catalog-explorer-upgrade-wizard.md) instead.^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md)
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md)
- [Hive metastore migration to Unity Catalog](/concepts/hive-metastore-federation-to-unity-catalog.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Unity Catalog Privilege Management](/concepts/unity-catalog-privilege-management.md)

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
