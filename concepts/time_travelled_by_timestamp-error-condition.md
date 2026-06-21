---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1171e9e9eff1a73c594183d34f2e7d7609eec85aff5d79951dc1dbedbb66fb62
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_travelled_by_timestamp-error-condition
    - TEC
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: TIME_TRAVELLED_BY_TIMESTAMP error condition
description: A specific sub-error of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE raised when the source table uses timestamp-based time travel, which is not supported for clone with history
tags:
  - databricks
  - error-messages
  - delta-lake
  - time-travel
timestamp: "2026-06-19T18:22:28.183Z"
---

# TIME_TRAVELLED_BY_TIMESTAMP error condition

The **TIME_TRAVELLED_BY_TIMESTAMP** error condition occurs when a [Delta Lake](/concepts/delta-lake.md) `CLONE` operation with history enabled receives a source table that has been time travelled by a timestamp. This operation is not supported; only cloning from the latest version of a table (without time travel) is supported when using `CLONE WITH HISTORY`. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Details

TIME_TRAVELLED_BY_TIMESTAMP is a sub‑condition of the broader DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error condition. It is raised when the source table was referenced using a timestamp‑based time travel specification (e.g., `TIMESTAMP AS OF '...'`). The error message simply states: *“Source table time travelled by timestamp is not supported.”* The SQLSTATE for this error condition is `0AKDC` (Feature not supported). ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Workaround

To successfully perform a `CLONE WITH HISTORY`, reference the source table at its latest version or use a version‑based time travel specification if supported. Avoid using timestamp‑based time travel on the source table when cloning with history. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md] *(Inferred: the source only documents the error, not a workaround, but the inference follows from the error description.)*

## Related concepts

- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class|DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error condition — The parent error class containing other unsupported source patterns such as `NON_DELTA`.
- [Delta Lake Time Travel](/concepts/delta-lake-time-travel.md) — The feature that allows querying previous versions of a Delta table by timestamp or version number.
- CLONE command (Delta Lake) — The command used to create a copy of a Delta table, optionally with history.

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
