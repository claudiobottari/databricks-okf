---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1fa696e84188905091b5133c1c55dd65e6fa790ada2b5e76ead49fa3285873fb
  pageDirectory: concepts
  sources:
    - convert-to-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-table-conversion-limitations
    - ITCL
  citations:
    - file: convert-to-delta-lake-databricks-on-aws.md
title: Iceberg Table Conversion Limitations
description: Restrictions and unsupported scenarios when converting Iceberg tables, including partition evolution, metastore tables, and truncated column type limitations.
tags:
  - delta-lake
  - iceberg
  - limitations
timestamp: "2026-06-19T17:53:17.482Z"
---

# Iceberg Table Conversion Limitations

**Iceberg Table Conversion Limitations** refer to the constraints and unsupported scenarios when using the `CONVERT TO DELTA` SQL command in Databricks to transform an Apache Iceberg table into a [Delta Lake](/concepts/delta-lake.md) table. While the command performs a one-time conversion, several limitations affect the types of Iceberg tables that can be successfully converted.

## Overview

The `CONVERT TO DELTA` command supports conversion of [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) tables stored in external locations managed by [Unity Catalog](/concepts/unity-catalog.md). However, the conversion process has specific restrictions related to Iceberg table metadata, partition evolution, and data types. ^[convert-to-delta-lake-databricks-on-aws.md]

## Supported and Unsupported Conversion Scenarios

### Iceberg [Metastore](/concepts/metastore.md) Tables
Converting Iceberg [Metastore](/concepts/metastore.md) tables is **not supported**. The conversion command only applies to Iceberg tables that are stored as directories of Parquet or Iceberg files in an external location, not those managed through the Iceberg [Metastore](/concepts/metastore.md). ^[convert-to-delta-lake-databricks-on-aws.md]

### Partition Evolution
Converting Iceberg tables that have experienced **partition evolution** is not supported. If an Iceberg table has undergone partition evolution — where the partitioning scheme changed over the table's lifetime — the conversion command will fail. ^[convert-to-delta-lake-databricks-on-aws.md]

### Truncated Column Partitions
Iceberg tables with partitions defined on **truncated columns** have specific limitations depending on the Databricks Runtime version:

- **Databricks Runtime 12.2 LTS and below**: The only supported truncated column type is `string`. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Databricks Runtime 13.3 LTS and above**: Support extends to truncated columns of types `string`, `long`, or `int`. ^[convert-to-delta-lake-databricks-on-aws.md]
- **Unsupported**: Databricks does not support working with truncated columns of type `decimal` in any runtime version. ^[convert-to-delta-lake-databricks-on-aws.md]

### Data Type Restrictions
For Iceberg tables with partitions on truncated columns, the `decimal` data type is not supported. This limitation applies across all supported Databricks Runtime versions. ^[convert-to-delta-lake-databricks-on-aws.md]

## Conversion Requirements

### Write Access
Conversion requires write access on the storage location where the Iceberg table's Parquet or Iceberg files are stored. For Unity Catalog-managed external locations, you must configure appropriate access permissions. ^[convert-to-delta-lake-databricks-on-aws.md]

### Partitioning Information
For tables registered to the Hive [Metastore](/concepts/metastore.md), `CONVERT TO DELTA` in Databricks Runtime 11.3 LTS and above automatically infers partitioning information. For Unity Catalog external tables, you must provide partitioning information if the Iceberg table is partitioned. ^[convert-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Parquet Table Conversion](/concepts/parquet-to-delta-conversion.md)
- [Incremental Cloning to Delta Lake](/concepts/incremental-cloning-to-delta-lake.md)
- Delta Lake Conversion Best Practices

## Sources

- convert-to-delta-lake-databricks-on-aws.md

# Citations

1. [convert-to-delta-lake-databricks-on-aws.md](/references/convert-to-delta-lake-databricks-on-aws-85c3b3fb.md)
