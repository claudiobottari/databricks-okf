---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7592bf24a37eecd5187e9ca34f1491c2af67b354fb4a32e8386d45753e72fb3c
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-file-compaction
    - DLFC
    - Data file compaction
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake File Compaction
description: The practice of running OPTIMIZE to compact small files into larger ones, improving read throughput and query performance
tags:
  - delta-lake
  - performance
  - optimization
timestamp: "2026-06-19T22:12:46.007Z"
---

```yaml
---
title: Delta Lake File Compaction
summary: Best practice of running OPTIMIZE and VACUUM commands to compact small files into larger ones for improved read performance.
sources:
  - best-practices-delta-lake-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:08:43.418Z"
updatedAt: "2026-06-19T17:40:08.693Z"
tags:
  - performance
  - file-management
  - delta-lake
aliases:
  - delta-lake-file-compaction
  - DLFC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Lake File Compaction

**Delta Lake File Compaction** refers to the process of consolidating small files in a [[delta-lake-table|Delta Lake Table]] into larger, more efficient files to improve query performance and reduce storage overhead. It is a critical maintenance operation for tables that receive frequent small writes. ^[best-practices-delta-lake-databricks-on-aws.md]

## Overview

Delta Lake stores data as Parquet files, and each write operation creates new files. Over time, frequent writes — especially from streaming or batch operations — can produce many small files. Reading these small files is inefficient because it requires opening many files, performing many small I/O operations, and managing metadata for each file. Compaction addresses this by combining small files into larger ones, improving read throughput and reducing the search space for operations like Delta Lake merge. ^[best-practices-delta-lake-databricks-on-aws.md]

## Recommended Approach: `OPTIMIZE`

Databricks recommends frequently running the `OPTIMIZE` command to compact small files. This is the primary compaction mechanism for Delta Lake tables. ^[best-practices-delta-lake-databricks-on-aws.md]

```sql
OPTIMIZE <table-name>;
```

### Automatic Compaction with Predictive Optimization

For [[Unity Catalog managed tables]], [[Predictive Optimization for Delta Lake|Predictive optimization]] automatically runs `OPTIMIZE` and `VACUUM` commands without manual intervention. This is the preferred approach for most workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

## How `OPTIMIZE` Works

- **Rewrites data**: `OPTIMIZE` rewrites smaller files into larger files, optimizing the file layout for better read performance. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Does not remove old files**: The operation creates new compacted files but does not immediately delete old files. To remove them, run the [[VACUUM Command (Databricks)|VACUUM command]]. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Preserves data layout optimizations**: When using [[Low Shuffle Merge]], `OPTIMIZE` preserves existing data layout optimizations such as [[Liquid clustering]] on unmodified data. ^[best-practices-delta-lake-databricks-on-aws.md]

## Compaction for `MERGE` Performance

For Delta Lake merge operations, compacting files reduces the search space for matches, making merges faster. If data is stored in many small files, reading the data to search for matches can become slow. Compacting small files into larger files improves read throughput. ^[best-practices-delta-lake-databricks-on-aws.md]

Additionally, when using `MERGE` on partitioned tables, you can further optimize by adding known constraints in the match condition:

```sql
events.date = current_date() AND events.country = 'USA'
```

This reduces the search space and decreases conflict likelihood with concurrent operations. ^[best-practices-delta-lake-databricks-on-aws.md]

## Tuning File Sizes

Databricks automatically tunes file sizes based on table size:
- **Smaller tables**: Use smaller files.
- **Larger tables**: Use larger files. ^[best-practices-delta-lake-databricks-on-aws.md]

## Best Practices

1. **Run `OPTIMIZE` frequently** for tables with frequent small writes. ^[best-practices-delta-lake-databricks-on-aws.md]
2. **Use predictive optimization** for automatic compaction on Unity Catalog managed tables. ^[best-practices-delta-lake-databricks-on-aws.md]
3. **Use liquid clustering** for better data layout when combined with compaction. ^[best-practices-delta-lake-databricks-on-aws.md]
4. **Do not manually modify data files** — Delta Lake uses the transaction log to commit changes atomically. Manually modifying Parquet files can cause data loss or table corruption. ^[best-practices-delta-lake-databricks-on-aws.md]
5. **Use `CREATE OR REPLACE TABLE`** when deleting and recreating tables in the same location. ^[best-practices-delta-lake-databricks-on-aws.md]
6. **Enable optimized writes** for partitioned tables to reduce the number of small files produced by operations like `merge`. ^[best-practices-delta-lake-databricks-on-aws.md]
7. **Control shuffle partitions** by setting `spark.sql.shuffle.partitions` appropriately — increasing parallelism can generate more small data files. ^[best-practices-delta-lake-databricks-on-aws.md]

## Related Concepts

- Optimize data file layout — The broader optimization of file sizes for read performance.
- [VACUUM command](/concepts/vacuum-command-databricks.md) — Cleanup operation that removes old files after `OPTIMIZE`.
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) — Automatic optimization for Unity Catalog managed tables.
- [Low Shuffle Merge](/concepts/low-shuffle-merge.md) — Optimized `MERGE` implementation that preserves layout.
- [Liquid Clustering](/concepts/liquid-clustering.md) — Clustering method that works with `OPTIMIZE`.
- File size tuning — Automatic file size adjustments based on table size.
- [Optimized writes](/concepts/optimized-writes-for-partitioned-tables.md) — Feature to reduce small file counts for partitioned tables.
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Table type that supports predictive optimization.

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
