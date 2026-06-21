---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f8d91ec0c93b20c89acde7f6f089e0c6703011df082e954ba31515ca07ac483
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-travel-unsupported-on-streaming-table-deep-clones
    - TTUOSTDC
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Time travel unsupported on streaming table deep clones
description: Time travel queries cannot be used in conjunction with deep clone operations on streaming tables in Databricks.
tags:
  - delta-lake
  - time-travel
  - streaming
timestamp: "2026-06-18T11:53:07.651Z"
---

# Time Travel Unsupported on Streaming Table Deep Clones

**Time travel unsupported on streaming table deep clones** is an error condition that occurs when attempting to perform a time travel query on a [Deep Clone](/concepts/deep-clone.md) of a streaming table in Databricks. The operation fails because streaming table deep clones do not support time travel capabilities.

## Error Details

When you attempt to use time travel (e.g., `VERSION AS OF` or `TIMESTAMP AS OF`) on a deep clone of a streaming table, Databricks returns the following error:

**SQLSTATE: 0A000** — Feature not supported

```
TIME_TRAVEL_NOT_SUPPORTED: Time travel is not supported for streaming table deep clone.
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Root Cause

Streaming tables use a different storage architecture than regular [Delta tables](/concepts/delta-lake-table.md). When you create a deep clone of a streaming table, the clone inherits the streaming table's managed storage and publishing mode properties. The time travel feature, which allows querying historical versions of data, relies on the data versioning history maintained by [Delta Lake](/concepts/delta-lake.md). Deep clones of streaming tables do not maintain this full version history, making time travel operations unsupported. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Affected Scenario

The error triggers specifically when:

- You create a deep clone of a streaming table
- You then attempt to query the clone using time travel syntax (e.g., `SELECT * FROM clone VERSION AS OF <timestamp>`)

The operation fails because the deep clone process does not preserve the streaming table's version history in a way that supports time travel queries. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Error Conditions

This error is part of the broader DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class, which includes other unsupported operations on streaming table deep clones:

| Error | Description |
|-------|-------------|
| LOCATION_NOT_SUPPORTED | Specifying a `LOCATION` is not supported | 
| OLD_ARCHITECTURE_NOT_SUPPORTED | Only streaming tables using the default publishing mode are supported |
| REQUIRES_WITH_HISTORY | `WITH HISTORY` is required for deep clone |
| SCHEDULED_TABLE_NOT_SUPPORTED | Scheduled streaming tables are not supported |
| **TIME_TRAVEL_NOT_SUPPORTED** | Time travel is not supported |

## Workaround

If you need historical data access from a streaming table, consider these alternatives:

- Use `CREATE TABLE ... DEEP CLONE ... WITH HISTORY` to preserve the change history in the clone, though time travel still may not work on streaming tables.
- Query the original source streaming table directly with time travel instead of using a deep clone.
- Use a [Shallow Clone](/concepts/shallow-clone.md) instead of a deep clone, which may support time travel depending on the source table's properties.

## Related Concepts

- Streaming Tables — Tables that continuously ingest data from streams
- [Deep Clone](/concepts/deep-clone.md) — A full copy of a table including data files
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) — The ability to query historical versions of Delta tables
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) — Storage location managed by Databricks for streaming tables

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
