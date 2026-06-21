---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60ad837ddaceab4e21a6765b92fb79eaab488aa3415f106ab1b76c57ce1ae26e
  pageDirectory: concepts
  sources:
    - drop-bloom-filter-index-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bloom-filter-index-lifecycle-and-cleanup
    - Cleanup and Bloom Filter Index Lifecycle
    - BFILAC
  citations:
    - file: drop-bloom-filter-index-databricks-on-aws.md
title: Bloom Filter Index Lifecycle and Cleanup
description: Bloom filter index files on disk are only physically removed when the table is vacuumed after dropping the index.
tags:
  - delta-lake
  - storage
  - indexing
  - maintenance
timestamp: "2026-06-18T12:09:54.299Z"
---

# Bloom Filter Index Lifecycle and Cleanup

**Bloom Filter Index Lifecycle and Cleanup** refers to the process of managing [Bloom filter indexes](/concepts/bloom-filter-index.md) from creation through deletion, including the cleanup of related metadata and index files after an index is dropped.

## Overview

Bloom filter indexes are indexing structures that improve query performance on [Delta Lake](/concepts/delta-lake.md) tables by allowing fast skipping of data files that cannot contain a requested value. As of 2025-06-18, Bloom filter indexes are **deprecated** on Databricks. Databricks recommends dropping all existing Bloom filter indexes and using the specified alternatives. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Lifecycle Stages

### Creation

Bloom filter indexes are created on Delta tables to accelerate predicate-based lookups (e.g., equality checks on specific columns). They store per-column Bloom filter data structures in index files that the query engine uses during file skipping. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Maintenance

While active, Bloom filter indexes are periodically rebuilt as data in the table changes. There is no explicit maintenance command; the rebuild is triggered automatically or can be initiated by recreating the index. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Dropping

The `DROP BLOOM FILTER INDEX` command removes the index. The syntax is: ^[drop-bloom-filter-index-databricks-on-aws.md]

```sql
DROP BLOOMFILTER INDEX
ON [TABLE] table_name
[FOR COLUMNS (columnName1 [, ...] ) ]
```

**Parameters:**

- `table_name` — Identifies an existing Delta table. The name must not include a temporal or options specification. The command fails if the table or any specified column does not exist. ^[drop-bloom-filter-index-databricks-on-aws.md]

When the command executes, all Bloom filter related metadata is removed from the specified columns. If no column list is provided, the index is dropped from all columns on which it was defined. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Cleanup of Index Files

The underlying Bloom filter index files (the physical files stored in the table's `_delta_index/` directory) are **not immediately deleted** when the index is dropped. Instead, they are cleaned up as part of the normal table vacuum process. ^[drop-bloom-filter-index-databricks-on-aws.md]

- Once the table has no Bloom filter indexes on any column, the index files become orphaned and are eligible for removal during the next `VACUUM` operation on the table. ^[drop-bloom-filter-index-databricks-on-aws.md]
- The `VACUUM` command removes files that are no longer referenced by the table's transaction log. Because the Bloom filter index metadata is removed during `DROP`, the index files are no longer referenced and will be removed. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Caveat: Retention Period

Vacuum retains files for a configurable retention period (default 7 days) before deleting unreferenced files. If you need to immediately free the storage space, you can set a shorter retention period (though this is not recommended for production workloads). ^[drop-bloom-filter-index-databricks-on-aws.md]

## Best Practices

### Before Dropping

1. **Check for active indexes** — Use `DESCRIBE DETAIL` or query the table's metadata to confirm which columns currently have Bloom filter indexes. ^[drop-bloom-filter-index-databricks-on-aws.md]
2. **Plan for the index removal** — If the table is being queried frequently, schedule the `DROP` during a maintenance window to avoid query performance degradation during the operation. ^[drop-bloom-filter-index-databricks-on-aws.md]

### After Dropping

1. **Run VACUUM** — After dropping the index, run `VACUUM` on the table to clean up the orphaned index files and reclaim storage space: ^[drop-bloom-filter-index-databricks-on-aws.md]

   ```sql
   VACUUM table_name;
   ```

2. **Consider alternatives** — Because Bloom filter indexes are deprecated, evaluate alternative performance optimization strategies such as [Z-ordering](/concepts/z-ordering-delta-lake.md), [Liquid Clustering](/concepts/liquid-clustering.md), or data skipping for the query patterns that the Bloom filter indexes were serving. ^[drop-bloom-filter-index-databricks-on-aws.md]

## Syntax Reference

### Full Command

```sql
DROP BLOOMFILTER INDEX
ON [TABLE] table_name
[FOR COLUMNS (column1, column2, ...)]
```

- `table_name` — Required. The fully qualified Delta table name (including [Catalog and Schema](/concepts/catalog-and-schema.md) if applicable).
- `FOR COLUMNS` — Optional. If omitted, the index is dropped from all columns. ^[drop-bloom-filter-index-databricks-on-aws.md]

### Example: Drop from Specific Columns

```sql
DROP BLOOMFILTER INDEX
ON sales_db.transactions
FOR COLUMNS (customer_id, product_id);
```

### Example: Drop from All Columns

```sql
DROP BLOOMFILTER INDEX
ON sales_db.transactions;
```

## Related Concepts

- [Bloom filter indexes](/concepts/bloom-filter-index.md) — The deprecated feature that this page describes
- [Delta Lake](/concepts/delta-lake.md) — The storage layer on which Bloom filter indexes operate
- Data skipping — The core optimization technique that Bloom filter indexes accelerate
- [Z-ordering](/concepts/z-ordering-delta-lake.md) — A recommended alternative for clustering data for efficient file skipping
- [Liquid Clustering](/concepts/liquid-clustering.md) — An advanced clustering strategy for Delta tables
- Vacuum — The operation that removes unreferenced files, including orphaned Bloom filter files
- Table maintenance — General best practices for keeping Delta tables performant

## Sources

- drop-bloom-filter-index-databricks-on-aws.md

# Citations

1. [drop-bloom-filter-index-databricks-on-aws.md](/references/drop-bloom-filter-index-databricks-on-aws-7a6d5bf4.md)
