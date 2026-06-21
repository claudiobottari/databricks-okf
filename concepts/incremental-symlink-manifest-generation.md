---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc3d4139a83ea6a96327e233df2ea5569aed75d053121874360919d0859a1530
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incremental-symlink-manifest-generation
    - ISMG
    - Incremental Manifest Generation
    - incremental manifest generation
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: Incremental Symlink Manifest Generation
description: A Delta Lake feature for generating symlink manifests incrementally, which is mutually exclusive with persistent deletion vectors.
tags:
  - delta-lake
  - manifest-generation
  - databricks
timestamp: "2026-06-19T15:09:53.845Z"
---

# Incremental Symlink Manifest Generation

**Incremental Symlink Manifest Generation** is a Delta Lake feature that automatically updates symlink manifests incrementally as new data is written to a table, rather than regenerating the entire manifest from scratch on each write operation.

## Overview

Symlink manifests are files that contain a list of data file paths (symlinks) for a Delta table, enabling external query engines like Presto and Athena to read Delta tables without direct Delta Lake integration. Incremental generation improves performance by only updating the manifest with new or changed files, reducing the overhead of manifest maintenance. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Compatibility Constraints

Incremental symlink manifest generation has specific compatibility requirements and constraints with other Delta Lake features:

### Deletion Vectors

Incremental symlink manifest generation is **unsupported** when deletion vectors are present in the table. If a table has existing deletion vectors, you must remove them before enabling incremental manifest generation. To produce a version of the table without deletion vectors, run: ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

```sql
REORG TABLE <table> APPLY (PURGE)
```

### Persistent Deletion Vectors

Persistent deletion vectors and incremental symlink manifest generation are **mutually exclusive**. These two features cannot be enabled simultaneously on the same table. ^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Error Conditions

When attempting to use incremental symlink manifest generation with incompatible features, Delta Lake raises the `DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED` error with specific sub-conditions:

- `EXISTING_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION` — Occurs when deletion vectors already exist in the table and incremental manifest generation is requested.
- `PERSISTENT_DELETION_VECTORS_WITH_INCREMENTAL_MANIFEST_GENERATION` — Occurs when attempting to enable both persistent deletion vectors and incremental manifest generation simultaneously.

## Related Concepts

- [Symlink Manifest](/concepts/symlink-manifest-generation.md) — The file format that lists data file paths for external query engines.
- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta Lake feature for marking deleted rows without rewriting data files.
- Delta Lake Table Properties — Configuration options that control table behavior.
- External Query Engine Integration — Using symlink manifests to connect Delta tables with Presto, Athena, and other engines.
- [REORG TABLE](/concepts/reorg-table.md) — Command for removing deletion vectors from a Delta table.

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
