---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62c24fa20f4095773b4e9156eea9631006f259113d5b5555bd5f61f1f8de47f5
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cannot_finalize_redirect
    - CANNOT_FINALIZE_REDIRECT
    - cannot_finalize_redirect-error
    - cannot_finalize_redirect-sub-error
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: CANNOT_FINALIZE_REDIRECT
description: A sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED indicating the migration cannot finalize because the redirect configuration does not exist, possibly due to a concurrent rollback to external.
tags:
  - databricks
  - error-messages
  - migration
timestamp: "2026-06-18T11:49:28.487Z"
---

# CANNOT_FINALIZE_REDIRECT

**CANNOT_FINALIZE_REDIRECT** is a specific error condition that occurs when executing an `ALTER TABLE <table> SET MANAGED` statement in Databricks, and the operation fails because it cannot finalize the redirect process on the table's external location.

## Error Detail

The full error message appears as:

```
DELTA_ALTER_TABLE_SET_MANAGED_FAILED
SQLSTATE: 42809
CANNOT_FINALIZE_REDIRECT
```

This error indicates that the system attempted to finalize a redirect on the external location associated with the table, but the redirect configuration does not exist. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Common Causes

### Table Rolling Back to External

The most common cause is that the table is currently in the process of rolling back to an External Table state. When a table migration to managed fails or is interrupted, the system may attempt to revert to the external configuration. If this rollback process is incomplete or corrupt, attempting to finalize the redirect will fail. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Troubleshooting and Resolution

### 1. Check the Table's Current State

Examine the table's metadata to understand its current status:

```sql
DESC EXTENDED <table_name>;
```

Look for properties related to the managed/external state to determine if the table is in an incomplete migration state. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### 2. Verify No Concurrent Operations

Ensure no other concurrent `ALTER TABLE SET MANAGED` statements are running against the same table. Concurrent operations can cause conflicting state transitions. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### 3. Retry the Operation

In some cases, simply retrying the `ALTER TABLE SET MANAGED` command may succeed if the underlying transient condition has resolved. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### 4. Contact Databricks Support

If the issue persists after verifying there are no concurrent operations and retrying, contact Databricks Support for assistance with resolving the table's state. This error can indicate an internal state inconsistency that requires engineering intervention to resolve. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

Other errors that can occur under the `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` error class include:

- FILE_VALIDATION_FAILED — File migration failure
- REDIRECT_READY_ALREADY_EXISTS — Table already has a RedirectReady state
- VERSION_MISMATCH — Delta log version mismatch

## Related Concepts

- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The operation that triggers this error
- [Managed Tables in Databricks](/concepts/managed-tables-in-databricks.md) — The target state of the migration
- External Table — The source state before migration
- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying the table

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
