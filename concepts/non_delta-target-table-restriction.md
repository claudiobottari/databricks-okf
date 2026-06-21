---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a59079adcdd4203fb0d2812d1ae2177b78202412dd0531a9e9846010f55a0ac1
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non_delta-target-table-restriction
    - NTTR
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: NON_DELTA target table restriction
description: Delta clone with history does not support target tables that are not in Delta format.
tags:
  - databricks
  - delta-lake
  - clone-operation
timestamp: "2026-06-19T18:22:43.974Z"
---

# NON_DELTA target table restriction

The **NON_DELTA target table restriction** is a subtype of the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error condition that occurs when attempting to clone a Delta table with history into a target table that is not in [Delta table|Delta format](/concepts/delta-lake-table.md). The error message states: "Target table of non-delta format is not supported." ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error context

This error belongs to SQLSTATE class **0AKDC**, which denotes a feature-not-supported condition. The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error class has three subtypes:

- **NON_DELTA** – the target table is in a non-Delta format.
- PATH_BASED target table restriction|PATH_BASED target table restriction|PATH_BASED – the target table is a path-based table (not a catalog or schema table).
- SESSION_TEMPORARY target table restriction|SESSION_TEMPORARY target table restriction|SESSION_TEMPORARY – the target table is a session-scoped temporary table.

Only target tables that are themselves Delta tables can accept a [Clone|clone with history](/concepts/delta-clone-with-history.md) operation. Non-Delta formats (e.g., Parquet, CSV, JSON, or tables managed by other systems) are not supported as targets for this operation. ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Typical cause and resolution

A user may encounter this error when running a `CREATE OR REPLACE TABLE` or `CLONE` command with the `HISTORY` option against a table that is not backed by the Delta format. The fix is to ensure the target table is a Delta table (e.g., using the `USING DELTA` clause or creating it with `delta` as the format). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related concepts

- [Delta table](/concepts/delta-lake-table.md) – The required format for the target of a clone-with-history operation.
- [Clone with history](/concepts/delta-clone-with-history.md) – The feature that triggers this error when the target is non-Delta.
- Error classes in Databricks – The error classification system that includes this condition.
- DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET – The parent error class.

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
