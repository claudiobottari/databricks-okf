---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50b802dde48986f51813a71cd482eab99fc2b9db7a143a248a149406dd423c17
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-travel-on-streaming-tables
    - TTOST
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Time Travel on Streaming Tables
description: The ability to query historical versions of a streaming table, which is not supported when performing deep clone operations
tags:
  - databricks
  - delta-lake
  - time-travel
timestamp: "2026-06-18T15:19:07.483Z"
---

# Time Travel on Streaming Tables

**Time Travel on Streaming Tables** refers to the ability to query or clone a Streaming Table at a previous point in time using [Delta Time Travel](/concepts/delta-lake-time-travel.md). As of the current Databricks documentation, this capability is explicitly **not supported** in the context of performing a deep clone of a streaming table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Limitation

When attempting a `DEEP CLONE` of a streaming table, Delta Lake raises the error condition `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` with the reason `TIME_TRAVEL_NOT_SUPPORTED`. The full error message states:

> Time travel is not supported for streaming table deep clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

This restriction applies only to streaming tables that use the default publishing mode. Deep cloning a streaming table with an explicit time-travel specification (e.g., using `VERSION AS OF` or `TIMESTAMP AS OF`) will fail. The operation requires the `WITH HISTORY` clause if you wish to preserve the streaming table's history, but even with history, time-travel targeting a specific version or timestamp is disallowed. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Error Condition

The `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class includes several sub-errors:

| Sub-error | Description |
|-----------|-------------|
| `LOCATION_NOT_SUPPORTED` | Specifying a custom `LOCATION` is not allowed; the cloned table uses managed storage only. |
| `OLD_ARCHITECTURE_NOT_SUPPORTED` | Only streaming tables using the default publishing mode are supported. |
| `REQUIRES_WITH_HISTORY` | Deep clone of a streaming table without `WITH HISTORY` fails. |
| `SCHEDULED_TABLE_NOT_SUPPORTED` | Scheduled streaming tables cannot be deep cloned. |
| `TIME_TRAVEL_NOT_SUPPORTED` | Time-travel is not supported for streaming table deep clone. |

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Workaround

If you need to create a copy of a streaming table at a specific historical version, consider alternative approaches such as:

- Using a batch `CREATE OR REPLACE TABLE` with time travel on a non-streaming copy of the data.
- Materializing the streaming table to a static table first, then performing a deep clone with time travel.
- Accepting the deep clone without `VERSION AS OF`, which copies only the current state of the streaming table.

Note that these workarounds are inferred from general Delta Lake practices; the source material does not provide explicit guidance.

## Related Concepts

- Streaming Tables — Continuous ingestion tables that are maintained by Delta Live Tables.
- [Deep Clone](/concepts/deep-clone.md) — A Delta Lake operation that creates a full copy of a table, including its data and metadata.
- [Delta Time Travel](/concepts/delta-lake-time-travel.md) — The ability to query, restore, or clone a Delta table at a previous version.
- Delta Live Tables — The framework that manages streaming tables in Databricks.
- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR — The full error class for deep clone failures on streaming tables.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
