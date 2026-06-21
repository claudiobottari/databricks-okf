---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc38f80bddf1a960666ad937c23bd9a8399552bb77c77048d7a5aaa34271f413
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-level-conflict-detection-in-delta-lake
    - RCDIDL
    - Conflict Detection in Delta Lake
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Row-Level Conflict Detection in Delta Lake
description: A mechanism in Delta Lake that detects conflicts at the row level when concurrent transactions modify the same data, with specific sub-conditions and limitations.
tags:
  - delta-lake
  - concurrency
  - transactions
timestamp: "2026-06-19T18:23:06.831Z"
---

# Row-Level Conflict Detection in Delta Lake

**Row-Level Conflict Detection** is a mechanism in [Delta Lake](/concepts/delta-lake.md) that enables concurrent transactions to detect and report conflicts at the granularity of individual rows, rather than at the table or partition level. When a transaction attempts to modify data that a concurrent transaction has already modified, Delta Lake raises conflict conditions with specific error classes and sub‑errors describing exactly what went wrong. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## How Row-Level Conflict Detection Works

Delta Lake tracks which rows each transaction reads and writes using its Delta Log and [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) mechanisms. When two transactions overlap in their write sets — for example, both attempt to append to the same rows or modify overlapping data — the engine detects the conflict at row level. The detector inspects the filter predicates or scan scope of the current transaction and compares them against the write set of the concurrent transaction. If any row appears in both write sets, the conflict is raised. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

Row-level conflict detection provides more granular conflict information than traditional table-level or partition-level detection, allowing applications to handle conflicts more precisely and retry operations efficiently.

## Error Class: `DELTA_CONCURRENT_APPEND`

The `DELTA_CONCURRENT_APPEND` error class (SQLSTATE `2D521`) is raised when a row-level conflict is detected during an append operation. It indicates that a concurrent transaction added data to the same table that the current transaction attempted to modify. The error message includes the table name and the version at which the concurrent commit occurred, followed by a sub‑error that provides the specific reason for the conflict and suggests the appropriate resolution. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Sub‑errors

| Sub‑error | Description |
|-----------|-------------|
| `ALLOTTED_TIME_EXCEEDED` | Row-level conflict resolution exceeded the allotted time. Retry the operation. |
| `CHANGE_TYPE_COLUMN` | The table contains a column named `_change_type` that conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Rename the column or disable CDC. |
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Row-level conflict detection could not be performed on a partitioned table. Retry the operation. |
| `PREDICATES_NEED_REWRITE` | The filter predicates used by this transaction could not be applied for row-level conflict detection. Retry the operation. |
| `PROTOCOL_CHANGE` | The concurrent operation upgraded the table protocol. Retry the operation. |
| `ROW_LEVEL_CHANGES` | The concurrent operation modified the same rows that this transaction attempted to modify. Retry the operation. |
| `WHOLE_TABLE_READ` | This transaction attempted to read the entire table, conflicting with the concurrent modification. Add filters to narrow the data scope and retry. |
| `WHOLE_TABLE_REPLACE` | The concurrent operation replaced all data in the table. Retry the operation. |
| `WITHOUT_HINT` | The concurrent operation modified data read by this operation. Retry the operation. |
| `WITH_PARTITION_HINT` | The concurrent operation modified data in a specific partition that was read by this operation. Retry the operation. |

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Requirements and Configuration

Row-level conflict detection requires specific table configurations:

- The table must be configured to track row-level changes, typically by enabling features like [Delta Lake change data feed](/concepts/delta-lake-change-data-feed-cdf.md) or row tracking.
- Columns named `_change_type` cannot exist in the table if Change Data Feed is enabled, because that column name is reserved for CDC metadata. If such a column exists, the `CHANGE_TYPE_COLUMN` sub‑error is raised. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Best Practices

### Use Filtered Predicates

Always provide a `WHERE` clause or filter in your `INSERT` (or other mutation) statements. Empty read predicates cause the `WHOLE_TABLE_READ` sub‑error and force a retry. Adding filters helps the engine narrow the scope of conflict detection. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Avoid Whole‑Table Modifications

If a transaction modifies the entire table, consider splitting it into smaller batches or adding a filter. The `WHOLE_TABLE_REPLACE` sub‑error indicates that a concurrent operation replaced all data while the transaction attempted a modification. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Retry on Transient Errors

Most sub‑errors (such as `ALLOTTED_TIME_EXCEEDED`, `PROTOCOL_CHANGE`, `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`, `PREDICATES_NEED_REWRITE`, and `METADATA_CHANGE`) are transient. Retrying the operation often succeeds. Implementing retry logic with exponential backoff is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Handle Genuine Conflicts

The `ROW_LEVEL_CHANGES` sub‑error indicates a real data-level conflict where a concurrent transaction modified rows that the current transaction attempted to modify. Application-level retry logic or transaction reordering may be necessary to resolve these conflicts definitively. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The broader mechanism for handling concurrent writes and reads
- Delta Log — The transaction log that tracks changes at the file and row level
- Change Data Feed (CDC) — A feature that can conflict with row-level detection when column names collide
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying model that allows multiple readers and writers to proceed and detect conflicts on commit
- [MERGE Operations in Delta Lake](/concepts/merge-into-delta-lake.md) — Operations that may also trigger row-level conflict detection
- SQLSTATE 2D521 — The standard SQL error class for invalid transaction termination

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
