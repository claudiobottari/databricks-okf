---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55968646cedfa3dd4ffa025df7b89bc99eeed8bb23afc3a02facd3e8c955b03d
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-metadata-column-conflicts
    - CDFMCC
    - Change Data Feed metadata columns
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Change Data Feed Metadata Column Conflicts
description: A conflict where user-defined columns named '_change_type' interfere with Change Data Feed (CDF) metadata columns, preventing row-level conflict detection in Delta Lake.
tags:
  - delta-lake
  - change-data-feed
  - metadata
timestamp: "2026-06-19T15:02:59.460Z"
---

Here is the wiki page for "Change Data Feed Metadata Column Conflicts".

# Change Data Feed Metadata Column Conflicts

**Change Data Feed Metadata Column Conflicts** occur when a Delta table contains a user-defined column named `_change_type` that conflicts with the internal metadata column required by [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDC) functionality. This conflict prevents row-level conflict detection during concurrent operations on the table.

## Overview

Delta Lake's Change Data Feed uses a reserved metadata column named `_change_type` to track the type of change (insert, update, delete) for each row. If a table already contains a column with this name, the CDC feature cannot properly manage its metadata, leading to operational errors. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Error Conditions

When a transaction encounters this conflict, it raises an error with SQLSTATE `2D521` (Invalid Transaction Termination). The specific error messages differ slightly depending on the type of operation involved:

### DELTA_CONCURRENT_DELETE_DELETE

This error occurs when a concurrent operation deletes data that the current transaction also attempts to delete. The error message reads:

```
The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column or disable CDC.
```

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### DELTA_CONCURRENT_DELETE_READ

This error occurs when a concurrent operation deletes data that the current transaction has already read. The error message is identical:

```
The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column or disable CDC.
```

^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Causes

The conflict arises when a user or application creates a column named `_change_type` in a Delta table that also has Change Data Feed enabled. Delta Lake reserves this column name internally for tracking change types (insert, update, delete) in the change data feed. When both exist simultaneously, Delta cannot distinguish between user data and CDC metadata, which breaks the row-level conflict resolution mechanism. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Solutions

Two options are available to resolve the conflict:

1. **Rename the conflicting column**: Change the name of the user-defined `_change_type` column to something that does not conflict with reserved CDC metadata column names.

2. **Disable Change Data Feed**: If the CDC feature is not required for the table, disable it to remove the metadata column reservation.

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md, delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- Change Data Feed (CDC) — The feature that uses the reserved `_change_type` metadata column
- Delta Lake Transaction Protocol — The underlying protocol for concurrent write operations
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — The mechanism that CDC metadata columns support
- [Delta Table Schema Constraints](/concepts/delta-table-schema-requirements.md) — Rules about reserved column names in Delta tables
- DELTA_CONCURRENT_DELETE_DELETE Error Class|DELTA_CONCURRENT_DELETE_DELETE Error — The full error class including all sub-conditions
- DELTA_CONCURRENT_DELETE_READ Error — Related error for read-delete conflicts

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
2. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
