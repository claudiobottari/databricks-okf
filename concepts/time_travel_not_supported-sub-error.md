---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9436a09c53ec556785966f26f17b0ca7e25ba555335d97ec7d04abefb6e64387
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_travel_not_supported-sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: TIME_TRAVEL_NOT_SUPPORTED sub-error
description: Sub-error indicating that time travel syntax (e.g., VERSION AS OF, TIMESTAMP AS OF) is incompatible with deep clone on streaming tables.
tags:
  - error-messages
  - delta-lake
  - time-travel
timestamp: "2026-06-19T10:05:30.091Z"
---

# TIME_TRAVEL_NOT_SUPPORTED Sub-Error

**TIME_TRAVEL_NOT_SUPPORTED** is a sub-error condition of the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class in Databricks. It occurs when attempting to perform a time travel operation during a deep clone of a streaming table.

## Error Details

When cloning a streaming table with deep clone, time travel is not supported. The error is thrown if the deep clone operation includes a time travel specification, such as a version number or timestamp.^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

This error has SQLSTATE code `0A000`, which falls under the "Feature not supported" class of SQL states.^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Full Error Message

The error appears as part of the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` and is reported with the following message:

```
TIME_TRAVEL_NOT_SUPPORTED: Time travel is not supported for streaming table deep clone.
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Cause

Streaming tables maintain their data as a continuous stream of changes. The deep clone operation for streaming tables only supports cloning the current state of the table — it cannot clone a historical snapshot of the table at a specific point in time.^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

Attempting to use a time travel syntax (e.g., specifying a version via `VERSION AS OF` or a timestamp via `TIMESTAMP AS OF`) in a `CREATE OR REPLACE TABLE ... DEEP CLONE` statement on a streaming table triggers this error.

## Solution

Remove the time travel specification from the deep clone statement. The deep clone will clone the current state of the streaming table.^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

For example, instead of:

```sql
CREATE OR REPLACE TABLE target_table
DEEP CLONE source_streaming_table VERSION AS OF 5;
```

Use:

```sql
CREATE OR REPLACE TABLE target_table
DEEP CLONE source_streaming_table;
```

## Related Concepts

- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR — The parent error class for this sub-error
- [Deep Clone](/concepts/deep-clone.md) — The operation that fails when combined with time travel on streaming tables
- Streaming tables — The type of table that does not support time travel during deep clone
- [Time travel](/concepts/delta-lake-time-travel.md) — The Delta Lake feature that is not supported in this context
- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR#LOCATION_NOT_SUPPORTED — Related sub-error for location specification
- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR#OLD_ARCHITECTURE_NOT_SUPPORTED — Related sub-error for old architecture
- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR|DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR#REQUIRES_WITH_HISTORY — Related sub-error for history requirement
- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR#SCHEDULED_TABLE_NOT_SUPPORTED — Related sub-error for scheduled tables

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
