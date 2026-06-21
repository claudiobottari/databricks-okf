---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81405056c46165ee10be20fcf36cc4959c7f070f69d468e2291a2d6fdef6635a
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deletion-vectors
    - Deletion Vector
    - deletion vector
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: Deletion Vectors
description: A Delta Lake feature for marking rows as deleted without rewriting data files; conflicts with symlink manifest generation and has Parquet-only persistence constraints
tags:
  - delta-lake
  - storage
  - data-engineering
timestamp: "2026-06-19T10:10:55.632Z"
---

# Deletion Vectors

**Deletion Vectors** are a Delta Lake feature that tracks logically deleted or updated rows in a table without immediately rewriting the underlying Parquet data files. They allow certain operations to avoid rewriting entire files, improving write performance at the cost of read complexity and compatibility with some table features.

## Characteristics

Deletion vectors can exist in a Delta table as part of its state. When present, they affect the behavior of other features:

- Persistent deletion vectors **are only supported on Parquet-based Delta tables**. A non-Parquet table cannot host persistent deletion vectors. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]
- Persistent deletion vectors and **incremental symlink manifest generation are mutually exclusive**. If a table uses deletion vectors, incremental manifest generation cannot be enabled. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Constraints

Operations that require symlink manifests (e.g., for external query engines) will fail if the table contains deletion vectors. The error `DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED` with sub‑type `EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION` indicates that symlink manifest generation is unsupported while deletion vectors are present. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

Similarly, attempts to use persistent deletion vectors on a non‑Parquet table produce the error sub‑type `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Resolution

To produce a version of the table without deletion vectors, run:

```sql
REORG TABLE <table> APPLY (PURGE)
```

This command purges the deletion vectors, after which features like symlink manifest generation can be enabled. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- Parquet
- [REORG TABLE](/concepts/reorg-table.md)
- [Symlink Manifest Generation](/concepts/symlink-manifest-generation.md)
- DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED|Table Property Validation

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
