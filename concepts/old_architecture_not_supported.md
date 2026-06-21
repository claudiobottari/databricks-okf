---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08ce0d9ae36077a07a2c4e63c0b2d31f55b72d6953c547607249af78ce82e718
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - old_architecture_not_supported
    - OLD_ARCHITECTURE_NOT_SUPPORTED
    - Old Architecture Not Supported
    - old_architecture_not_supported-sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: OLD_ARCHITECTURE_NOT_SUPPORTED
description: Sub-error indicating that only streaming tables using the default publishing mode are supported for deep clone operations.
tags:
  - error
  - databricks
  - delta-lake
  - streaming
timestamp: "2026-06-19T18:24:36.933Z"
---

# OLD_ARCHITECTURE_NOT_SUPPORTED

**OLD_ARCHITECTURE_NOT_SUPPORTED** is a specific error condition that occurs when attempting to perform a `DEEP CLONE` operation on a streaming table that does not use the default publishing mode. The error is raised as part of the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Overview

The error indicates that the deep clone operation only supports streaming tables that use the **default publishing mode**. If the source streaming table has been configured with a non-default publishing architecture, the deep clone operation is rejected with the `OLD_ARCHITECTURE_NOT_SUPPORTED` error. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Context

This error belongs to the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` class, which encompasses several unsupported operations on streaming tables. The full error message includes the SQLSTATE code `0A000`, which corresponds to the "Feature not supported" category in the SQL standard. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Cause

The error is triggered when:

- The streaming table was created using an older publishing architecture or a non-default publishing mode.
- A `DEEP CLONE` command is executed against such a streaming table.

The deep clone operation requires streaming tables to be using the current default publishing mode to proceed successfully. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Resolution

To resolve the `OLD_ARCHITECTURE_NOT_SUPPORTED` error, ensure that the source streaming table uses the default publishing mode. This may require recreating the streaming table with the appropriate configuration before performing the deep clone operation. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Errors

The `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` class also includes other unsupported operation errors for deep cloning streaming tables:

- LOCATION_NOT_SUPPORTED — Specifying a `LOCATION` is not supported because the cloned streaming table uses managed storage.
- REQUIRES_WITH_HISTORY — The `WITH HISTORY` clause is required for deep clone operations on streaming tables.
- SCHEDULED_TABLE_NOT_SUPPORTED — Scheduled streaming tables are not supported for deep clone.
- TIME_TRAVEL_NOT_SUPPORTED — Time travel is not supported for streaming table deep clone.

## Related Concepts

- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR — The parent error class for unsupported deep clone operations on streaming tables.
- [Deep Clone](/concepts/deep-clone.md) — A Delta Lake operation that creates a deep copy of a table, including its data and metadata.
- Streaming Tables — Delta tables that are continuously updated from streaming data sources.
- SQLSTATE 0A000 — The SQL state code for feature not supported errors.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
