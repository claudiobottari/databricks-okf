---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8671f687671258b9885a01b2f6a08abbc5ec2b330d29785a332099f514430e7
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-to-delta-lake-conversion-limitations
    - ITDLCL
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Iceberg to Delta Lake Conversion Limitations
description: Constraints and unsupported scenarios when converting Apache Iceberg tables to Delta Lake, including partition evolution, metastore tables, and truncated column types.
tags:
  - iceberg
  - delta-lake
  - limitations
  - data-migration
timestamp: "2026-06-18T14:44:53.764Z"
---

# Iceberg to Delta Lake Conversion Limitations

**Iceberg to Delta Lake Conversion Limitations** refers to the constraints and unsupported scenarios when using the `CONVERT TO DELTA` SQL command to transform Apache Iceberg tables into [Delta Lake](/concepts/delta-lake.md) tables on Databricks. Understanding these limitations is essential for planning migration workflows and avoiding conversion failures.

## Unsupported Scenarios

### [Metastore](/concepts/metastore.md) Tables

Converting Iceberg [Metastore](/concepts/metastore.md) tables is not supported. The `CONVERT TO DELTA` command can only convert Iceberg tables stored as directories of data files in external locations, not tables registered in the Hive [Metastore](/concepts/metastore.md) or other metastores. ^[convert-to-delta-lake-databricks-on-aws.md]

### Partition Evolution

Iceberg tables that have experienced [partition evolution](https://iceberg.apache.org/docs/latest/evolution/#partition-evolution) are not supported for conversion. Partition evolution occurs when a table's partitioning scheme changes over time, resulting in data files organized under different partition specifications. Databricks cannot convert such tables to Delta Lake format. ^[convert-to-delta-lake-databricks-on-aws.md]

## Truncated Column Partition Limitations

When converting Iceberg tables with partitions defined on truncated columns, the following limitations apply depending on the Databricks Runtime version:

- **Databricks Runtime 12.2 LTS and below**: The only truncated column type supported is `string`. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Databricks Runtime 13.3 LTS and above**: You can work with truncated columns of types `string`, `long`, or `int`. ^[convert-to-delta-lake-databricks-on-aws.md]
- **All versions**: Databricks does not support working with truncated columns of type `decimal`. ^[convert-to-delta-lake-databricks-on-aws.md]

## General Requirements and Constraints

### Runtime Version

Converting Iceberg tables is supported in Databricks Runtime 10.4 LTS and above. Older runtimes cannot perform this conversion. ^[convert-to-delta-lake-databricks-on-aws.md]

### Partition Information

For Unity Catalog external tables, you must provide partitioning information if the Parquet or Iceberg table is partitioned. The `CONVERT TO DELTA` command will not automatically infer partitioning for Unity Catalog external tables. ^[convert-to-delta-lake-databricks-on-aws.md]

### Write Access

You must have write access on the storage location to perform the conversion. For Unity Catalog-managed external locations, the appropriate permissions must be configured. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA SQL Command](/concepts/convert-to-delta-sql-command.md) — The technical reference for the conversion command
- [Delta Lake](/concepts/delta-lake.md) — The target format for conversion
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source format being converted
- [External Tables on Unity Catalog](/concepts/external-tables-in-unity-catalog.md) — How to register converted tables
- [Incremental Clone to Delta Lake](/concepts/incremental-cloning-to-delta-lake.md) — Alternative approach for ongoing conversion
- Partition Evolution — An Iceberg feature that blocks conversion
- Hive Metastore Migration — Converting Hive-managed tables instead of Iceberg

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
