---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3f52340de7a991ac4870175b06969fb982a297033a398800bf876c25af55090
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_concurrent_append-error-class
    - DEC
    - DELTA_CONCURRENT_APPEND Error Class
    - DELTA_CONCURRENT_APPEND error class
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: DELTA_CONCURRENT_APPEND Error Class
description: A Delta Lake error class indicating transaction conflicts when concurrent operations modify the same table or partition
tags:
  - delta-lake
  - error-handling
  - transaction-conflicts
timestamp: "2026-06-19T10:03:27.360Z"
---

---
title: DELTA_CONCURRENT_APPEND Error Class
summary: A Delta Lake transaction conflict error that occurs when a concurrent operation adds data to a table. The error includes multiple sub-error conditions for specific conflict scenarios such as row‑level changes, partition modifications, or protocol upgrades.
sources:
  - delta_concurrent_append-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:51:35.026Z"
updatedAt: "2026-06-18T17:30:00.000Z"
tags:
  - delta-lake
  - error-handling
  - transaction-conflicts
aliases:
  - delta_concurrent_append-error-class
  - DEC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DELTA_CONCURRENT_APPEND Error Class

The **DELTA_CONCURRENT_APPEND Error Class** is a transaction conflict error in [Delta Lake](/concepts/delta-lake.md) that signals that a concurrent operation added data to a table between the time a transaction read the table state and the time it attempted to write. The error belongs to SQLSTATE class `2D521` (invalid transaction termination). ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Message

The base error message has the following format:

```
Transaction conflict detected. A concurrent <operation> added data to table <tableName> committed at version <version>.
```

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

The error class includes several sub-types that provide more specific information about the nature of the conflict. Each sub-type includes a suggestion to retry the operation unless otherwise noted.

## Sub-Error Types

| Sub-Type | Description |
|----------|-------------|
| `ALLOTTED_TIME_EXCEEDED` | Row-level conflict resolution exceeded the allotted time. Retry the operation. |
| `CHANGE_TYPE_COLUMN` | The table contains a column named `_change_type` that conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Rename this column and retry. |
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Row-level conflict detection could not be performed on this partitioned table. Retry the operation. |
| `PREDICATES_NEED_REWRITE` | The filter predicates used by this transaction could not be applied for row-level conflict detection. Retry the operation. |
| `PROTOCOL_CHANGE` | A concurrent operation upgraded the table protocol. Retry the operation. |
| `ROW_LEVEL_CHANGES` | The concurrent operation modified the same rows that this transaction attempted to modify. Retry the operation. |
| `WHOLE_TABLE_READ` | This transaction attempted to read the entire table, conflicting with the concurrent modification. Add filters to narrow the data scope or retry the operation. |
| `WHOLE_TABLE_REPLACE` | The concurrent operation replaced all data in the table. Retry the operation. |
| `WITHOUT_HINT` | General concurrent append conflict without a specific partition hint. Retry the operation. |
| `WITH_PARTITION_HINT` | The concurrent operation modified data in a partition that should have been read by this operation. Retry the operation. |

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Notes on Sub-Error Conditions

- **`ALLOTTED_TIME_EXCEEDED`**: Indicates that [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) took longer than permitted. The system timed out attempting to resolve conflicts at the row level. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`CHANGE_TYPE_COLUMN`**: Occurs when a user-defined column named `_change_type` exists in the table. This column name is reserved by the Change Data Feed (CDC) feature. Row-level conflict detection is disabled in this case until the column is renamed. The concurrent operation that triggered the error may have also changed the table metadata (e.g., schema or partitioning). ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`**: Relevant for partitioned tables when row-level conflict detection cannot be applied because the merge source is not available. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`PREDICATES_NEED_REWRITE`**: The filter predicates (e.g., those used in a `MERGE` or `UPDATE` statement) could not be rewritten for row-level conflict detection. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`PROTOCOL_CHANGE`**: A concurrent writer upgraded the Delta Lake [table protocol](/concepts/delta-lake-table-protocol-changes.md) version, which invalidates the current transaction’s view of the table. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`ROW_LEVEL_CHANGES`**: The most specific conflict; another transaction modified the exact rows this transaction wanted to modify. Retrying will re-read the new row versions. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`WHOLE_TABLE_READ`**: The transaction attempted to read the entire table, which conflicts with any concurrent write that added data. Adding filters (e.g., partition predicates) reduces the read scope and may avoid the conflict. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`WHOLE_TABLE_REPLACE`**: A concurrent operation replaced all data (e.g., an `INSERT OVERWRITE` or `DELETE` that removed all rows). ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **`WITHOUT_HINT`** and **`WITH_PARTITION_HINT`**: Both indicate a concurrent append conflict. `WITH_PARTITION_HINT` provides the specific partition values that were modified. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Resolution

For most sub-error types, the recommended action is to retry the operation. Delta Lake’s [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) mechanism will re-read the latest table state on retry. For `WHOLE_TABLE_READ`, consider adding filters to limit the data scope. For `CHANGE_TYPE_COLUMN`, rename the conflicting column `_change_type`. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer providing ACID transactions on data lakes.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – The conflict resolution mechanism used by Delta Lake.
- Change Data Feed (CDC) – A feature that introduces a metadata column named `_change_type`.
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) – The mechanism inside Delta Lake that detects and resolves conflicts at the row level.
- Table protocol version – The version of the Delta Lake transaction log protocol.
- Partition pruning – Techniques to narrow data scope and avoid whole‑table reads.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
