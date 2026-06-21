---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6496c768eb80ed1cbe605c4125f083c5ccbd889598f1467f8b6105c0c6abc25
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - in-place-table-format-conversion
    - ITFC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: In-place Table Format Conversion
description: The process of converting a table from one format (Parquet or Iceberg) to Delta Lake without copying or rewriting the underlying data files, only generating transaction metadata.
tags:
  - delta-lake
  - data-migration
  - performance
timestamp: "2026-06-19T09:24:29.974Z"
---

# In-place Table Format Conversion

**In-place Table Format Conversion** refers to the process of converting an existing table stored in one format — such as Apache Parquet or Apache Iceberg — into a [Delta Lake](/concepts/delta-lake.md) table without moving or copying the underlying data files. The conversion operates directly on the existing directory structure, creating a Delta Lake transaction log that tracks the existing files and updates the [Metastore](/concepts/metastore.md) to reflect the new format. ^[convert-to-delta-databricks-on-aws.md]

## Overview

The conversion command lists all files in the directory, creates a Delta Lake transaction log that tracks these files, and automatically infers the data schema by reading the footers of all Parquet files. The process collects statistics to improve query performance on the converted Delta table. If a table name is provided, the [Metastore](/concepts/metastore.md) is also updated to reflect that the table is now a Delta table. ^[convert-to-delta-databricks-on-aws.md]

## Supported Source Formats

### Parquet Tables

The command converts existing Apache Parquet tables to Delta tables in-place. For partitioned Parquet data, the partition specification must be provided or loaded from the [Metastore](/concepts/metastore.md). The conversion aborts with an exception if the directory structure does not conform to the partition specification. ^[convert-to-delta-databricks-on-aws.md]

### Iceberg Tables

The command supports converting Apache Iceberg tables whose underlying file format is Parquet. For Iceberg tables, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. Only paths can be used for Iceberg tables, as converting managed Iceberg tables is not supported. ^[convert-to-delta-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

### table_name

Either an optionally qualified table identifier or a path to a Parquet or Iceberg file directory. The name must not include a temporal specification or options specification. ^[convert-to-delta-databricks-on-aws.md]

### NO STATISTICS

Bypasses statistics collection during the conversion process, finishing conversion faster. After the table is converted to Delta Lake, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics. ^[convert-to-delta-databricks-on-aws.md]

### PARTITIONED BY

Partitions the created table by the specified columns. When `table_name` is a path, `PARTITIONED BY` is required for partitioned data. When the `table_name` is a qualified table identifier, `PARTITIONED BY` is optional and the partition specification is loaded from the [Metastore](/concepts/metastore.md). The conversion process aborts if the directory structure does not conform to the provided or loaded specification. ^[convert-to-delta-databricks-on-aws.md]

## Examples

```sql
-- For Parquet tables registered in the [[metastore|Metastore]]
CONVERT TO DELTA database_name.table_name;

-- For partitioned Parquet tables using a path
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table` PARTITIONED BY (date DATE);

-- For Iceberg tables
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

## Caveats

Any file not tracked by Delta Lake is invisible and can be deleted when running `VACUUM`. Users should avoid updating or appending data files during the conversion process. After the table is converted, all writes must go through Delta Lake. ^[convert-to-delta-databricks-on-aws.md]

If multiple external tables share the same underlying Parquet directory, converting one external table prevents access to the others. To query or write to those external tables again, they must also be converted to Delta Lake. ^[convert-to-delta-databricks-on-aws.md]

The `CONVERT` command populates catalog information — such as schema and table properties — to the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. ^[convert-to-delta-databricks-on-aws.md]

## Best Practices

- **Plan for partitioning**: Ensure the directory structure matches the partition specification before conversion, or the process will abort.
- **Avoid concurrent writes**: Do not update or append data files during the conversion process to maintain consistency.
- **Consider statistics**: Use `NO STATISTICS` for faster conversion, but plan to apply liquid clustering afterward to optimize query performance.
- **Coordinate external tables**: If multiple external tables share a directory, convert them all during the same maintenance window to avoid access interruptions.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The target format for conversion
- Apache Parquet — A source format supported for conversion
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — A source format supported for conversion (Parquet-backed)
- VACUUM — Removes files not tracked by the Delta Lake transaction log
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended post-conversion optimization for data layout and statistics
- External Tables — Can share underlying directories, requiring coordinated conversion

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
