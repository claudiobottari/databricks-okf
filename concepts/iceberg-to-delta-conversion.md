---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cce0409a960c1e13a202450338483e753d823865f9f8257fe025a137c1c7895c
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-to-delta-conversion
    - ITDC
    - Iceberg Table Conversion
    - apache-iceberg-to-delta-lake-conversion
    - AITDLC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Iceberg to Delta Conversion
description: Converting Apache Iceberg tables whose underlying file format is Parquet to Delta Lake, using the Iceberg table's native file manifest, schema and partitioning information.
tags:
  - delta-lake
  - iceberg
  - table-conversion
timestamp: "2026-06-19T17:52:29.779Z"
---

# Iceberg to Delta Conversion

**Iceberg to Delta Conversion** refers to the process of converting an existing Apache Iceberg table (with Parquet underlying files) to a [Delta Lake Table](/concepts/delta-lake-table.md) in-place using the `CONVERT TO DELTA` SQL command. This conversion enables organizations to migrate Iceberg workloads to [Delta Lake](/concepts/delta-lake.md) without rewriting data files, preserving the underlying data while transitioning to Delta Lake's transaction log and performance optimizations. ^[convert-to-delta-databricks-on-aws.md]

## Overview

Iceberg to Delta conversion transforms an Iceberg table whose underlying file format is Parquet into a Delta table. Rather than rewriting data files, the converter generates a Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. This approach allows for a relatively fast migration since the bulk of the data remains unchanged. ^[convert-to-delta-databricks-on-aws.md]

## Syntax

The conversion uses the `CONVERT TO DELTA` command with the `iceberg.` prefix to indicate the source format:

```sql
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

- **table_name**: For Iceberg tables, only paths are supported. Converting managed Iceberg tables is not supported. The path must point to the Iceberg table directory. ^[convert-to-delta-databricks-on-aws.md]
- **NO STATISTICS**: Bypasses statistics collection during conversion for faster processing. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics. ^[convert-to-delta-databricks-on-aws.md]
- **PARTITIONED BY**: For Iceberg tables, you do not need to provide partitioning information — the converter automatically reads it from the Iceberg metadata. ^[convert-to-delta-databricks-on-aws.md]

## How It Works

The conversion process performs the following steps:

1. Reads the Iceberg table's native file manifest to identify all data files
2. Extracts schema and partitioning information from Iceberg metadata
3. Creates a [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) that tracks these files
4. Automatically infers the data schema by reading the footers of all Parquet files
5. Collects statistics to improve query performance on the converted Delta table

If a table name is provided (for Parquet tables), the [Metastore](/concepts/metastore.md) is also updated to reflect the new Delta table format. ^[convert-to-delta-databricks-on-aws.md]

## Important Considerations

### File Visibility

Any file not tracked by the Delta Lake transaction log is invisible and can be deleted when running `VACUUM`. You should avoid updating or appending data files during the conversion process. After conversion, all writes must go through Delta Lake. ^[convert-to-delta-databricks-on-aws.md]

### Shared Directories

Multiple external tables may share the same underlying Iceberg or Parquet directory. If you run `CONVERT` on one external table, other tables sharing that directory become inaccessible because the underlying directory is converted from Iceberg/Parquet to Delta Lake. To query or write to those tables again, you must run `CONVERT` on them as well. ^[convert-to-delta-databricks-on-aws.md]

### Metadata Mismatch

`CONVERT TO DELTA` populates catalog information (schema, table properties) to the Delta Lake transaction log. If the underlying directory has already been converted to Delta Lake and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown. In Databricks Runtime, you can set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false` to overwrite existing metadata. ^[convert-to-delta-databricks-on-aws.md]

## Comparison: Iceberg vs. Parquet Conversion

| Feature | Parquet Conversion | Iceberg Conversion |
|---------|-------------------|-------------------|
| Source format | Apache Parquet | Apache Iceberg (Parquet-backed) |
| Metadata source | Reads Parquet file footers | Reads Iceberg file manifest |
| Partitioning info | May require `PARTITIONED BY` | Automatically inferred |
| Path vs. table name | Both supported | Paths only |
| Managed tables | Supported | Not supported |

^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The target format after conversion
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source table format
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The general command for converting Parquet or Iceberg tables
- VACUUM — Cleanup operation for untracked files after conversion
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended optimization after conversion
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The metadata layer created during conversion
- [Parquet-to-Delta Conversion](/concepts/parquet-to-delta-conversion.md) — Converting Parquet tables to Delta Lake

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
