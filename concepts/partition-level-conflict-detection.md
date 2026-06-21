---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1219d06270af25e0898f0909c18185089c48ab1e872e46b407a8642a658461dd
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-level-conflict-detection
    - PCD
    - Row-Level Conflict Detection
    - Row-level Conflict Detection
    - Row-level conflict detection
    - row-level conflict detection
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Partition-Level Conflict Detection
description: Conflict detection that operates at the partition level, where concurrent modifications to specific partitions invalidate reads or writes targeting those partitions
tags:
  - delta-lake
  - partitioning
  - concurrency
timestamp: "2026-06-19T10:03:50.414Z"
---

# Partition-Level Conflict Detection

**Partition-Level Conflict Detection** is a mechanism in [Delta Lake](/concepts/delta-lake.md) that identifies and resolves transaction conflicts occurring within the same table partition. When concurrent operations modify data in overlapping partitions, this detection system helps determine whether the conflict can be safely resolved or requires a transaction retry.

## Overview

Partition-level conflict detection is a sub-type of [Delta Lake Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) that focuses on conflicts arising from concurrent modifications to specific table partitions. When concurrent transactions attempt to modify data in the same partition, Delta Lake's conflict detection system evaluates whether the operations can proceed or must be retried.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Conflict Detection Mechanisms

### Partition-Based Hints

Delta Lake supports partition-level conflict resolution through explicit partition hints. The `WITH_PARTITION_HINT` error condition indicates that a concurrent operation modified data in a partition that should have been read by the current operation. When this occurs, the system provides the specific partition values that caused the conflict.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

```text
WITH_PARTITION_HINT: The concurrent operation modified data in the partition
<partitionValues> that should have been read by this operation.
```

### Partitioned Tables Without Merge Source

The `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` error occurs when row-level conflict detection cannot be performed on a partitioned table, typically because the merge operation lacks sufficient source information to determine partition boundaries. In such cases, Delta Lake falls back to requiring a retry of the operation.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Whole-Table vs. Partition-Level Reads

The `WHOLE_TABLE_READ` error indicates that a transaction attempted to read the entire table rather than specific partitions, conflicting with concurrent modifications. This error includes guidance to add filters to narrow the data scope, which effectively enables partition-level conflict detection by restricting the read to specific partitions.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Common Conflict Scenarios

| Error Condition | Description | Resolution |
|-----------------|-------------|------------|
| `WITH_PARTITION_HINT` | Concurrent operation modified a partition that should have been read | Retry the operation |
| `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` | Cannot determine partition boundaries for conflict detection | Retry with partition hints or merge source |
| `WHOLE_TABLE_READ` | Transaction read entire table, conflicting with concurrent writes | Add partition filters or retry |
| `WHOLE_TABLE_REPLACE` | Concurrent operation replaced all data in the table | Retry the operation |

## Best Practices

### Use Partition Filtering

To maximize partition-level conflict detection effectiveness, include partition filters in your queries. This allows Delta Lake to identify which partitions are affected and only check for conflicts within those partitions, rather than performing whole-table conflict detection.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Provide Merge Source Information

When performing MERGE operations on partitioned tables, ensure the merge source contains sufficient partition information. This enables Delta Lake to perform partition-level conflict detection and avoid the `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` error.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Monitor for Partition Conflicts

Watch for `WITH_PARTITION_HINT` errors in application logs, as these indicate hot partitions where multiple concurrent operations are contending for the same data. Consider redesigning partitioning strategies or implementing retry logic with exponential backoff for workloads with frequent partition-level conflicts.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Relationship to Other Conflict Detection

Partition-level conflict detection works alongside [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) and Table-Level Conflict Detection in Delta Lake's three-tiered conflict resolution system. While row-level detection provides fine-grained granularity for individual rows, partition-level detection operates at an intermediate scope, balancing precision with performance for workloads that naturally partition their data. The `ALLOTTED_TIME_EXCEEDED` error may occur when partition-level resolution takes too long, indicating the need to optimize the query or partition strategy.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The foundation for conflict detection and ACID transactions
- Concurrent Writes in Delta Lake — Understanding how multiple writers interact
- Partitioning Strategies in Delta Lake — Design considerations for partition schemes
- [MERGE Operations in Delta Lake](/concepts/merge-into-delta-lake.md) — Complex operations prone to partition conflicts
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — Fine-grained conflict detection for individual rows

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
