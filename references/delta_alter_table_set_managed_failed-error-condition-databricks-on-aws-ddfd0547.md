---
title: DELTA_ALTER_TABLE_SET_MANAGED_FAILED error condition | Databricks on AWS
source: https://docs.databricks.com/aws/en/error-messages/delta-alter-table-set-managed-failed-error-class
ingestedAt: "2026-06-18T08:06:59.394Z"
---

[SQLSTATE: 42809](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation)

`ALTER TABLE <table> SET MANAGED` failed.

## CANNOT\_FINALIZE\_REDIRECT[​](#cannot_finalize_redirect "Direct link to CANNOT_FINALIZE_REDIRECT")

It cannot finalize redirect on the external location because redirect configuration doesn't exist.

This can happen if the table is currently rolling back to external. Otherwise, contact Databricks support.

## FILE\_VALIDATION\_FAILED[​](#file_validation_failed "Direct link to FILE_VALIDATION_FAILED")

File validation failed: `<missingFileCount>` file(s) could not be migrated. Retry the operation or contact Databricks support if the issue persists.

## REDIRECT\_READY\_ALREADY\_EXISTS[​](#redirect_ready_already_exists "Direct link to REDIRECT_READY_ALREADY_EXISTS")

The table already has RedirectReady state. The migration may have already finished by concurrent `ALTER TABLE tbl SET MANAGED` command.

Check if the table is already migrated to `MANAGED` by running `DESC EXTENDED tbl`.

## VERSION\_MISMATCH[​](#version_mismatch "Direct link to VERSION_MISMATCH")

The version of the managed DeltaLog (`<managedDeltaLogVersion>`) does not match the expected one (`<expectedVersion>`).

This can happen if there is a concurrent `ALTER TABLE tbl SET MANAGED` command that already successfully migrated the table to managed.

Check if the table is already migrated to managed by running `DESC EXTENDED tbl`.
