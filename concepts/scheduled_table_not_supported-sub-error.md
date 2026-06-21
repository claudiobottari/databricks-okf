---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05fd46ac8ee229d2aa2e8aeee050af08a576b6c29d69b4cf3bff1c9f868313c6
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduled_table_not_supported-sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: SCHEDULED_TABLE_NOT_SUPPORTED sub-error
description: Sub-error indicating that scheduled (automated refresh) streaming tables cannot be deep cloned.
tags:
  - error-messages
  - streaming-tables
  - scheduling
timestamp: "2026-06-19T10:04:54.470Z"
---

# SCHEDULED_TABLE_NOT_SUPPORTED Sub-Error

**SCHEDULED_TABLE_NOT_SUPPORTED** is a sub-error of the DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR|DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class that occurs when attempting to perform a deep clone operation on a scheduled streaming table. This operation is not permitted by the system.

## Error Message

The error is returned as part of the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class:

```
Deep clone of streaming table failed: SCHEDULED_TABLE_NOT_SUPPORTED
```

## Cause

This error occurs when a user attempts to [Deep Clone](/concepts/deep-clone.md) a streaming table that has been configured with a schedule. The system does not support deep cloning for streaming tables that are scheduled for automatic refreshes. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, remove the schedule from the source streaming table before performing the deep clone operation, or use an alternative approach for copying the data that does not involve deep cloning a scheduled streaming table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR|DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class — The parent error class containing this sub-error
- Streaming tables — Tables that incrementally process data from streaming sources
- [Deep Clone](/concepts/deep-clone.md) — A copy operation that duplicates table metadata and data
- LOCATION_NOT_SUPPORTED sub-error — Another sub-error in the same error class
- REQUIRES_WITH_HISTORY sub-error — Related sub-error requiring `WITH HISTORY` clause

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
