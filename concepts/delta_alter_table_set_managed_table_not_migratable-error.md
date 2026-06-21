---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c27668e0481ee7f51dc58014b81c1e5198dae1ed1e806e556f6df24f694fb51
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_alter_table_set_managed_table_not_migratable-error
    - DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error condition
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error
description: A Databricks error condition that occurs when ALTER TABLE SET MANAGED fails to migrate a table to managed storage
tags:
  - databricks
  - error-messages
  - delta-lake
timestamp: "2026-06-19T15:00:53.798Z"
---

# DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error

**`DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE`** is an error condition that occurs when the `ALTER TABLE <table> SET MANAGED` command fails to migrate the specified table to a managed table. The error belongs to SQLSTATE class 55019 (object not in prerequisite state). ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Description

The error indicates that the migration cannot proceed because the table is not in a valid state. The recommended course of action is to ensure the table is in a valid state, retry the command, and, if the issue persists, contact Databricks support. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## METADATA_CLEANUP_ERROR

A specific sub‑error reported under this class is `METADATA_CLEANUP_ERROR`. This sub‑error occurs when the system is unable to create a checkpoint or clean up old metadata files before migrating the table. The exact error message will contain additional details. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Troubleshooting

- Verify that the table is in a valid state and that no concurrent operations are blocking the migration.
- Retry the `ALTER TABLE SET MANAGED` command.
- If the `METADATA_CLEANUP_ERROR` sub‑error persists, the underlying metadata cleanup issue may require further investigation. Contact Databricks support for assistance. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – Storage layer used by managed tables.
- ALTER TABLE – SQL command for modifying table properties.
- [Managed Table](/concepts/unity-catalog-managed-tables.md) – A table where Databricks manages both the data and metadata.
- [Error classes](/concepts/databricks-error-classes.md) – System for categorizing Databricks error conditions.
- SQLSTATE – Standard SQL state codes, including class 55 for object not in prerequisite state.

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
