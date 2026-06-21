---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a35c571b30f0b20d441109fe244fff0a5b84ae53e598825237c6e2f37837e207
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-hints-for-delta-lake-conflict-resolution
    - PHFDLCR
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Partition Hints for Delta Lake Conflict Resolution
description: A technique using partition hints to narrow the scope of read operations in Delta Lake, reducing the chance of concurrent delete conflicts to specific partitions.
tags:
  - delta-lake
  - partitioning
  - transaction-conflicts
timestamp: "2026-06-19T15:03:57.777Z"
---

# Partition Hints for Delta Lake Conflict Resolution

**Partition Hints for Delta Lake Conflict Resolution** refers to the use of partition-level metadata hints to reduce transaction conflicts during DELETE operations in [Delta Lake](/concepts/delta-lake.md). By informing the conflict detection engine which partitions were read, partition hints allow more precise row-level conflict detection, avoid full-table scans, and improve retry success rates.

## Overview

When a [Delta Lake](/concepts/delta-lake.md) transaction conflicts with a concurrent write, the error class `DELTA_CONCURRENT_DELETE_READ` is raised. One way to resolve such conflicts is to apply partition hints that tell the engine which partitions the transaction read. This enables the engine to perform row-level conflict detection efficiently and avoid false conflicts on unrelated partitions. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## WITH_PARTITION_HINT Error Condition

The `WITH_PARTITION_HINT` sub‑error occurs when a concurrent DELETE operation deleted data from a partition that the current transaction had read. The error message identifies the specific partition values that caused the conflict:

> The concurrent operation deleted data in the partition `<partitionValues>` that was read by this operation. Please retry the operation.

This indicates that the engine recognised the partition hint, but the concurrent write touched a relevant partition. Retrying the operation often succeeds because the second attempt sees the updated partition state and can proceed. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE Error Condition

The `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` sub‑error occurs when row‑level conflict detection cannot be performed on a partitioned table, typically because the operation lacks a source that can be used to infer partition boundaries (for example, in a MERGE statement). The recommended action is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

This error highlights the importance of providing merge sources (e.g., a well‑defined source table or sub‑query) that allow Delta Lake to determine which partitions are affected. Without that information, the engine may fall back to a full table read, increasing the chance of conflict. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Other Partition-Related Sub‑errors

While not directly about hints, the following sub‑errors relate to partition-level conflict detection:

- **WHOLE_TABLE_READ** – The transaction read the entire table without filters, conflicting with a concurrent deletion. The recommendation is to add filters to narrow the data scope and retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **EMPTY_READ_PREDICATES** – The transaction had no filters and read the whole table; adding filters is advised. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WITHOUT_HINT** – The concurrent operation deleted data that was read by the current operation, but no partition hint was used. Retrying is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## How Partition Hints Help

Partition hints (for example, in `DELETE`, `UPDATE`, or `MERGE` statements) tell Delta Lake which partitions the transaction reads. When a concurrent transaction touches the same partitions, the conflict detector can flag the conflict accurately and retry the operation. Without partition hints, the engine might conservatively report conflicts on unrelated partitions (the `WHOLE_TABLE_READ` sub‑error) or fail entirely with `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`. Common patterns include:

- Using `WHERE` clauses on partition columns.
- Explicitly using partition hints in SQL (e.g., `SELECT /*+ PARTITION(...) */`).
- Pre‑filtering input data to restrict reads to known partitions.

## Retry Behavior

All `DELTA_CONCURRENT_DELETE_READ` sub‑errors, including `WITH_PARTITION_HINT` and `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`, recommend retrying the operation. In many cases, a retry succeeds because the concurrent transaction has already completed and the next attempt sees the updated table state. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – How Delta Lake handles multiple writers.
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) – Mechanism for detecting conflicts at the row level.
- [MERGE Statement](/concepts/delta-lake-dml-statements.md) – Common operation that benefits from partition hints.
- Partition Pruning – Optimization that limits the data scanned and reduces conflict surface.
- DELTA_CONCURRENT_APPEND – Similar conflict class for concurrent append operations.

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
