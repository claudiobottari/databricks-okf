---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 705409df32785222fa9c0b9016a33163b8041d39ce889609ca5904b09b25e0a1
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - allotted_time_exceeded-in-delta-lake
    - AIDL
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: ALLOTTED_TIME_EXCEEDED in Delta Lake
description: A specific sub-error of DELTA_CONCURRENT_DELETE_READ indicating that row-level conflict resolution exceeded its allotted time and the operation should be retried.
tags:
  - delta-lake
  - error-handling
  - timeouts
timestamp: "2026-06-19T10:04:32.331Z"
---

## ALLOTTED_TIME_EXCEEDED in Delta Lake

`ALLOTTED_TIME_EXCEEDED` is a [SQLSTATE: 2D521](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-2d-invalid-transaction-termination) error condition in Delta Lake that occurs when row-level conflict resolution exceeds its allotted time limit during a concurrent write operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### When It Occurs

This error is raised when Delta Lake's optimistic concurrency control mechanism attempts to resolve a transaction conflict at the row level, but the resolution process takes longer than the configured time limit. The system terminates the transaction rather than allowing it to proceed with an unresolved conflict. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Recommended Action

The documented remediation is to retry the operation. The error is typically transient; a subsequent attempt may succeed if the concurrent operation completes before the retry's resolution deadline. Refer to the linked documentation in the error message for further guidance. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Related Concepts

- Transaction conflict detection in Delta Lake — The broader class of errors this condition belongs to
- DELTA_CONCURRENT_DELETE_READ Error Class|Concurrent delete read error class — The parent error class for transaction conflicts
- [Optimistic concurrency control in Delta Lake](/concepts/delta-lake-optimistic-concurrency-control.md) — The mechanism that detects and resolves write conflicts
- [Delta Lake write conflict resolution](/concepts/delta-lake-row-level-conflict-resolution.md) — Strategies for avoiding `ALLOTTED_TIME_EXCEEDED`

### Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
