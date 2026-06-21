---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89234dc642718acb754fc73d2f6f91fc892091848c37d2ded742499fbd7ced67
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-transaction-log-generation
    - DLTLG
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Delta Lake Transaction Log Generation
description: During conversion, CONVERT TO DELTA scans existing Parquet files (or Iceberg manifests) and creates a Delta Lake transaction log that tracks those files, with no data rewriting required.
tags:
  - delta-lake
  - transaction-log
  - conversion
timestamp: "2026-06-18T14:44:31.831Z"
---

# Delta Lake Transaction Log Generation

**Delta Lake Transaction Log Generation** refers to the process by which the `CONVERT TO DELTA` command creates a Delta Lake transaction log for an existing Apache Parquet or Apache Iceberg table, enabling Delta Lake features such as ACID transactions, time travel, and improved query performance.

## Overview

When converting an existing table to Delta Lake format, the system generates a Delta Lake transaction log that tracks all existing data files. This log is the core metadata component that enables Delta Lake's transactional capabilities. The conversion process is performed in-place, meaning the original data files are not copied or moved. ^[convert-to-delta-databricks-on-aws.md]

## Conversion Process

### For Parquet Tables

The `CONVERT TO DELTA` command lists all files in the directory, creates a Delta Lake transaction log that tracks these files, and automatically infers the data schema by reading the footers of all Parquet files. The conversion process also collects statistics to improve query performance on the converted Delta table. If a table name is provided, the [Metastore](/concepts/metastore.md) is updated to reflect that the table is now a Delta table. ^[convert-to-delta-databricks-on-aws.md]

### For Iceberg Tables

The command supports converting Apache Iceberg tables whose underlying file format is Parquet. In this case, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. ^[convert-to-delta-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

- **table_name**: Either an optionally qualified table identifier or a path to a Parquet or Iceberg file directory. For Iceberg tables, only paths can be used, as converting managed Iceberg tables is not supported. ^[convert-to-delta-databricks-on-aws.md]

- **NO STATISTICS**: Bypasses statistics collection during the conversion process to finish conversion faster. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics. ^[convert-to-delta-databricks-on-aws.md]

- **PARTITIONED BY**: Partitions the created table by the specified columns. When `table_name` is a path, `PARTITIONED BY` is required for partitioned data. When the `table_name` is a qualified table identifier, the partition specification is loaded from the [Metastore](/concepts/metastore.md). The conversion process aborts if the directory structure does not conform to the provided or loaded partition specification. ^[convert-to-delta-databricks-on-aws.md]

## Examples

```sql
-- Convert a Parquet table registered in the [[metastore|Metastore]]
CONVERT TO DELTA database_name.table_name;

-- Convert a partitioned Parquet table at a specific path
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table` PARTITIONED BY (date DATE);

-- Convert an Iceberg table using its manifest for metadata
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

## Caveats

Any file not tracked by Delta Lake is invisible and can be deleted when running `VACUUM`. Users should avoid updating or appending data files during the conversion process. After the table is converted, all writes must go through Delta Lake. ^[convert-to-delta-databricks-on-aws.md]

If multiple external tables share the same underlying Parquet directory, running `CONVERT` on one table will prevent access to the other external tables because their underlying directory has been converted from Parquet to Delta Lake. To query or write to these external tables again, `CONVERT` must be run on them as well. ^[convert-to-delta-databricks-on-aws.md]

The `CONVERT` command populates catalog information, such as schema and table properties, to the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. In Databricks Runtime, setting the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false` allows `CONVERT` to overwrite existing metadata in the Delta Lake transaction log. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and scalable metadata handling
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The ordered record of every change made to a Delta table
- VACUUM — The command that removes files not tracked by the Delta Lake transaction log
- [Liquid Clustering](/concepts/liquid-clustering.md) — A technique for reorganizing data layout and generating statistics after conversion
- Parquet — The underlying file format for Delta Lake tables
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — Another open table format that can be converted to Delta Lake

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
