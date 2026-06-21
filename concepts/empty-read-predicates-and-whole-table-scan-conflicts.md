---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67102450002d2ce2c4374a93ea9b9df78933565abb52344c556c2d0f98140b84
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - empty-read-predicates-and-whole-table-scan-conflicts
    - Whole Table Scan Conflicts and Empty Read Predicates
    - ERPAWTSC
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Empty Read Predicates and Whole Table Scan Conflicts
description: A conflict scenario where a transaction reads an entire table without filters while a concurrent operation deletes data, requiring filter predicates to narrow the read scope and resolve the conflict.
tags:
  - delta-lake
  - query-optimization
  - concurrency
timestamp: "2026-06-18T11:52:32.249Z"
---

# Empty Read Predicates and Whole Table Scan Conflicts

**Empty Read Predicates** (`EMPTY_READ_PREDICATES`) and **Whole Table Scan Conflicts** (`WHOLE_TABLE_READ`) are two related sub‑errors of the broader `DELTA_CONCURRENT_DELETE_READ` transaction conflict. They occur when a Delta Lake transaction reads the entire table without any filtering, and a concurrent operation deletes data from the same table. These conflicts are detected by Delta Lake’s row‑level conflict resolution mechanism. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## EMPTY_READ_PREDICATES

The `EMPTY_READ_PREDICATES` error is raised in two distinct scenarios:

1. **Missing filters on the read operation** – The transaction did not include any filter predicates and therefore read the entire table. This full scan conflicted with a concurrent deletion that removed data from the table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
2. **Concurrent metadata change** – The concurrent operation altered the table metadata (for example, the schema or partitioning) while this transaction was reading metadata without filters. Even if no actual data rows were deleted, the metadata change itself can cause the conflict. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Resolution for EMPTY_READ_PREDICATES

- Add filter predicates to the query to narrow the scope of data read. This allows Delta Lake’s row‑level conflict detection to compare only the relevant rows, reducing the chance of a conflict with concurrent deletions.
- If the cause was a metadata change, retrying the operation is often sufficient, as the metadata change will have completed. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## WHOLE_TABLE_READ

The `WHOLE_TABLE_READ` error occurs when a transaction attempts to read the entire table (i.e., a full scan without any partition pruning or filter predicates) while a concurrent deletion is removing data from the table. Unlike `EMPTY_READ_PREDICATES`, this sub‑error is specifically tied to the read operation’s lack of filtering, not to metadata changes. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Resolution for WHOLE_TABLE_READ

- Add filters (e.g., `WHERE` clauses) to the reading transaction so that only a subset of the data is read. This limits the conflict to the rows actually touched by the concurrent deletion. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- If filtering is not possible (e.g., the operation genuinely needs all rows), consider serialising the conflicting operations (e.g., by using a separate lock or running them sequentially).

## Common Approach

Both errors share the same recommended resolution pattern:

1. **Add filters** to the reading query to prune the data scope. This enables row‑level conflict detection to work effectively.
2. **Retry** the operation after the concurrent deletion has completed. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

More broadly, these errors highlight the importance of designing Delta Lake workloads with [row‑level conflict resolution](/concepts/row-level-conflict-resolution.md) in mind. Whenever possible, read operations should include predicates that match the table’s partitioning or are supported by data skipping to avoid full‑table scans in high‑concurrency write environments.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and conflict detection.
- Concurrent delete operations — Operations that remove data while other transactions are reading.
- [Row‑level conflict resolution](/concepts/row-level-conflict-resolution.md) — The mechanism that detects and resolves conflicts at the row granularity.
- Data skipping — Technique to avoid scanning irrelevant data by using file‑level statistics.
- Partition pruning — Filtering data based on partition columns to reduce scan scope.
- DELTA_CONCURRENT_DELETE_READ Error|DELTA_CONCURRENT_DELETE_READ — The parent error class that includes these sub‑errors.
- Transaction conflict — A broader topic covering all Delta Lake concurrency‑related errors.

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
