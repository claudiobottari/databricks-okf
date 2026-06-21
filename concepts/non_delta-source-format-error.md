---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 469cbf7a953e1cc649562d626f5571defc4357077a2e7a1cb80ac93b8f69025d
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_delta-source-format-error
    - NSFE
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: NON_DELTA source format error
description: A sub-error of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE indicating the source table is not in Delta format, so cloning with history is unsupported.
tags:
  - databricks
  - delta-lake
  - format
timestamp: "2026-06-18T15:17:33.435Z"
---

# NON_DELTA Source Format Error

The **NON_DELTA source format error** occurs when attempting to clone a table using `CLONE WITH HISTORY` (also known as shallow clone with history) and the source table is not in Delta format. The operation requires the source to be a Delta table because history cloning relies on Delta transaction logs. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Message

The error is part of the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error class (SQLSTATE: 0AKDC). The specific sub‑condition is:

```
NON_DELTA: Source table of `<format>` format is not supported.
```

where `<format>` is the actual format of the source table (e.g., `PARQUET`, `CSV`, `JSON`). ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

The `CLONE WITH HISTORY` operation is designed to copy a [Delta table](/concepts/delta-lake-table.md) along with its full version history (transaction log). Non‑Delta sources such as Parquet, CSV, JSON, or external tables in other formats do not have a transaction log, so the history cannot be preserved. Databricks rejects the operation with this error. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Solution

- **Convert the source to Delta format** using a `CONVERT TO DELTA` statement before attempting the history clone. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]
- Alternatively, use a **regular clone** (`CLONE`) without the `WITH HISTORY` clause, which does not require the source to be Delta but also does not preserve the source’s history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [CLONE WITH HISTORY](/concepts/delta-clone-with-history.md) – The operation that triggers this error.
- [Delta table](/concepts/delta-lake-table.md) – The required source format for history cloning.
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – Command to change a non‑Delta table to Delta format.
- [Shallow clone vs. deep clone](/concepts/shallow-clone-delta-lake.md) – Distinction between clone types and history preservation.
- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE – The parent error class, which also includes TIME_TRAVELLED_BY_TIMESTAMP error|TIME_TRAVELLED_BY_TIMESTAMP sub‑condition.

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
