---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37b279df166ebbfb249c90a8d26dc4058433c2282d96895dca6c30e0f2f32a34
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-lake-optimistic-concurrency-control
    - DLOCC
    - Delta Lake Concurrency Control
    - Delta Lake concurrency control
    - Optimistic Concurrency Control
    - Optimistic concurrency control
    - optimistic concurrency control
    - Concurrency Control
    - Delta Lake concurrent write conflicts
    - Optimistic Concurrency Control in Delta Lake
    - Optimistic concurrency control in Delta Lake
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Delta Lake Optimistic Concurrency Control
description: The concurrency model underlying Delta Lake that detects conflicts at commit time rather than locking resources upfront, leading to error conditions like DELTA_CONCURRENT_DELETE_DELETE.
tags:
  - delta-lake
  - concurrency
  - transactions
timestamp: "2026-06-19T15:03:10.238Z"
---

# Delta Lake Optimistic Concurrency Control

**Delta Lake Optimistic Concurrency Control** is a transaction management protocol that allows multiple writers to operate on a Delta table simultaneously. Conflicts are detected at commit time rather than through upfront locking. When a concurrent operation deletes data that another transaction has already read or modified, Delta Lake raises a conflict error with the SQLSTATE class **2D521** (Invalid Transaction Termination). The error class for delete–delete conflicts is `DELTA_CONCURRENT_DELETE_DELETE`. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Error Message

A `DELTA_CONCURRENT_DELETE_DELETE` error is reported as:

> Transaction conflict detected, a concurrent `<operation>` deleted data from table `<tableName>` (committed at version `<version>`) that this transaction attempted to delete. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

The error includes a sub‑classification that provides additional context about why row-level conflict resolution could not automatically resolve the conflict, or why the transaction must be retried. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Sub‑Conditions

| Sub‑condition | Meaning |
|---------------|---------|
| `ALLOTTED_TIME_EXCEEDED` | Row-level conflict resolution exceeded the allotted time. Retry the operation. |
| `CHANGE_TYPE_COLUMN` | The table contains a column named `_change_type`, which conflicts with [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDC) metadata columns. Rename the column or disable CDC. |
| `EMPTY_READ_PREDICATES` | This transaction did not include any filters and modified the entire table, conflicting with the concurrent modification. Add filters to narrow the data scope and retry. |
| `METADATA_CHANGED` (implied by generic message) | The concurrent operation changed the table metadata (e.g., schema or partitioning). Retry the operation. |
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Row-level conflict detection could not be performed on this partitioned table. Retry the operation. |
| `PREDICATES_NEED_REWRITE` | The filter predicates used by this transaction could not be applied for row-level conflict detection. Retry the operation. |
| `PROTOCOL_CHANGE` | A concurrent operation upgraded the table protocol. Retry the operation. |
| `ROW_LEVEL_CHANGES` | A concurrent operation modified the same rows that this transaction attempted to modify. Retry the operation. |
| `WHOLE_TABLE_READ` | This transaction attempted to modify the entire table, conflicting with a concurrent modification. Add filters and retry. |
| `WHOLE_TABLE_REPLACE` | A concurrent operation replaced all data in the table. Retry the operation. |
| `WITHOUT_HINT` | A concurrent operation deleted data that was read by this operation. Retry the operation. |
| `WITH_PARTITION_HINT` | A concurrent operation deleted data in a partition that was read by this operation. Retry the operation. |

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Conflict Resolution

For most sub‑conditions, the recommended action is to retry the operation. Optimistic concurrency control assumes that conflicts are transient; once the conflicting transaction completes, the retry may succeed. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- For `EMPTY_READ_PREDICATES` and `WHOLE_TABLE_READ`, adding filter predicates to narrow the data scope reduces the likelihood of future conflicts and also enables row-level conflict detection. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- For `CHANGE_TYPE_COLUMN`, either rename the conflicting column or disable Change Data Feed to allow row-level conflict detection. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Relationship with Delta Lake Features

- [Delta transaction log](/concepts/delta-transaction-log.md) – The atomic commit log underpinning optimistic concurrency control.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Required for row-level conflict resolution; column `_change_type` must not conflict.
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) – Partitioning affects how conflicts are detected; some partitioned tables may not support row-level detection without a merge source.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
