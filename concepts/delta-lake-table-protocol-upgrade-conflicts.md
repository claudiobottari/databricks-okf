---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 407e56725fa0cfc95faee419b3d58ec78dca64a635d949127ae37681296ffb47
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-protocol-upgrade-conflicts
    - DLTPUC
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Delta Lake Table Protocol Upgrade Conflicts
description: A conflict scenario where a concurrent operation upgrades a Delta table's protocol version, requiring the conflicting transaction to retry.
tags:
  - delta-lake
  - protocol-version
  - concurrency
timestamp: "2026-06-19T18:23:23.735Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) Protocol Upgrade Conflicts

**Delta Lake Table Protocol Upgrade Conflicts** occur when a concurrent operation upgrades the table protocol while another transaction is reading from or modifying the table. These conflicts are classified under the `DELTA_CONCURRENT_DELETE_DELETE` error class and manifest as the `PROTOCOL_CHANGE` sub-condition. The protocol upgrade alters metadata constraints (e.g., schema, partitioning, or supported features) after a prior transaction has already started, forcing the conflicting transaction to retry with the new protocol. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## PROTOCOL_CHANGE Error Condition

When a transaction receives the `PROTOCOL_CHANGE` error, it indicates that a concurrent operation committed a protocol upgrade on the table. The error message advises the user to retry the operation because the table’s protocol has changed. Retrying allows the transaction to re-read the table under the current (upgraded) protocol and proceed without conflict. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

This error is one of several row-level conflict resolution outcomes reported by Delta Lake. Other related conditions include `WHOLE_TABLE_REPLACE`, `ROW_LEVEL_CHANGES`, and `PREDICATES_NEED_REWRITE`, but the `PROTOCOL_CHANGE` condition specifically stems from a table protocol upgrade. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Resolution

The recommended resolution for a protocol upgrade conflict is to **retry the operation**. Because the protocol change is typically backward-compatible, a simple retry after the upgrade completes is usually sufficient. If the same conflict persists, inspect the sequence of commits on the table to ensure that protocol upgrades are not occurring repeatedly. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Lake Concurrency – Overview of optimistic concurrency control in Delta Lake.
- Delta Lake Protocol – Versioned table protocol that governs metadata and feature support.
- DELTA_CONCURRENT_DELETE_DELETE Error Class – The broader error category containing `PROTOCOL_CHANGE`.
- Concurrent Write Conflicts – General discussion of conflicts when multiple transactions modify the same table.
- Retry Logic in Delta Lake – Best practices for handling transactional conflicts.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
