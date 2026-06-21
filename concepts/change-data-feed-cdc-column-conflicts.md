---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f6034502515cddca034dd4b8110442f9047a9b5f84bb41b17d7f254caa0b507
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-cdc-column-conflicts
    - CDF(CC
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Change Data Feed (CDC) Column Conflicts
description: A specific conflict scenario where a table contains a user-defined column named '_change_type' that interferes with Delta Lake's Change Data Feed metadata, preventing row-level conflict detection.
tags:
  - delta-lake
  - cdc
  - metadata
  - conflict
timestamp: "2026-06-19T18:23:33.158Z"
---

# Change Data Feed (CDC) Column Conflicts

**Change Data Feed (CDC) Column Conflicts** occur when a Delta table contains a column named `_change_type` that conflicts with the metadata columns required by Delta Lake's Change Data Feed feature. This conflict prevents row-level conflict detection during concurrent operations.

## Overview

Delta Lake's Change Data Feed (CDC) uses specific metadata columns to track row-level changes in a table. When a table contains a user-defined column named `_change_type`, it creates a naming conflict with the CDC metadata column, making row-level conflict detection impossible. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Error Behavior

When a CDC column conflict is detected, the system raises the `DELTA_CONCURRENT_DELETE_READ` error with the subcategory `CHANGE_TYPE_COLUMN`. This error prevents the transaction from proceeding and requires corrective action before the operation can be retried. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Resolution Options

To resolve a CDC column conflict, choose one of the following approaches:

1. **Rename the conflicting column**: Change the name of the `_change_type` column in your table schema to avoid the naming conflict with CDC metadata columns.

2. **Disable Change Data Feed**: If CDC functionality is not required for your use case, disable CDC on the table to eliminate the metadata column conflict.

After applying either resolution, retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- Change Data Feed (CDC) — The Delta Lake feature tracking row-level changes in tables.
- Delta Lake Concurrent Operations — Understanding transaction conflicts in Delta Lake.
- DELTA_CONCURRENT_DELETE_READ Error|DELTA_CONCURRENT_DELETE_READ — The error class associated with concurrent read-delete conflicts.
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — The mechanism that CDC column conflicts prevent.
- [Delta Table Schema Management](/concepts/delta-table-schema-requirements.md) — How to manage table columns and avoid naming conflicts.

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
