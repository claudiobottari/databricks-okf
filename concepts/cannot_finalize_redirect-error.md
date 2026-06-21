---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f25ee8de9047e6a0a7c8c579564e8a4a09b3717eaa2d10d836926d1f7da8df9
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cannot_finalize_redirect-error
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: CANNOT_FINALIZE_REDIRECT error
description: A sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED raised when the redirect configuration for an external location does not exist, often during a rollback-to-external scenario.
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-19T15:00:15.733Z"
---

# CANNOT_FINALIZE_REDIRECT Error

The **`CANNOT_FINALIZE_REDIRECT`** error is a sub‑error of the DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class. It occurs when an `ALTER TABLE SET MANAGED` operation cannot finalize a redirect on the external location because the required redirect configuration does not exist. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Error Message

```
DELTA_ALTER_TABLE_SET_MANAGED_FAILED: CANNOT_FINALIZE_REDIRECT
```

The full error text reads: *“It cannot finalize redirect on the external location because redirect configuration doesn’t exist.”* ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The redirect configuration is missing. This can happen if the table is currently in the process of rolling back to an external location — for example, a previous migration attempt was reversed but the redirect metadata was not properly cleaned up. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

1. **Check if the table is rolling back to external.** If a rollback is ongoing, wait for it to complete before retrying `ALTER TABLE SET MANAGED`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

2. **Contact Databricks support.** If the table is not rolling back, the missing redirect configuration may require intervention from Databricks engineering. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class – The parent error class that groups all `ALTER TABLE SET MANAGED` failures.
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) – The command that triggers this error.
- [External tables](/concepts/unity-catalog-external-table-conversion.md) – Tables stored in an external location before conversion to managed.
- [Managed tables](/concepts/managed-tables-in-databricks.md) – Tables whose data is fully managed by a Delta Lake.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
