---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a88916e027051335ee549a9e276cf289d8325558b677c7f8c76a5304e0afb83
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - deep-clone-restrictions-on-streaming-tables
    - DCROST
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Deep Clone Restrictions on Streaming Tables
description: A set of constraints preventing deep clone operations on Delta streaming tables, including location, architecture, history, scheduling, and time travel limitations.
tags:
  - delta-lake
  - streaming-tables
  - databricks
timestamp: "2026-06-19T10:04:46.078Z"
---

# Deep Clone Restrictions on Streaming Tables

The **Deep Clone Restrictions on Streaming Tables** error class (`DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR`) occurs when an attempt is made to deep clone a streaming table using [Delta Lake](/concepts/delta-lake.md) operations that are not supported for that table type. The error has SQLSTATE `0A000` (feature not supported). This page documents each specific restriction and the workaround required. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Overview

[Deep Clone](/concepts/deep-clone.md) is a Delta Lake operation that creates a copy of a table including its data and metadata. When applied to streaming tables, several constraints apply. The following error sub-conditions may be raised depending on the table configuration and the syntax used.

## Restrictions

### LOCATION_NOT_SUPPORTED

Specifying a `LOCATION` clause in the `DEEP CLONE` command is not supported for streaming tables. The cloned streaming table must use [managed storage](/concepts/managed-storage-location.md); an explicit location path cannot be provided. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### OLD_ARCHITECTURE_NOT_SUPPORTED

Only streaming tables that use the **default publishing mode** are supported for deep clone. Streaming tables configured with an older publishing architecture cannot be deep cloned. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### REQUIRES_WITH_HISTORY

Deep cloning a streaming table requires the `WITH HISTORY` clause. The correct syntax is:

```sql
CREATE TABLE <target> DEEP CLONE <source> WITH HISTORY
```

Omitting `WITH HISTORY` causes this error. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### SCHEDULED_TABLE_NOT_SUPPORTED

Scheduled streaming tables — those that automatically refresh on a schedule — are **not** supported for deep clone. Attempting to deep clone a scheduled streaming table raises this error. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### TIME_TRAVEL_NOT_SUPPORTED

[Time travel](/concepts/delta-lake-time-travel.md) is not supported for deep clone operations on streaming tables. You cannot specify a version or timestamp to clone a previous state of a streaming table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Summary Table

| Error Sub-Condition | Restriction | Required Action |
|---------------------|-------------|-----------------|
| `LOCATION_NOT_SUPPORTED` | `LOCATION` clause not allowed | Remove `LOCATION`; use managed storage |
| `OLD_ARCHITECTURE_NOT_SUPPORTED` | Non-default publishing mode | Use default publishing mode |
| `REQUIRES_WITH_HISTORY` | `WITH HISTORY` missing | Add `WITH HISTORY` to `DEEP CLONE` statement |
| `SCHEDULED_TABLE_NOT_SUPPORTED` | Scheduled streaming table | Do not deep clone scheduled tables |
| `TIME_TRAVEL_NOT_SUPPORTED` | Time travel syntax used | Remove version/timestamp specification |

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) — The Delta Lake operation being restricted
- Streaming Tables — The table type subject to these restrictions
- Delta Lake Managed Storage — Required storage model for cloned streaming tables
- Time Travel in Delta Lake — Feature not available for streaming table deep clones
- Scheduled Tables — Additional restriction for auto-refreshing streaming tables
- SQLSTATE 0A000 — Feature not supported error class

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
