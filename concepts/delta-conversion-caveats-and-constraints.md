---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c8dd200b1ce15b56c386a984c77564558330a8268c17771e1e17315f4ca5ccc
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-conversion-caveats-and-constraints
    - Constraints and Delta Conversion Caveats
    - DCCAC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Delta Conversion Caveats and Constraints
description: "Important limitations: file visibility after conversion, shared external directories across tables, and metadata mismatch exceptions when catalog and log diverge."
tags:
  - delta-lake
  - best-practices
  - operations
timestamp: "2026-06-18T11:10:47.792Z"
---

# Delta Conversion Caveats and Constraints

**Delta Conversion Caveats and Constraints** describes the limitations, risks, and behavioral rules that apply when converting existing Parquet or Iceberg tables to [Delta Lake](/concepts/delta-lake.md) using the `CONVERT TO DELTA` command. Understanding these caveats is essential to avoid data loss, table inaccessibility, or metadata mismatches after conversion. ^[convert-to-delta-databricks-on-aws.md]

## Overview

`CONVERT TO DELTA` creates a Delta Lake transaction log for an existing Parquet or Iceberg table, tracks all files in the directory, and updates the [Metastore](/concepts/metastore.md) if a table name is provided. For Iceberg tables whose underlying file format is Parquet, the converter generates the Delta log from the Iceberg manifest. ^[convert-to-delta-databricks-on-aws.md]

## Caveats

### File Visibility and Data Integrity

Any file not tracked by Delta Lake after conversion becomes invisible to Delta Lake operations and can be deleted when `VACUUM` is run. You should avoid updating or appending data files during the conversion process. Once the table is converted, all writes must go through Delta Lake; otherwise, files added externally remain invisible and may be removed by `VACUUM`. ^[convert-to-delta-databricks-on-aws.md]

### Shared Parquet Directories

If multiple external tables share the same underlying Parquet directory and you run `CONVERT TO DELTA` on one of them, the other external tables become inaccessible because their underlying directory has been converted from Parquet to Delta Lake. To restore access, you must also run `CONVERT TO DELTA` on each of those tables. ^[convert-to-delta-databricks-on-aws.md]

### Metadata Mismatch

`CONVERT TO DELTA` populates catalog information — such as schema and table properties — into the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. In Databricks Runtime, you can override this check by setting `spark.databricks.delta.convert.metadataCheck.enabled` to `false`, which allows the conversion to overwrite the existing metadata. ^[convert-to-delta-databricks-on-aws.md]

## Constraints

### Managed Iceberg Tables Not Supported

You can only convert Iceberg tables by specifying a path (e.g., `iceberg.`s3://bucket/path/to/table``). Converting managed Iceberg tables is not supported. ^[convert-to-delta-databricks-on-aws.md]

### Partitioning Requirements

When converting a partitioned table by path, the `PARTITIONED BY` clause is **required** and must match the directory structure. When converting a qualified table identifier, the partitioning specification is loaded from the [Metastore](/concepts/metastore.md). In either case, the conversion process aborts with an exception if the directory structure does not conform to the provided or loaded partitioning specification. ^[convert-to-delta-databricks-on-aws.md]

### Statistics Collection

By default, `CONVERT TO DELTA` collects statistics from the footers of all Parquet files to improve query performance. You can bypass this step with the `NO STATISTICS` keyword to finish conversion faster. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The SQL command that performs the conversion
- [Delta Lake](/concepts/delta-lake.md) — The table format created by the conversion
- VACUUM — Delta Lake cleanup operation that removes untracked files
- Parquet — File format that can be converted to Delta Lake
- Iceberg — Table format that can be converted to Delta Lake (Parquet-based only)
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended re-clustering after conversion for performance
- Partitioning — Partitioning scheme that must match directory structure
- Statistics Collection — Performance optimization during conversion

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
