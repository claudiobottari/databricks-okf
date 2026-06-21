---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3266309e8f6c556ee2b7d859125af018c691bdc7b231e846804b9512ed517e5b
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session_temporary-target-error
    - STE
    - SESSION_TEMPORARY target error
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: SESSION_TEMPORARY target error
description: A subtype of DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET indicating the target table is a session temporary table (not supported for clone with history).
tags:
  - databricks
  - error-subtype
  - delta-lake
timestamp: "2026-06-18T11:51:08.180Z"
---

# SESSION_TEMPORARY Target Error

The **SESSION_TEMPORARY target error** occurs when a `DELTA_CLONE` operation with history is attempted on a session temporary target table. Session temporary tables are not supported as targets for a historical clone of a Delta table.

## Error Class

This error is a sub-condition of the `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` error class (SQLSTATE: 0AKDC). The error class includes two other unsupported targets: `NON_DELTA` (non-Delta format target) and `PATH_BASED` (path-based target table). ^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Message

When triggered, the error returns the following message:

```
SESSION_TEMPORARY: Session temporary target table is not supported.
```

^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Cause

A `CLONE` operation that includes the table history (`CLONE ... WITH HISTORY`) requires a permanent Delta table as the target. A session temporary table exists only for the duration of a Spark session and cannot serve as a durable target for historical data. The engine rejects the operation to prevent data loss or inconsistency.

## Solution

Change the target to a permanent Delta table or use a global temporary view if session-scoped behavior is needed. If you only need the current snapshot of the source table, consider using `CLONE` without the `WITH HISTORY` clause, which does not have this restriction.

## Related Concepts

- [Delta Cloning](/concepts/delta-table-cloning.md) — The operation used to create a copy of a Delta table
- [Delta Clone with History](/concepts/delta-clone-with-history.md) — A deep clone that preserves the full transaction log
- Session Temporary Tables — Ephemeral tables scoped to a Spark session
- Global Temporary Views — Temporary views that persist across sessions in the same cluster
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
