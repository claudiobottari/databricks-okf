---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2c9c83d5a134a2f6e3e3ff1c923be71ede649f6586d3764dedca4ecf4d707b9
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_delta-source-restriction-for-clone-with-history
    - NSRFCWH
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: NON_DELTA source restriction for clone with history
description: The error condition raised when cloning a Delta table with history from a source that is not in Delta format (e.g., Parquet, CSV, JSON).
tags:
  - databricks
  - delta-lake
  - cloning
  - format-restrictions
timestamp: "2026-06-19T10:02:52.849Z"
---

# NON_DELTA Source Restriction for Clone with History

**NON_DELTA source restriction for clone with history** is a specific error condition under the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error class. It occurs when a user attempts to perform a [Deep Clone](/concepts/deep-clone.md) (clone with history) on a source table that is not a Delta table.

## Error Overview

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error class has two sub-conditions: `NON_DELTA` and `TIME_TRAVELLED_BY_TIMESTAMP`. The `NON_DELTA` sub-condition specifically indicates that the source table must be in [Delta Lake](/concepts/delta-lake.md) format to support cloning with history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Message

When a `CLONE` operation targets a non-Delta table, Databricks returns an error similar to:

```
Source table of <format> format is not supported.
```

where `<format>` is the actual format of the source table (e.g., `parquet`, `csv`, `json`, etc.). ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

Deep clone (clone with history) relies on the [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) to replicate the full history of changes — including versions, timestamps, and operations — to the target table. Non-Delta formats do not maintain a transaction log, so the history cannot be recreated. Only Delta tables are supported as a source for clone with history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Solution

Convert the source table to [Delta Lake](/concepts/delta-lake.md) format (e.g., using `CONVERT TO DELTA`) before performing a clone with history. Alternatively, use a shallow clone (`CLONE WITHOUT HISTORY`) which does not require a Delta source. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Related Sub-Condition

The `TIME_TRAVELLED_BY_TIMESTAMP` sub-condition occurs when the source table has been time-travelled by timestamp, which is also unsupported for clone with history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deep Clone](/concepts/deep-clone.md) – A clone that copies the full table history.
- [Delta Lake](/concepts/delta-lake.md) – The open-source storage layer required for clone with history.
- [Shallow Clone](/concepts/shallow-clone.md) – A clone that does not copy history and can use non-Delta sources.
- [Time travel](/concepts/delta-lake-time-travel.md) – The ability to query previous versions of a Delta table; timestamp-based time travel cannot be cloned with history.

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
