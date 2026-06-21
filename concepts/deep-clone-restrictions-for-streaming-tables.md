---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f32aaf226bd8645aae4aff2d181e246865a96779289546003bbde817f8c7f6b0
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-clone-restrictions-for-streaming-tables
    - DCRFST
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Deep clone restrictions for streaming tables
description: "Databricks imposes multiple restrictions on deep cloning streaming tables: no custom LOCATION, only default publishing mode, WITH HISTORY required, no scheduled tables, no time travel."
tags:
  - delta-lake
  - streaming
  - databricks
timestamp: "2026-06-18T11:52:46.984Z"
---

# Deep Clone Restrictions for Streaming Tables

**Deep clone** is not supported for streaming tables in Delta Lake. Attempting to perform a `CREATE OR REPLACE TABLE ... DEEP CLONE` on a streaming table raises the error class `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` (SQLSTATE: 0A000 — feature not supported). The error message includes a sub‑reason that identifies which restriction was violated. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Supported Architecture Only

Only streaming tables that use the **default publishing mode** are eligible for deep clone. If the table was created with a non‑default architecture, the operation fails with:

```
OLD_ARCHITECTURE_NOT_SUPPORTED
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Managed Storage Location Must Not Be Overridden

You cannot specify a `LOCATION` clause when cloning a streaming table. The cloned table inherits the managed storage location of the source. An explicit location produces:

```
LOCATION_NOT_SUPPORTED
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## `WITH HISTORY` Is Required

When cloning a streaming table, the `WITH HISTORY` clause **must** be included in the `CREATE TABLE ... DEEP CLONE` statement. Omitting it results in:

```
REQUIRES_WITH_HISTORY
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Scheduled Streaming Tables Not Supported

A streaming table that is configured with a **schedule** (for example, a refresh schedule) cannot be deeply cloned. Attempting to do so raises:

```
SCHEDULED_TABLE_NOT_SUPPORTED
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Time Travel Not Supported

Using a **time‑travel** version or timestamp in the `DEEP CLONE` statement is not allowed for streaming tables. The error raised is:

```
TIME_TRAVEL_NOT_SUPPORTED
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Summary of Restrictions

| Restriction | Error Sub‑reason | Details |
|-------------|------------------|---------|
| Non‑default publishing mode | `OLD_ARCHITECTURE_NOT_SUPPORTED` | Only default publish mode is supported. |
| Explicit `LOCATION` | `LOCATION_NOT_SUPPORTED` | Managed storage location cannot be overridden. |
| Missing `WITH HISTORY` | `REQUIRES_WITH_HISTORY` | The `WITH HISTORY` clause is mandatory. |
| Scheduled streaming table | `SCHEDULED_TABLE_NOT_SUPPORTED` | Tables with a schedule cannot be cloned. |
| Time travel | `TIME_TRAVEL_NOT_SUPPORTED` | Version / timestamp references are not allowed. |

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — The Delta Lake operation used to create a full copy of a table including its history.
- Streaming Tables — Delta Lake tables that are populated incrementally from streaming sources.
- Delta Lake Publishing Modes — How streaming table changes are committed (default vs. other modes).
- [Time Travel](/concepts/delta-lake-time-travel.md) — Querying or cloning previous versions of a Delta table.
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) — Storage that is managed by Unity Catalog or the [Metastore](/concepts/metastore.md).

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
