---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14086f0902e32475da86c848df4589c481f912e3e1c8dc39a129a9dac470edad
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - truncated_history
    - truncated_history-rollback-error
    - TRE
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: TRUNCATED_HISTORY
description: Sub-error indicating the Delta table history has been truncated, making rollback from managed to external impossible
tags:
  - databricks
  - error-message
  - delta-lake
timestamp: "2026-06-19T18:21:36.166Z"
---

# TRUNCATED_HISTORY

**TRUNCATED_HISTORY** is a sub‑error condition of the DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class|DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class. It occurs when an attempt to roll back a [Unity Catalog](/concepts/unity-catalog.md) managed table to an external table fails because the Delta table history has been truncated and cannot locate all the commits needed to restore the table to its original state. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The `ALTER TABLE ... UNSET MANAGED` command must replay the full set of commits that were applied after the table was converted from an external table to a managed table. If the [Delta Lake](/concepts/delta-lake.md) [transaction log](/concepts/delta-transaction-log.md) has been truncated — typically by running VACUUM or by automatic log retention policies — the missing commits make the rollback impossible, and Databricks raises the `TRUNCATED_HISTORY` error. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related concepts

- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class|DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED – The parent error class that contains `TRUNCATED_HISTORY` and other sub‑conditions such as `TIME_WINDOW_EXCEEDED` and `VERSION_MISMATCH`.
- [Managed vs External tables in Unity Catalog](/concepts/managed-vs-external-tables-in-unity-catalog.md) – The distinction between tables whose storage is owned by Unity Catalog and tables that remain linked to an external location.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The ordered record of all changes to a Delta table; truncation of this log can prevent certain operations.
- VACUUM – The command that removes old files and can truncate history beyond the retention threshold.

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
