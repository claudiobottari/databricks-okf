---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4dd1e3273fbda6f830baca20d32d2e752855bafb4fe15a29631fd6cd74cef65f
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - requires_with_history-sub-error
    - REQUIRES_WITH_HISTORY sub-error
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: REQUIRES_WITH_HISTORY sub-error
description: Sub-error stating that WITH HISTORY clause is mandatory when performing a deep clone of a streaming table.
tags:
  - error-messages
  - delta-lake
  - clone
timestamp: "2026-06-19T10:04:46.480Z"
---

# REQUIRES_WITH_HISTORY sub-error

The **REQUIRES_WITH_HISTORY** sub-error occurs when attempting to perform a deep clone operation on a streaming table without including the `WITH HISTORY` clause in the command. This is a sub-error of the DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR error class. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, the system returns the following message:

```
WITH HISTORY is required. Use CREATE TABLE ... DEEP CLONE ... WITH HISTORY.
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Cause

The error is triggered when a [Deep Clone](/concepts/deep-clone.md) operation is performed on a streaming table without the mandatory `WITH HISTORY` clause. Deep cloning a streaming table requires explicit inclusion of the history metadata to properly replicate the table's structure and change tracking. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, include the `WITH HISTORY` clause in the deep clone command. The correct syntax is:

```sql
CREATE TABLE <target_table> DEEP CLONE <source_table> WITH HISTORY
```

^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- Streaming Tables — Tables that continuously ingest data from streaming sources
- [Deep Clone](/concepts/deep-clone.md) — A full copy of a Delta table, including data and metadata
- DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR — The parent error class containing this sub-error
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for streaming tables

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
