---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca12d50d4173d040bcf09cfaa1d95dd7872e30f42a083cbd41951ed4cfb563f8
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_concurrent_append-error-condition
    - DEC
    - DELTA_CONCURRENT_APPEND Error Condition
    - DELTA_CONCURRENT_APPEND error condition
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: DELTA_CONCURRENT_APPEND Error Condition
description: A Delta Lake transaction conflict detected when a concurrent operation adds data to a table, described by SQLSTATE 2D521 with multiple sub-conditions.
tags:
  - delta-lake
  - error-handling
  - databricks
timestamp: "2026-06-19T15:02:36.976Z"
---

# DELTA_CONCURRENT_APPEND Error Condition

**DELTA_CONCURRENT_APPEND** is an error condition in [Delta Lake](/concepts/delta-lake.md) that occurs when a Transaction Conflict is detected — a concurrent operation has added data to a table during the time another transaction was being executed. The error is classified under SQLSTATE class 2D521 (Invalid Transaction Termination). ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Overview

When a Delta Lake transaction attempts to commit, the system detects that another concurrent operation has already committed new data to the same table. The error message includes the concurrent `<operation>` that was performed, the `<tableName>` affected, and the `<version>` at which the concurrent commit occurred. Each specific scenario has a distinct sub‑error condition with a recommended resolution. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Sub‑Error Conditions

### ALLOTTED_TIME_EXCEEDED

Row-level conflict resolution exceeded the allotted time. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### CHANGE_TYPE_COLUMN

The table contains a column named `_change_type`, which conflicts with [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) metadata columns. This prevents row-level conflict detection. The fix is to rename the conflicting column. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

Row-level conflict detection could not be performed on this partitioned table. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE

The filter predicates used by this transaction could not be applied for row-level conflict detection. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE

The concurrent operation upgraded the table protocol. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### ROW_LEVEL_CHANGES

The concurrent operation modified the same rows that this transaction attempted to modify. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

This transaction attempted to read the entire table, conflicting with the concurrent modification. Consider adding filters to narrow the data scope, or retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

The concurrent operation replaced all data in the table. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITHOUT_HINT

Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITH_PARTITION_HINT

The concurrent operation modified data in a partition that this operation should have read. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Concurrent Metadata Change

The concurrent operation changed the table metadata (for example, schema or partitioning). Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — How Delta Lake handles concurrent reads and writes.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying mechanism used by Delta Lake for transaction isolation.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The record of all commits and the source of conflict detection.
- SQLSTATE 2D521 — The SQL standard error class for invalid transaction termination.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — Delta Lake feature for capturing row-level changes, which can conflict with column naming.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
