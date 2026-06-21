---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 918c9939a74a3cb658bc76e5caecf66dee885b319b47440e76de1acb15f73245
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-metadata-conflicts
    - CDFMC
    - Change Data Feed on Databricks
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Change Data Feed Metadata Conflicts
description: A conflict that occurs when a user-defined column named '_change_type' collides with Delta Lake's Change Data Feed metadata columns, preventing row-level conflict detection
tags:
  - delta-lake
  - change-data-feed
  - metadata
timestamp: "2026-06-19T10:03:43.315Z"
---

# Change Data Feed Metadata Conflicts

**Change Data Feed Metadata Conflicts** occur when columns used by the [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) mechanism in [Delta Lake](/concepts/delta-lake.md) clash with user-defined column names in a table. These conflicts can prevent row-level conflict detection from working correctly, leading to transaction errors.

## Overview

The DELTA_CONCURRENT_APPEND error condition includes a specific sub-type related to Change Data Feed metadata conflicts. When a table contains a column named `_change_type`, this conflicts with the internal metadata columns that [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) uses to track row changes, making row-level conflict detection impossible. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Details

### CHANGE_TYPE_COLUMN

The `CHANGE_TYPE_COLUMN` sub-type of the DELTA_CONCURRENT_APPEND error is triggered when a user-defined column named `_change_type` exists in a Delta table. This column name is reserved by [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) for its internal metadata tracking. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

**Error message:** "The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Please rename this column." ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Cause

[Change Data Feed](/concepts/delta-change-data-feed-cdf.md) uses specific metadata columns—including `_change_type`—to track which rows were inserted, updated, or deleted in a Delta table. When a user creates a column with the same name, [Delta Lake](/concepts/delta-lake.md) cannot distinguish between the user's data and the CDF metadata, effectively breaking row-level conflict resolution for concurrent transactions. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Solution

Rename the conflicting column in the table schema to a name that does not clash with [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) metadata columns. The table must not contain any column named `_change_type` for row-level conflict detection to function properly. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Error Sub-Types

The DELTA_CONCURRENT_APPEND error class includes several other sub-types that may arise during concurrent transactions:

- ALLOTTED_TIME_EXCEEDED Sub-error|ALLOTTED_TIME_EXCEEDED – Row-level conflict resolution time exceeded
- [PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE](/concepts/partitioned-table-merge-conflicts-in-delta-lake.md) – Partitioned table conflict issues
- PREDICATES_NEED_REWRITE – Filter predicate incompatibility
- ROW_LEVEL_CHANGES – Concurrent modification of same rows
- [WHOLE_TABLE_READ](/concepts/whole-table-readreplace-conflicts.md) – Full table read conflicts
- [WHOLE_TABLE_REPLACE](/concepts/whole-table-readreplace-conflicts.md) – Full table replacement conflicts

## Related Concepts

- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – Delta Lake feature for tracking row-level changes
- [Delta Lake](/concepts/delta-lake.md) – Open-source storage layer for Lakehouse architecture
- Concurrent Transaction Conflicts – Understanding transaction management in Delta Lake
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) – Mechanism for resolving concurrent writes
- Schema Design Considerations – Best practices for avoiding reserved column names

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
