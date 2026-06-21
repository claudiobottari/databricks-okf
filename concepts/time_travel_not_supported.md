---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e31b5946353d2d656c8a4a8d276a7649e525f312880c383fcd6da0b03260593a
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_travel_not_supported
    - TIME_TRAVEL_NOT_SUPPORTED
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: TIME_TRAVEL_NOT_SUPPORTED
description: Sub-error indicating that time travel is not supported when performing a deep clone on a streaming table.
tags:
  - error
  - databricks
  - delta-lake
  - streaming
  - time-travel
timestamp: "2026-06-19T18:24:16.879Z"
---

# TIME_TRAVEL_NOT_SUPPORTED

**TIME_TRAVEL_NOT_SUPPORTED** is an error condition that occurs when a [Deep Clone](/concepts/deep-clone.md) operation is attempted on a Streaming Table with a [Time Travel](/concepts/delta-lake-time-travel.md) specification. The Databricks delta engine rejects the operation because time travel queries are not compatible with deep cloning a streaming table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Context

This error is a specific reason under the broader error class DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR. The full error message typically includes the reason `TIME_TRAVEL_NOT_SUPPORTED` to indicate that the deep clone failed because a time travel version or timestamp was provided. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

The only supported resolution is to remove the time travel clause from the deep clone statement. If you need to clone a streaming table with a specific historical state, consider alternative approaches such as copying the underlying data manually or using a snapshot-based clone without time travel.

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) – The operation that triggers the error when combined with streaming tables.
- Streaming Table – The type of table that does not support time travel during deep clone.
- [Time Travel](/concepts/delta-lake-time-travel.md) – The feature that allows querying previous versions of a Delta table, but is incompatible with deep cloning streaming tables.
- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR – The parent error class under which `TIME_TRAVEL_NOT_SUPPORTED` is raised.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
