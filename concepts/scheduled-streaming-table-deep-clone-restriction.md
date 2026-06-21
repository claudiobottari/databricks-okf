---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 031b83e5e9e5f23bb481014feb8499a2bcc3ffb37003ae528c44942c473bbc4a
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduled-streaming-table-deep-clone-restriction
    - SSTDCR
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Scheduled Streaming Table Deep Clone Restriction
description: Scheduled streaming tables cannot be used as the source of a deep clone operation
tags:
  - delta-lake
  - streaming-tables
  - scheduling
  - deep-clone
timestamp: "2026-06-19T15:04:04.300Z"
---

# Scheduled Streaming Table Deep Clone Restriction

The **Scheduled Streaming Table Deep Clone Restriction** is a limitation that prevents deep cloning of [Scheduled Streaming Tables](/concepts/scheduled-streaming-tables.md) in Databricks. When attempting to perform a `DEEP CLONE` operation on a streaming table that has an active schedule, the system returns the error `SCHEDULED_TABLE_NOT_SUPPORTED`.

## Error Condition

The error is categorized under the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class with SQLSTATE `0A000` (Feature Not Supported). The specific error message is:

> Scheduled streaming tables are not supported for deep clone.

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Restrictions

The scheduled streaming table deep clone restriction is part of a broader set of limitations on deep cloning streaming tables. Other related restrictions include:

- **LOCATION_NOT_SUPPORTED**: Specifying a `LOCATION` is not supported because the cloned streaming table uses managed storage. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]
- **OLD_ARCHITECTURE_NOT_SUPPORTED**: Only streaming tables using the default publishing mode are supported for deep clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]
- **REQUIRES_WITH_HISTORY**: The `WITH HISTORY` clause is required when deep cloning streaming tables. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]
- **TIME_TRAVEL_NOT_SUPPORTED**: Time travel is not supported for streaming table deep clone operations. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Workaround

To deep clone a scheduled streaming table, you must first remove or pause the schedule before performing the `DEEP CLONE` operation. Once the clone is complete, the schedule can be re-established on the cloned table if needed. Alternatively, consider using [CREATE TABLE ... AS SELECT](/concepts/create-table-as-select-ctas-for-migration.md) or other data copying approaches that do not rely on the deep clone functionality.

## Related Concepts

- Streaming Tables
- Scheduled Tables
- [Deep Clone](/concepts/deep-clone.md)
- Delta Live Tables
- [Delta Lake](/concepts/delta-lake.md)

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
