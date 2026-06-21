---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50c6e4c4668c65660b9c7da8d5fa6da5b0f0e577a4c9bfc420772307323e5a81
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-42809
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: SQLSTATE 42809
description: The SQL standard state code for syntax error or access rule violation, associated in Databricks with the DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class.
tags:
  - sqlstate
  - error-code
  - databricks
  - sql-standards
timestamp: "2026-06-19T15:01:24.842Z"
---

```markdown
---
title: SQLSTATE 42809
summary: A SQL standard error code (class 42: Syntax Error or Access Rule Violation) associated with the DELTA_ALTER_TABLE_SET_MANAGED_FAILED and DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED errors in Databricks.
source:
  - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - sql
  - error-codes
  - databricks
  - delta-lake
aliases:
  - sqlstate-42809
  - class-42-syntax-error
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# SQLSTATE 42809

**SQLSTATE 42809** is a SQL state code that indicates a syntax error or access rule violation in Databricks. It is associated with two error conditions related to altering a table’s managed status: `DELTA_ALTER_TABLE_SET_MANAGED_FAILED`, which occurs when a table fails to convert from external to managed, and `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED`, which occurs when rolling back from managed to external table fails. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md, delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Classification

SQLSTATE 42809 falls under **Class 42 — Syntax Error or Access Rule Violation** in the Databricks SQL state classification system. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md, delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Conditions

### DELTA_ALTER_TABLE_SET_MANAGED_FAILED

This error occurs when the `ALTER TABLE <table> SET MANAGED` command fails. The following sub‑conditions are defined: ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

- **CANNOT_FINALIZE_REDIRECT** — Cannot finalize redirect on the external location because redirect configuration doesn't exist. This can happen if the table is currently rolling back to external. Otherwise, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- **FILE_VALIDATION_FAILED** — File validation failed: `<missingFileCount>` file(s) could not be migrated. Retry the operation or contact Databricks support if the issue persists. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- **REDIRECT_READY_ALREADY_EXISTS** — The table already has RedirectReady state. The migration may have already finished by a concurrent `ALTER TABLE tbl SET MANAGED` command. Check if the table is already migrated to managed by running `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- **VERSION_MISMATCH** — The version of the managed DeltaLog (`<managedDeltaLogVersion>`) does not match the expected one (`<expectedVersion>`). This can happen if there is a concurrent `ALTER TABLE tbl SET MANAGED` command that already successfully migrated the table to managed. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED

This error occurs when attempting to roll back a table from a managed table to an external table in Unity Catalog. The error message is: ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

`<table> cannot be rolled back from managed to external table.`

The following sub‑conditions are defined: ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

- **TIME_WINDOW_EXCEEDED** — The time window for rolling back the table has been exceeded. Rollback is only supported within `<numDays>` days after the migration to a Unity Catalog managed table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- **TRUNCATED_HISTORY** — The table history is truncated and cannot find all the necessary commits to rollback the table to its original state. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- **UNEXPECTED_ERROR** — An unexpected error occurred. The specific error details are provided in the message. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- **VERSION_MISMATCH** — The versions of the managed DeltaLog (`<managedDeltaLogVersion>`) and external DeltaLog (`<externalDeltaLogVersion>`) do not match. This can happen if there is a concurrent `ALTER TABLE tbl UNSET MANAGED` command that already successfully rolled back the table to external. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] — The storage layer that manages table metadata and versioning.
- [[Unity Catalog]] — The governance layer that tracks managed and external tables.
- ALTER TABLE — The SQL command used to modify table properties, including managed status.
- Delta Log — The transaction log that tracks table history and versions.
- [[DESC EXTENDED diagnostic command|DESC EXTENDED]] — A command to inspect a table’s metadata and migration status.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
2. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
