---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81284f65fbcc33ae14d85e562a0a535d4ad8e5ee7402ab525c01d0d9d469b475
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-55019-object-not-in-prerequisite-state
    - S5(NIPS
    - SQLSTATE Class 55 - Object Not in Prerequisite State
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: SQLSTATE 55019 (Object Not in Prerequisite State)
description: A SQL standard state code indicating that an object is not in the prerequisite state required for the requested operation.
tags:
  - sqlstate
  - error-classification
  - databricks
timestamp: "2026-06-18T15:16:21.805Z"
---

# SQLSTATE 55019 (Object Not in Prerequisite State)

**SQLSTATE 55019** is a class 55 error (Object Not in Prerequisite State) in Databricks. It is raised when an operation cannot be completed because the target object is not in the required state. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, the following message is returned:

```
ALTER TABLE <table> SET MANAGED is unable to migrate the given table. 
Make sure the table is in a valid state and retry the command. 
If the issue persists, contact Databricks support.
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Cause

The error is triggered by `ALTER TABLE <table> SET MANAGED` when the [Delta Lake](/concepts/delta-lake.md) table cannot be migrated to a managed table. The operation requires the table to be in a consistent, valid state. If the table is in an incomplete or corrupted state—for example, if metadata cleanup fails—the migration cannot proceed. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

### Subclass: METADATA_CLEANUP_ERROR

A specific subclass of this error, `METADATA_CLEANUP_ERROR`, occurs when the system is unable to create a checkpoint or clean up old metadata files before migrating the table. The full error output includes:

```
== Error ==
<error>
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error:

1. **Verify the table is in a valid state.** Check that the table does not have pending operations or corruption.
2. **Retry the command.** Simple transient issues may be resolved by retrying.
3. **Contact Databricks support** if the error persists after retrying.

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related Concepts

- [SQLSTATE Class 55 - Object Not in Prerequisite State](/concepts/sqlstate-55019-object-not-in-prerequisite-state.md)
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md)
- [Managed Tables vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- Delta Lake Table State
- Metadata Cleanup in Delta Lake

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
