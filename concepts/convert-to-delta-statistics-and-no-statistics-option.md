---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 871160ceefe22770de1071af68bcafd3696077531d4841b30edd381dea033b96
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - convert-to-delta-statistics-and-no-statistics-option
    - NO STATISTICS Option and CONVERT TO DELTA Statistics
    - CTDSANSO
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: CONVERT TO DELTA Statistics and NO STATISTICS Option
description: The command automatically collects statistics on data files during conversion for query performance; the NO STATISTICS keyword bypasses this to finish faster.
tags:
  - statistics
  - optimization
  - delta-lake
timestamp: "2026-06-18T14:44:48.129Z"
---

# CONVERT TO DELTA Statistics and NO STATISTICS Option

**CONVERT TO DELTA Statistics** refers to the automatic data profiling that occurs when converting a Parquet table to a Delta table using the `CONVERT TO DELTA` command. The **NO STATISTICS** option allows users to bypass this collection for faster conversion.

## Overview

When you run `CONVERT TO DELTA` on an existing Parquet table, the command lists all files in the directory, creates a Delta Lake transaction log, and infers the data schema by reading the footers of all Parquet files. As part of this process, statistics are automatically collected to improve query performance on the converted Delta table. This statistics collection reads metadata from the Parquet files to populate the Delta transaction log with column-level statistics, enabling query optimizations like data skipping. ^[convert-to-delta-databricks-on-aws.md]

## Statistics Collection During Conversion

The statistics collection in `CONVERT TO DELTA` is an automatic step that gathers information about the data distribution within each Parquet file. These statistics are stored in the Delta transaction log and enable Delta Lake to perform data skipping during queries — skipping over files that do not contain relevant data. This is a key performance feature for Delta tables. ^[convert-to-delta-databricks-on-aws.md]

### Impact of Statistics on Query Performance

- **With statistics (default):** Query plans can use the collected file-level statistics to prune partitions and reduce I/O, leading to faster query execution on large datasets.
- **Without statistics (NO STATISTICS):** The conversion completes faster, but subsequent queries may not benefit from data skipping optimizations until statistics are regenerated.

## NO STATISTICS Option

The `NO STATISTICS` clause is an optional parameter in the `CONVERT TO DELTA` syntax. It instructs the converter to skip the statistics collection phase during the initial conversion. This results in a faster conversion process, especially for large tables where reading all Parquet footers to gather statistics can be time-consuming. ^[convert-to-delta-databricks-on-aws.md]

### Syntax

```sql
CONVERT TO DELTA table_name [ NO STATISTICS ] [ PARTITIONED BY clause ]
```

### When to Use NO STATISTICS

- **Large tables with many Parquet files** — skipping statistics reduces conversion time.
- **Tables where you plan to reorganize data immediately** — after conversion, you can use [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize data layout and generate fresh statistics.

### Recommendation After Using NO STATISTICS

After converting a table without statistics, Databricks recommends using [Liquid Clustering](/concepts/liquid-clustering.md) to reorganize the data layout and generate statistics. This ensures that the Delta table benefits from data skipping optimizations without the overhead of statistics collection during the initial conversion. ^[convert-to-delta-databricks-on-aws.md]

## Converting Iceberg and Other Table Types

The `CONVERT TO DELTA` command also supports converting Apache Iceberg tables whose underlying file format is Parquet. In this case, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information — rather than reading all Parquet footers. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The metadata layer that tracks all operations on a Delta table
- Data skipping — Query optimization that skips irrelevant files based on stored statistics
- [Liquid Clustering](/concepts/liquid-clustering.md) — A data organization and statistics generation technique for Delta tables
- VACUUM — A command to clean up files not tracked by Delta Lake
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The full conversion command and its parameters

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
