---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 465714fe1b199a141c8333228145dc2881f099948d4f70f77f4821794633fb7b
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - with-history-requirement-for-deep-clone-of-streaming-tables
    - WHRFDCOST
    - WITH HISTORY Requirement
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: With History Requirement for Deep Clone of Streaming Tables
description: The WITH HISTORY clause is required when performing a DEEP CLONE on a streaming table
tags:
  - delta-lake
  - streaming-tables
  - deep-clone
  - with-history
timestamp: "2026-06-19T15:04:09.855Z"
---

## With History Requirement for Deep Clone of Streaming Tables

The **With History Requirement for Deep Clone of Streaming Tables** is an error condition that occurs when attempting to perform a deep clone of a streaming table without including the `WITH HISTORY` clause. The error is raised as `REQUIRES_WITH_HISTORY` in the class `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR`. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Error Details

When a deep clone of a streaming table is attempted and the `WITH HISTORY` clause is omitted, the system returns the following error message:

```
WITH HISTORY is required. Use `CREATE TABLE ... DEEP CLONE ... WITH HISTORY`.
```

The error has SQLSTATE `0A000` (feature not supported). ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Cause

[Deep Clone](/concepts/deep-clone.md) of a Streaming Table on Databricks must preserve the table’s history metadata — including change data feed and streaming-related metadata — to maintain the table’s ability to process incremental data. The `WITH HISTORY` clause explicitly tells the system to copy that metadata. If the clause is omitted, the system cannot guarantee a valid streaming table clone and raises the error. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Solution

Include the `WITH HISTORY` clause in the deep clone statement. The correct syntax is:

```sql
CREATE TABLE target_table DEEP CLONE source_streaming_table WITH HISTORY;
```

This instructs the deep clone operation to retain the streaming history metadata required for the cloned table to function as a streaming table. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Related Error Conditions

The `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` class also includes other subconditions that may arise when deep cloning streaming tables:

- `LOCATION_NOT_SUPPORTED` – Specifying a custom `LOCATION` is not supported because the clone uses managed storage.
- `OLD_ARCHITECTURE_NOT_SUPPORTED` – Only streaming tables using the default publishing mode are eligible.
- `SCHEDULED_TABLE_NOT_SUPPORTED` – Scheduled streaming tables cannot be deep cloned.
- `TIME_TRAVEL_NOT_SUPPORTED` – Time travel is not supported for streaming table deep clones.

These conditions are mutually exclusive; only one may appear per failed operation. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

### Related Concepts

- [Deep Clone](/concepts/deep-clone.md) – A command that creates a full, independent copy of a Delta table including its data and metadata.
- Streaming Table – A Delta table that is maintained incrementally by a streaming query.
- [CREATE TABLE ... DEEP CLONE](/concepts/create-table-clone-syntax.md) – The SQL syntax for deep cloning.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – A feature that tracks row-level changes in a Delta table; relevant for streaming table history.
- SQLSTATE 0A000 – The SQL standard error class for feature not supported.

### Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
