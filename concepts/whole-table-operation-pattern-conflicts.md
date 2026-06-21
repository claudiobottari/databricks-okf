---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b752c0ee9eb24a180adff0d584ab5f63d8af7834a416edf8762aa5695318b2c
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - whole-table-operation-pattern-conflicts
    - WOPC
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Whole-Table Operation Pattern Conflicts
description: A class of Delta Lake conflicts that arise when a transaction attempts to modify or read the entire table (without filters), conflicting with concurrent operations; resolution requires adding filters to narrow the data scope.
tags:
  - delta-lake
  - concurrency
  - optimization
timestamp: "2026-06-18T11:51:59.183Z"
---

# Whole-Table Operation Pattern Conflicts

**Whole-Table Operation Pattern Conflicts** are a category of transaction conflicts that occur when a Delta Lake operation attempts to modify or replace the entire table (without row-level filters) while another concurrent operation modifies overlapping data. These conflicts are surfaced as specific subconditions of the [`DELTA_CONCURRENT_DELETE_DELETE` error class](https://docs.databricks.com/aws/en/error-messages/delta-concurrent-delete-delete-error-class) (SQLSTATE 2D521). ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Error Subconditions

### WHOLE_TABLE_READ

Raised when the current transaction attempted to modify the entire table (no filter or a filter that matches all rows) and a concurrent operation also modified data in the table. The full error message states:

> This transaction attempted to modify the entire table, conflicting with the concurrent modification. Add filters to your query to narrow the data scope and retry the operation.

Resolution: Restructure the operation to use narrower predicates so only the intended rows are targeted, reducing the conflict surface. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

Raised when a concurrent operation replaced **all** data in the table, invalidating the current transaction’s assumptions. The error message says:

> The concurrent operation replaced all data in the table. Please retry the operation.

Resolution: Retry the operation after the concurrent replacement completes. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### EMPTY_READ_PREDICATES

Raised when the current transaction did not include any filters and therefore attempted to modify the entire table, conflicting with a concurrent change. The error states:

> This transaction did not include any filters and modified the entire table, conflicting with the concurrent modification. Add filters to your query to narrow the data scope and retry the operation.

This subcondition is closely related to whole-table patterns: an unfiltered DELETE, UPDATE, or MERGE is treated as a whole-table operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Subconditions

While not strictly whole-table patterns, the following subconditions can also appear in scenarios where whole-table operations are attempted on partitioned tables or without proper merge sources:

| Subcondition | Meaning |
|---|---|
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Row-level conflict detection could not be performed on a partitioned table; retry. |
| `PREDICATES_NEED_REWRITE` | Filters could not be applied for row-level conflict detection; retry. |
| `ROW_LEVEL_CHANGES` | Concurrent operation modified the same rows; retry. |

These indicate that the transaction tried to work at the whole-table level (or without sufficient predicate granularity) on a table where row-level conflict detection is required. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## General Resolution

For all whole-table operation pattern conflicts, the recommended response is:

1. **Add filters** to narrow the scope of the operation to only the rows that need changing.
2. **Retry** the operation if the conflict is transient (e.g., due to a concurrent replacement or protocol upgrade).
3. **Restructure** large-scale updates as smaller, filtered batches when possible.

These steps align with Delta Lake’s concurrency model, which uses optimistic concurrency control and row-level conflict detection to allow high throughput while preserving serializability. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing ACID transactions and concurrent access
- Transaction Conflicts — General overview of conflict types in Delta Lake
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) — The mechanism that resolves conflicts on individual rows
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model
- DELTA_CONCURRENT_DELETE_DELETE Error Class — Parent error class containing these subconditions

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
