---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 141b1c3ca872f3aded334725038513c214c7b7efae5eb1b4397887a69f6ae08e
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apache-iceberg-to-delta-lake-conversion
    - AITDLC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Apache Iceberg to Delta Lake Conversion
description: Converting Iceberg tables (with Parquet file format) to Delta Lake by using the Iceberg manifest for metadata, schema, and partitioning information.
tags:
  - delta-lake
  - iceberg
  - data-migration
  - interoperability
timestamp: "2026-06-18T11:10:24.914Z"
---

# Apache Iceberg to Delta Lake Conversion

**Apache Iceberg to Delta Lake Conversion** is a feature of the [CONVERT TO DELTA](/concepts/convert-to-delta.md) SQL command that allows in-place conversion of existing Apache Iceberg tables (whose underlying file format is Parquet) to [Delta Lake](/concepts/delta-lake.md) tables. The converter reads the Iceberg table’s native file manifest, schema, and partitioning information to generate a Delta Lake transaction log, avoiding a full data rewrite.^[convert-to-delta-databricks-on-aws.md]

## Overview

The `CONVERT TO DELTA` command converts an existing table to Delta Lake in place. For Parquet-based tables (including those from Iceberg), the command lists files, creates a Delta Lake transaction log that tracks those files, and infers the schema from the footer of each Parquet file. Statistics are collected during conversion to improve query performance on the resulting Delta table. If a table name is provided, the [Metastore](/concepts/metastore.md) is also updated to reflect the new table format.^[convert-to-delta-databricks-on-aws.md]

For Iceberg tables specifically, the converter uses the Iceberg manifest, schema, and partition metadata directly, rather than scanning Parquet file footers. This makes the conversion faster and more accurate for Iceberg tables.^[convert-to-delta-databricks-on-aws.md]

## Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

^[convert-to-delta-databricks-on-aws.md]

## Parameters

- **`table_name`**: Either an optionally qualified table identifier or a path to a Parquet or Iceberg file directory. The name must not include a temporal specification or options specification. For Iceberg tables, only paths are supported — converting managed Iceberg tables is not allowed.^[convert-to-delta-databricks-on-aws.md]
- **`NO STATISTICS`**: Bypasses statistics collection during conversion. This speeds up the conversion but disables statistics‑based optimizations. After conversion, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize data and generate statistics.^[convert-to-delta-databricks-on-aws.md]
- **`PARTITIONED BY`**: Partitions the resulting Delta table by the specified columns. When `table_name` is a path, this clause is required for partitioned data. When `table_name` is a qualified table identifier, the partition specification is loaded from the [Metastore](/concepts/metastore.md) (making the clause optional). If the directory structure does not match the provided or loaded partitioning, the conversion aborts with an exception.^[convert-to-delta-databricks-on-aws.md]

You do **not** need to provide partitioning information for Iceberg tables or tables already registered in the [Metastore](/concepts/metastore.md).^[convert-to-delta-databricks-on-aws.md]

## Examples

```sql
-- Convert a Parquet table registered in the [[metastore|Metastore]]
CONVERT TO DELTA database_name.table_name;

-- Convert a partitioned Parquet table by path
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table`
  PARTITIONED BY (date DATE);

-- Convert an Iceberg table by path (uses Iceberg manifest)
CONVERT TO DELTA iceberg.`s3://my-bucket/path/to/table`;
```

^[convert-to-delta-databricks-on-aws.md]

## Caveats

- Any file not tracked by the Delta Lake transaction log becomes invisible and can be deleted when `VACUUM` is run. Avoid updating or appending data files during the conversion process. After conversion, ensure all writes go through Delta Lake.^[convert-to-delta-databricks-on-aws.md]
- If multiple external tables share the same underlying Parquet directory, converting one will break the others because the directory format changes from Parquet to Delta Lake. You must run `CONVERT TO DELTA` on each of those tables before they can be accessed again.^[convert-to-delta-databricks-on-aws.md]
- The `CONVERT` command populates catalog information (schema, table properties) into the Delta Lake transaction log. If the underlying directory has already been converted and its metadata differs from the catalog metadata, a `convertMetastoreMetadataMismatchException` is thrown.^[convert-to-delta-databricks-on-aws.md]
- In Databricks Runtime, you can override this check by setting `spark.databricks.delta.convert.metadataCheck.enabled` to `false`, allowing the conversion to overwrite existing transaction log metadata.^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open‑format storage layer that the conversion targets
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source table format supported for conversion
- Parquet table — The common underlying file format for both Iceberg and direct Parquet conversions
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The SQL command that performs the conversion
- [Transaction log](/concepts/delta-transaction-log.md) — The Delta Lake component generated during conversion
- VACUUM — The operation that removes untracked files after conversion
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended post‑conversion optimization for data layout and statistics

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
