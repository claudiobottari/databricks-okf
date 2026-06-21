---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94f5e20615e914d1734a0f47c68f0ad6a961d4133cce2da1f03075f92a923f8f
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - file_validation_failed-error
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: FILE_VALIDATION_FAILED error
description: A sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED raised when one or more files cannot be migrated from external to managed storage during table conversion.
tags:
  - databricks
  - error-messages
  - file-migration
timestamp: "2026-06-19T15:00:25.040Z"
---

# FILE_VALIDATION_FAILED error

**FILE_VALIDATION_FAILED** is an error condition that occurs when executing the `ALTER TABLE <table> SET MANAGED` command on a Delta table and file validation fails because one or more files could not be migrated. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Error Details

The error is raised under the DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class (SQLSTATE 42809). When file validation fails, the following error message is returned:

```
FILE_VALIDATION_FAILED: File validation failed: <missingFileCount> file(s) could not be migrated. Retry the operation or contact Databricks support if the issue persists.
```

The `<missingFileCount>` placeholder indicates the number of files that could not be migrated during the managed table conversion. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

The recommended actions are:

1. **Retry the operation.** The table migration may succeed on a subsequent attempt.
2. **Contact Databricks support** if the issue persists after retrying.

The error implies that the table's data files could not be fully moved into the managed storage location, possibly due to access permissions, missing files, or transient failures. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

Other conditions under DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class:

- CANNOT_FINALIZE_REDIRECT – Happens when a redirect configuration does not exist during finalization.
- REDIRECT_READY_ALREADY_EXISTS – Occurs when the table is already in a redirect-ready state from a concurrent `ALTER TABLE SET MANAGED` command.
- VERSION_MISMATCH – Indicates a version mismatch in the managed Delta log, likely from a concurrent migration.

## Related Concepts

- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) – The command that triggers this error.
- [Managed table](/concepts/unity-catalog-managed-tables.md) – The target table type after migration.
- [Delta table](/concepts/delta-lake-table.md) – The storage format to which the command applies.
- Data migration – The underlying process of moving files to the managed location.
- [Databricks Error Classes](/concepts/databricks-error-classes.md) – The error classification system used in Databricks.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
