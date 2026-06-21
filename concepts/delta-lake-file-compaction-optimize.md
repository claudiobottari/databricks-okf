---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f48d7a8c2f909a79993d7093dff10d68895b886513ca577dfa7634367932cac3
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-file-compaction-optimize
    - DLFC(
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
      start: 34
      end: 37
    - file: best-practices-delta-lake-databricks-on-aws.md
      start: 39
      end: 42
    - file: best-practices-delta-lake-databricks-on-aws.md
      start: 98
      end: 100
    - file: best-practices-delta-lake-databricks-on-aws.md
      start: 14
      end: 17
    - file: 34-37
title: Delta Lake File Compaction (OPTIMIZE)
description: Best practice of running OPTIMIZE to compact small files into larger ones for improved read throughput, with VACUUM to remove old files.
tags:
  - delta-lake
  - performance
  - optimization
timestamp: "2026-06-18T14:32:07.961Z"
---

# Delta Lake File Compaction (OPTIMIZE)

**Delta Lake File Compaction** refers to the process of consolidating small Parquet data files in a [Delta Lake](/concepts/delta-lake.md) table into larger files to improve read performance and reduce metadata overhead. The primary mechanism for compaction is the `OPTIMIZE` command, which merges small files without altering the data's logical content.

## Overview

As data is written incrementally to a [Delta Lake Table](/concepts/delta-lake-table.md) — for example through stream ingestion, `INSERT`, or `MERGE` operations — the number of small Parquet files can grow significantly. Reading from a table with many small files is slower because Spark must open, list, and plan each file. The `OPTIMIZE` command rewrites the small files into a smaller number of larger files, improving read throughput and reducing planning time. ^[best-practices-delta-lake-databricks-on-aws.md:34-37]

## Relationship with VACUUM

The `OPTIMIZE` operation does not remove the old files after compacting them; the old files remain in the table directory to support [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) and rollback. To delete the old files, you must run the `VACUUM` command. For Unity Catalog managed tables, if [predictive optimization](/concepts/delta-lake-predictive-optimization.md) is enabled, both `OPTIMIZE` and `VACUUM` are run automatically. ^[best-practices-delta-lake-databricks-on-aws.md:39-42]

## Performance Benefits

File compaction directly benefits workloads that scan or search large portions of a table. For example, during a Delta Lake MERGE operation, the search for matching rows reads data from disk. If the data is stored in many small files, reading them to locate matches becomes slow. Compacting small files into larger ones improves read throughput and reduces the overall duration of the `MERGE`. ^[best-practices-delta-lake-databricks-on-aws.md:98-100]

## Automatic Compaction with Predictive Optimization

Databricks’ [predictive optimization](/concepts/delta-lake-predictive-optimization.md) feature automatically runs `OPTIMIZE` and `VACUUM` on Unity Catalog managed tables. When predictive optimization is enabled, no manual scheduling of compaction is required. Databricks recommends enabling predictive optimization for Unity Catalog managed tables. ^[best-practices-delta-lake-databricks-on-aws.md:14-17, 34-37]

## Best Practices

- Run `OPTIMIZE` frequently on tables that receive high volumes of small writes. ^[best-practices-delta-lake-databricks-on-aws.md:34-37]
- Enable [predictive optimization](/concepts/delta-lake-predictive-optimization.md) for Unity Catalog managed tables to automate compaction. ^[best-practices-delta-lake-databricks-on-aws.md:14-17]
- After `OPTIMIZE`, run `VACUUM` to remove unreferenced files and reclaim storage (unless predictive optimization handles this). ^[best-practices-delta-lake-databricks-on-aws.md:39-42]
- Use [Liquid Clustering](/concepts/liquid-clustering.md) as a modern alternative to traditional partitioning and Z-order; it works together with compaction to maintain an optimal file layout. ^[best-practices-delta-lake-databricks-on-aws.md:14-17]

## Related Concepts

- Predictive Optimization
- VACUUM
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)
- Delta Lake Merge
- [Liquid Clustering](/concepts/liquid-clustering.md)
- [Optimized Writes](/concepts/delta-lake-optimized-writes.md)
- File Size Tuning

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md:34-37](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
2. [best-practices-delta-lake-databricks-on-aws.md:39-42](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
3. [best-practices-delta-lake-databricks-on-aws.md:98-100](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
4. [best-practices-delta-lake-databricks-on-aws.md:14-17](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
5. 34-37
