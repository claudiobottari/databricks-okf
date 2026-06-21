---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6afd90a7ca773e530bec31aa639af58380ed3d90403267cb7a2aa8bb1d3d2e08
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - symlink-manifest-generation
    - SMG
    - Symlink Manifest
    - symlink-manifest-generation-incremental
    - SMG(
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
      start: 7
      end: 9
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
      start: 15
      end: 16
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
      start: 12
      end: 13
title: Symlink Manifest Generation
description: A Delta Lake feature for generating symlink manifests for external query engines; mutually exclusive with deletion vectors in several configurations
tags:
  - delta-lake
  - query-engines
  - data-engineering
timestamp: "2026-06-19T10:11:10.071Z"
---

# Symlink Manifest Generation

**Symlink Manifest Generation** is a Delta Lake feature that produces file manifests enabling external systems to discover the underlying data files of a Delta table. This page describes known compatibility restrictions documented in the Delta Lake error condition reference.

## Limitations and Conflicts

Symlink manifest generation is incompatible with [Deletion Vectors](/concepts/deletion-vectors.md), a Delta Lake feature that tracks deleted rows in separate files. The error `EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION` is raised when symlink manifest generation is attempted on a table that contains deletion vectors. To produce a version of the table without deletion vectors, run the [REORG Command](/concepts/reorg-table.md): `REORG TABLE <table> APPLY (PURGE)`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:7-9]

Persistent deletion vectors and incremental symlink manifest generation are mutually exclusive. The error `PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION` indicates that both features cannot be enabled simultaneously. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:15-16]

Persistent deletion vectors are only supported on Parquet‑based Delta tables. Attempting to use them on a table stored in a different file format raises the error `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE`. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:12-13]

## Related Concepts

- [Deletion Vectors](/concepts/deletion-vectors.md) – row‑level delete tracking that conflicts with symlink manifests.
- [REORG Command](/concepts/reorg-table.md) – used to purge deletion vectors and restore compatibility.
- [Persistent Deletion Vectors](/concepts/persistent-deletion-vectors.md) – a variant of deletion vectors that cannot coexist with incremental symlink manifest generation.
- Parquet – the required file format for tables using persistent deletion vectors.

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:7-9](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
2. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:15-16](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
3. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md:12-13](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
