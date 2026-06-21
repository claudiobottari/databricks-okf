---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eedf0cc2e08ffda8855c0924f4a4fbb036319ea768e8fce23d702d1253c541f7
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-cdf-metadata-column-conflicts
    - CDF(MCC
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Change Data Feed (CDF) Metadata Column Conflicts
description: A conflict scenario where a table contains a column named '_change_type' that interferes with Delta Lake's Change Data Feed metadata columns, preventing row-level conflict detection.
tags:
  - delta-lake
  - change-data-feed
  - metadata-conflicts
timestamp: "2026-06-18T15:17:44.820Z"
---

# Change Data Feed (CDF) Metadata Column Conflicts

**Change Data Feed (CDF) Metadata Column Conflicts** occur when a Delta table contains a user-defined column named `_change_type`, which conflicts with the reserved metadata columns used by the [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) feature. This conflict prevents row-level conflict detection from functioning correctly during concurrent write operations. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Condition

When a table has a column named `_change_type` that conflicts with CDF metadata columns, the system raises a `DELTA_CONCURRENT_APPEND` error with the `CHANGE_TYPE_COLUMN` sub-condition. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Error Message

```
CHANGE_TYPE_COLUMN: The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column.
```

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Cause

The [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) feature in Delta Lake uses reserved metadata columns to track row-level changes. One of these reserved columns is `_change_type`. When a user creates a table with a column that has the same name as a CDF metadata column, the system cannot distinguish between user data and CDF metadata, which prevents row-level conflict detection from working properly. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Solution

Rename the conflicting column in the table to a name that does not match any CDF metadata column names. The error message explicitly recommends renaming the column. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — The Delta Lake feature that tracks row-level changes
- DELTA_CONCURRENT_APPEND — The parent error class for transaction conflicts
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — The mechanism that CDF metadata columns support
- Delta Lake Transaction Protocol — The underlying protocol for concurrent writes
- Reserved Column Names in Delta Lake — Columns that Delta Lake reserves for internal use

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
