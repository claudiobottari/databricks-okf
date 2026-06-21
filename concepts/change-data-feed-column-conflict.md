---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88b5079a73d09219e3dc36f3eb369f535b6e00dce9aa16f84c3bbfb1f1272b54
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-column-conflict
    - CDFCC
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Change Data Feed Column Conflict
description: A conflict condition where a user-defined column named '_change_type' clashes with Delta Lake's Change Data Feed metadata, preventing row-level conflict detection.
tags:
  - delta-lake
  - change-data-feed
  - schema-management
timestamp: "2026-06-19T18:23:17.821Z"
---

# Change Data Feed Column Conflict

**Change Data Feed Column Conflict** is a specific error condition that occurs when a Delta table contains a column named `_change_type`, which conflicts with the metadata columns used by [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md). This conflict prevents row-level conflict detection from functioning properly during concurrent write operations.

## Error Details

The error is raised with SQLSTATE `2D521` and falls under the `DELTA_CONCURRENT_DELETE_DELETE` error class. The full error message states:

> The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column or disable CDC.

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Cause

When [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) is enabled on a Delta table, the system uses reserved metadata columns—including `_change_type`—to track row-level changes. If a user-created column in the table has the same name `_change_type`, it creates a naming conflict that prevents the Delta engine from distinguishing between user data and CDF metadata. This conflict blocks row-level conflict detection during concurrent transactions. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, choose one of the following approaches:

1. **Rename the conflicting column**: Change the name of the `_change_type` column in your table schema to avoid the naming conflict with CDF metadata columns.
2. **Disable Change Data Feed**: If CDF is not required for your use case, disable it on the table to eliminate the metadata column conflict.

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) — The feature that tracks row-level changes in Delta tables
- Delta Lake Transaction Conflicts — Overview of concurrent transaction handling
- DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE — The broader error class for concurrent delete conflicts
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — The mechanism that CDF metadata columns support
- Delta Table Schema — Table structure and column naming considerations

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
