---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc57924366603fd5b5c42fbf65a8f2af3e6b3798679f11e7f7871651b03e9720
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reorg-table-apply-purge-command
    - RTA(C
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: REORG TABLE APPLY (PURGE) Command
description: A Delta Lake command used to rewrite a table to remove deletion vectors, enabling operations like symlink manifest generation that are incompatible with deletion vectors.
tags:
  - delta-lake
  - sql-commands
  - data-maintenance
timestamp: "2026-06-19T18:29:25.309Z"
---

# REORG TABLE APPLY (PURGE) Command

The **REORG TABLE APPLY (PURGE) Command** is a Delta Lake SQL command used to rewrite a Delta table by removing persistent deletion vectors from all data files. It is primarily employed to resolve compatibility issues that arise when deletion vectors conflict with other Delta table features.

## Syntax

```sql
REORG TABLE <table_name> APPLY (PURGE)
```

^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Purpose

The command addresses conflicts between [Deletion Vectors](/concepts/deletion-vectors.md) and other Delta table features that are mutually exclusive. Specifically, it is used in the following scenarios:

- **Existing deletion vectors with incremental manifest generation:** Symlink manifest generation is unsupported while deletion vectors are present in the table. Running `REORG TABLE APPLY (PURGE)` produces a version of the table without deletion vectors, enabling symlink manifest generation. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

- **Persistent deletion vectors with non-Parquet tables:** Persistent deletion vectors are only supported on Parquet-based Delta tables. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

- **Persistent deletion vectors with incremental manifest generation:** Persistent deletion vectors and incremental symlink manifest generation are mutually exclusive and cannot both be enabled simultaneously. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## When to Use

This command is typically executed when encountering the `DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED` error condition, which indicates that the current table properties violate supported configurations. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Effect

The `PURGE` operation rewrites the table data files to eliminate deletion vectors while preserving the table's data integrity. After execution, the table no longer contains deletion vectors, allowing previously blocked operations (such as symlink manifest generation) to proceed. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta Lake feature for soft deletion that can conflict with other features
- [Symlink Manifest Generation](/concepts/symlink-manifest-generation.md) — A feature that generates symlink manifests for external query engines
- Delta Table Properties — Configuration settings that control table behavior
- DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED — The error condition that recommends using this command

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
