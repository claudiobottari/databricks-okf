---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 160904d5dd13a07e01f6bff4e060709324079a67582e91772a95e84774d6410d
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - location_not_supported
    - LOCATION_NOT_SUPPORTED
    - PROJECTION_NOT_SUPPORTED
    - Location Not Supported for Streaming Table Deep Clone
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: LOCATION_NOT_SUPPORTED
description: Sub-error indicating that specifying a LOCATION is not supported when deep cloning a streaming table because the cloned table uses managed storage.
tags:
  - error
  - databricks
  - delta-lake
  - streaming
timestamp: "2026-06-19T18:24:06.860Z"
---

# LOCATION_NOT_SUPPORTED

The **LOCATION_NOT_SUPPORTED** error is a sub‑condition of the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class. It occurs when a user attempts to perform a deep clone of a streaming table and specifies a `LOCATION` clause. The error message reads: “Specifying a `LOCATION` is not supported. The cloned streaming table uses managed storage.” ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Cause

A deep clone of a streaming table always produces a managed table. Because managed tables store their data in the metastore‑defined location, they do not accept an explicit `LOCATION` path. The error fires when the user provides a `LOCATION` option in the `CREATE OR REPLACE TABLE … DEEP CLONE` statement, which is incompatible with the managed storage requirement. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Solution

Remove the `LOCATION` clause from the deep clone statement. The cloned streaming table will automatically use the default managed storage location configured for the catalog or schema. If an external location is required, consider an alternative approach such as [Deep Clone](/concepts/deep-clone.md) of a non‑streaming table or using external tables with [managed storage](/concepts/managed-storage-location.md) rules. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Error Sub‑conditions

The `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` class includes several other sub‑conditions:

| Sub‑condition | Description |
|---|---|
| OLD_ARCHITECTURE_NOT_SUPPORTED | Only streaming tables using the default publishing mode are supported. |
| REQUIRES_WITH_HISTORY | `WITH HISTORY` is required. Use `CREATE TABLE … DEEP CLONE … WITH HISTORY`. |
| SCHEDULED_TABLE_NOT_SUPPORTED | Scheduled streaming tables are not supported for deep clone. |
| TIME_TRAVEL_NOT_SUPPORTED | Time travel is not supported for streaming table deep clone. |

## Related Concepts

- Streaming Tables – Delta tables that ingest data incrementally from a streaming source.
- [Deep Clone](/concepts/deep-clone.md) – A full copy of a Delta table including its data and metadata.
- [Managed vs. External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) – Managed tables use metastore‑managed storage; external tables point to user‑specified locations.
- Delta Lake Error Classes – The structured error classification used by Databricks.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
