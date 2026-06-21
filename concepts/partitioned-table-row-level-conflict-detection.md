---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d3afbade3f939e0746464f69a22e47ce7fb1364dc2f7ef117cd841502a22ab11
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partitioned-table-row-level-conflict-detection
    - PTRCD
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Partitioned Table Row-Level Conflict Detection
description: A limitation where row-level conflict detection cannot be performed on certain partitioned Delta tables, requiring a retry.
tags:
  - delta-lake
  - partitioning
  - concurrency
timestamp: "2026-06-18T11:51:26.236Z"
---

# Partitioned Table Row-Level Conflict Detection

**Partitioned Table Row-Level Conflict Detection** refers to a sub-error condition of the `DELTA_CONCURRENT_APPEND` error class in [Delta Lake](/concepts/delta-lake.md). It occurs when row-level conflict detection cannot be performed on a partitioned table, typically during concurrent write operations such as `MERGE`, `UPDATE`, or `DELETE`.

## Error Message

The error is returned with the following message:

```
DELTA_CONCURRENT_APPEND.PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE
Row-level conflict detection could not be performed on this partitioned table. Please retry the operation.
```

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Cause

Row-level conflict detection is a mechanism in Delta Lake that identifies whether concurrent transactions modify the same rows. For partitioned tables, Delta Lake normally uses the merge source (e.g., the source dataset in a `MERGE` statement) to determine which partitions are affected and to detect conflicts at the row level. If the system cannot identify or use the merge source for the partitioned table — for example, because the source is missing or the operation does not provide enough partition-level information — the detection cannot proceed and this error is raised.

Inferred factors: The error may occur due to a transient state where the partition pruning or source inference fails, or when the concurrent operation changes the table’s partitioning schema (though that is covered by a different sub-error, `METADATA_CHANGE`). Retrying the operation often resolves the issue.

## Solution

The recommended action is to retry the operation. The error is frequently caused by a temporary condition that clears on a subsequent attempt. If the error persists, verify that the operation (especially a `MERGE`) includes an explicit source dataset and that the table’s partitioning columns are correctly defined.

For `MERGE` statements, ensure the `USING` clause provides a well-defined source that can be pruned to relevant partitions. For partitioned tables, consider adding partition filter hints (`WITH PARTITION HINT`) to help Delta Lake identify the target partitions.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and conflict detection
- DELTA_CONCURRENT_APPEND Error Class — Parent error class for transaction conflicts
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) — The mechanism that detects modifications to the same rows
- Partitioning in Delta Lake — How data is organized into partitions
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — Operation often affected by this error

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
