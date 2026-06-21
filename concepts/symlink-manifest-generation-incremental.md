---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86ab20e057252349cd00c76a316722abfe843b8074d365dfe184e18053db3b3f
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - symlink-manifest-generation-incremental
    - SMG(
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: Symlink Manifest Generation (Incremental)
description: A mechanism for generating symlink manifests in Delta Lake, used for integrating with external query engines, which has constraints when combined with deletion vectors.
tags:
  - delta-lake
  - data-integration
  - external-engines
timestamp: "2026-06-19T18:29:15.899Z"
---

# Symlink Manifest Generation (Incremental)

**Incremental symlink manifest generation** is a feature in [Delta Lake](/concepts/delta-lake.md) that produces incremental updates to symlink manifests — text files containing paths to the underlying Parquet data files — so that external query engines (e.g., Presto, Athena) can read Delta tables without the Delta Lake transaction log. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Incompatibility with Deletion Vectors

Incremental symlink manifest generation is **mutually exclusive** with [Deletion Vectors](/concepts/deletion-vectors.md) in Delta Lake. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

- **Existing deletion vectors:** Symlink manifest generation is unsupported while any deletion vectors are present in the table. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]
- **Persistent deletion vectors:** Persistent deletion vectors (a specific type of deletion vector that is stored separately from the data file) and incremental symlink manifest generation are mutually exclusive — they cannot be enabled simultaneously. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

This restriction exists because deletion vectors represent logical row-level modifications that are not reflected in the static file listing produced by a symlink manifest; allowing both would cause manifest readers to return stale or incorrect results.

## Resolving the Conflict

To use incremental symlink manifest generation on a table that has deletion vectors, you must first remove the deletion vectors by rewriting the table’s data files. Use the `REORG TABLE` command with `APPLY (PURGE)`:

```sql
REORG TABLE <table_name> APPLY (PURGE)
```

This command materialises all pending row-level changes (deletions and updates) into new Parquet files and clears the deletion vectors, producing a version of the table that is compatible with incremental symlink manifests. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) — The Delta Lake feature that tracks row-level modifications without rewriting data files.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer underpinning Delta tables.
- [Symlink Manifest](/concepts/symlink-manifest-generation.md) — A file listing all data files (Parquet) in a Delta table snapshot, used by external engines.
- [REORG TABLE](/concepts/reorg-table.md) — The SQL command used to rewrite data and purge deletion vectors.
- [Persistent Deletion Vectors](/concepts/persistent-deletion-vectors.md) — A variant of deletion vectors that is stored persistently in the table directory.

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
