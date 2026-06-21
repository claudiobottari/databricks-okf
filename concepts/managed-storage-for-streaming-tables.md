---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0050cd8db86246cd65837d50a44ca4f9c012863591cf672e874a5e92bf748e6
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-storage-for-streaming-tables
    - MSFST
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Managed Storage for Streaming Tables
description: Databricks-managed storage location for streaming tables, where users cannot specify a custom LOCATION during deep clone
tags:
  - databricks
  - storage
  - delta-lake
timestamp: "2026-06-18T15:19:01.926Z"
---

# Managed Storage for Streaming Tables

**Managed Storage for Streaming Tables** refers to the storage architecture within Databricks where a streaming table's data is fully managed by the system, rather than being stored at a user-specified external location. This architecture has important implications for operations like deep cloning and other data management tasks.

## Overview

When a streaming table uses managed storage, its data is stored in a location controlled by the Databricks system rather than at a user-specified `LOCATION` path. This managed storage model affects which operations can be performed on the table, particularly when attempting to create deep clones. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Implications for Deep Clone Operations

[Deep cloning](/concepts/deep-clone.md) of a streaming table that uses managed storage may fail under certain conditions, returning a `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error. The error includes specific subtypes that provide additional detail about why the operation failed. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### LOCATION_NOT_SUPPORTED

Specifying a `LOCATION` is not supported when deep cloning a streaming table that uses managed storage. The cloned streaming table must continue to use managed storage, and cannot be redirected to an external storage location through the `LOCATION` parameter. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Other Supported Operations

The following operations are supported on managed storage streaming tables, with specific requirements:

- **WITH HISTORY**: When performing a deep clone, the `WITH HISTORY` clause is required. The correct syntax is `CREATE TABLE ... DEEP CLONE ... WITH HISTORY`. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

- **Default Publishing Mode**: Only streaming tables using the default publishing mode are supported for deep clone operations. Tables using alternative publishing architectures will receive an `OLD_ARCHITECTURE_NOT_SUPPORTED` error. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Unsupported Operations

The following operations are not supported for managed storage streaming tables:

- **Scheduled Streaming Tables**: [Scheduled Streaming Tables](/concepts/scheduled-streaming-tables.md) are not supported for deep clone operations. These tables are on a schedule and cannot be deep cloned. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

- **Time Travel**: [Time travel](/concepts/delta-lake-time-travel.md) operations are not supported for streaming table deep clones. The system cannot access historical versions of the data for the deep clone operation. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- Streaming Tables — Tables that continuously ingest data from streaming sources.
- [Deep Clone](/concepts/deep-clone.md) — A full copy of a Delta table that includes both data and metadata.
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) — Storage where the system manages the data location and lifecycle.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides the foundation for these operations.
- [Publishing Mode](/concepts/streaming-table-publishing-modes.md) — The architecture used to publish streaming data to the table.
- Scheduled Tables — Tables that run on a predefined schedule for data processing.

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
