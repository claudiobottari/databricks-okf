---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4276ba6849958524b96ca26b3458372bc39bf6a422622ceac789a3c4e774467
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - file_validation_failed-sub-error
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: FILE_VALIDATION_FAILED Sub-Error
description: Sub-error raised when one or more files cannot be migrated during ALTER TABLE SET MANAGED
tags:
  - error-messages
  - databricks
  - file-migration
timestamp: "2026-06-19T18:21:13.099Z"
---

# FILE_VALIDATION_FAILED Sub-Error

The **FILE_VALIDATION_FAILED** sub‑error is a specific failure condition of the DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class. It occurs when an `ALTER TABLE … SET MANAGED` operation attempts to migrate a table from external to managed, but one or more files cannot be validated or moved. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Error Message

When the sub‑error is triggered, the system returns the following message:

> `FILE_VALIDATION_FAILED`
> File validation failed: `<missingFileCount>` file(s) could not be migrated.

The placeholder `<missingFileCount>` indicates the number of files that failed validation and were not migrated. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The `ALTER TABLE … SET MANAGED` command requires that all files associated with the table be successfully moved into the managed storage location. If any files are missing, inaccessible, or otherwise fail the migration process, the command aborts with `FILE_VALIDATION_FAILED`. Common causes include transient file system errors, permission issues, or concurrent modifications to the table’s data directory. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

1. **Retry the operation** — The error may be temporary. Running `ALTER TABLE … SET MANAGED` again can succeed if the file system issues are resolved.
2. **If the issue persists**, contact Databricks support for further investigation. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_FAILED – The parent error class containing this sub‑error.
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) – The SQL command that triggers this error.
- [Managed tables vs External tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) – The difference between managed and external table storage.
- [Delta Lake](/concepts/delta-lake.md) – The underlying table format used for managed tables.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
