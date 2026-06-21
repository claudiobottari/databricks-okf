---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1de6bb10d4c8ee1b6d223c3d164956fa6798517e0778f74281f80f33cf530b76
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - partition-hinted-vs-unhinted-conflict-resolution
    - PVUCR
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Partition-Hinted vs Unhinted Conflict Resolution
description: Two related sub-errors (WITH_PARTITION_HINT and WITHOUT_HINT) describing partition-level conflicts in Delta Lake concurrent operations, where the presence or absence of partition hints affects the error message.
tags:
  - delta-lake
  - partitioning
  - concurrency
timestamp: "2026-06-19T15:03:23.793Z"
---

# Partition-Hinted vs Unhinted Conflict Resolution

**Partition-Hinted vs Unhinted Conflict Resolution** refers to two sub‑conditions of the `DELTA_CONCURRENT_DELETE_DELETE` error class in [Delta Lake](/concepts/delta-lake.md) that indicate whether the conflicting transaction used a partition hint to narrow the scope of row‑level conflict detection. Both are specialized variants of a concurrent delete conflict error, and the recommended resolution is to retry the operation.

## Overview

Delta Lake uses optimistic concurrency control. When a `DELETE` operation conflicts with a concurrent modification, it raises `DELTA_CONCURRENT_DELETE_DELETE`. The error can be subclassed based on how the conflict was detected — specifically, whether the transaction provided a partition hint that identifies the affected partition. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

The two sub‑conditions are:

- **`WITHOUT_HINT`** — The transaction did not include a partition hint. The concurrent operation deleted data that was read by the transaction. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **`WITH_PARTITION_HINT`** — The transaction supplied a partition hint. The concurrent operation deleted data in the specified partition (`<partitionValues>`) that was also read by the transaction. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Semantic Difference

The distinction reflects the granularity of the conflict detection:

| Sub‑condition | Hint present | Conflict scope | Suggested action |
| :--- | :---: | :--- | :--- |
| `WITHOUT_HINT` | No | Entire read set of the transaction | Retry the operation. |
| `WITH_PARTITION_HINT` | Yes | Specific partition(s) named in the hint | Retry the operation. |

In both cases the error message instructs the user to retry. The presence of a partition hint does not change the recovery action — it simply provides additional context about which partition was involved in the conflict. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Use in Debugging

When troubleshooting concurrent delete errors, checking whether the error includes `WITH_PARTITION_HINT` or `WITHOUT_HINT` can help understand the scope of the conflict. A `WITH_PARTITION_HINT` error indicates that the transaction had an explicit partition filter; a `WITHOUT_HINT` error means no such filter was provided. This information can guide efforts to reduce conflict likelihood by adding partition hints to queries, though the error itself recommends only a retry. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — Optimistic concurrency model underlying this error.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — Where concurrent modifications are recorded.
- Conflict Detection in Delta Lake — How conflicts between concurrent writes are identified.
- Partition Pruning — Technique to limit the data scanned (and potentially conflicted).
- Retry Strategy for Delta Lake Errors — Best practice for handling transient concurrent‑modification errors.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
