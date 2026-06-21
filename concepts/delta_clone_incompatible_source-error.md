---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 117a03017baec65645e47bcc7d20dacab7e910317b7ac5bbc42688fe1fe49096
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_clone_incompatible_source-error
    - DELTA_CLONE_INCOMPATIBLE_SOURCE error condition
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: DELTA_CLONE_INCOMPATIBLE_SOURCE Error
description: A Databricks error that occurs when cloning a Delta table from a source that has a valid format but unsupported features, including sub-classes like HAS_INDEXES, ICEBERG_MISSING_PARTITION_SPECS, and ICEBERG_UNDERGONE_PARTITION_EVOLUTION.
tags:
  - databricks
  - delta-lake
  - error-handling
  - cloning
timestamp: "2026-06-19T18:22:14.798Z"
---

## DELTA_CLONE_INCOMPATIBLE_SOURCE Error

The **DELTA_CLONE_INCOMPATIBLE_SOURCE** error occurs when attempting to clone a source table that, while having a valid format, includes an unsupported feature that Delta Lake cannot handle during a clone operation. The error’s SQL state is `0AKDC`, which falls under the “Feature not supported” class. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Sub‑errors

The error class includes three specific sub‑errors, each indicating a different incompatibility:

#### HAS_INDEXES

```
Table <tableName> has indexes: <indexNames>. Drop the indexes before cloning.
```

This sub-error is raised when the source table contains indexes. Delta Lake does not support cloning tables that have indexes. The resolution is to drop the indexes from the source table before attempting the clone. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

#### ICEBERG_MISSING_PARTITION_SPECS

```
Source Apache Iceberg table has no partition specs in table.
```

This sub-error occurs when the source is an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table that lacks partition specifications. Delta Lake requires valid partition metadata when cloning from Iceberg. The table must be repaired or repartitioned to include partition specs before cloning. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

#### ICEBERG_UNDERGONE_PARTITION_EVOLUTION

```
Source Apache Iceberg table has undergone partition evolution.
```

This sub-error is raised when the source Iceberg table’s partition scheme has changed over time (partition evolution). Delta cloning from Iceberg does not support tables whose partition definitions have evolved. The user must ensure the Iceberg table has a single, stable partition specification before cloning. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Related concepts

- [Delta Clone](/concepts/delta-clone.md) – The operation that triggers the error.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – An alternative table format that may cause incompatibilities.
- SQL States – The classification system for SQL errors.

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
