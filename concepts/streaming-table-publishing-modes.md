---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a522e73c0f5f7b36ab6341dcb7093f61f7a40ebee803b866c22f533577f3798d
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - streaming-table-publishing-modes
    - STPM
    - Publishing Mode
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Streaming Table Publishing Modes
description: Different publishing modes for streaming tables in Databricks, where only the default mode supports deep clone operations
tags:
  - databricks
  - streaming
  - delta-live-tables
timestamp: "2026-06-18T15:18:43.777Z"
---

# Streaming Table Publishing Modes

**Streaming Table Publishing Modes** refer to the different methods by which Streaming Tables in Databricks make their data available for querying and downstream processing. The publishing mode determines how table metadata and data files are committed, which affects query consistency, performance, and compatibility with operations like [Deep Clone](/concepts/deep-clone.md).

## Default Publishing Mode

Only streaming tables using the **default publishing mode** are supported for deep clone operations. When attempting to deep clone a streaming table, the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error condition returns `OLD_ARCHITECTURE_NOT_SUPPORTED` if the streaming table does not use the default publishing mode. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Supported Operations by Publishing Mode

### Operations Supported Only on Default Publishing Mode

- **Deep clone with history**: The `WITH HISTORY` clause is required when performing a deep clone on a streaming table (`CREATE TABLE ... DEEP CLONE ... WITH HISTORY`). Without this clause, the `REQUIRES_WITH_HISTORY` sub-error is raised. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Operations Not Supported on Any Streaming Table Publishing Mode

The following operations are not supported for streaming tables regardless of publishing mode:

- **Custom location specification**: Specifying a `LOCATION` is not supported. The cloned streaming table uses managed storage. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]
- **Scheduled streaming tables**: Deep clone does not support scheduled streaming tables. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]
- **Time travel**: Time travel queries are not supported for streaming table deep clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Conditions Related to Publishing Modes

When performing unsupported operations on streaming tables with non-default publishing modes, the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class is returned with the `OLD_ARCHITECTURE_NOT_SUPPORTED` sub-error. This indicates that only streaming tables using the default publishing mode are eligible for deep clone operations. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- Streaming Tables — Tables that are continuously updated from streaming data sources
- [Deep Clone](/concepts/deep-clone.md) — Operation to create a full copy of a Delta table including its history
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) — Databricks-managed storage locations for tables
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for streaming tables
- [Error Handling in Databricks](/concepts/error-handling-in-databricks-notebook-workflows.md) — General guidance on resolving Databricks error conditions

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
