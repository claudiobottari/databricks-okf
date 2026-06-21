---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d7434debb5d4a514d30274bc960879808b2dcc09d5164c3d46769c6ac30c9169
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-lake-concurrent-operation-retry-strategy
    - DLCORS
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Delta Lake Concurrent Operation Retry Strategy
description: "The recommended resolution pattern for DELTA_CONCURRENT_APPEND errors: retrying the failed operation after a concurrent modification completes."
tags:
  - delta-lake
  - error-handling
  - best-practices
timestamp: "2026-06-18T11:51:58.527Z"
---

# Delta Lake Concurrent Operation Retry Strategy

**Delta Lake Concurrent Operation Retry Strategy** refers to the recommended approach for handling transaction conflicts that arise when multiple concurrent operations attempt to modify the same Delta table. Delta Lake uses optimistic concurrency control and, when a conflict is detected, throws a `DELTA_CONCURRENT_APPEND` error (SQLSTATE 2D521). The appropriate retry response depends on the specific sub‑condition reported in the error message.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Overview

When a concurrent operation adds data to a Delta table at a version that conflicts with the current transaction, Delta Lake aborts the transaction and raises `DELTA_CONCURRENT_APPEND`. The error message includes a sub‑condition that identifies the nature of the conflict. In most cases the recommended action is to simply retry the operation; Delta Lake will re‑read the latest table state and attempt the operation again. For certain sub‑conditions, additional steps such as narrowing the read scope or renaming a conflicting column are needed before retrying.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Sub‑Conditions and Retry Guidance

Each sub‑condition of `DELTA_CONCURRENT_APPEND` has a specific retry or mitigation strategy.

### ALLOTTED\_TIME\_EXCEEDED

Row‑level conflict resolution exceeded the allotted time. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### CHANGE\_TYPE\_COLUMN

The table contains a column named `_change_type`, which conflicts with [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDC) metadata columns and prevents row‑level conflict detection. **Rename the column** before retrying.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### METADATA\_CHANGE

The concurrent operation changed the table metadata (for example, schema or partitioning). **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PARTITIONED\_TABLE\_WITHOUT\_MERGE\_SOURCE

Row‑level conflict detection could not be performed on this partitioned table. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PREDICATES\_NEED\_REWRITE

The filter predicates used by this transaction could not be applied for row‑level conflict detection. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PROTOCOL\_CHANGE

The concurrent operation upgraded the table protocol. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### ROW\_LEVEL\_CHANGES

The concurrent operation modified the same rows that this transaction attempted to modify. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE\_TABLE\_READ

This transaction attempted to read the entire table, conflicting with the concurrent modification. **Add filters** to narrow the data scope, or **retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE\_TABLE\_REPLACE

The concurrent operation replaced all data in the table. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITHOUT\_HINT

No additional information is available. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITH\_PARTITION\_HINT

The concurrent operation modified data in a partition that this operation should have read. **Retry the operation.**^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## General Retry Strategy

For most `DELTA_CONCURRENT_APPEND` sub‑conditions, the simplest and most effective strategy is to implement an automatic retry loop in your application logic. After a short, randomized backoff, re‑attempt the write, merge, or delete operation. Delta Lake will reload the latest table snapshot and re‑evaluate the operation against the new state.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

A retry should be attempted only when the sub‑condition is transient (e.g., `ALLOTTED_TIME_EXCEEDED`, `ROW_LEVEL_CHANGES`, `WHOLE_TABLE_REPLACE`). Sub‑conditions like `CHANGE_TYPE_COLUMN` require a schema change before retrying. For `WHOLE_TABLE_READ`, consider adding a partition filter or predicate to reduce the read scope.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Recommended Retry Loop Pseudocode

1. Attempt the Delta operation.
2. On `DELTA_CONCURRENT_APPEND`:
   - Inspect the sub‑condition.
   - If `CHANGE_TYPE_COLUMN` → rename the conflicting column, then retry.
   - If `WHOLE_TABLE_READ` → consider adding filters, then retry.
   - Otherwise → wait (e.g., 500 ms exponential backoff) and retry.
3. If the retry limit is reached, surface the error to the user.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage layer that provides ACID transactions and optimistic concurrency control.
- [Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — How Delta Lake manages simultaneous writes.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — Metadata that can conflict with the `_change_type` column.
- Optimistic Concurrency — The conflict detection mechanism used by Delta Lake.
- Retry Logic — General patterns for handling transient errors in distributed systems.
- Spark Structured Streaming — A common source of concurrent Delta writes.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
