---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f08bb794d243beb36db57d3d231e7c99f20db2ecb46889bd96b2392f5818acc1
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - session-temporary-target-tables-in-delta-clone-with-history
    - STTTIDCWH
  citations:
    - file: delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md
title: Session temporary target tables in Delta Clone with History
description: An error sub-condition (SESSION_TEMPORARY) where the target table for a Delta Clone with History operation is a session-scoped temporary table
tags:
  - databricks
  - delta-lake
  - error-messages
timestamp: "2026-06-19T10:03:12.524Z"
---

# Session Temporary Target Tables in Delta Clone with History

**Session Temporary Target Tables in Delta Clone with History** refers to the error condition that occurs when attempting to use a session temporary table as the target of a `CREATE OR REPLACE TABLE … CLONE … WITH HISTORY` operation. The operation is not supported for session-temporary target tables.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Error Details

The error is raised by the error class `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_TARGET` (SQLSTATE: `0AKDC`). The subcondition [`SESSION_TEMPORARY`](https://docs.databricks.com/aws/en/error-messages/delta-clone-with-history-unsupported-target-error-class#session_temporary) returns the message:  

> Session temporary target table is not supported.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Cause

A [Delta Clone with History](/concepts/delta-clone-with-history.md) operation requires a target table that can persist historical data. Session temporary tables, which exist only for the duration of a session and are automatically dropped, cannot preserve the history metadata required by this clone variant. As a result, the operation fails before writing any data.^[delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Clone with History](/concepts/delta-clone-with-history.md) – The operation that is blocked for session temporary targets.
- Session Temporary Tables – Non-persistent tables scoped to a single session.
- [Delta Clone](/concepts/delta-clone.md) – The general mechanism for creating a copy of a Delta table.
- Error Classes in Databricks – Parent category for this error class.

## Sources

- delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_target-error-condition-databricks-on-aws-797521da.md)
