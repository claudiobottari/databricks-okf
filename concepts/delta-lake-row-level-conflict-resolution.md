---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: daa3e73229c221319e5792142ed62f8ffa97c3ed02dfb36623de64d38c6bfe3d
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-row-level-conflict-resolution
    - DLRCR
    - Delta Lake conflict resolution
    - Delta Lake write conflict resolution
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Delta Lake Row-Level Conflict Resolution
description: A mechanism in Delta Lake that detects and resolves conflicts at the row level when concurrent transactions delete data being read by another transaction.
tags:
  - delta-lake
  - concurrency-control
  - transaction-conflicts
timestamp: "2026-06-19T15:03:33.480Z"
---

# Delta Lake Row-Level Conflict Resolution

**Delta Lake Row-Level Conflict Resolution** is a mechanism that detects and resolves transaction conflicts at the granularity of individual rows, rather than requiring a full transaction retry. When two transactions attempt to modify overlapping data, row-level resolution aims to identify whether the conflict affects only distinct rows and can be resolved automatically, improving concurrency for write-heavy workloads. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## How It Works

The resolution engine uses filter predicates and data-reading metadata (such as partition values) to determine whether a concurrent transaction modified rows that the current transaction depends on. If the overlapping changes are limited to non-conflicting rows, the operation can commit without a full retry. When resolution cannot be performed, the transaction aborts with the `DELTA_CONCURRENT_DELETE_READ` error class, which has SQLSTATE `2D521` (invalid transaction termination). ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

The table must have a sufficient Delta Lake Protocol version to support row-level conflict resolution. If a concurrent operation upgrades the table protocol, resolution fails with a `PROTOCOL_CHANGE` sub‑condition. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Error Conditions That Prevent Resolution

Row-level conflict resolution can fail for several reasons, each reported with a distinct sub‑condition of the `DELTA_CONCURRENT_DELETE_READ` error class. The following table lists the sub‑conditions and the recommended action for each.

| Sub‑condition | Meaning | Suggested Action |
|---------------|---------|------------------|
| `ALLOTTED_TIME_EXCEEDED` | Resolution exceeded the allotted time. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `CHANGE_TYPE_COLUMN` | A column named `_change_type` conflicts with Change Data Feed (CDC) metadata, preventing detection. | Rename the column or disable CDC. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `EMPTY_READ_PREDICATES` | The transaction modified the entire table without any filters, conflicting with a concurrent deletion. | Add filters to narrow the data scope and retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Row-level conflict detection could not be performed on this partitioned table. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `PREDICATES_NEED_REWRITE` | The filter predicates used by the transaction could not be applied for row-level conflict detection. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `PROTOCOL_CHANGE` | The concurrent operation upgraded the table protocol. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `ROW_LEVEL_CHANGES` | The concurrent operation deleted rows that this transaction attempted to read. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `WHOLE_TABLE_READ` | This transaction attempted to read the entire table, conflicting with a concurrent deletion. | Add filters to narrow the data scope, or retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `WHOLE_TABLE_REPLACE` | The concurrent operation replaced all data in the table. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `WITHOUT_HINT` | The concurrent operation deleted data that was read by this operation. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |
| `WITH_PARTITION_HINT` | The concurrent operation deleted data in a specific partition that was read by this operation. | Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md] |

Additionally, if the concurrent operation changed the table metadata (such as schema or partitioning), a generic metadata-change sub‑condition fires. In all such cases, the recommended action is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Best Practices

- **Use filter predicates** to narrow the data scope of reads and writes. This reduces the chance of whole-table conflicts and enables the resolution engine to identify row-level overlaps. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **Avoid columns named `_change_type`** when [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) is enabled, or disable CDC if that column name is required. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **Use partition hints** when operating on partitioned tables. This helps the conflict detection logic pinpoint the affected partitions. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **Retry on transient failures**. Most sub‑conditions are resolved by simply retrying the operation after the conflicting transaction commits. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- Concurrent Transaction Conflicts
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- Delta Lake Protocol
- Partitioning in Delta Lake
- [MERGE INTO (Delta Lake)](/concepts/merge-into-delta-lake.md)
- Change Data Feed (CDC)

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
