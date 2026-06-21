---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3e71be2d846daa93fed7aabb832b1a6663ee214b82e49fe09e5e25553711554
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - partition-based-transaction-conflicts-in-delta-lake
    - PTCIDL
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Partition-based Transaction Conflicts in Delta Lake
description: Conflict detection scenarios specific to partitioned Delta tables, including cases where partition hints narrow the conflict scope or where partitioned tables lack merge source information for row-level detection.
tags:
  - delta-lake
  - partitioning
  - transactions
timestamp: "2026-06-18T15:18:25.076Z"
---

# Partition-based Transaction Conflicts in Delta Lake

**Partition-based Transaction Conflicts in Delta Lake** occur when a transaction reads data from one or more partitions of a table while a concurrent transaction deletes data from overlapping partitions. Delta Lake detects these conflicts at commit time and raises a `DELTA_CONCURRENT_DELETE_READ` error with specific sub‑conditions that describe the nature of the partition‑level conflict. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Common Partition-Related Sub‑conditions

### WITH_PARTITION_HINT

This error occurs when the concurrent operation deleted data in a specific partition (identified by `<partitionValues>`) that the current transaction had read. The transaction likely used a partition hint to target that partition. To resolve, retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

When a transaction attempts row‑level conflict detection on a partitioned table but the source of the merge (or other operation) does not align with the partitioning scheme, Delta Lake cannot perform row‑level conflict detection. The safe recovery is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ (Partition Scope)

If the reading transaction scans the entire table (no filters or partition pruning) and a concurrent transaction deletes data in a specific partition, the conflict is reported as `WHOLE_TABLE_READ`. The remedy is to add filters (e.g., partition predicates) to narrow the data scope before retrying. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### EMPTY_READ_PREDICATES

When the reading transaction did not include any filters and read the entire table, it may conflict with a concurrent deletion. Although not exclusively partition‑based, this condition forces a full table scan that can cause partition‑level conflicts. Add partition filters to reduce the chance of conflict. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Other Related Sub‑conditions

- **ALLOTTED_TIME_EXCEEDED**: Row‑level conflict resolution took too long. Retry.
- **CHANGE_TYPE_COLUMN**: A column named `_change_type` interferes with Change Data Feed metadata for conflict detection.
- **PROTOCOL_CHANGE**: Concurrent operation upgraded table protocol; retry.
- **ROW_LEVEL_CHANGES**: Concurrent operation deleted rows that this transaction read; retry.
- **WHOLE_TABLE_REPLACE**: Concurrent operation replaced all data; retry.
- **WITHOUT_HINT**: Concurrent delete affected data read without explicit hint; retry.
- **PREDICATES_NEED_REWRITE**: Filter predicates could not be applied for row-level detection; retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Best Practices to Avoid Partition Conflicts

- Use partition predicates (e.g., `WHERE partition_col = value`) in read queries to limit the scan scope and reduce overlap with concurrent deletions.
- For merge operations on partitioned tables, ensure the merge source is partitioned on the same keys or use row-level conflict detection with appropriate predicates.
- Use partition hints (e.g., `delta.autoOptimize.optimizeWrite`) carefully in concurrent workloads.
- When a conflict occurs, retry the operation; Delta Lake’s [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) typically resolves transient conflicts on retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- Concurrent Write Conflicts
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md)
- Partition Pruning

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
