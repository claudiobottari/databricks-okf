---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e969339a61f31f49cd89dd33706cc7266aea763de516921e08acf5c57698810
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-metadata-change-transaction-conflicts
    - TMCTC
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Table Metadata Change Transaction Conflicts
description: A conflict type where concurrent operations that change table metadata (schema, partitioning, protocol) cause read transactions to fail, typically resolved by retrying the operation.
tags:
  - delta-lake
  - schema-evolution
  - concurrency
timestamp: "2026-06-18T11:52:28.087Z"
---

# Table Metadata Change Transaction Conflicts

**Table Metadata Change Transaction Conflicts** occur when a concurrent operation modifies the metadata of a Delta table — such as its schema, partitioning, or protocol — while another transaction is in progress, causing the reading transaction to fail with a conflict error. These conflicts are a subtype of Delta Lake Transaction Conflicts and are identified by the SQLSTATE `2D521`. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Overview

Delta Lake uses [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) to manage concurrent reads and writes on tables. When a transaction reads table metadata and a concurrent operation changes that metadata before the transaction commits, Delta Lake detects the conflict and raises an error. The specific error condition depends on the type of metadata change that occurred. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Error Conditions

### PROTOCOL_CHANGE

The concurrent operation upgraded the table protocol. This occurs when another transaction changes the Delta Lake protocol version of the table while your transaction is in progress. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

**Resolution:** Retry the operation. The protocol change is typically a one-time upgrade that will not recur. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

Row-level conflict detection could not be performed on this partitioned table. This occurs when a concurrent operation changes the partitioning scheme of the table while a transaction is reading from it. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

**Resolution:** Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### CHANGE_TYPE_COLUMN

The table contains a column named `_change_type` which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. This is a schema-related metadata conflict where the user-defined column name collides with a reserved CDC metadata column. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

**Resolution:** Rename the `_change_type` column or disable CDC on the table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE

The filter predicates used by this transaction could not be applied for row-level conflict detection. This occurs when a concurrent metadata change invalidates the predicate-based conflict detection mechanism. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

**Resolution:** Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## General Resolution Strategy

For most table metadata change transaction conflicts, the recommended resolution is to **retry the operation**. Metadata changes such as protocol upgrades or schema modifications are typically one-time events, and retrying after the concurrent operation completes will succeed. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Error Conditions

The following related error conditions involve concurrent data modifications rather than metadata changes, but share the same SQLSTATE `2D521`:

- DELTA_CONCURRENT_DELETE_READ - ROW_LEVEL_CHANGES — Concurrent row deletions
- DELTA_CONCURRENT_DELETE_READ - WHOLE_TABLE_READ — Full table scan conflicts
- DELTA_CONCURRENT_DELETE_READ Error Class|DELTA_CONCURRENT_DELETE_READ - WHOLE_TABLE_REPLACE — Full table replacement
- DELTA_CONCURRENT_DELETE_READ - ALLOTTED_TIME_EXCEEDED — Timeout during conflict resolution

## Related Concepts

- Delta Lake Transaction Conflicts — The broader category of concurrency conflicts
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model
- Change Data Feed (CDC) — Feature that can conflict with user-defined column names
- [Delta Table Protocol](/concepts/delta-lake-table-protocol-changes.md) — Versioning mechanism that can be upgraded concurrently
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — Mechanism for detecting fine-grained conflicts

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
