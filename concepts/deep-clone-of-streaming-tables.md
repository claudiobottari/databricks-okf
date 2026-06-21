---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44fdeee7a62977e65e8e49759a9dd8d4bcbd2200ad75fddf25b4f5378413bcb7
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-clone-of-streaming-tables
    - DCOST
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Deep Clone of Streaming Tables
description: The operation of creating a deep copy of a Delta streaming table, which has specific constraints and requirements in Databricks
tags:
  - databricks
  - delta-lake
  - streaming
  - clone-operations
timestamp: "2026-06-18T15:18:43.999Z"
---

# Deep Clone of Streaming Tables

**Deep Clone of Streaming Tables** refers to the process of creating a full copy (including history) of a Streaming Table in [Delta Lake](/concepts/delta-lake.md) using the `DEEP CLONE` command. This operation is subject to several constraints that, if violated, raise the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class (SQLSTATE: 0A000). ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Overview

A deep clone copies both the data and the metadata of a streaming table. However, due to the continuous, incremental nature of streaming tables, not all features of a standard Delta table deep clone are supported. Attempting to use an unsupported feature causes a feature-not-supported error with one of the following sub‑conditions. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Conditions

Each sub‑condition describes a specific unsupported scenario and, where applicable, the required workaround.

### LOCATION_NOT_SUPPORTED

Specifying a custom `LOCATION` for the cloned streaming table is not supported. The cloned table must use [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) — its location is automatically determined by the [Metastore](/concepts/metastore.md). ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### OLD_ARCHITECTURE_NOT_SUPPORTED

Only streaming tables that use the **default publishing mode** are supported for deep clone. Streaming tables using an older publishing architecture cannot be deep cloned. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### REQUIRES_WITH_HISTORY

A deep clone of a streaming table **must** include the `WITH HISTORY` clause. The correct syntax is: ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

```sql
CREATE TABLE ... DEEP CLONE ... WITH HISTORY
```

Omitting `WITH HISTORY` causes this error.

### SCHEDULED_TABLE_NOT_SUPPORTED

[Scheduled Streaming Tables](/concepts/scheduled-streaming-tables.md) (streaming tables that are refreshed on a schedule) are not eligible for deep clone. The deep clone operation is blocked for any streaming table that has an associated schedule. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### TIME_TRAVEL_NOT_SUPPORTED

[Time Travel](/concepts/delta-lake-time-travel.md) is not supported for streaming table deep clone. You cannot deep clone a streaming table at a specific version or timestamp; only the current state can be cloned. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- Streaming Tables
- [Deep Clone](/concepts/deep-clone.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md)
- [Time Travel](/concepts/delta-lake-time-travel.md)
- [Scheduled Streaming Tables](/concepts/scheduled-streaming-tables.md)
- [CREATE TABLE CLONE Syntax](/concepts/create-table-clone-syntax.md)

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
