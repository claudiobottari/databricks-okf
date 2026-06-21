---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f95232a348f62fdab172fbaa2c5e62428063bf5e8b677f2c87bd86844e9ae52
  pageDirectory: concepts
  sources:
    - delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - with-history-clause-for-deep-clone
    - WHCFDC
    - with-history-clause-for-databricks-deep-clone
    - WHCFDDC
  citations:
    - file: delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md
title: WITH HISTORY Clause for Deep Clone
description: A required clause when performing a deep clone of a streaming table in Databricks to preserve the table's history
tags:
  - databricks
  - delta-lake
  - sql-syntax
timestamp: "2026-06-18T15:18:34.352Z"
---

# WITH HISTORY Clause for Deep Clone

The **`WITH HISTORY` clause** is a required syntactical element when performing a [Deep Clone](/concepts/deep-clone.md) of a Streaming Table. Omitting this clause causes the `DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR` error class with the sub‑error `REQUIRES_WITH_HISTORY`. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Error Condition

If a deep clone operation on a streaming table is attempted without `WITH HISTORY`, the following error is raised:

```
DELTA_DEEP_CLONE_STREAMING_TABLE_ERROR
REQUIRES_WITH_HISTORY
```

The error message states: `WITH HISTORY is required. Use CREATE TABLE ... DEEP CLONE ... WITH HISTORY.` ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Required Syntax

To successfully deep clone a streaming table, the `WITH HISTORY` clause must be appended to the standard deep clone syntax:

```sql
CREATE TABLE target_table DEEP CLONE source_streaming_table WITH HISTORY;
```

Without this clause, the operation fails with the error described above. ^[delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) – General mechanism for creating an independent copy of a Delta table.
- Streaming Table – A table that is continuously populated by a streaming query.
- [CREATE TABLE ... DEEP CLONE](/concepts/create-table-clone-syntax.md) – The full DDL statement for deep cloning.
- [Delta Sharing](/concepts/delta-sharing.md) – Another method for sharing table snapshots (not related to deep clone but often compared).

## Sources

- delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md

# Citations

1. [delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws.md](/references/delta_deep_clone_streaming_table_error-error-condition-databricks-on-aws-0f9a5f3c.md)
