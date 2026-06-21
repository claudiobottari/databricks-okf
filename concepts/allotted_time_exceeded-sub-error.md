---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e89158fd416ef49ce3d03672ad9db3d2ddc9e3dfe26d6bf1efefabfcf10024a
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allotted_time_exceeded-sub-error
    - ALLOTTED_TIME_EXCEEDED
    - Allotted time exceeded
    - allotted_time_exceeded-in-delta-lake
    - AIDL
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: ALLOTTED_TIME_EXCEEDED Sub-error
description: A sub-error of DELTA_CONCURRENT_DELETE_DELETE indicating that row-level conflict resolution exceeded the allotted time and the operation should be retried.
tags:
  - delta-lake
  - error-handling
  - timeout
timestamp: "2026-06-19T15:03:01.474Z"
---

## ALLOTTED_TIME_EXCEEDED Sub-error

**ALLOTTED_TIME_EXCEEDED** is a sub-error of the DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE error condition. It occurs when [Delta Lake](/concepts/delta-lake.md)’s row-level conflict resolution logic takes longer than the system‑allowed time limit, causing the transaction to fail.

### Description

When a concurrent delete operation on a Delta table triggers row-level conflict detection, the resolution process must complete within a fixed time budget. If that budget is exhausted, Delta Lake raises the `ALLOTTED_TIME_EXCEEDED` sub-error. The error message directs the user to retry the operation and provides a documentation link for further details. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Resolution

The recommended course of action is to **retry the operation**. Retrying gives the system an opportunity to succeed under less contention or with a more favourable scheduling of conflict resolution work. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Related Concepts

- DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE error condition – The parent error class for concurrent deletion conflicts.
- Delta Lake transaction conflicts – Broader topic covering all concurrency‑related errors.
- Retry strategy – Best practices for handling transient errors in distributed data pipelines.

### Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
