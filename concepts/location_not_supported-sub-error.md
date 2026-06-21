---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 411ebe5ce7f32b49975aa3e9973d89ac430e75caaf5bab4c5a9571f6d02ecbb5
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - location_not_supported-sub-error
    - LOCATION_NOT_SUPPORTED sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: LOCATION_NOT_SUPPORTED sub-error
description: Sub-error of DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR indicating that specifying a custom LOCATION is forbidden because the cloned streaming table uses managed storage.
tags:
  - error-messages
  - delta-lake
  - managed-storage
timestamp: "2026-06-19T10:04:51.091Z"
---

# LOCATION_NOT_SUPPORTED sub-error

**LOCATION_NOT_SUPPORTED** is a sub-error of the DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class (SQLSTATE: 0A000, feature not supported). It occurs when a user attempts to deep clone a streaming table and specifies an explicit `LOCATION` clause. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Cause

The error is raised because the cloned streaming table uses [managed storage](/concepts/managed-storage-location.md), and specifying a separate `LOCATION` is not supported in that scenario. The streaming table’s data is already governed by the catalog’s managed storage location, so an external path cannot be assigned to the clone. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Resolution

To avoid the error, omit the `LOCATION` clause when performing a deep clone of a streaming table. The clone will inherit the managed storage location of the source table.

## Related sub-errors

The `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` class includes several other sub-errors that may occur in similar contexts:

- **OLD_ARCHITECTURE_NOT_SUPPORTED** – Only streaming tables using the default publishing mode are supported.
- **REQUIRES_WITH_HISTORY** – The `WITH HISTORY` clause is required when deep cloning a streaming table.
- **SCHEDULED_TABLE_NOT_SUPPORTED** – Scheduled streaming tables cannot be deep cloned.
- **TIME_TRAVEL_NOT_SUPPORTED** – Time travel queries are not supported for deep clone of a streaming table.

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related concepts

- [Deep Clone](/concepts/deep-clone.md) – The operation that triggers this error.
- Streaming Table – The type of table being cloned.
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) – The storage model that prevents an explicit `LOCATION`.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
