---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9760d9d0970a2fdd3d4b301fc520db4dc862ab5552386a8082e16731cd7ef304
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-conversion-from-apache-iceberg
    - DLCFAI
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Delta Lake Conversion from Apache Iceberg
description: Process and limitations for converting Iceberg tables to Delta Lake, including version requirements and unsupported features like partition evolution
tags:
  - delta-lake
  - iceberg
  - data-migration
timestamp: "2026-06-19T09:24:45.969Z"
---

# Delta Lake Conversion from Apache Iceberg

**Delta Lake Conversion from Apache Iceberg** refers to the one-time process of transforming an Apache Iceberg table into a [Delta Lake](/concepts/delta-lake.md) table using the `CONVERT TO DELTA` SQL command on Databricks. This operation enables existing Iceberg data to be managed under the Delta Lake format, unlocking the full set of lakehouse features available on the Databricks platform.

## Overview

The `CONVERT TO DELTA` SQL command performs a one-time conversion for both Parquet and Apache Iceberg tables to Delta Lake tables. For incremental conversion of Iceberg tables, Databricks recommends using the [Incremental Clone](/concepts/incremental-cloning-to-delta-lake.md) functionality instead. ^[convert-to-delta-lake-databricks-on-aws.md]

Unity Catalog supports the `CONVERT TO DELTA` command for Iceberg tables stored in external locations that are managed by Unity Catalog. The command can convert a directory of Iceberg files in an external location directly into a [Delta Lake Table](/concepts/delta-lake-table.md), provided the user has write access to the storage location. ^[convert-to-delta-lake-databricks-on-aws.md]

## Prerequisites

- **Databricks Runtime version**: Converting Iceberg tables is supported in Databricks Runtime 10.4 LTS and above. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Unity Catalog external location**: The Iceberg data must reside in a storage location that has been configured as an external location in Unity Catalog. The user performing the conversion needs `CREATE EXTERNAL TABLE` permission on that external location to load the converted table as an external table in Unity Catalog. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Write access**: The user must have write access to the underlying cloud storage (e.g., S3 bucket) where the Iceberg files reside. ^[convert-to-delta-lake-databricks-on-aws.md]

## Limitations

The following limitations apply when converting Iceberg tables to Delta Lake:

- **Metastore tables are not supported**: Converting Iceberg [Metastore](/concepts/metastore.md) tables (tables registered only in the Hive [Metastore](/concepts/metastore.md)) is not supported. The Iceberg table must be directly accessible as a directory of files. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Partition evolution not supported**: Iceberg tables that have experienced [partition evolution](/concepts/partition-evolution-in-iceberg.md) (where the partitioning scheme has been changed over time) cannot be converted. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Truncated column partitions**: 
  - In Databricks Runtime 12.2 LTS and below, only `string` type is supported for truncated columns used in partitioning.
  - In Databricks Runtime 13.3 LTS and above, truncated columns of types `string`, `long`, or `int` are supported.
  - Truncated columns of type `decimal` are not supported in any version. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting a Directory of Iceberg Files

To convert a directory of Iceberg files in an external location to a [Delta Lake Table](/concepts/delta-lake-table.md), use the following SQL syntax:

```sql
CONVERT TO DELTA iceberg.`s3://my-bucket/iceberg-data`;
```

This command reads the Iceberg metadata and rewrites the files (or creates a Delta log) to produce a valid [Delta Lake Table](/concepts/delta-lake-table.md). After conversion, the table can be queried as a Delta table. ^[convert-to-delta-lake-databricks-on-aws.md]

### Partition Information

For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the Hive [Metastore](/concepts/metastore.md). However, for Unity Catalog external tables, you **must** provide partitioning information if the Iceberg table is partitioned. This is done using the `PARTITIONED BY` clause. ^[convert-to-delta-lake-databricks-on-aws.md]

Example:

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

## Converting Managed and External Tables to Delta Lake on Unity Catalog

The `CONVERT TO DELTA` syntax can only be used for creating Unity Catalog external tables. To convert a legacy Hive [Metastore](/concepts/metastore.md) managed table (e.g., a managed Parquet table) directly to a managed Unity Catalog [Delta Lake Table](/concepts/delta-lake-table.md), use a `CREATE TABLE AS SELECT` (CTAS) statement instead. See Upgrade Hive tables to Unity Catalog for details. ^[convert-to-delta-lake-databricks-on-aws.md]

To upgrade an external table (including an Iceberg table) to a Unity Catalog external table, use the Upgrade wizard for Unity Catalog or the `ALTER TABLE` syntax. After the table is registered in Unity Catalog as an external Parquet or Iceberg table, you can convert it to Delta Lake using `CONVERT TO DELTA` as shown above. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- Incremental Clone from Iceberg – For ongoing, incremental synchronization of Iceberg tables to Delta Lake.
- [CONVERT TO DELTA SQL Command](/concepts/convert-to-delta-sql-command.md) – Full technical reference for the command.
- Unity Catalog external tables – How to manage external data sources in Unity Catalog.
- Partition Evolution – Understanding the limitation that prevents conversion of Iceberg tables with evolved partitions.
- Delta Lake vs Iceberg – Comparative overview of the two table formats.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
