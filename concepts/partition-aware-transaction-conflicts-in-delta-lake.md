---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bb9d349134a0e6ab515718575d96f77ebe2097be248b85ada412022b3c3d015
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - partition-aware-transaction-conflicts-in-delta-lake
    - PTCIDL
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Partition-Aware Transaction Conflicts in Delta Lake
description: Conflict scenarios in Delta Lake specifically related to partitioned tables, including inability to detect conflicts on partitioned tables and conflicts limited to specific partition values.
tags:
  - delta-lake
  - partitioning
  - concurrency
timestamp: "2026-06-19T15:02:53.163Z"
---

# Partition-Aware Transaction Conflicts in Delta Lake

Transaction conflicts in Delta Lake arise when concurrent operations modify the same table. Some of these conflicts are detected at the partition level, where the conflict detection logic uses partition boundaries or partition hints to identify conflicting writes. The DELTA_CONCURRENT_APPEND error class (SQLSTATE 2D521) includes several error sub‑types that are directly related to partition‑aware conflict scenarios.

The following sub-types are reported when a partition‑aware conflict occurs:

- **WITH_PARTITION_HINT**  
  The concurrent operation modified data in the partition `<partitionValues>` that should have been read by this operation. Retrying the operation is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE**  
  Row‑level conflict detection could not be performed on this partitioned table. Retrying the operation is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **PREDICATES_NEED_REWRITE**  
  The filter predicates used by this transaction could not be applied for row‑level conflict detection. Because partition pruning often relies on filter predicates, this sub‑type can also indicate a partition‑aware conflict. Retrying the operation is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

The **WITH_PARTITION_HINT** sub‑type is particularly partition‑aware: it explicitly reports which partition(s) were modified by a concurrent operation, allowing the user to target retries or adjust partition‑level access patterns.

For non‑partition‑aware conflict sub‑types (such as `ROW_LEVEL_CHANGES`, `WHOLE_TABLE_READ`, or `WHOLE_TABLE_REPLACE`), see the DELTA_CONCURRENT_APPEND error class documentation.

## Related Concepts

- [Delta Lake concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md)
- DELTA_CONCURRENT_APPEND Error Class|DELTA_CONCURRENT_APPEND error class
- [Delta Lake transactions](/concepts/delta-lake-transaction-log.md)
- Partition pruning
- Change Data Feed (CDC)

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
