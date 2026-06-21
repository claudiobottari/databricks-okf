---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a8db315a7136b71a1f0ce6a2974d19089c9c6faaa43aa2ae64213d59b2b83f1
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parquet-to-delta-lake-conversion
    - PTDLC
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Parquet to Delta Lake Conversion
description: Process of converting a directory of Parquet data files or a Parquet external table into a Delta Lake table using CONVERT TO DELTA.
tags:
  - delta-lake
  - parquet
  - data-migration
timestamp: "2026-06-18T11:10:49.474Z"
---

# Parquet to Delta Lake Conversion

The **Parquet to Delta Lake conversion** is a one-time operation that transforms a Parquet table or directory of Parquet files into a [Delta Lake](/concepts/delta-lake.md) table using the `CONVERT TO DELTA` SQL command. This conversion unlocks Delta Lake features on the Databricks lakehouse, such as ACID transactions, time travel, and schema enforcement, while keeping the existing data in place. ^[convert-to-delta-lake-databricks-on-aws.md]

## When to Use `CONVERT TO DELTA`

`CONVERT TO DELTA` performs a one-time conversion for Parquet (and Apache Iceberg) tables. For ongoing, incremental synchronization of Parquet or Iceberg data into Delta Lake, use the [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) approach instead. ^[convert-to-delta-lake-databricks-on-aws.md]

## Prerequisites

- The Parquet data must reside in an external location managed by [Unity Catalog](/concepts/unity-catalog.md), or you must have write access on the storage location (for directory-level conversion). ^[convert-to-delta-lake-databricks-on-aws.md]
- To load the converted table as an external table in Unity Catalog, you need the `CREATE EXTERNAL TABLE` permission on the external location. ^[convert-to-delta-lake-databricks-on-aws.md]
- For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the Hive [Metastore](/concepts/metastore.md). For Unity Catalog external tables, you must provide partitioning information if the table is partitioned. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting a Directory of Parquet Files

You can convert a directory of Parquet data files directly to a [Delta Lake Table](/concepts/delta-lake-table.md) using the `parquet.` path prefix. The syntax is: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;
```

This writes the Delta transaction log on top of the existing Parquet files. The original Parquet files are not deleted; they become part of the Delta table’s version history. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting an External Parquet Table Registered in Unity Catalog

If you have already registered an external Parquet table in Unity Catalog (for example, using the upgrade wizard), you can convert it to a Delta Lake external table with the following syntax: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name;
```

If the table is partitioned, you must specify the partition columns: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

To upgrade a legacy Hive [Metastore](/concepts/metastore.md) managed Parquet table directly to a managed Unity Catalog [Delta Lake Table](/concepts/delta-lake-table.md), use a `CTAS` statement rather than `CONVERT TO DELTA`. See [Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT](/concepts/ctas-for-migrating-hive-tables-to-unity-catalog-managed-delta-tables.md). ^[convert-to-delta-lake-databricks-on-aws.md]

## Partition Handling

- For tables registered in the Hive [Metastore](/concepts/metastore.md) (Databricks Runtime 11.3 LTS+), partitioning is automatically inferred by the `CONVERT TO DELTA` command. ^[convert-to-delta-lake-databricks-on-aws.md]
- For Unity Catalog external tables, you must explicitly provide the partition columns using the `PARTITIONED BY` clause if the source Parquet data is partitioned. ^[convert-to-delta-lake-databricks-on-aws.md]

## Limitations and Notes

- The `CONVERT TO DELTA` command is a one-time operation. To keep a Parquet source automatically synced to a Delta table, use incremental cloning instead. ^[convert-to-delta-lake-databricks-on-aws.md]
- The command is supported for Parquet tables stored in external locations managed by Unity Catalog. ^[convert-to-delta-lake-databricks-on-aws.md]
- After conversion, the table becomes a full [Delta Lake Table](/concepts/delta-lake-table.md); existing workflows that read the Parquet files directly will continue to work, but Delta features become available. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and data versioning
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for managing external tables and permissions
- [External tables](/concepts/unity-catalog-external-table-conversion.md) — Tables with data stored in cloud object storage, not managed by Databricks
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The SQL command for performing the conversion
- [Incrementally clone to Delta Lake](/concepts/incremental-cloning-to-delta-lake.md) — Alternative approach for ongoing synchronization
- [Hive metastore](/concepts/built-in-hive-metastore.md) — Legacy [Metastore](/concepts/metastore.md) that can be migrated to Unity Catalog
- CTAS — CREATE TABLE AS SELECT for converting managed tables

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
