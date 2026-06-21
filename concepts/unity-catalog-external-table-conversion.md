---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 636720a9c30080e745005ebd6ada303879ac23c8aec654b6b57116ddc7443ff1
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-external-table-conversion
    - UCETC
    - Unity Catalog External Tables
    - Unity Catalog external tables
    - External tables
    - Unity Catalog External Tables|external data assets
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Unity Catalog External Table Conversion
description: Converting Parquet or Iceberg tables stored in external locations managed by Unity Catalog to Delta Lake using CONVERT TO DELTA.
tags:
  - unity-catalog
  - delta-lake
  - migration
timestamp: "2026-06-19T17:53:47.571Z"
---

# Unity Catalog External Table Conversion

**Unity Catalog External Table Conversion** is the process of registering existing Parquet or Apache Iceberg data files stored in external cloud storage as [Unity Catalog](/concepts/unity-catalog.md) external tables, and then converting them to [Delta Lake](/concepts/delta-lake.md) format using the `CONVERT TO DELTA` SQL command. This conversion unlocks the full feature set of the Databricks lakehouse, including ACID transactions, time travel, and schema enforcement. ^[convert-to-delta-lake-databricks-on-aws.md]

## Overview

The `CONVERT TO DELTA` SQL command performs a one-time conversion for Parquet and Apache Iceberg tables to Delta Lake tables. For incremental conversion, see [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md). Unity Catalog supports this command for tables stored in external locations managed by Unity Catalog. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting a Directory of Files

You can convert a directory of Parquet or Iceberg data files to a [Delta Lake Table](/concepts/delta-lake-table.md) as long as you have write access to the storage location. For information on configuring access with Unity Catalog, see Connect to cloud object storage using Unity Catalog. ^[convert-to-delta-lake-databricks-on-aws.md]

### SQL Syntax

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;
CONVERT TO DELTA iceberg.`s3://my-bucket/iceberg-data`;
```

The syntax uses `parquet.<path>` or `iceberg.<path>` to point to the directory of files. The command converts the files in place to Delta Lake format. ^[convert-to-delta-lake-databricks-on-aws.md]

### Registering as External Tables

To load converted tables as [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md), you need the `CREATE EXTERNAL TABLE` permission on the external location. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting Managed and External Tables

`CONVERT TO DELTA` syntax can only be used for creating Unity Catalog external tables. Use a `CREATE TABLE AS SELECT` (CTAS) statement to convert a legacy Hive [Metastore](/concepts/metastore.md) managed Parquet table directly to a managed Unity Catalog [Delta Lake Table](/concepts/delta-lake-table.md). See [Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT](/concepts/ctas-for-migrating-hive-tables-to-unity-catalog-managed-delta-tables.md). ^[convert-to-delta-lake-databricks-on-aws.md]

To upgrade an external Parquet table to a Unity Catalog external table, use the upgrade wizard. See [Upgrade a schema or tables from the Hive metastore to Unity Catalog external tables using the upgrade wizard](/concepts/hive-metastore-to-unity-catalog-table-migration.md). ^[convert-to-delta-lake-databricks-on-aws.md]

### Converting an Existing External Table

After you have registered an external Parquet table to Unity Catalog, you can convert it to an external [Delta Lake Table](/concepts/delta-lake-table.md) using the `CONVERT TO DELTA` command with the Unity Catalog table name: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name;
```

### Partitioning Considerations

For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the Hive [Metastore](/concepts/metastore.md). However, you must provide partitioning information for Unity Catalog external tables if the Parquet table is partitioned: ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

## Iceberg Table Conversion Limitations

Converting Iceberg tables has the following limitations: ^[convert-to-delta-lake-databricks-on-aws.md]

- Converting Iceberg tables is supported in Databricks Runtime 10.4 LTS and above.
- Converting Iceberg [Metastore](/concepts/metastore.md) tables is not supported.
- Converting Iceberg tables that have experienced [partition evolution](/concepts/partition-evolution-in-iceberg.md) is not supported.
- For Iceberg tables with partitions defined on truncated columns:
  - In Databricks Runtime 12.2 LTS and below, the only supported truncated column type is `string`.
  - In Databricks Runtime 13.3 LTS and above, you can work with truncated columns of types `string`, `long`, or `int`.
  - Databricks does not support working with truncated columns of type `decimal`.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage format that tables are converted to
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) — Tables stored in external cloud storage managed by Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for managing external locations and permissions
- [Incrementally clone Parquet and Apache Iceberg tables to Delta Lake](/concepts/incremental-clone-of-parquet-and-iceberg-to-delta-lake.md) — Alternative approach for incremental conversion
- [CONVERT TO DELTA SQL Command](/concepts/convert-to-delta-sql-command.md) — The technical documentation for the SQL command
- Connect to cloud object storage using Unity Catalog — How to configure access for conversion
- [Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT](/concepts/ctas-for-migrating-hive-tables-to-unity-catalog-managed-delta-tables.md) — Method for converting managed Hive tables
- [Upgrade a schema or tables from the Hive metastore to Unity Catalog external tables using the upgrade wizard](/concepts/hive-metastore-to-unity-catalog-table-migration.md) — Alternative method for upgrading external tables

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
