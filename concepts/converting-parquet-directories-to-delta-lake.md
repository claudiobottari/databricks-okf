---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb0fdb9738e719736d8574bec95cfcb46b5e025be7265aa3aff711d3a865c063
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - converting-parquet-directories-to-delta-lake
    - CPDTDL
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Converting Parquet directories to Delta Lake
description: Converting directories of Parquet data files stored in external locations into Delta Lake tables
tags:
  - parquet
  - delta-lake
  - external-tables
timestamp: "2026-06-19T14:26:33.293Z"
---

# Converting Parquet directories to Delta Lake

**Converting Parquet directories to Delta Lake** refers to the process of transforming existing Parquet data files into Delta Lake tables, enabling access to the full feature set of the Databricks lakehouse. This one-time conversion can be performed using the `CONVERT TO DELTA` SQL command on Parquet directories stored in external locations. ^[convert-to-delta-lake-databricks-on-aws.md]

## Overview

The `CONVERT TO DELTA` SQL command performs a one-time conversion for Parquet and Apache Iceberg tables to Delta Lake tables. For incremental conversion, see [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md). Unity Catalog supports this command for tables stored in external locations managed by Unity Catalog. ^[convert-to-delta-lake-databricks-on-aws.md]

You can configure existing Parquet data files as [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) and then convert them to Delta Lake to unlock all features of the Databricks lakehouse. ^[convert-to-delta-lake-databricks-on-aws.md]

## Prerequisites

To convert a directory of Parquet files to a [Delta Lake Table](/concepts/delta-lake-table.md), you must have write access on the storage location. For information on configuring access with Unity Catalog, see Connect to cloud object storage using Unity Catalog. To load converted tables as external tables to Unity Catalog, you need the `CREATE EXTERNAL TABLE` permission on the external location. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting a directory of Parquet files

You can convert a directory of Parquet data files to a [Delta Lake Table](/concepts/delta-lake-table.md) using the following SQL syntax: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;
```

This command converts all Parquet files in the specified directory into a [Delta Lake Table](/concepts/delta-lake-table.md), creating the Delta transaction log that enables features such as [time travel](/concepts/delta-lake-time-travel.md), schema enforcement, and [ACID transactions](/concepts/delta-acid-transactions.md). ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting Unity Catalog external tables

After you've registered an external Parquet table to Unity Catalog, you can convert it to an external [Delta Lake Table](/concepts/delta-lake-table.md) using the fully qualified table name: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name;
```

### Partitioning information

For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the Hive [Metastore](/concepts/metastore.md). However, you must provide partitioning information for Unity Catalog external tables. If the Parquet table is partitioned, include the `PARTITIONED BY` clause: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

## Converting managed tables

The `CONVERT TO DELTA` syntax can only be used for creating Unity Catalog external tables. To convert a legacy Hive [Metastore](/concepts/metastore.md) managed Parquet table directly to a managed Unity Catalog [Delta Lake Table](/concepts/delta-lake-table.md), use a `CREATE TABLE AS SELECT` (CTAS) statement instead. See [Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT](/concepts/ctas-for-migrating-hive-tables-to-unity-catalog-managed-delta-tables.md). ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting external Hive [Metastore](/concepts/metastore.md) tables

To upgrade an external Parquet table from the Hive [Metastore](/concepts/metastore.md) to a Unity Catalog external table before conversion, see [Upgrade a schema or tables from the Hive metastore to Unity Catalog external tables using the upgrade wizard](/concepts/hive-metastore-to-unity-catalog-migration.md). ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that brings ACID transactions to Apache Spark
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) — Tables whose data resides in cloud object storage managed by Unity Catalog
- [Incremental conversion](/concepts/incremental-cloning-vs-one-time-conversion.md) — Cloning Parquet or Iceberg tables to Delta Lake on an ongoing basis
- [CONVERT TO DELTA SQL Command](/concepts/convert-to-delta-sql-command.md) — The technical documentation for the SQL syntax

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
