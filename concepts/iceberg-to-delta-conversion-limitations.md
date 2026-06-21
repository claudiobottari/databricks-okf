---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 301d1a992f3a6aaa8bb798ce55d2657df6eaeb17daa47b34766c7bb7cde076cb
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-to-delta-conversion-limitations
    - ITDCL
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Iceberg to Delta conversion limitations
description: Technical constraints when converting Iceberg tables including partition evolution and truncated column type restrictions
tags:
  - iceberg
  - delta-lake
  - limitations
timestamp: "2026-06-19T14:26:34.466Z"
---

# Iceberg to Delta Conversion Limitations

**Iceberg to Delta Conversion Limitations** refers to the constraints and unsupported scenarios when using the `CONVERT TO DELTA` SQL command to convert Apache Iceberg tables to [Delta Lake](/concepts/delta-lake.md) tables on Databricks. Understanding these limitations is essential before planning a migration from Iceberg to Delta Lake.

## Supported Environments

Converting Iceberg tables is supported in Databricks Runtime 10.4 LTS and above. However, several important restrictions apply regardless of the runtime version. ^[convert-to-delta-lake-databricks-on-aws.md]

## Unsupported Conversion Scenarios

### Iceberg [Metastore](/concepts/metastore.md) Tables

Converting Iceberg [Metastore](/concepts/metastore.md) tables is not supported. The `CONVERT TO DELTA` command can only convert directories of Iceberg files in external locations, not tables registered in the Hive [Metastore](/concepts/metastore.md) as Iceberg tables. ^[convert-to-delta-lake-databricks-on-aws.md]

### Partition Evolution

Iceberg tables that have experienced [partition evolution](/concepts/partition-evolution-in-iceberg.md) — where the partitioning scheme of a table has changed over time — are not supported for conversion to Delta Lake. ^[convert-to-delta-lake-databricks-on-aws.md]

## Partition on Truncated Columns

When an Iceberg table has partitions defined on truncated columns, additional limitations apply based on the Databricks Runtime version:

| Runtime Version | Supported Truncated Column Types |
|:----------------|:---------------------------------|
| 12.2 LTS and below | `string` only |
| 13.3 LTS and above | `string`, `long`, `int` |
| All versions | `decimal` is not supported |

^[convert-to-delta-lake-databricks-on-aws.md]

For Databricks Runtime 12.2 LTS and below, the only truncated column type supported is `string`. In Databricks Runtime 13.3 LTS and above, you can work with truncated columns of types `string`, `long`, or `int`. Databricks does not support working with truncated columns of type `decimal` at any runtime version. ^[convert-to-delta-lake-databricks-on-aws.md]

## Conversion Requirements

### Partitioning Information

For Databricks Runtime 11.3 LTS and above, `CONVERT TO DELTA` automatically infers partitioning information for tables registered to the Hive [Metastore](/concepts/metastore.md). However, you must provide partitioning information for [Unity Catalog](/concepts/unity-catalog.md) external tables. ^[convert-to-delta-lake-databricks-on-aws.md]

### Write Access

You can convert a directory of Parquet or Iceberg files to a [Delta Lake Table](/concepts/delta-lake-table.md) only if you have write access on the storage location. For Unity Catalog, this requires the `CREATE EXTERNAL TABLE` permission on the external location. ^[convert-to-delta-lake-databricks-on-aws.md]

## One-Time Conversion Only

The `CONVERT TO DELTA` command performs a one-time conversion for Iceberg tables to Delta Lake. For incremental conversion of Iceberg tables to Delta Lake, see the documentation on incrementally cloning Parquet and Apache Iceberg tables to Delta Lake. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The target format for conversion
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source format being converted
- [CONVERT TO DELTA Command](/concepts/convert-to-delta-command.md) — The SQL command used for conversion
- Incremental cloning from Iceberg to Delta Lake — Alternative approach for ongoing migration
- Unity Catalog external tables — Target storage for converted tables
- [Partition Evolution in Iceberg](/concepts/partition-evolution-in-iceberg.md) — Unsupported table feature for conversion
- [Hive metastore migration to Unity Catalog](/concepts/hive-metastore-federation-to-unity-catalog.md) — Related migration workflow

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
