---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b520f64a498e4c5b47fca74e6c63e7e3b4277dcd644e427f872f02e255b15806
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - file_validation_failed
    - FILE_VALIDATION_FAILED
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: FILE_VALIDATION_FAILED
description: A sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED indicating that one or more files could not be migrated during the external-to-managed table transition.
tags:
  - databricks
  - error-messages
  - file-migration
timestamp: "2026-06-18T11:49:26.543Z"
---

# FILE_VALIDATION_FAILED

**FILE_VALIDATION_FAILED** is an error condition that occurs when the `ALTER TABLE <table> SET MANAGED` command fails because one or more data files could not be migrated from an external location to managed storage during the conversion process.

## Error Message

When this error occurs, the system returns the following message:

```
FILE_VALIDATION_FAILED: File validation failed: <missingFileCount> file(s) could not be migrated. Retry the operation or contact Databricks support if the issue persists.
```

^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Cause

This error indicates that during the conversion of an external table to a managed table using `ALTER TABLE <table> SET MANAGED`, a specified number of files could not be located or migrated to the new managed storage location. The `<missingFileCount>` placeholder in the error message indicates how many files failed validation. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

1. **Retry the operation** — The simplest first step is to retry the `ALTER TABLE <table> SET MANAGED` command. Transient issues may resolve on a subsequent attempt.
2. **Investigate missing files** — If the error persists, investigate why the specified files are missing from the external location. Possible causes include:
   - Files were deleted or moved from the external storage location after the table was created but before the migration.
   - Permissions issues preventing access to the external storage location.
   - Corrupted or incomplete file manifests.
3. **Contact Databricks support** — If retrying does not resolve the issue and you cannot determine the cause of the missing files, contact Databricks support for further assistance.

## Related Concepts

- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The command that triggers this error
- DELTA_ALTER_TABLE_SET_MANAGED_FAILED — The parent error class for this condition
- [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) — The target state of the migration
- External Tables — The source state before migration
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
