---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a051714503a6ff2782663ec5bce68cb1d9680e6459db61414f56c8772816a2e5
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ctas-for-migrating-hive-tables-to-unity-catalog-managed-delta-tables
    - CFMHTTUCMDT
    - Upgrade Hive table to Unity Catalog managed table
    - Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: CTAS for Migrating Hive Tables to Unity Catalog Managed Delta Tables
description: Using CREATE TABLE AS SELECT (CTAS) to convert legacy Hive metastore managed Parquet tables to managed Unity Catalog Delta Lake tables.
tags:
  - unity-catalog
  - migration
  - hive-metastore
timestamp: "2026-06-19T17:53:12.920Z"
---

# CTAS for Migrating Hive Tables to Unity Catalog Managed Delta Tables

**CTAS for Migrating Hive Tables to Unity Catalog Managed Delta Tables** refers to using the `CREATE TABLE AS SELECT` (CTAS) statement to convert a legacy [Hive metastore](/concepts/built-in-hive-metastore.md) managed table (in Parquet format) directly into a [Unity Catalog](/concepts/unity-catalog.md) managed [Delta Lake](/concepts/delta-lake.md) table. This is the recommended approach when the target table should be a Unity Catalog managed table rather than an external table. ^[convert-to-delta-lake-databricks-on-aws.md]

## Context and Purpose

When migrating tables from the Hive [Metastore](/concepts/metastore.md) to Unity Catalog, the `CONVERT TO DELTA` syntax can only be used to create Unity Catalog **external** tables. To create a Unity Catalog **managed** table from a legacy Hive managed table, you must use a CTAS statement instead. The CTAS approach copies the data from the source Hive table into a new managed Delta table under Unity Catalog governance. ^[convert-to-delta-lake-databricks-on-aws.md]

## Procedure

The general pattern is:

```sql
CREATE TABLE catalog_name.database_name.new_table
USING delta
AS SELECT * FROM hive_metastore.database_name.source_table;
```

Replace the placeholders with the appropriate three‑level Unity Catalog name and the two‑level Hive [Metastore](/concepts/metastore.md) table name. The new table inherits Unity Catalog’s data governance, access control, and lineage tracking. ^[convert-to-delta-lake-databricks-on-aws.md]

### Requirements

- The source table must be a **managed** Parquet table registered in the Hive [Metastore](/concepts/metastore.md).
- The destination must be a Unity Catalog [Catalog and Schema](/concepts/catalog-and-schema.md) (database) where you have `CREATE TABLE` and `CREATE MANAGED TABLE` privileges.
- Sufficient workspace and storage permissions are needed to read the source and write the managed Delta location.

## Comparison with `CONVERT TO DELTA`

| Approach | Target Table Type | Use Case | Source Format |
|----------|------------------|----------|---------------|
| `CONVERT TO DELTA` | Unity Catalog **external** table | Parquet or Iceberg data in external locations | Parquet, Iceberg (directories or external tables) |
| `CTAS` | Unity Catalog **managed** table | Hive [Metastore](/concepts/metastore.md) managed Parquet tables | Parquet (managed tables) |

^[convert-to-delta-lake-databricks-on-aws.md]

## Limitations

- CTAS is specific to **managed** Hive tables. For external Hive tables (data stored in external locations), use the upgrade wizard or `CONVERT TO DELTA` after registering the table as a Unity Catalog external table. ^[convert-to-delta-lake-databricks-on-aws.md]
- The CTAS operation performs a full copy of the data, which can be expensive for large tables. For incremental conversion scenarios, consider the [Incrementally Clone Parquet and Iceberg Tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) pattern.

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – One‑time conversion for Parquet/Iceberg directories or external tables.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance layer for managing access and lineage.
- [Hive Metastore](/concepts/built-in-hive-metastore.md) – Legacy metadata store for Hive tables.
- [Delta Lake](/concepts/delta-lake.md) – Open‑format storage layer with ACID transactions.
- [Managed Tables vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) – Distinction between data owned by the [Metastore](/concepts/metastore.md) vs. external storage.
- [External Locations](/concepts/external-location.md) – Cloud storage paths managed by Unity Catalog for external tables.
- Upgrade Wizard for Hive Metastore Migration – Alternative bulk migration tool for schemas and tables.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
