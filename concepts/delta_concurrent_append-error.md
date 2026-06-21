---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b6e9b00be8e80b5843e9c9b22d49597b9149f08277ab46c24b9c583f6fc57bf
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_concurrent_append-error
    - DELTA_CONCURRENT_APPEND
    - DELTA_CONCURRENT_APPEND Error
    - delta_concurrent_append-error-class
    - DEC
    - DELTA_CONCURRENT_APPEND Error Class
    - DELTA_CONCURRENT_APPEND error class
    - delta_concurrent_append-error-condition
    - DELTA_CONCURRENT_APPEND Error Condition
    - DELTA_CONCURRENT_APPEND error condition
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: DELTA_CONCURRENT_APPEND Error
description: A Delta Lake error indicating a transaction conflict was detected because a concurrent operation added data to the table.
tags:
  - delta-lake
  - error-handling
  - concurrency
timestamp: "2026-06-19T18:23:34.851Z"
---

# DELTA_CONCURRENT_APPEND Error

The **DELTA_CONCURRENT_APPEND Error** is a [Delta Lake](/concepts/delta-lake.md) transaction conflict error (SQLSTATE: 2D521) that occurs when a concurrent operation adds data to a Delta table while another transaction is attempting to write to the same table. The error message identifies the conflicting operation, the table name, and the version at which the concurrent write was committed.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## How Delta Lake Handles Concurrent Writes

[Delta Lake](/concepts/delta-lake.md) uses [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) to manage concurrent writes to a table. When two or more transactions attempt to write to the same table simultaneously, Delta Lake detects the conflict and raises a `DELTA_CONCURRENT_APPEND` error. Some of these conflicts can be automatically resolved using [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md), while others require the user to retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Sub-Error Conditions

The `DELTA_CONCURRENT_APPEND` error class includes several sub-conditions that provide specific information about why the conflict occurred and how to resolve it.

### ALLOTTED_TIME_EXCEEDED

Row-level conflict resolution exceeded the allotted time. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### CHANGE_TYPE_COLUMN

The table contains a column named `_change_type`, which conflicts with [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) metadata columns. This conflict prevents row-level conflict detection. To resolve this error, rename the conflicting column.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### METADATA_CHANGE

The concurrent operation changed the table metadata, such as the schema or partitioning. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

Row-level conflict detection could not be performed on this partitioned table. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE

The filter predicates used by this transaction could not be applied for row-level conflict detection. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE

The concurrent operation upgraded the table protocol. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### ROW_LEVEL_CHANGES

The concurrent operation modified the same rows that this transaction attempted to modify. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

This transaction attempted to read the entire table, which conflicts with the concurrent modification. To resolve this error, consider adding filters to your query to narrow the data scope, or retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

The concurrent operation replaced all data in the table. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITHOUT_HINT

A general conflict occurred without a specific hint. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITH_PARTITION_HINT

The concurrent operation modified data in a partition that should have been read by this operation. The error message specifies the partition values involved. To resolve this error, retry the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## General Resolution Strategy

For most `DELTA_CONCURRENT_APPEND` sub-conditions, retrying the operation is the recommended course of action. In some cases, such as `CHANGE_TYPE_COLUMN`, a schema change is required. For `WHOLE_TABLE_READ`, adding filters to narrow the data scope can help avoid the conflict.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and concurrency control
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The mechanism Delta Lake uses to manage concurrent writes
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) — Delta Lake's ability to automatically resolve certain concurrent write conflicts
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — Delta Lake feature that tracks row-level changes
- SQLSTATE error codes — Standard SQL error code classification
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The foundation for conflict detection

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
