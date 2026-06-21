---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d68c19db1c0900b2cd6cb08f3e69ae7fffa5450b0737f225adefc040b890e1e5
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-to-delta-lake-conversion
    - ITDLC
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Iceberg to Delta Lake Conversion
description: Conversion of Apache Iceberg tables to Delta Lake using CONVERT TO DELTA, with specific version and feature limitations.
tags:
  - delta-lake
  - iceberg
  - data-migration
timestamp: "2026-06-18T11:10:49.764Z"
---

# Iceberg to Delta Lake Conversion

**Iceberg to Delta Lake conversion** refers to the one-time migration of an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table to a [Delta Lake](/concepts/delta-lake.md) table using the `CONVERT TO DELTA` SQL command on Databricks. This enables tables previously stored as Iceberg to use Delta Lake features such as [Delta Lake ACID transactions](/concepts/delta-acid-transactions.md), [time travel](/concepts/delta-lake-time-travel.md), and [Unity Catalog](/concepts/unity-catalog.md) integration.^[convert-to-delta-lake-databricks-on-aws.md]

For incremental conversion of Iceberg tables (or Parquet tables) to Delta Lake, Databricks recommends using the [incremental clone](/concepts/incremental-cloning-to-delta-lake.md) approach instead.^[convert-to-delta-lake-databricks-on-aws.md]

## Supported Configurations

Unity Catalog supports `CONVERT TO DELTA` for Iceberg tables stored in external locations managed by Unity Catalog. The command can also convert a directory of Iceberg files in an external location to a [Delta Lake Table](/concepts/delta-lake-table.md), provided you have write access on the storage location.^[convert-to-delta-lake-databricks-on-aws.md]

SQL syntax for directories:  
`CONVERT TO DELTA iceberg.\`<path-to-data>\`;`  

For tables registered as [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md), the syntax is:  
`CONVERT TO DELTA catalog_name.database_name.table_name;`  

^[convert-to-delta-lake-databricks-on-aws.md]

## Requirements and Limitations

- Conversion is supported starting in **Databricks Runtime 10.4 LTS** and above.  
- **Iceberg [Metastore](/concepts/metastore.md) tables** are **not** supported for conversion.  
- **Partition evolution** — if the Iceberg table has undergone partition evolution (i.e., its partition scheme changed over time), conversion is **not** supported.  
- **Truncated column partitions** have specific support:  
  - In Databricks Runtime **12.2 LTS and below**, only `string` type is supported for truncated columns.  
  - In Databricks Runtime **13.3 LTS and above**, truncated columns of types `string`, `long`, or `int` are supported.  
  - Truncated columns of type `decimal` are **not** supported at any runtime version.

^[convert-to-delta-lake-databricks-on-aws.md]

## Using `CONVERT TO DELTA` for Unity Catalog External Tables

After you register an external Iceberg table in Unity Catalog (by granting the `CREATE EXTERNAL TABLE` permission on the external location), you can convert it to a Delta Lake external table.  

If the Iceberg table is partitioned, you **must** provide partitioning information explicitly in the command. For example:  
`CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);`  

^[convert-to-delta-lake-databricks-on-aws.md]

## Conversion of Managed and External Tables

- `CONVERT TO DELTA` can only be used to **create Unity Catalog external tables**.  
- To convert a legacy Hive [Metastore](/concepts/metastore.md) managed Parquet table to a managed Unity Catalog [Delta Lake Table](/concepts/delta-lake-table.md), use a `CTAS` (CREATE TABLE AS SELECT) statement instead (see [Upgrade Hive table to Unity Catalog managed table](/concepts/ctas-for-migrating-hive-tables-to-unity-catalog-managed-delta-tables.md)).  
- To upgrade an external Parquet table (not Iceberg) to a Unity Catalog external table, use the [upgrade wizard](/concepts/catalog-explorer-upgrade-wizard.md).

^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides ACID transactions, schema enforcement, and time travel.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that can be converted to Delta Lake.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages external locations and tables.
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The SQL command reference.
- [Incremental clone](/concepts/incremental-cloning-to-delta-lake.md) — For ongoing, incremental conversion of Iceberg to Delta Lake.
- [External tables](/concepts/unity-catalog-external-table-conversion.md) — Tables whose data resides in cloud object storage.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
