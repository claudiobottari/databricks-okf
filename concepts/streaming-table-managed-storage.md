---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 959038b03ecce46d94aacac8111f1e6b76917a9016eef303cb85a01ffae71a0a
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-table-managed-storage
    - STMS
    - streaming-table-managed-storage-location-restriction
    - STMSLR
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: Streaming table managed storage
description: Streaming tables in Databricks use managed storage, preventing specification of a custom LOCATION during deep clone operations.
tags:
  - delta-lake
  - streaming
  - storage
timestamp: "2026-06-18T11:52:50.585Z"
---

# Streaming Table Managed Storage

**Streaming table managed storage** refers to the storage model used by streaming tables in Databricks where the system automatically manages the underlying data location, rather than requiring users to specify an explicit `LOCATION` path. This is the default storage mode for streaming tables created without a user-specified location. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Overview

When a streaming table uses managed storage, Databricks handles the physical data placement within the [Unity Catalog](/concepts/unity-catalog.md) managed storage location. This simplifies table creation and management by removing the need for users to specify and maintain external storage paths. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Impact on Operations

### Deep Clone Limitations

Streaming tables that use managed storage have specific constraints when performing deep clone operations. The `LOCATION_NOT_SUPPORTED` error occurs when attempting to specify a `LOCATION` during a deep clone of a streaming table that uses managed storage. This is because the cloned streaming table inherits the managed storage model and cannot be redirected to an external location. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Supported Operations

Deep clone operations on streaming tables with managed storage are supported only under the following conditions: ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

- The streaming table must use the default publishing mode (not an older architecture).
- The `WITH HISTORY` clause is required when performing a deep clone.
- Scheduled streaming tables are not supported for deep clone.
- Time travel is not supported for streaming table deep clone operations.

## Related Concepts

- Streaming Tables — Tables that continuously ingest and process streaming data
- [Managed Storage](/concepts/managed-storage-in-unity-catalog.md) — Storage locations managed by Unity Catalog
- [Deep Clone](/concepts/deep-clone.md) — A full copy of a Delta table including data and metadata
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for streaming tables
- Unity Catalog Managed Storage — The system-managed storage locations in Unity Catalog

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
