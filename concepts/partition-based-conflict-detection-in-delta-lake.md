---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aab058fe36f61f5a2350ba936c2ae35835b8a02dfc92ba3fee0dc369674b96b3
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - partition-based-conflict-detection-in-delta-lake
    - PCDIDL
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Partition-based Conflict Detection in Delta Lake
description: Using partition hints and partition pruning to narrow the scope of transaction conflict detection, with specific error subclasses for partitioned tables.
tags:
  - delta-lake
  - partitioning
  - concurrency
timestamp: "2026-06-18T15:18:13.321Z"
---

# Partition-based Conflict Detection in Delta Lake

**Partition-based Conflict Detection in Delta Lake** is a mechanism that limits concurrency conflicts by narrowing the scope of contention to specific partitions rather than the entire table. When concurrent transactions operate on disjoint partitions, Delta Lake can detect and resolve conflicts more efficiently, reducing the likelihood of transaction retries.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## How It Works

Delta Lake uses partition metadata to determine whether two concurrent operations affect the same subset of data. If a transaction includes a partition hint (e.g., in a `DELETE` or `UPDATE` statement), the conflict detection system can check whether the concurrent modification involved the same partition value. When the partitions do not overlap, the conflict can often be resolved without aborting one of the transactions.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

Operations that modify the entire table (e.g., a `DELETE` without any filter or partition hint) always conflict with any concurrent modification because there is no partition boundary to limit the scope. Delta Lake therefore encourages the use of partition filters to reduce contention.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Error Conditions Related to Partitions

The following `DELTA_CONCURRENT_DELETE_DELETE` error subtypes directly involve partition-based conflict detection:

| Error Subtype | Description |
|---------------|-------------|
| `WITH_PARTITION_HINT` | A concurrent operation deleted data in the partition `<partitionValues>` that was read by this operation. The operation used a partition hint, but the partitions overlapped.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md] |
| `WITHOUT_HINT` | A concurrent operation deleted data that was read by this operation, and no partition hint was used. The conflict could not be narrowed to a specific partition.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md] |
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Row-level conflict detection could not be performed on this partitioned table. This typically happens when a MERGE operation is run against a partitioned table and the source does not provide partition columns for filtering.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md] |
| `WHOLE_TABLE_READ` / `WHOLE_TABLE_REPLACE` | The transaction attempted to modify the entire table (no partition boundaries), causing a conflict with the concurrent operation.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md] |

Additionally, a concurrent operation that changes the table metadata (including partitioning schema) can cause partition-based detection to fail, resulting in a generic `METADATA_CHANGE` conflict.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Best Practices

- **Use partition filters in transactional operations.** Add WHERE clauses that reference partition columns to scope the operation to a subset of data.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **Include partition columns in MERGE source queries.** When merging into a partitioned table, ensure the source query includes the partition key so Delta Lake can apply partition pruning and reduce conflicts.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **Avoid concurrent operations that modify the entire table.** Operations that touch all partitions (e.g., `DELETE` or `UPDATE` without a partition predicate, or full table replacement) are likely to conflict with any concurrent write. Schedule such operations during quiet periods or use [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) with retries.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **Handle `WITH_PARTITION_HINT` errors by checking partition overlap.** If a `WITH_PARTITION_HINT` error occurs, the partitions specified in the hint overlap with those modified by a concurrent transaction. Review the application logic to ensure concurrent writers target distinct partition values.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **Retry on transient conflicts.** Many partition‑related conflicts are transient (e.g., `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`) and can be resolved by retrying the operation.^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- Partition Pruning in Delta Lake
- [MERGE Operations](/concepts/delta-lake-dml-operations.md)
- Table Metadata Changes
- [Row-level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md)

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
