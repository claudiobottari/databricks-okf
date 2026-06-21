---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8498d58ee7690bc7888b6a3aebaa7ab136e254be12a2505be2df0ac60396edf0
  pageDirectory: concepts
  sources:
    - upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-tables-in-unity-catalog
    - ETIUC
    - Delta Tables in Unity Catalog
    - External Tables on Unity Catalog
    - External Tables and Volumes in Unity Catalog|external tables and volumes
    - External Table|external
  citations:
    - file: upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md
title: External Tables in Unity Catalog
description: Tables whose data lifecycle, file layout, and storage are not managed by Unity Catalog; support multiple formats and allow direct non-Databricks compute access to data.
tags:
  - unity-catalog
  - tables
  - data-governance
timestamp: "2026-06-19T23:19:01.861Z"
---

# External Tables in [Unity Catalog](/concepts/unity-catalog.md)

**External tables** in [Unity Catalog](/concepts/unity-catalog.md) are tables whose data lifecycle, file layout, and storage location are not managed by [Unity Catalog](/concepts/unity-catalog.md). Unlike [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md), external tables store their data outside of [Unity Catalog](/concepts/unity-catalog.md)'s reserved managed storage, and [Unity Catalog](/concepts/unity-catalog.md) does not control the underlying data files. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Overview

External tables are typically used when you need direct access to data using non-Databricks compute (that is, not using Databricks clusters or Databricks SQL warehouses). They also serve as a convenient option in [Hive to Unity Catalog Migration](/concepts/hive-metastore-to-unity-catalog-migration.md) scenarios because you can register existing data in [Unity Catalog](/concepts/unity-catalog.md) quickly without having to copy data. This is possible because data in external tables does not have to reside in reserved managed storage. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

Multiple data formats are supported for external tables, as opposed to managed tables which always use the [Delta Lake](/concepts/delta-lake.md) table format. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Prerequisites for External Tables

To create external tables in [Unity Catalog](/concepts/unity-catalog.md), you need the following:

- A [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) for an IAM role that authorizes [Unity Catalog](/concepts/unity-catalog.md) to access the tables' location path
- An [External location](/concepts/external-location.md) that references the storage credential and the path to the data on your cloud tenant
- The `CREATE EXTERNAL TABLE` permission on the external locations where the tables will reside

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Creating External Tables

### Using [Catalog Explorer](/concepts/catalog-explorer.md)

The **Catalog Explorer** upgrade wizard allows you to copy complete schemas (databases) and multiple tables from your Databricks default Hive [Metastore](/concepts/metastore.md) to [Unity Catalog](/concepts/unity-catalog.md). The upgraded tables will be external tables in [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

The upgrade process involves:
1. Selecting a schema from `hive_metastore`
2. Choosing tables to upgrade (only external tables in formats supported by [Unity Catalog](/concepts/unity-catalog.md))
3. Setting the destination catalog, schema, and owner for each table
4. Running the upgrade

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### Using the SYNC Command

The `SYNC` SQL command copies external tables in your Hive [Metastore](/concepts/metastore.md) to external tables in [Unity Catalog](/concepts/unity-catalog.md). You can sync individual tables or entire schemas. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

To sync an external Hive table:

```sql
SYNC TABLE <uc-catalog>.<uc-schema>.<new-table> FROM hive_metastore.<source-schema>.<source-table> SET OWNER <principal>;
```

To sync an entire schema:

```sql
SYNC SCHEMA <uc-catalog>.<new-schema> FROM hive_metastore.<source-schema> SET OWNER <principal>;
```

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

You can also use `SYNC` to copy Hive managed tables that are stored outside of Databricks workspace storage (sometimes called DBFS root) to external tables in [Unity Catalog](/concepts/unity-catalog.md):

```sql
SYNC TABLE <uc-catalog>.<uc-schema>.<new-table> AS EXTERNAL FROM hive_metastore.<source-schema>.<source-table> SET OWNER <principal>;
```

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

Notably, `SYNC` cannot be used to copy Hive managed tables stored in workspace storage. To copy those tables, use `CREATE TABLE CLONE` instead. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

### Incremental Updates with SYNC

`SYNC` can also be used to update existing [Unity Catalog](/concepts/unity-catalog.md) tables when the source tables in the Hive [Metastore](/concepts/metastore.md) are changed. This makes it a useful tool for transitioning to [Unity Catalog](/concepts/unity-catalog.md) gradually. The `SYNC` command performs a write operation to each source table it upgrades to add additional table properties for bookkeeping, including a record of the target [Unity Catalog](/concepts/unity-catalog.md) external table. ^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Differences from Managed Tables

| Feature | External Tables | Managed Tables |
|---------|----------------|----------------|
| Data lifecycle management | Not managed by [Unity Catalog](/concepts/unity-catalog.md) | Fully managed by [Unity Catalog](/concepts/unity-catalog.md) |
| File layout | Not managed by [Unity Catalog](/concepts/unity-catalog.md) | Managed by [Unity Catalog](/concepts/unity-catalog.md) |
| Storage location | Any accessible location | Reserved managed storage |
| Supported formats | Multiple formats | [Delta Lake](/concepts/delta-lake.md) only |
| Performance optimization | Not automatically optimized | Automatically optimized |
| Migration convenience | No data copy required | Requires CLONE or CTAS |

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Post-Migration Considerations

After upgrading tables to [Unity Catalog](/concepts/unity-catalog.md) external tables, you should:

1. **Grant access**: Define fine-grained access control using the **Permissions** tab of each new table
2. **Add deprecation comments**: Optionally add comments to original Hive tables pointing users to the new [Unity Catalog](/concepts/unity-catalog.md) tables
3. **Update workloads**: Modify existing queries and workloads to use the new tables
4. **Test dependencies**: Before dropping old tables, revoke access and re-run related queries to test for dependencies
5. **Remove old tables**: If no longer needed, drop old tables from the Hive [Metastore](/concepts/metastore.md) (dropping an external table does not modify the data files on your cloud tenant)

^[upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md)
- [Hive Metastore](/concepts/built-in-hive-metastore.md)
- [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md)
- [External location](/concepts/external-location.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Hive to Unity Catalog Migration](/concepts/hive-metastore-to-unity-catalog-migration.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws.md](/references/upgrade-hive-tables-and-views-to-unity-catalog-databricks-on-aws-c9a7f3f8.md)
