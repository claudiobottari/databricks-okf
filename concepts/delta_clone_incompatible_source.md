---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e18e32de8ba5875a94b9c2026446f1941a1452a7d1234b77e704df49a1c3000
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_clone_incompatible_source
    - DELTA_CLONE_INCOMPATIBLE_SOURCE
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: DELTA_CLONE_INCOMPATIBLE_SOURCE
description: A Databricks error class raised when attempting to clone a table into Delta format from a source that has valid format but unsupported features.
tags:
  - error-message
  - delta-lake
  - databricks
timestamp: "2026-06-19T10:02:33.790Z"
---

# DELTA_CLONE_INCOMPATIBLE_SOURCE

The **DELTA_CLONE_INCOMPATIBLE_SOURCE** error condition occurs when a [`CLONE`](https://docs.databricks.com/en/sql/language-manual/delta-clone.html) operation targets a source table that is in a valid format but uses a feature that [Delta Lake](/concepts/delta-lake.md) does not support for cloning. The error belongs to SQLSTATE class `0AKDC` (feature not supported). ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Sub‑error Conditions

The error class defines three specific conditions, each with its own message and remediation.

### HAS_INDEXES

```
Table `<tableName>` has indexes: `<indexNames>`. Drop the indexes before cloning.
```

The source Delta table contains secondary indexes. Cloning a table with indexes is not supported. The fix is to drop the indexes from the source table before attempting the clone operation. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### ICEBERG_MISSING_PARTITION_SPECS

The source [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table has no partition specifications defined in its metadata. A partition spec is required for Delta Lake to correctly interpret the Iceberg table's structure during a clone. Without it, the operation cannot proceed. The resolution involves ensuring the Iceberg table has at least one partition spec before cloning. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### ICEBERG_UNDERGONE_PARTITION_EVOLUTION

The source Apache Iceberg table has undergone partition evolution (its partitioning scheme has changed over time). Delta Lake cannot clone Iceberg tables that have undergone partition evolution because the historical partition metadata is not representable in Delta's format. The workaround is to use a different approach, such as reading the Iceberg table with a direct read connector or rewriting the data into a fresh Delta table without cloning. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- CLONE (SQL) — The SQL command that triggers this error
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that enforces compatibility checks
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — A table format that can be a clone source but may have incompatibilities
- [Delta Table Cloning](/concepts/delta-table-cloning.md) — The general process of creating a Delta table copy
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) — The feature-not-supported SQL state that encompasses this error class

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
