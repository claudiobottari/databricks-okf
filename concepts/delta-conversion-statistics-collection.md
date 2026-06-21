---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc55c00dde5812ea1160b89a192c5073c9ca504443c6221a08870c24e4394aa1
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-conversion-statistics-collection
    - DCSC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Delta Conversion Statistics Collection
description: The automatic process during CONVERT TO DELTA that collects statistics to improve query performance on the converted Delta table, which can be bypassed with the NO STATISTICS option.
tags:
  - delta-lake
  - performance
  - query-optimization
timestamp: "2026-06-19T14:26:07.994Z"
---

# Delta Conversion Statistics Collection

**Delta Conversion Statistics Collection** refers to the automatic process by which the `CONVERT TO DELTA` command gathers column-level statistics during the conversion of a Parquet or Iceberg table to a [Delta Lake](/concepts/delta-lake.md) table. These statistics are used to improve query performance on the converted Delta table. ^[convert-to-delta-databricks-on-aws.md]

## Overview

When you run `CONVERT TO DELTA` on a table stored in Apache Parquet format (or an Iceberg table whose underlying files are Parquet), the command reads the footers of all Parquet files to infer the data schema. In addition, it collects column-level statistics (such as min, max, null counts) and records them in the Delta Lake transaction log. These statistics enable Delta Lake’s query engine to perform data skipping during reads, significantly speeding up queries that filter on columns with collected statistics. ^[convert-to-delta-databricks-on-aws.md]

## How Statistics Collection Works

The conversion process does the following for Parquet tables:

1. Lists all files in the table directory.
2. Reads the metadata footers of every Parquet file to extract schema information and column statistics.
3. Creates the Delta Lake transaction log that tracks these files and stores the collected statistics.
4. If a table name is provided, updates the [Metastore](/concepts/metastore.md) to mark the table as a Delta table.

For Iceberg tables whose file format is Parquet, the converter generates the Delta transaction log using the Iceberg table’s native file manifest, schema, and partitioning information, rather than scanning each Parquet file directly. ^[convert-to-delta-databricks-on-aws.md]

## NO STATISTICS Option

The `NO STATISTICS` keyword bypasses statistics collection during conversion, finishing the conversion faster. However, without statistics, query performance on the converted table may be suboptimal because Delta Lake cannot perform data skipping.

Your code block example:

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/path/to/table` NO STATISTICS
```

After using `NO STATISTICS`, Databricks recommends reorganizing the data layout and generating statistics via [Liquid Clustering](/concepts/liquid-clustering.md). See [Use liquid clustering for tables](https://docs.databricks.com/aws/en/tables/clustering). ^[convert-to-delta-databricks-on-aws.md]

## Recommendations

- Use the default conversion (with statistics collection) for most workloads to immediately benefit from query performance improvements.
- Reserve `NO STATISTICS` for cases where conversion speed is critical and statistics can be generated later through clustering or `ANALYZE` operations.
- For partitioned tables, ensure the `PARTITIONED BY` clause is provided correctly (required for path-based conversions; optional for metastore-registered tables). The conversion will abort if the directory structure does not match the partition specification. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The command that triggers statistics collection.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage layer that uses these statistics.
- [Liquid Clustering](/concepts/liquid-clustering.md) — Recommended method for reorganizing data and generating statistics after a `NO STATISTICS` conversion.
- Data Skipping— Query optimization enabled by collected column statistics.
- VACUUM — Cleanup operation that removes files not tracked by Delta Lake.
- [Iceberg Table Conversion](/concepts/iceberg-to-delta-conversion.md) — Conversion of Apache Iceberg tables to Delta Lake.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
