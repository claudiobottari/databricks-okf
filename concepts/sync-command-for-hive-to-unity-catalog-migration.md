---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: efe3671809fa7914024eadcae74f9790599adb95fa1ca6815b557d0cf05a614a
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sync-command-for-hive-to-unity-catalog-migration
    - SCFHM
    - SYNC for Unity Catalog Migration
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: SYNC Command for Hive-to-Unity-Catalog Migration
description: SQL command (SYNC TABLE / SYNC SCHEMA) that copies Hive metastore external tables to Unity Catalog external tables, with support for ongoing synchronization when source tables change.
tags:
  - unity-catalog
  - migration
  - sql-commands
timestamp: "2026-06-19T23:18:45.028Z"
---

# SYNC Command for Hive-to-Unity-Catalog Migration

The **SYNC command** is a SQL statement used to copy tables and schemas from the workspace-local Hive [Metastore](/concepts/metastore.md) to external tables in [Unity Catalog](/concepts/unity-catalog.md). It provides a mechanism for migrating existing Hive tables to [Unity Catalog](/concepts/unity-catalog.md) without copying the underlying data files. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Overview

The `SYNC` command creates [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) that point to the same data location as the source Hive tables. Because external tables do not require data to reside in [Unity Catalog](/concepts/unity-catalog.md)'s managed storage, `SYNC` enables rapid migration by registering existing metadata in [Unity Catalog](/concepts/unity-catalog.md) rather than moving data. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

The command performs a write operation to each source table it upgrades, adding additional table properties for bookkeeping, including a record of the target [Unity Catalog](/concepts/unity-catalog.md) external table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Supported Use Cases

`SYNC` can be used to copy:

- **External Hive tables** to [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Hive managed tables stored outside of Databricks workspace storage** (sometimes called DBFS root) to [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- **Entire schemas** (databases) and all their tables to [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

`SYNC` cannot be used to copy Hive managed tables stored in workspace storage. To copy those tables, use [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) instead. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Incremental Migration Support

`SYNC` can also be used to update existing [Unity Catalog](/concepts/unity-catalog.md) tables when the source tables in the Hive [Metastore](/concepts/metastore.md) are changed. This makes it a good tool for transitioning to [Unity Catalog](/concepts/unity-catalog.md) gradually, allowing you to keep the Hive [Metastore](/concepts/metastore.md) as the source of truth during a phased migration. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Requirements

Before using `SYNC`, you must have:

- A workspace with a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) and at least one [Unity Catalog](/concepts/unity-catalog.md) catalog. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- A [storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) for an IAM role that authorizes [Unity Catalog](/concepts/unity-catalog.md) to access the tables' location path. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- An [External location](/concepts/external-location.md) that references the storage credential and the path to the data on your cloud tenant. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- The `CREATE EXTERNAL TABLE` permission on the external locations of the tables to be upgraded. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- A compute resource that supports [Unity Catalog](/concepts/unity-catalog.md) (SQL warehouses or compute resources using standard or dedicated access mode). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
- If using [Standard Access Mode](/concepts/standard-access-mode.md), access to the tables in the Hive [Metastore](/concepts/metastore.md) granted using legacy table access control. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Syntax

### Sync an external Hive table

```sql
SYNC TABLE <uc-catalog>.<uc-schema>.<new-table> FROM hive_metastore.<source-schema>.<source-table>
SET OWNER <principal>;
```

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### Sync an external Hive schema and all its tables

```sql
SYNC SCHEMA <uc-catalog>.<new-schema> FROM hive_metastore.<source-schema>
SET OWNER <principal>;
```

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### Sync a managed Hive table stored outside workspace storage

```sql
SYNC TABLE <uc-catalog>.<uc-schema>.<new-table> AS EXTERNAL FROM hive_metastore.<source-schema>.<source-table>
SET OWNER <principal>;
```

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### Sync a schema containing managed Hive tables stored outside workspace storage

```sql
SYNC SCHEMA <uc-catalog>.<new-schema> AS EXTERNAL FROM hive_metastore.<source-schema>
SET OWNER <principal>;
```

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Post-Migration Steps

After running `SYNC`, you should:

1. Grant account-level users or groups access to the new table using [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
2. (Optional) Add a deprecation comment to the original Hive table pointing users to the new [Unity Catalog](/concepts/unity-catalog.md) table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
3. Update existing queries and workloads to use the new table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]
4. Before dropping the old table, test for dependencies by revoking access and re-running related queries. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Comparison with Other Migration Methods

`SYNC` is one of several migration options. The [Catalog Explorer Upgrade Wizard](/concepts/catalog-explorer-upgrade-wizard.md) provides a UI-based alternative for upgrading external tables. For managed tables, [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md) ([Deep Clone](/concepts/deep-clone.md)) and CREATE TABLE AS SELECT (CTAS) are alternatives that create [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) rather than external tables. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- [External tables](/concepts/unity-catalog-external-table-conversion.md)
- [Managed tables](/concepts/managed-tables-in-databricks.md)
- Storage credentials
- [External locations](/concepts/external-location.md)
- [CREATE TABLE CLONE](/concepts/create-table-clone-syntax.md)
- CREATE TABLE AS SELECT
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
