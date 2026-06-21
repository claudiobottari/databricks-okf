---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85ee33def46c3705a730866cc49c2ce432dbba7e32788c4648f9b13c5c36a54c
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduled_table_not_supported
    - SCHEDULED_TABLE_NOT_SUPPORTED
    - Scheduled Tables Not Supported
    - scheduled_table_not_supported-sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: SCHEDULED_TABLE_NOT_SUPPORTED
description: Sub-error indicating that scheduled streaming tables cannot be used as the source for a deep clone operation.
tags:
  - error
  - databricks
  - delta-lake
  - streaming
  - scheduling
timestamp: "2026-06-19T18:24:13.342Z"
---

# SCHEDULED_TABLE_NOT_SUPPORTED

**SCHEDULED_TABLE_NOT_SUPPORTED** is an error condition that occurs when attempting to perform a [Deep Clone](/concepts/deep-clone.md) operation on a Streaming Table that has an associated schedule. The error indicates that scheduled streaming tables are not supported for deep clone operations.

## Error Message

```
SCHEDULED_TABLE_NOT_SUPPORTED
Scheduled streaming tables are not supported for deep clone.
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Cause

This error is raised when a `DEEP CLONE` command is executed against a streaming table that has been configured with a schedule. The deep clone operation is incompatible with scheduled streaming tables due to architectural constraints. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Error Conditions

This error is part of the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class, which includes several other unsupported operations for streaming table deep clones:

- LOCATION_NOT_SUPPORTED — Specifying a `LOCATION` is not supported because the cloned streaming table uses managed storage.
- OLD_ARCHITECTURE_NOT_SUPPORTED — Only streaming tables using the default publishing mode are supported.
- REQUIRES_WITH_HISTORY — The `WITH HISTORY` clause is required; use `CREATE TABLE ... DEEP CLONE ... WITH HISTORY`.
- TIME_TRAVEL_NOT_SUPPORTED — Time travel is not supported for streaming table deep clone.

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## SQLSTATE

This error belongs to SQLSTATE class `0A000` (Feature Not Supported). ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Workaround

To deep clone a streaming table, remove any schedule from the table before running the `DEEP CLONE` command. After the clone operation completes, you can reapply the schedule if needed.

## Related Concepts

- Streaming Table — A Delta table that is continuously updated from a streaming data source.
- [Deep Clone](/concepts/deep-clone.md) — A Delta Lake operation that creates a full copy of a table including all data and metadata.
- Scheduled Table — A table that is refreshed on a defined schedule.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
