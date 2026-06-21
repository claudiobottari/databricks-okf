---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55e96e03dfa03a2d1a435f6a2aa4f0ff2e1667d14fa22a26d5b607f7f50bbdbb
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-clone-limitations-for-streaming-tables
    - DCLFST
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Deep Clone Limitations for Streaming Tables
description: Streaming tables have specific restrictions when used as the source of a deep clone operation
tags:
  - delta-lake
  - streaming-tables
  - deep-clone
  - databricks
timestamp: "2026-06-19T15:04:01.471Z"
---

# Deep Clone Limitations for Streaming Tables

**Deep Clone Limitations for Streaming Tables** refers to the restrictions and error conditions that apply when attempting to use the `DEEP CLONE` operation on streaming tables in Databricks. Deep cloning a streaming table has several specific limitations that trigger the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Overview

When a deep clone operation fails on a streaming table, the system returns a `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` with SQLSTATE `0A000` (feature not supported). This error can contain one of several sub-conditions that identify the specific limitation encountered. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Specific Limitations

### LOCATION_NOT_SUPPORTED

Specifying a `LOCATION` is not supported when deep cloning a streaming table. The cloned streaming table uses managed storage instead. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### OLD_ARCHITECTURE_NOT_SUPPORTED

Only streaming tables using the default publishing mode are supported for deep clone operations. Streaming tables using older or non-default publishing architectures will fail. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### REQUIRES_WITH_HISTORY

The `WITH HISTORY` clause is required when performing a deep clone on a streaming table. The correct syntax is:

```sql
CREATE TABLE ... DEEP CLONE ... WITH HISTORY
```

Omitting `WITH HISTORY` will trigger this error. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### SCHEDULED_TABLE_NOT_SUPPORTED

Scheduled streaming tables cannot be deep cloned. This operation is not supported for tables that have been configured with a schedule. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### TIME_TRAVEL_NOT_SUPPORTED

[Time Travel](/concepts/delta-lake-time-travel.md) is not supported for streaming table deep clone operations. Deep cloning always operates on the current state of the streaming table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — The general operation for creating a deep copy of a Delta table.
- Streaming Tables — Tables that are continuously updated from streaming data sources.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage layer for Delta tables.
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) — Table storage managed by the Databricks [Metastore](/concepts/metastore.md).
- [Time Travel](/concepts/delta-lake-time-travel.md) — Delta Lake feature for accessing previous versions of a table.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
