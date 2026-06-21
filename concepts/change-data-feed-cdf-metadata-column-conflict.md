---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfd0dc2590fbda85628927042f5739443888982f2437475cb979dd7f89811e86
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-cdf-metadata-column-conflict
    - CDF(MCC
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Change Data Feed (CDF) Metadata Column Conflict
description: A specific conflict scenario where a table column named '_change_type' conflicts with CDF metadata columns, preventing row-level conflict detection.
tags:
  - delta-lake
  - change-data-feed
  - schema
timestamp: "2026-06-19T18:22:57.448Z"
---

# Change Data Feed (CDF) Metadata Column Conflict

The **Change Data Feed (CDF) Metadata Column Conflict** is a specific error condition that occurs when a [Delta Lake Table](/concepts/delta-lake-table.md) contains a user-defined column named `_change_type`, which conflicts with a reserved metadata column used by [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md). This conflict prevents [row-level conflict detection](/concepts/delta-lake-row-level-conflict-detection.md) during concurrent write operations, leading to a `DELTA_CONCURRENT_APPEND` transaction failure. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Condition

The error condition is identified by the sub‑condition `CHANGE_TYPE_COLUMN` within the `DELTA_CONCURRENT_APPEND` error class (SQLSTATE 2D521). The full error message states:

> The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column. Refer to `<docLink>` for more information. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Cause

When Change Data Feed is enabled on a Delta table, Databricks automatically adds reserved metadata columns, including `_change_type`, to track row‑level changes (insert, update, delete). If a user manually creates a column with the same name `_change_type`, the Delta transaction protocol cannot distinguish between the user‑defined column and the system‑managed metadata column. This ambiguity disables row‑level conflict detection, and any concurrent operation that would normally rely on that detection will fail with the `CHANGE_TYPE_COLUMN` error. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Resolution

The only supported fix is to rename the conflicting user‑defined column. After renaming, row‑level conflict detection can function correctly. Databricks does not allow overriding or disabling the reserved `_change_type` column; the column name is reserved for CDF metadata. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

The `<docLink>` in the error message points to detailed guidance (typically the Databricks documentation on Change Data Feed or Delta Lake conflict resolution).

## Related Concepts

- DELTA_CONCURRENT_APPEND Error Condition|DELTA_CONCURRENT_APPEND error condition — The parent error class that includes `CHANGE_TYPE_COLUMN` and other sub‑conditions.
- [Row-level conflict detection](/concepts/delta-lake-row-level-conflict-detection.md) — The mechanism that is blocked by the naming conflict.
- Delta Lake reserved metadata columns — Columns like `_change_type` that are automatically managed by the Delta protocol.
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — The feature that uses the `_change_type` column for tracking row changes.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
