---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 753325439c275bc47323ff9d696d7753ba0c9b12fce99b5e0b0a9ba28906b178
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_clone_with_history_unsupported_source-error-class
    - DEC
    - DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class
    - DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error condition
    - DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE
  citations:
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class
description: A Databricks error class indicating that a Delta table CLONE operation with history is attempted on an unsupported source table
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-19T18:22:29.639Z"
---

# DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE error class

The **DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE** error class is raised when a `CLONE WITH HISTORY` operation is attempted on a source table that cannot support the deep-clone-with-history workflow. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## SQLSTATE and Classification

- **SQLSTATE**: `0AKDC` ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]
- **Error class**: `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`
- **SQLSTATE Class**: `0A` — Feature Not Supported ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Sub-Conditions

This error class contains two sub-conditions that identify the specific reason for the failure.

### NON_DELTA

**Error message**: `Source table of <format> format is not supported.` ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

This sub-condition is triggered when the source table is in a format other than [Delta Lake](/concepts/delta-lake.md). The deep clone with history operation requires the source to be a Delta table because only Delta tables maintain the version history and metadata necessary for the operation.

### TIME_TRAVELLED_BY_TIMESTAMP

**Error message**: `Source table time travelled by timestamp is not supported.` ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

This sub-condition is triggered when the source table is accessed using a timestamp-based [time travel](/concepts/delta-lake-time-travel.md) query rather than a version-based query. The `CLONE WITH HISTORY` operation requires a specific commit version reference, not a timestamp-based snapshot.

## Related Concepts

- [CLONE WITH HISTORY](/concepts/delta-clone-with-history.md) — The operation that creates a deep clone of a Delta table with full version history
- [Delta table](/concepts/delta-lake-table.md) — The storage format required for versioned deep cloning
- [TIME TRAVEL](/concepts/delta-lake-time-travel.md) — Accessing previous versions of a Delta table by timestamp or version number
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — The feature-not-supported SQL state class
- [Deep Clone](/concepts/deep-clone.md) — A clone operation that copies all data and metadata from the source

## Sources

- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
