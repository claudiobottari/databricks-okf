---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8725885dd3d3d637a3ec6612409812bb13eb0b922fe920a4529d772a3004cc92
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_travelled_by_timestamp-sub-error
    - time_travelled_by_timestamp-error-condition
    - TEC
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: TIME_TRAVELLED_BY_TIMESTAMP sub-error
description: A specific sub-condition of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE raised when the source table uses timestamp-based time travel, which is not supported for clone with history.
tags:
  - databricks
  - delta-lake
  - time-travel
  - clone-operation
timestamp: "2026-06-19T15:02:19.907Z"
---

# TIME_TRAVELLED_BY_TIMESTAMP Sub‑Error

**TIME_TRAVELLED_BY_TIMESTAMP** is a sub‑error of the DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error condition (SQLSTATE: 0AKDC). It occurs when a `CLONE` command attempts to clone a Delta table **with history** but specifies a time‑travel timestamp, which is not supported.

## Error Type and SQLSTATE

- **Error class:** `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`
- **Sub‑error:** `TIME_TRAVELLED_BY_TIMESTAMP`
- **SQLSTATE:** 0AKDC (Feature not supported)

^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

The `CLONE` operation with the `WITH HISTORY` clause (or equivalent) allows cloning a Delta table along with its full version history. However, when the source table is specified using a time‑travel timestamp (e.g., `TIMESTAMP AS OF`), the operation is not supported. Only cloning by version number is permitted for history‑preserving clones. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Affected Operation

Any attempt to run a `CLONE` command that requests history preservation and simultaneously uses a timestamp‑based time travel reference will fail with this sub‑error. For example:

```sql
CREATE OR REPLACE TABLE target CLONE source WITH HISTORY
TIMESTAMP AS OF '2025-01-01T00:00:00Z';
```

This command will raise `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE: TIME_TRAVELLED_BY_TIMESTAMP`.

The error message returned is:

> Source table time travelled by timestamp is not supported.

^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Resolution

The source material does not provide a direct resolution. To avoid the error, use a version‑based time travel reference (`VERSION AS OF`) instead of a timestamp when cloning with history. Alternatively, perform a regular `CLONE` (without history preservation) after time‑travelling to the desired timestamp.

## Related Concepts

- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE – Parent error condition with additional sub‑errors (e.g., NON_DELTA).
- CLONE command (Delta Lake) – Overview of cloning Delta tables.
- Time travel in Delta Lake – How to query and clone previous table versions.
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) – SQLSTATE class for feature not supported.

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
