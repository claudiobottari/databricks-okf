---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed82caf1f3eeff8654c6d5aae2028141cb230cd963b721d8c97073f445914f8a
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-cdf-metadata-conflicts
    - CDF(MC
    - change-data-feed-metadata-column-conflicts
    - CDFMCC
    - Change Data Feed metadata columns
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Change Data Feed (CDF) metadata conflicts
description: A conflict scenario where a user-defined column named '_change_type' collides with Change Data Feed metadata columns, preventing row-level conflict detection in Delta Lake.
tags:
  - delta-lake
  - change-data-feed
  - metadata
timestamp: "2026-06-19T10:04:43.392Z"
---

# Change Data Feed (CDF) Metadata Conflicts

**Change Data Feed (CDF) metadata conflicts** occur when a Delta table contains a column named `_change_type` that conflicts with the reserved metadata columns used by the [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) feature. This conflict prevents row-level conflict detection during concurrent read and write operations, leading to the `DELTA_CONCURRENT_DELETE_READ` error with the `CHANGE_TYPE_COLUMN` sub-type.

## Error Details

When a table includes a column named `_change_type`, the Delta Lake row-level conflict detection mechanism cannot distinguish between user-defined data columns and CDF metadata columns. As a result, the transaction cannot resolve conflicts at the row level and fails with the following error:

```
DELTA_CONCURRENT_DELETE_READ
CHANGE_TYPE_COLUMN: The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection.
```

^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Cause

The [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) feature in Delta Lake automatically adds metadata columns to track changes, including the `_change_type` column that indicates whether a row was inserted, updated, or deleted. If a user creates a table with a column already named `_change_type`, this creates a naming conflict that interferes with the CDF metadata system and makes row-level conflict resolution impossible. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Resolution Options

There are two approaches to resolve this conflict:

1. **Rename the conflicting column**: Change the user-defined column to a name that does not conflict with CDF metadata columns, such as `change_type` (without the leading underscore) or any other non-reserved name.

2. **Disable Change Data Feed**: If the CDF feature is not required for the table, disable it to eliminate the metadata column conflict. This removes the `_change_type` column reservation, allowing the user-defined column to coexist without issues.

^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Impact

The conflict blocks row-level conflict detection, which means the system falls back to coarser conflict resolution strategies. This can lead to more transaction conflicts and retries when concurrent operations attempt to read and modify the same data. The conflict specifically affects operations that try to read from the table while a concurrent deletion is occurring. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Prevention

To avoid CDF metadata conflicts:

- When designing schemas for Delta tables that use or might use [Change Data Feed](/concepts/delta-change-data-feed-cdf.md), avoid naming columns `_change_type`
- Review existing schemas for reserved CDF column names before enabling the feature
- Consider using a naming convention that prefixes user-defined metadata columns with a different pattern (e.g., `user_change_type`) to prevent accidental conflicts

## Related Concepts

- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — The feature that introduces reserved metadata columns
- DELTA_CONCURRENT_DELETE_READ Error|DELTA_CONCURRENT_DELETE_READ — The parent error class containing this conflict
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — The conflict resolution mechanism blocked by this issue
- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — How Delta manages concurrent read and write operations
- Delta Table Properties — Configuration options including CDF settings

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
