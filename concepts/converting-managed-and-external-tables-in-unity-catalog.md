---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fbe2ec5e2a70c464d3510db2dca245fe80f510c468acdbf3872eab6f9f9073f4
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - converting-managed-and-external-tables-in-unity-catalog
    - external tables in Unity Catalog and Converting managed
    - CMAETIUC
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Converting managed and external tables in Unity Catalog
description: Process for converting Hive metastore Parquet tables to Unity Catalog Delta Lake tables using CONVERT TO DELTA or CTAS
tags:
  - unity-catalog
  - hive-metastore
  - data-migration
timestamp: "2026-06-19T14:27:17.698Z"
---

# Converting Managed and [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md)

**Converting managed and external tables in Unity Catalog** refers to the process of transforming existing Parquet or Apache Iceberg data files—registered as either managed or external tables in Unity Catalog—into [Delta Lake](/concepts/delta-lake.md) tables. This conversion unlocks full Delta Lake features including ACID transactions, time travel, schema enforcement, and performance optimizations. ^[convert-to-delta-lake-databricks-on-aws.md]

## Overview

Unity Catalog supports the `CONVERT TO DELTA` SQL command for Parquet and Iceberg tables stored in [external locations](/concepts/external-location.md) managed by Unity Catalog. You can configure existing Parquet data files as [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) and then convert them to Delta Lake to unlock all features of the Databricks lakehouse. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting External Tables to Delta Lake

After you have registered an external Parquet table to Unity Catalog, you can convert it to an external [Delta Lake Table](/concepts/delta-lake-table.md) using the `CONVERT TO DELTA` command. You must provide partitioning information if the Parquet table is partitioned. ^[convert-to-delta-lake-databricks-on-aws.md]

### Syntax

```sql
CONVERT TO DELTA catalog_name.database_name.table_name;
```

To specify partitioning information for a partitioned Parquet table:

```sql
CONVERT TO DELTA catalog_name.database_name.table_name PARTITIONED BY (date_updated DATE);
```

^[convert-to-delta-lake-databricks-on-aws.md]

## Converting a Directory of Parquet or Iceberg Files

You can also convert a directory of Parquet or Iceberg data files stored in an external location directly to a [Delta Lake Table](/concepts/delta-lake-table.md), provided you have write access on the storage location. ^[convert-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;
CONVERT TO DELTA iceberg.`s3://my-bucket/iceberg-data`;
```

For information on configuring access with Unity Catalog, see Connect to cloud object storage using Unity Catalog. ^[convert-to-delta-lake-databricks-on-aws.md]

### Requirements for External Location Conversion

- You must have write access on the storage location. ^[convert-to-delta-lake-databricks-on-aws.md]
- To load converted tables as external tables to Unity Catalog, you need the `CREATE EXTERNAL TABLE` permission on the external location. ^[convert-to-delta-lake-databricks-on-aws.md]
- For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the [Hive metastore](/concepts/built-in-hive-metastore.md). You must provide partitioning information for [Unity Catalog](/concepts/unity-catalog.md) external tables. ^[convert-to-delta-lake-databricks-on-aws.md]

### Converting Iceberg Tables

Converting Iceberg tables is supported in Databricks Runtime 10.4 LTS and above, with the following limitations: ^[convert-to-delta-lake-databricks-on-aws.md]

- Converting Iceberg [Metastore](/concepts/metastore.md) tables is not supported. ^[convert-to-delta-lake-databricks-on-aws.md]
- Converting Iceberg tables that have experienced [partition evolution](/concepts/partition-evolution-in-iceberg.md) is not supported. ^[convert-to-delta-lake-databricks-on-aws.md]
- For Iceberg tables with partitions defined on truncated columns:
    - In Databricks Runtime 12.2 LTS and below, the only supported truncated column type is `string`. ^[convert-to-delta-lake-databricks-on-aws.md]
    - In Databricks Runtime 13.3 LTS and above, you can work with truncated columns of types `string`, `long`, or `int`. ^[convert-to-delta-lake-databricks-on-aws.md]
    - Databricks does not support working with truncated columns of type `decimal`. ^[convert-to-delta-lake-databricks-on-aws.md]

## Converting [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md)

`CONVERT TO DELTA` syntax can only be used for creating Unity Catalog external tables. To convert a legacy Hive [Metastore](/concepts/metastore.md) managed Parquet table directly to a managed Unity Catalog [Delta Lake Table](/concepts/delta-lake-table.md), use a CTAS (Create Table As Select) statement. ^[convert-to-delta-lake-databricks-on-aws.md]

See [Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT](/concepts/ctas-for-migrating-hive-tables-to-unity-catalog-managed-delta-tables.md) for details. ^[convert-to-delta-lake-databricks-on-aws.md]

To upgrade an external Parquet table to a Unity Catalog external table, see [Upgrade a schema or tables from the Hive metastore to Unity Catalog external tables using the upgrade wizard](/concepts/hive-metastore-to-unity-catalog-migration.md). ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The foundation of the Databricks lakehouse, providing ACID transactions, scalable metadata handling, and unified batch/streaming.
- [External tables](/concepts/unity-catalog-external-table-conversion.md) — Tables whose data is stored outside the Unity Catalog managed storage location.
- [Managed tables](/concepts/managed-tables-in-databricks.md) — Tables whose data is managed by Unity Catalog.
- [Hive metastore](/concepts/built-in-hive-metastore.md) — The legacy metadata store for non-Unity Catalog tables.
- Parquet — Columnar storage format commonly used in Spark and Delta Lake ecosystems.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — An open table format for large analytic datasets.
- Partitioning — Technique to improve query performance by organizing data into partitions.
- CTAS — Create Table As Select statement used for table conversion.

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
