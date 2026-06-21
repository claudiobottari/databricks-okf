---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ba60232e84c507a25282b9ffce6680563e1d82986d4a8b4a0abd46737b993dee
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_travelled_by_timestamp-error
    - TIME_TRAVELLED_BY_TIMESTAMP
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: TIME_TRAVELLED_BY_TIMESTAMP error
description: A sub-error of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE indicating the source table used time travel by timestamp, which is incompatible with cloning with history.
tags:
  - databricks
  - delta-lake
  - time-travel
timestamp: "2026-06-18T15:17:17.697Z"
---

# TIME_TRAVELLED_BY_TIMESTAMP Error

The **TIME_TRAVELLED_BY_TIMESTAMP error** occurs when attempting to clone a [Delta Lake](/concepts/delta-lake.md) table with history (`CLONE WITH HISTORY`) from a source that has been time-travelled using a timestamp-based query. The error indicates that the source table was queried at a specific timestamp, but the `WITH HISTORY` clone operation cannot preserve the full history from such a point-in-time snapshot. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Class and Context

- **Error class:** `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`  
- **SQLSTATE:** `0AKDC` (Feature not supported)  
- **Error message:** `Source table time travelled by timestamp is not supported.`  

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE` error class has two variants: `NON_DELTA` (source is not a Delta table) and `TIME_TRAVELLED_BY_TIMESTAMP` (source was time-travelled by timestamp). ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

Delta Lake supports two forms of [time travel](/concepts/delta-lake-time-travel.md): by timestamp string (e.g., `TIMESTAMP '2025-01-01'`) and by version number (e.g., `VERSION AS OF 5`). When you clone a Delta table and request the full history (`CLONE WITH HISTORY`), the operation requires the source to be a complete table snapshot that preserves lineage. If the source was specified using a timestamp-based time travel query, the engine cannot reconstruct the full history because the timestamp may not correspond to a single version boundary or may refer to a state that lacks complete metadata for history restoration. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## How to Resolve

- **Use version‑based time travel instead of timestamp-based.** Replace the timestamp condition with a known version number. For example, change `CLONE WITH HISTORY FOR TIMESTAMP AS OF '2025-06-01'` to `CLONE WITH HISTORY FOR VERSION AS OF 42`.  
- **Clone without history if a point-in-time snapshot is sufficient.** Use `CLONE` (without `WITH HISTORY`) to create a shallow copy of the source at the specified timestamp.  
- **Ensure the source is a full Delta table.** If the source is not a Delta table, the `NON_DELTA` variant applies; convert the source to Delta format first.

## Related Concepts

- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class – The parent error class covering all unsupported sources
- [Delta Lake clone](/concepts/delta-clone.md) – Creating copy-on-write or shallow copies of Delta tables
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) – Querying previous versions of a table by timestamp or version
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) – Feature not supported SQLSTATE code

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
