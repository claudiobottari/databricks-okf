---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e4af8fc0d5602b16ebc225e4fe6fddb0d30878f5ad08a06620d814d52626c22
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session-temporary-target-restriction-for-clone-with-history
    - STTRFCWH
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Session temporary target restriction for clone with history
description: Cloning a Delta table with history to a session temporary target table is not supported in Databricks.
tags:
  - databricks
  - delta-lake
  - restrictions
timestamp: "2026-06-18T15:17:46.569Z"
---

# Session Temporary Target Restriction for Clone with History

**Session temporary target restriction for clone with history** is an error condition that occurs when attempting to use `[CLONE WITH HISTORY](/concepts/delta-clone-with-history.md)` or `[Deep Clone](/concepts/deep-clone.md)` operations on a session temporary table in Databricks's [Delta Lake](/concepts/delta-lake.md). This operation is not supported because session temporary tables have a fundamentally different lifecycle and persistence model than permanent Delta tables, making historical tracking through clone operations incompatible.

## Error Identification

The error is classified under [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) (Feature Not Supported) with the error class `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` and the specific sub-condition `SESSION_TEMPORARY`.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Message

When triggered, the system returns the following error message:

> Session temporary target table is not supported.

## Cause

This error occurs when a [CLONE](/concepts/deep-clone.md) operation (either `CLONE WITH HISTORY` or `DEEP CLONE`) specifies a session temporary table as the target. Session temporary tables in Databricks are temporary by nature — they exist only within the scope of a Spark session and are automatically dropped when the session ends. Because [clone with history](/concepts/delta-clone-with-history.md) operations create a full copy of the source table including its commit history, and that history is intended for permanent storage and querying, targeting a session-scoped table is inherently incompatible with the operation's purpose.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Affected Operations

The following operations are blocked when targeting a session temporary table:

- `CREATE OR REPLACE TABLE ... CLONE` with the `WITH HISTORY` flag
- `CREATE OR REPLACE TABLE ... DEEP CLONE`

Both operations attempt to preserve the complete change history of the source table, which requires a persistent target table.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Unsupported Target Types

The `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error class also covers two other unsupported target types:

- NON_DELTA — Target table of non-Delta format is not supported
- PATH_BASED target error|PATH_BASED — Path-based target table is not supported

These represent distinct but related reasons why a clone operation cannot proceed.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Workaround

To avoid this error, use a permanent Delta table as the target for clone operations that require history preservation. Session temporary tables should only be used for intermediate data processing steps within a single session, not as final destinations for cloned data that needs to retain its change log.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
