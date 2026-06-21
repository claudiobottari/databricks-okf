---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 180aa329bfd0839ebf7f6170e5464cea14994d7d700eb27982c8597c0d22a5d3
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-table-managed-storage-location-restriction
    - STMSLR
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Streaming Table Managed Storage Location Restriction
description: Specifying a custom LOCATION when deep cloning a streaming table is not supported because the cloned table uses managed storage
tags:
  - delta-lake
  - streaming-tables
  - storage
  - databricks
timestamp: "2026-06-19T15:04:09.516Z"
---

# Streaming Table Managed Storage Location Restriction

**Streaming Table Managed Storage Location Restriction** refers to the error condition `LOCATION_NOT_SUPPORTED` that occurs when attempting to perform a deep clone operation on a streaming table that uses managed storage.

## Error Overview

When running `CREATE TABLE ... DEEP CLONE` on a streaming table, the operation fails with the error:

```
DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR: LOCATION_NOT_SUPPORTED
```

The full SQLSTATE code for this error is `0A000` (Feature Not Supported). ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Details

The error occurs with the sub-message:

> Specifying a `LOCATION` is not supported. The cloned streaming table uses managed storage.

This means that when you attempt to clone a streaming table that uses [managed storage](/concepts/managed-storage-location.md) (where Databricks manages the data location), you cannot specify a custom `LOCATION` for the cloned table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Cause

The restriction applies specifically to streaming tables that use **managed storage** rather than external storage. When a streaming table is created with managed storage, Databricks controls the underlying data directory. Specifying a `LOCATION` in a deep clone operation is incompatible with this managed storage model. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Resolution

To avoid this error, do not specify a `LOCATION` when deep cloning a streaming table that uses managed storage. Instead, use the `WITH HISTORY` clause as required by the `REQUIRES_WITH_HISTORY` sub-condition, which states:

> `WITH HISTORY` is required. Use `CREATE TABLE ... DEEP CLONE ... WITH HISTORY`.

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Error Conditions

This error is part of a family of DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR conditions that apply to streaming table deep clones:

- **OLD_ARCHITECTURE_NOT_SUPPORTED**: Only streaming tables using the default publishing mode are supported
- **REQUIRES_WITH_HISTORY**: `WITH HISTORY` clause is mandatory
- **SCHEDULED_TABLE_NOT_SUPPORTED**: Scheduled streaming tables cannot be deep cloned
- **TIME_TRAVEL_NOT_SUPPORTED**: Time travel queries are not supported for streaming table deep clones

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- Streaming tables – [Delta Lake](/concepts/delta-lake.md) tables that continuously ingest data
- [Managed storage](/concepts/managed-storage-location.md) – Storage where Databricks manages the data location
- [Deep Clone](/concepts/deep-clone.md) – A complete copy of a Delta table including its history
- SQLSTATE codes – Standardized error classification for database operations

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
