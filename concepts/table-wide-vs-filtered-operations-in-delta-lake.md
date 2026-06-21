---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 727a62749eba22c4884ce2eec817a9ae54f14180ca2a44fe09302c41c01f62ba
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - table-wide-vs-filtered-operations-in-delta-lake
    - TVFOIDL
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Table-wide vs Filtered Operations in Delta Lake
description: The distinction between operations that modify an entire table versus filtered subsets, where whole-table modifications are more prone to concurrent transaction conflicts.
tags:
  - delta-lake
  - optimization
  - concurrency
timestamp: "2026-06-18T15:18:11.713Z"
---

# Table-wide vs Filtered Operations in Delta Lake

**Table-wide vs Filtered Operations in Delta Lake** describes the distinction between operations that modify an entire Delta table versus those that use predicate filters to operate on a subset of data. This distinction is critical for understanding concurrency control in Delta Lake, as table-wide operations are more likely to conflict with concurrent modifications than filtered operations.

## Overview

Delta Lake supports concurrent reads and writes using [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md). When a transaction commits, Delta Lake validates that the transaction's read snapshot has not been modified by a concurrent write. The scope of an operation — whether it targets the entire table or only specific rows — determines the likelihood of encountering a `DELTA_CONCURRENT_DELETE_DELETE` error condition. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Table-wide Operations

A table-wide operation modifies all data in a table without applying filter predicates. These operations include `DELETE`, `UPDATE`, or `MERGE` statements that lack a `WHERE` clause.

Table-wide operations have a high conflict probability because they interact with any concurrent modification. Delta Lake's error messages distinguish between two scenarios: ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **WHOLE_TABLE_READ**: This transaction attempted to modify the entire table, conflicting with a concurrent modification. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **WHOLE_TABLE_REPLACE**: A concurrent operation replaced all data in the table. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Empty Read Predicates

A variant of the table-wide case occurs when a transaction does not include any filters and modifies the entire table, conflicting with a concurrent modification. Delta Lake reports this as `EMPTY_READ_PREDICATES`. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Filtered Operations

Filtered operations use `WHERE` clauses or other predicates to target specific rows or partitions. These operations reduce the surface area for conflicts with concurrent writes.

Delta Lake uses row-level conflict detection when filters are present. If the concurrent operation modified the same rows that this transaction attempted to modify, Delta Lake reports `ROW_LEVEL_CHANGES`. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Partition Hints

When a filtered operation specifies partition values, Delta Lake can detect conflicts at the partition level rather than the row level. If a concurrent operation deleted data in a specific partition, Delta Lake reports `WITH_PARTITION_HINT`. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Without Hint

If a filtered operation does not use partition hints and a concurrent operation deleted data that was read by this operation, Delta Lake reports `WITHOUT_HINT`. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Error Subtypes

Delta Lake provides multiple error condition subtypes under `DELTA_CONCURRENT_DELETE_DELETE` to describe specific conflict scenarios:

| Subtype | Description |
|---------|-------------|
| `ALLOTTED_TIME_EXCEEDED` | Row-level conflict resolution exceeded the allotted time |
| `CHANGE_TYPE_COLUMN` | Table has a `_change_type` column conflicting with CDC metadata |
| `EMPTY_READ_PREDICATES` | Transaction had no filters and modified entire table |
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Row-level detection could not be performed on partitioned table |
| `PREDICATES_NEED_REWRITE` | Filter predicates could not be applied for conflict detection |
| `PROTOCOL_CHANGE` | Concurrent operation upgraded the table protocol |
| `ROW_LEVEL_CHANGES` | Concurrent operation modified the same rows |
| `WHOLE_TABLE_READ` | Transaction attempted to modify the entire table |
| `WHOLE_TABLE_REPLACE` | Concurrent operation replaced all table data |
| `WITHOUT_HINT` | Concurrent operation deleted data read by this operation |
| `WITH_PARTITION_HINT` | Concurrent operation deleted data in a specific partition |

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Recommended Practices

- **Add filters to narrow data scope.** Filtering reduces the chance of conflicts with concurrent writes and allows row-level conflict detection. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **Retry on conflict.** Delta Lake's concurrency control supports retry; many conflict subtypes recommend retrying the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **Use partition hints when possible.** Partition-level conflict detection is more efficient than row-level detection and reduces false conflicts. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **Avoid table-wide modifications during concurrent workloads.** If concurrent writes are expected, use filtered operations to minimize conflict probability. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — Optimistic concurrency model for ACID transactions.
- [Row-level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — Mechanism for detecting conflicts on specific rows.
- Partition Pruning — Using partition columns to limit scanned data.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — Transaction validation at commit time.
- [MERGE INTO Operations](/concepts/merge-into-delta-lake.md) — Complex operations that may conflict with concurrent writes.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
