---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7aa5de6220330f08c27a731963ab1212af1571ca1c5b5a5ed8e4b9d4af85216d
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-clone-with-history-operation
    - DCWHO
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: Delta CLONE with history operation
description: A Delta Lake operation that clones a table including its full version history, which has restrictions on supported source types and time travel methods
tags:
  - databricks
  - delta-lake
  - clone-operation
timestamp: "2026-06-19T18:22:36.556Z"
---

# Delta CLONE with history operation

The **Delta CLONE with history operation** (`CLONE WITH HISTORY`) is a feature of the [Delta Lake](/concepts/delta-lake.md) `CLONE` command that creates a shallow or deep copy of a Delta table and preserves the full version history of the source table. When an attempt is made to run a `CLONE WITH HISTORY` on an unsupported source, the system raises the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error condition: `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`

This error is classified under SQLSTATE `0AKDC` (Feature not supported). It occurs when the source table for a `CLONE WITH HISTORY` operation cannot be used as the source for cloning with history. The error message includes a sub‑reason that identifies the specific unsupported scenario. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### `NON_DELTA`

The source table is not a Delta table. `CLONE WITH HISTORY` requires the source to be a [Delta table](/concepts/delta-lake-table.md). If the source is stored in another format (for example, Parquet, CSV, or JSON), the operation fails with:

> Source table of `<format>` format is not supported.

### `TIME_TRAVELLED_BY_TIMESTAMP`

The source table was accessed with [time travel](/concepts/delta-lake-time-travel.md) using a timestamp rather than a version number. Cloning with history from a time‑travelled snapshot identified by timestamp is not supported. The error message states:

> Source table time travelled by timestamp is not supported.

## Related concepts

- CLONE command – The general SQL command for cloning Delta tables.
- [Delta Lake](/concepts/delta-lake.md) – The storage format required for `CLONE WITH HISTORY`.
- [Time travel](/concepts/delta-lake-time-travel.md) – Allows reading older versions of a Delta table, but timestamp‑based travel is not compatible with `CLONE WITH HISTORY`.
- Error classes in Databricks – A broader reference for error conditions.

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
