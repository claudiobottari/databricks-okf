---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15e0a3b07a35737f9571f18b40f1dacc3a5ee38701a164e6b259f36982e3836c
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allotted-time-for-conflict-resolution
    - ATFCR
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Allotted Time for Conflict Resolution
description: A timeout condition (ALLOTTED_TIME_EXCEEDED) indicating row-level conflict resolution exceeded the maximum allowed time, requiring a retry
tags:
  - delta-lake
  - timeouts
  - error-handling
timestamp: "2026-06-19T10:03:41.037Z"
---

# Allotted Time for Conflict Resolution

**Allotted Time for Conflict Resolution** refers to the maximum duration allowed for Delta Lake to resolve row-level conflicts that arise when concurrent transactions modify the same data. If conflict resolution does not complete within this time limit, the transaction fails with a specific error.

## Overview

When multiple Delta Lake transactions attempt to modify the same rows simultaneously, Delta Lake performs row-level conflict detection and resolution to maintain consistency. This process has a predefined time budget — the *allotted time* — to complete. If the conflict resolution logic exceeds this time limit, the operation is aborted. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Condition: `ALLOTTED_TIME_EXCEEDED`

The `ALLOTTED_TIME_EXCEEDED` subtype of the DELTA_CONCURRENT_APPEND error class is raised when row-level conflict resolution cannot finish within the allotted time. The error message advises the user to retry the operation and refers to a documentation link for more information. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

The exact error is:
```
Row-level conflict resolution exceeded the allotted time. Please retry the operation. Refer to <docLink> for more information.
```

## Cause

The allotted time is exceeded when the conflict resolution logic takes longer than the system’s configured timeout. This can happen due to:

- A high number of concurrent modifications to the same rows.
- Complex conflict resolution scenarios that require extensive computation.
- System resource contention or latency spikes.

## Resolution

The recommended action is to retry the operation. Retrying may succeed if the concurrent transaction that caused the conflict has completed, reducing the complexity of resolution in the next attempt. If the error persists, consider:

- Reducing concurrency on the same rows.
- Breaking large transactions into smaller ones.
- Adjusting isolation levels or enabling [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) features.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and conflict resolution.
- Concurrent transactions — Multiple operations attempting to modify the same Delta table simultaneously.
- [Row-level conflict detection](/concepts/delta-lake-row-level-conflict-detection.md) — The mechanism Delta Lake uses to identify and resolve conflicting row modifications.
- DELTA_CONCURRENT_APPEND — The error class that encompasses conflict-related transaction failures.
- Retry logic — A common pattern for handling transient transaction conflicts.
- [Optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying approach Delta Lake uses to manage concurrent writes.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
