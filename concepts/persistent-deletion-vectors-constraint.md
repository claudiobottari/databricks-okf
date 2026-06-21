---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d919286e8ce8e0460fb7ab59b03388ab0df3e8463ac7b42d47bff649be56879
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - persistent-deletion-vectors-constraint
    - PDVC
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: Persistent Deletion Vectors Constraint
description: Persistent deletion vectors are only supported on Parquet-based Delta tables and cannot coexist with incremental symlink manifest generation.
tags:
  - delta-lake
  - deletion-vectors
  - constraints
timestamp: "2026-06-18T11:58:26.362Z"
---

# Persistent Deletion Vectors Constraint

**Persistent Deletion Vectors Constraint** refers to the set of limitations that Delta Lake enforces on tables that use persistent [Deletion Vectors](/concepts/deletion-vectors.md). Persistent deletion vectors are a storage mechanism that tracks logically deleted rows without rewriting data files, but they come with compatibility restrictions that can produce the `DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED` error when violated. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Constraints

### Parquet-Based Delta Tables Only

Persistent deletion vectors are only supported on Parquet-based Delta tables. Attempting to enable or maintain them on a non-Parquet table (for example, a Delta table stored in a different format) triggers the error subcondition `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

### Incompatibility with Incremental Symlink Manifest Generation

Persistent deletion vectors and [Incremental Symlink Manifest Generation](/concepts/incremental-symlink-manifest-generation.md) are mutually exclusive. If a table has persistent deletion vectors enabled, any operation that relies on incremental symlink manifest generation (commonly used by external query engines such as Presto or Athena) will fail with the error subcondition `PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

A related constraint applies when **existing** (non-persistent) deletion vectors are present in the table: symlink manifest generation is unsupported while any deletion vectors exist. This is reported as `EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Resolution

To remove deletion vectors from a table and make it compatible with symlink manifest generation, run the `REORG TABLE` command with the `APPLY (PURGE)` option:

```sql
REORG TABLE <table> APPLY (PURGE);
```

This rewrites the table to a state without deletion vectors, after which incremental symlink manifest generation can be enabled. Note that this operation also applies to tables that already contain deletion vectors but are not using the persistent mode. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) — The mechanism for tracking deleted rows without rewriting data files
- [Delta Lake](/concepts/delta-lake.md) — The ACID transactional storage layer that supports deletion vectors
- [Symlink Manifest Generation](/concepts/symlink-manifest-generation.md) — A feature for exporting table metadata to external query engines
- [REORG TABLE](/concepts/reorg-table.md) — The command used to rewrite a table and remove deletion vectors
- Parquet — The file format required for persistent deletion vector support

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
