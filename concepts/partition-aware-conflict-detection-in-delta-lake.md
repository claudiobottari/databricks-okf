---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33ebff5e7fcff59b5227fff8b8a7c660db5c9fc98843c8ce739d36b792e6ed40
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - partition-aware-conflict-detection-in-delta-lake
    - PCDIDL
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Partition-Aware Conflict Detection in Delta Lake
description: Strategies for detecting and resolving concurrent delete conflicts on partitioned Delta tables, including partition hints and source table requirements for MERGE operations.
tags:
  - delta-lake
  - partitioning
  - concurrency
timestamp: "2026-06-19T18:23:28.438Z"
---

# Partition-Aware Conflict Detection in Delta Lake

**Partition-Aware Conflict Detection** is a feature in [Delta Lake](/concepts/delta-lake.md) that enables more granular conflict resolution during concurrent write operations by considering the specific partitions affected by each transaction. This allows Delta Lake to detect and resolve conflicts at the partition level rather than requiring full table-level retries.

## Overview

When multiple transactions attempt to modify a Delta table concurrently, Delta Lake uses optimistic concurrency control to detect conflicts. Partition-aware conflict detection improves upon basic conflict detection by narrowing the scope of conflict analysis to the specific partitions that each transaction reads or writes. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

This approach reduces the likelihood of false conflicts, where two transactions that modify different partitions are incorrectly flagged as conflicting. By understanding which partitions are involved, Delta Lake can allow non-overlapping partition modifications to proceed concurrently. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Conflict Detection with Partition Hints

When a transaction includes partition hints, Delta Lake can perform more precise conflict detection. The system tracks which partitions were read or modified by each concurrent operation and only flags a conflict if there is an actual overlap in the affected partitions. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WITH_PARTITION_HINT Error

If a concurrent operation deletes data in a partition that was read by the current transaction, Delta Lake raises the `WITH_PARTITION_HINT` error condition. The error message specifies the exact partition values that caused the conflict:

```
The concurrent operation deleted data in the partition <partitionValues> that was read by this operation.
```

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

This error indicates that the conflict was detected at the partition level, and the user can retry the operation knowing which specific partition caused the issue. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WITHOUT_HINT Error

When a transaction does not include partition hints, Delta Lake falls back to a broader conflict detection scope. The `WITHOUT_HINT` error condition occurs when a concurrent operation deletes data that was read by the current transaction, but the system cannot narrow the conflict to specific partitions:

```
The concurrent operation deleted data that was read by this operation.
```

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

This error is less informative than the partition-hinted variant because the system cannot identify which partition caused the conflict. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Error Conditions

Partition-aware conflict detection interacts with several other Delta Lake error conditions:

- **PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE**: Row-level conflict detection could not be performed on a partitioned table, requiring a retry. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **PREDICATES_NEED_REWRITE**: Filter predicates used by the transaction could not be applied for row-level conflict detection. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **ROW_LEVEL_CHANGES**: A concurrent operation modified the same rows that the current transaction attempted to modify. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **WHOLE_TABLE_READ**: The transaction attempted to modify the entire table, conflicting with a concurrent modification. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **WHOLE_TABLE_REPLACE**: A concurrent operation replaced all data in the table. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Best Practices

To maximize the benefits of partition-aware conflict detection:

1. **Use partition hints** in your queries to help Delta Lake narrow conflict detection scope. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
2. **Add filters** to your queries to narrow the data scope and reduce the likelihood of conflicts. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
3. **Design partition schemes** that align with your concurrent write patterns to minimize partition-level conflicts. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
4. **Retry operations** when conflict errors occur, as many conflicts are transient and resolve on retry. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The overall framework for managing concurrent writes
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model used by Delta Lake
- [Delta Lake Error Conditions](/concepts/delta-error-sub-conditions.md) — Complete catalog of Delta Lake error conditions
- Table Partitioning in Delta Lake — How partitioning affects query performance and conflict detection
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — CDC metadata that can interact with conflict detection

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
