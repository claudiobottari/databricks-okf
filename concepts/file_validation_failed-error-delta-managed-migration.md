---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa720393692ce1ee738d43de2f15f86dbae20da5fef15f454d9bffcfb83eb53a
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - file_validation_failed-error-delta-managed-migration
    - FE(MM
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: FILE_VALIDATION_FAILED error (Delta managed migration)
description: Sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED indicating one or more files could not be migrated during the external-to-managed transition
tags:
  - error-messages
  - databricks
  - delta-lake
timestamp: "2026-06-19T10:01:48.562Z"
---



# FILE_VALIDATION_FAILED error (Delta managed migration)

**FILE_VALIDATION_FAILED** is a SQLSTATE 42809 error condition that occurs when attempting to migrate a Delta table from external to managed storage using `ALTER TABLE SET MANAGED`. The error indicates that a subset of the table's underlying data files could not be successfully moved to the new managed location.

## Error message

When this condition is triggered, the system returns:

```
FILE_VALIDATION_FAILED: File validation failed: <missingFileCount> file(s) could not be migrated. Retry the operation or contact Databricks support if the issue persists.
```

^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

The `<missingFileCount>` placeholder reports the number of files that failed to transfer during the migration attempt.

## Cause

The error occurs when one or more files that reside on the table's [External location](/concepts/external-location.md) cannot be copied or moved to the [managed storage](/concepts/managed-storage-location.md) location that the table is being redirected to. This can happen due to transient cloud storage issues, permission problems, or when the source files are no longer accessible at the time of migration. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related error conditions

The `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` error class includes several related failure modes that may occur during the same migration operation:

- **CANNOT_FINALIZE_REDIRECT error (Delta managed migration)** – Occurs when the redirect configuration does not exist, typically if the table is rolling back to external.
- **REDIRECT_READY_ALREADY_EXISTS error|REDIRECT_READY_ALREADY_EXISTS error (Delta managed migration)** – Indicates the migration may have already completed successfully via a concurrent command.
- **VERSION_MISMATCH error (Delta managed migration)** – Signals a concurrent migration updated the managed DeltaLog version to an unexpected value.

## Resolution

### Retry the operation

The primary remediation step is to re-run the `ALTER TABLE SET MANAGED` command. Transient failures (such as temporary network issues or cloud storage throttling) may resolve on a second attempt. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### Investigate persistent failures

If the error persists after retrying, investigate the underlying cause:

1. **Check file permissions** – Verify that the source [External location](/concepts/external-location.md) is accessible and that the [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) has the necessary privileges to read and copy the files.
2. **Verify file existence** – Confirm that the files reported in the error message still exist at the expected path on the external location.
3. **Contact support** – If the issue continues, contact Databricks support for assistance, as this may indicate a deeper system problem requiring engineering intervention. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Prevention

To reduce the likelihood of encountering `FILE_VALIDATION_FAILED`:

- Ensure all files in the external table are accessible and not locked by concurrent operations before initiating the migration.
- Run `DESC EXTENDED <table_name>` to confirm the current table state and verify no concurrent migration is in progress. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- Perform migrations during low-activity periods to minimize conflicts with concurrent [Delta Lake](/concepts/delta-lake.md) operations.

## Related concepts

- [SQLSTATE 42809](/concepts/sqlstate-42809.md) – The SQL state class for syntax errors and access rule violations
- Delta managed migration – The overall process of converting a table from external to managed storage
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that manages the migration
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) – The SQL command that triggers the migration

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
