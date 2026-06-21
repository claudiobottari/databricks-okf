---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05fa4880d185a044376c59cad448a5f13dd14603deae77dd55c53d8198f4d760
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-level-conflict-resolution
    - RCR
    - Row‑Level Conflict Resolution
    - Row‑level conflict resolution
    - row‑level conflict resolution
    - Transaction conflict resolution
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Row-Level Conflict Resolution
description: A mechanism in Delta Lake that detects and resolves conflicts at the individual row level during concurrent transactions
tags:
  - delta-lake
  - concurrency
  - transactions
timestamp: "2026-06-19T10:03:33.516Z"
---

# Row-Level Conflict Resolution

**Row-Level Conflict Resolution** is a mechanism in [Delta Lake](/concepts/delta-lake.md) that detects and resolves conflicts when concurrent transactions attempt to modify the same rows in a table. When a transaction conflict is detected, Delta Lake can attempt to resolve it at the row level rather than failing the entire operation, but this process may encounter specific error conditions.

## Overview

Row-level conflict resolution is triggered when a concurrent transaction adds data to a table that conflicts with another transaction's operation. Delta Lake attempts to resolve these conflicts automatically by identifying which specific rows were affected and whether the operations can be reconciled at the row level rather than requiring the entire transaction to fail and retry. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Common Error Conditions

### ROW_LEVEL_CHANGES

When a concurrent operation modifies the same rows that another transaction attempted to modify, Delta Lake raises the `ROW_LEVEL_CHANGES` error condition. This indicates that row-level conflict resolution cannot resolve the conflict because the conflicting transactions targeted identical rows. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### ALLOTTED_TIME_EXCEEDED

Row-level conflict resolution is subject to a time limit. If the resolution process exceeds the allotted time, the `ALLOTTED_TIME_EXCEEDED` error condition is raised. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### CHANGE_TYPE_COLUMN

If a table contains a column named `_change_type`, this conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection from functioning. The fix requires renaming the conflicting column before row-level conflict resolution can proceed. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

Row-level conflict detection cannot be performed on certain partitioned tables when there is no suitable merge source available. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE

The filter predicates used by a transaction cannot be applied for row-level conflict detection. This occurs when the predicate structure is incompatible with the conflict resolution mechanism. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE

If a concurrent operation upgrades the table protocol (the Delta Lake protocol version), row-level conflict resolution cannot proceed. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

When a transaction attempts to read the entire table while a concurrent modification is in progress, row-level conflict resolution is not applicable. The recommended action is to add filters to narrow the data scope or retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

If a concurrent operation replaces all data in the table, row-level conflict resolution cannot reconcile this with other in-flight transactions. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITH_PARTITION_HINT

A concurrent operation modified data in a partition that another transaction should have read. This partition-level conflict prevents row-level resolution. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WITHOUT_HINT

A general conflict occurs without specific partition or row-level resolution available. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Best Practices

- **Retry operations** when row-level conflict resolution fails, as transient conflicts often resolve on retry.
- **Avoid columns named `_change_type`** in tables where concurrent write operations are expected.
- **Add query filters** to narrow data scope and reduce the likelihood of `WHOLE_TABLE_READ` conflicts.
- **Monitor for partition-level conflicts** and consider partition design adjustments if `WITH_PARTITION_HINT` errors are frequent.

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – The broader framework for handling concurrent transactions.
- Change Data Feed (CDC) – Captures row-level changes between table versions.
- Delta Lake Protocol – The versioned protocol governing table behavior and conflict resolution capabilities.
- Transaction Conflict Detection – The mechanism that identifies when concurrent operations conflict.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – The underlying approach Delta Lake uses for transaction management.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
