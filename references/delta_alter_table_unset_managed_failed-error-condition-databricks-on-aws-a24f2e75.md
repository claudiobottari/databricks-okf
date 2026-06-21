---
title: DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-alter-table-unset-managed-failed-error-class
ingestedAt: "2026-06-18T08:07:03.002Z"
---

[SQLSTATE: 42809](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation)

`<table>` cannot be rolled back from managed to external table.

## TIME\_WINDOW\_EXCEEDED[​](#time_window_exceeded "Direct link to TIME_WINDOW_EXCEEDED")

The time window for rolling back the table has been exceeded. Rollback is only supported

within `<numDays>` days after the migration to Unity Catalog managed table.

## TRUNCATED\_HISTORY[​](#truncated_history "Direct link to TRUNCATED_HISTORY")

The table history is truncated and cannot find all the necessary commits to rollback

the table to its original state.

## UNEXPECTED\_ERROR[​](#unexpected_error "Direct link to UNEXPECTED_ERROR")

An unexpected error occurred.

\== Error ==

`<error>`

## VERSION\_MISMATCH[​](#version_mismatch "Direct link to VERSION_MISMATCH")

The versions of the managed DeltaLog (`<managedDeltaLogVersion>`) and external DeltaLog (`<externalDeltaLogVersion>`) do not match.

This can happen if there is a concurrent `ALTER TABLE` tbl `UNSET MANAGED` command that already successfully rolled back the table to external.
