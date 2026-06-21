---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e07a4dc8d1d8b061f1ed9142933c9c44b53ea782ddce8fa41a1485a0ffcf8a2
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - deletion-vectors-in-delta-lake
    - DVIDL
    - Deletion vectors in Databricks
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: Deletion Vectors in Delta Lake
description: A Delta Lake table feature that must be purged or disabled before enabling IcebergCompat, as unresolved deletion vectors cause compatibility violations.
tags:
  - delta-lake
  - apache-iceberg
  - table-features
timestamp: "2026-06-19T15:05:44.093Z"
---

Here is the wiki page for **Deletion Vectors in Delta Lake**, based solely on the provided source material.

# Deletion Vectors in Delta Lake

**Deletion vectors** are a mechanism in [Delta Lake](/concepts/delta-lake.md) that allows the system to track which rows in existing Parquet data files have been logically removed, without immediately rewriting those files. This enables efficient handling of row-level updates and deletes by reducing write amplification. However, the presence of deletion vectors in a table introduces compatibility constraints with other Delta Lake and external query features. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Incompatibility with Symlink Manifest Generation

When a Delta table contains deletion vectors, **symlink manifest generation** is unsupported. If you attempt to generate a [Symlink Manifest](/concepts/symlink-manifest-generation.md) (an index used by external query engines like Presto or Athena), the operation fails with the error `EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION`. The error message states that the operation is not possible while deletion vectors are present. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

To produce a version of the table without deletion vectors, the recommended command is:

```sql
REORG TABLE <table> APPLY (PURGE)
```

This command removes the deletion vectors by consolidating the underlying data files. After this operation, you can generate a symlink manifest. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Format Restrictions

The ability to have **persistent** deletion vectors is only supported on **Parquet-based** Delta tables. If your table uses a different storage format, enabling or retaining persistent deletion vectors will fail with the error `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

### Mutual Exclusivity

Persistent deletion vectors and **incremental symlink manifest generation** are mutually exclusive features. If both features are active on the same table, the system will raise the error:

> `PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION`

To switch between these two workflows, you must first either purge the deletion vectors (using `REORG TABLE APPLY (PURGE)`) or disable incremental manifest generation on the table. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Resolving Incompatibilities

The standard method for removing deletion vectors from a Delta table to resolve these compatibility issues is the `REORG TABLE APPLY (PURGE)` command. This command rewrites the table’s data files to physically incorporate all logical deletions. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

---

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage framework that supports deletion vectors.
- Parquet — The storage format requirement for persistent deletion vectors.
- [Symlink Manifest](/concepts/symlink-manifest-generation.md) — An external index for query engines; incompatible with deletion vectors.
- [REORG TABLE](/concepts/reorg-table.md) — The command used to purge deletion vectors and compact files.

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
