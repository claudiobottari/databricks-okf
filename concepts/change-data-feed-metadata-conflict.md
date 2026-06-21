---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2cf17e34f2d4793fae7c881bae76ed7b8341e47401c7be555a475465c063ce25
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-metadata-conflict
    - CDFMC
    - Change Data Feed (Databricks)
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Change Data Feed Metadata Conflict
description: A conflict condition where a user-defined column named '_change_type' collides with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection in Delta Lake; resolution requires renaming the column or disabling CDC.
tags:
  - delta-lake
  - change-data-feed
  - metadata
timestamp: "2026-06-18T11:52:08.485Z"
---

---
title: Change Data Feed Metadata Conflict
summary: An error condition that occurs when a Delta table contains a column named `_change_type`, which conflicts with Change Data Feed metadata columns, preventing row-level conflict detection.
sources:
  - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - databricks
  - error
  - delta-lake
  - change-data-feed
aliases:
  - change-data-feed-metadata-conflict
  - CDFMC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Change Data Feed Metadata Conflict

A **Change Data Feed (CDC) Metadata Conflict** occurs when a [Delta table](/concepts/delta-lake-table.md) contains a user-defined column named `_change_type` that conflicts with the internal metadata column used by [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDC). This conflict prevents Databricks from performing row-level conflict detection during concurrent write operations, leading to the `CHANGE_TYPE_COLUMN` error condition. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Error Condition

The error is raised under the `DIELTA_CONCURRENT_DELETE_DELETE` error class with the following message:

> The table contains a column named '_change\_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column or disable CDC.

The corresponding SQLSTATE is `2D521` (invalid transaction termination). ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Cause

Delta Lake’s Change Data Feed feature uses the metadata column `_change_type` to record the type of change (insert, update, delete) in the change data output. If a table already has a user-defined column with the exact name `_change_type`, the system cannot distinguish between the user’s column and the CDC metadata column. This ambiguity blocks row-level conflict detection, which relies on unambiguous metadata columns to identify which rows were modified by a concurrent transaction. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Resolution

Two workarounds are available:

- **Rename the conflicting column.** Change the user-defined column `_change_type` to a name that does not conflict with CDC metadata columns (e.g., `change_type`, `change_type_user`).
- **Disable Change Data Feed on the table.** If CDC is not required, turn it off to remove the metadata column conflict. CDC can be disabled by setting the table property `delta.enableChangeDataFeed` to `false`.

After applying either fix, retry the operation that triggered the error. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The Delta Lake feature that captures row-level changes for downstream processing
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — The mechanism that detects concurrent modifications to the same rows during transactional operations
- DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE — The error class that includes the `CHANGE_TYPE_COLUMN` condition
- [Delta Table](/concepts/delta-lake-table.md) — The storage format that supports CDC and concurrent write operations

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
