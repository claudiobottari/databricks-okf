---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb399363d383abb902a038cc440cb3e333b898529163549305a901e6468d795e
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_delta-source-sub-error
    - NSS
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: NON_DELTA source sub-error
description: A specific sub-condition of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE raised when the source table is not in Delta format.
tags:
  - databricks
  - delta-lake
  - clone-operation
  - error-subclass
timestamp: "2026-06-19T15:02:04.933Z"
---

## NON_DELTA source sub-error

The **NON_DELTA source sub-error** is a specific condition of the DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class. It occurs when a [Delta Clone](/concepts/delta-clone.md) operation with history is attempted on a source table that is not in Delta format. The operation requires a Delta source because only Delta tables store the transaction log needed to replicate the full history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Error message

The full error message reads:

```
DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE
NON_DELTA: Source table of <format> format is not supported.
```

where `<format>` is replaced by the actual source format (e.g., Parquet, CSV, JSON, or a Hive-style table). ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Cause

`CLONE` with the `FOR HISTORY` option only supports Delta tables as the source. If the source is a non-Delta file format or a [Hive metastore](/concepts/built-in-hive-metastore.md) table that is not backed by Delta Lake, the command fails with the NON_DELTA sub-error. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Solution

To clone a non-Delta table with history, first convert the source to Delta format using `CONVERT TO DELTA`, or perform a shallow clone without history. If history is not required, omit the `FOR HISTORY` clause. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Related sub-error

The same error class also includes the **TIME_TRAVELLED_BY_TIMESTAMP** sub-error, which is raised when the source table uses time travel by timestamp during a history clone. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

### Related concepts

- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class
- [Delta Clone](/concepts/delta-clone.md)
- [CONVERT TO DELTA](/concepts/convert-to-delta.md)
- Time Travel in Delta Lake
- Error classes in Databricks

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
