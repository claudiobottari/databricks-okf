---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1990d9cdb7a433c86a43d6e5ba9bbd68dca59eb927716ab5a3dfb8d8ef929b38
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - requires_with_history
    - REQUIRES_WITH_HISTORY
    - requires_with_history-sub-error
    - REQUIRES_WITH_HISTORY sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: REQUIRES_WITH_HISTORY
description: Sub-error indicating that the WITH HISTORY clause is required when performing a DEEP CLONE on a streaming table.
tags:
  - error
  - databricks
  - delta-lake
  - streaming
  - syntax
timestamp: "2026-06-19T18:24:09.995Z"
---

# REQUIRES_WITH_HISTORY

**REQUIRES_WITH_HISTORY** is an error condition that occurs when attempting to perform a deep clone operation on a streaming table in Databricks without including the `WITH HISTORY` clause. The error indicates that the deep clone syntax is incomplete and must be corrected by adding `WITH HISTORY` to the `CREATE TABLE ... DEEP CLONE` statement. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Details

The `REQUIRES_WITH_HISTORY` condition is part of the DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class, which has SQLSTATE 0A000 (feature not supported). This error specifically applies to deep clone operations on streaming tables. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, include the `WITH HISTORY` clause in the deep clone statement. The correct syntax is:

```sql
CREATE TABLE <target_table> DEEP CLONE <source_table> WITH HISTORY
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Context

Deep clone creates a fresh copy of a Delta table, including its data and metadata. For streaming tables, the `WITH HISTORY` clause preserves the change data feed and streaming metadata in the cloned table, which is necessary for the clone to function as a streaming table. Without this clause, Databricks cannot properly replicate the streaming table's metadata. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR — The parent error class containing the `REQUIRES_WITH_HISTORY` condition
- Streaming Tables — The table type affected by this error
- [Deep Clone](/concepts/deep-clone.md) — The operation being performed
- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying these operations
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The metadata that `WITH HISTORY` preserves during cloning

## Related Error Conditions

The `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class also includes these related conditions:

- LOCATION_NOT_SUPPORTED — Specifying a `LOCATION` is not supported for streaming table deep clones
- OLD_ARCHITECTURE_NOT_SUPPORTED — Only streaming tables using the default publishing mode are supported
- SCHEDULED_TABLE_NOT_SUPPORTED — Scheduled streaming tables are not supported for deep clone
- TIME_TRAVEL_NOT_SUPPORTED — Time travel is not supported for streaming table deep clone

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
