---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7301435f37ecbad819be78d690ab712c17ac4a52079b76c1dd3358d1df516489
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - persistent-deletion-vectors
    - PDV
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
      start: 19
      end: 19
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
      start: 23
      end: 23
title: Persistent Deletion Vectors
description: A mode of deletion vectors in Delta Lake where the deletion metadata persists in the table metadata, supported only on Parquet-based Delta tables and incompatible with incremental symlink manifest generation.
tags:
  - delta-lake
  - deletion-vectors
  - table-properties
timestamp: "2026-06-19T18:29:29.442Z"
---

# Persistent Deletion Vectors

**Persistent Deletion Vectors** are a [Delta Lake Table](/concepts/delta-lake-table.md) property that marks logically deleted rows without rewriting underlying data files across table versions. They are supported only on Parquet-based Delta tables and are incompatible with incremental [Symlink Manifest Generation](/concepts/symlink-manifest-generation.md).

## Limitations

### Parquet-Only Support

Persistent deletion vectors can be used only on Parquet File Format|Parquet-based Delta tables. Attempting to enable them on a non-Parquet table triggers the `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE` error. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

### Incompatibility with Incremental Symlink Manifest Generation

Persistent deletion vectors and incremental symlink manifest generation are mutually exclusive. Enabling both on the same table raises the `PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION` error. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Error Conditions

The `DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED` error class includes the following sub‑conditions specific to persistent deletion vectors:

### PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE

Occurs when attempting to use persistent deletion vectors on a table that is not Parquet-based. The error message states: *“Persistent deletion vectors are only supported on Parquet-based Delta tables.”* ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:19]

### PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION

Occurs when attempting to use persistent deletion vectors while incremental symlink manifest generation is enabled. The error message states: *“Persistent deletion vectors and incremental symlink manifest generation are mutually exclusive.”* ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:23]

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) – The broader mechanism for tracking deleted rows in Delta Lake.
- [Symlink Manifest Generation](/concepts/symlink-manifest-generation.md) – A feature that is incompatible with persistent deletion vectors.
- Delta Lake Table Properties – Configuration options that control table behavior.
- Parquet File Format – The only file format that supports persistent deletion vectors.

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
2. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:19-19](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
3. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:23-23](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
