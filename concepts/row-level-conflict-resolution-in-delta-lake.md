---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98cef76daf281bc9add9fd5d17144b17f32bbd71ef9a32095996ea445855ed77
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - row-level-conflict-resolution-in-delta-lake
    - RCRIDL
    - Row-Level Conflicts in Delta Lake
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Row-Level Conflict Resolution in Delta Lake
description: A mechanism to resolve concurrent write conflicts at the row level rather than aborting the entire transaction, with specific failure modes like exceeded time or incompatible table features.
tags:
  - delta-lake
  - concurrency
  - transaction-management
timestamp: "2026-06-19T18:24:00.480Z"
---

# Row-Level Conflict Resolution in Delta Lake

**Row-Level Conflict Resolution** is a mechanism in Delta Lake that detects and resolves conflicts between concurrent transactions at the granularity of individual rows, rather than at the table or partition level. This approach enables higher throughput for concurrent operations by allowing transactions that affect different rows to proceed independently, while still maintaining ACID guarantees through Delta Lake's transaction protocol. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Overview

When concurrent transactions modify the same Delta table simultaneously, Delta Lake uses row-level conflict resolution to determine which operations can commit successfully. If conflicting transactions affect different rows, both can proceed. If they affect the same rows, one transaction must be retried. This contrasts with coarser-grained approaches that would block or abort transactions operating on different data within the same partition or table. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Conflict Detection

Delta Lake detects row-level conflicts using several mechanisms:

- **Transaction log versioning** — Each write operation records the version of the table it reads and modifies.
- **Read predicates** — The filter conditions used by each transaction to scope its data selection.
- **Change Data Feed (CDC)** — CDC metadata tracks which specific rows were modified by concurrent operations.
- **Table protocol** — The table's protocol version determines available conflict detection capabilities.

When a transaction reads or writes rows that overlap with another concurrent transaction's data, Delta Lake detects the conflict and attempts row-level resolution. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Supported Operations

Row-level conflict resolution applies to the following Delta Lake operations:

- **INSERT** — When concurrent inserts target different row sets, they proceed independently.
- **DELETE** — Concurrent deletes on non-overlapping rows are resolved successfully.
- **UPDATE** — Row-level resolution allows concurrent updates to different rows.
- **MERGE** — Complex merge operations are also supported at the row level.

## Error Conditions

When row-level conflict resolution fails, Delta Lake returns specific error conditions with SQLSTATE 2D521. These conditions help identify the cause of the conflict and guide resolution. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### ALLOTTED_TIME_EXCEEDED

Row-level conflict resolution exceeded the allotted time. The operation should be retried. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### ROW_LEVEL_CHANGES

The concurrent operation modified rows that this transaction attempted to modify (for delete-delete conflicts) or deleted rows that this transaction attempted to read (for delete-read conflicts). Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

This transaction attempted to read or modify the entire table without filters, conflicting with the concurrent modification. Add filters to narrow the data scope and retry. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### EMPTY_READ_PREDICATES

This transaction did not include any filters and read or modified the entire table, conflicting with the concurrent operation. Add filters to narrow the data scope and retry. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

The concurrent operation replaced all data in the table. Retry after the replacement completes. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### CHANGE_TYPE_COLUMN

The table contains a column named `_change_type` that conflicts with [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDC) metadata columns, preventing row-level conflict detection. Rename this column or disable CDC and retry. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

Row-level conflict detection could not be performed on a partitioned table without a merge source. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE

The filter predicates used by this transaction could not be applied for row-level conflict detection. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WITHOUT_HINT

The concurrent operation deleted data that was read by this operation. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WITH_PARTITION_HINT

The concurrent operation deleted data in the partition `<partitionValues>` that was read by this operation. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE

The concurrent operation upgraded the table protocol. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### TABLE_METADATA_CHANGE

The concurrent operation changed the table metadata (for example, schema or partitioning). Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Best Practices

To minimize row-level conflicts and improve throughput:

1. **Use selective filters** — Apply [WHERE clauses](/concepts/when-matched-clause.md) and partition pruning to narrow the data scope of each transaction.
2. **Design for non-overlapping rows** — Structure concurrent transactions to target distinct row sets when possible.
3. **Set appropriate timeouts** — Configure the allotted time for row-level conflict resolution to match workload latency requirements.
4. **Avoid CDC column name conflicts** — Ensure tables do not have a user-defined column named `_change_type` when using [Change Data Feed](/concepts/delta-change-data-feed-cdf.md).
5. **Provide merge sources for partitioned tables** — Include proper merge sources when performing operations on partitioned tables.

## Related Concepts

- Delta Lake transaction protocol
- Concurrent transaction retry
- [Optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md)
- Serializable isolation level
- Snapshot isolation
- Write conflict detection
- Partition pruning
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- [MERGE INTO (Delta Lake)](/concepts/merge-into-delta-lake.md)

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
2. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
