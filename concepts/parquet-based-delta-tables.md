---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5bba8860741a1a187124ef83d51b47662e43ff25f5482c483c10a852c8de26f6
  pageDirectory: concepts
  sources:
    - delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - parquet-based-delta-tables
    - PDT
  citations:
    - file: delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md
title: Parquet-based Delta Tables
description: Delta Lake tables stored in Parquet columnar format, which are required for features like persistent deletion vectors and serve as the standard storage format for Delta Lake.
tags:
  - delta-lake
  - parquet
  - storage-format
timestamp: "2026-06-19T18:29:49.003Z"
---

# Parquet-based Delta Tables

**Parquet-based Delta tables** are a specific type of [Delta Lake](/concepts/delta-lake.md) table that uses the Parquet file format as the underlying storage format for data files. These tables support advanced features such as [Deletion Vectors](/concepts/deletion-vectors.md) for improved write performance, but certain operations are restricted when the table is not Parquet-based.

## Key Characteristics

A Delta table is considered "Parquet-based" when its underlying data files are stored in the Parquet columnar storage format. This is the default and most common format for Delta Lake tables, as Delta Lake was originally built on top of Parquet files with a transaction log (the `_delta_log` directory).^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Feature Restriction: Persistent Deletion Vectors

The error condition `DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED` includes the sub-error:

### PERSISTENT\_DELETION\_VECTORS\_IN\_NON\_PARQUET\_TABLE[​](#persistent_deletion_vectors_in_non_parquet_table)

**Persistent deletion vectors are only supported on Parquet-based Delta tables.**

If a Delta table uses a non-Parquet storage format (such as Iceberg, Avro, or JSON), persistent deletion vectors are not supported. Attempting to enable or use persistent deletion vectors on such a table will result in the `DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED` error with the `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE` message.^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

Two other error conditions in the same class reference non-Parquet table types:

- **EXISTING\_DELETION\_VECTORS\_WITH\_INCREMENTAL\_MANIFEST\_GENERATION** — Symlink manifest generation is unsupported while deletion vectors are present in the table. To resolve, run `REORG TABLE <table> APPLY (PURGE)` to produce a version without deletion vectors.^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]
- **PERSISTENT\_DELETION\_VECTORS\_WITH\_INCREMENTAL\_MANIFEST\_GENERATION** — Persistent deletion vectors and incremental symlink manifest generation are mutually exclusive on the same table.^[delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md]

## When to Use Parquet-Based Delta Tables

Parquet is the recommended storage format for most Delta Lake workloads because:

- It provides efficient columnar storage and compression.
- It supports the full Delta Lake feature set, including deletion vectors, time travel, schema evolution, and [incremental manifest generation](/concepts/incremental-symlink-manifest-generation.md).
- It is the only format that supports persistent deletion vectors.

Use Parquet-based Delta tables unless you have a specific requirement for a non-Parquet format (e.g., interoperability with external systems that require a different format).

## Resolution

If you encounter `PERSISTENT_DELETION_VECTORS_IN_NON_PARQUET_TABLE` and need to use deletion vectors, convert your table to a Parquet-based Delta table by rewriting the data files in Parquet format using `REORG TABLE ... APPLY (PURGE)` or a full table rewrite.

## Related Concepts

- Parquet format — The columnar storage file format underlying Parquet-based Delta tables.
- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta Lake feature for improving write performance by marking rows as deleted without rewriting files.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and scalable metadata handling on top of Parquet files.
- DELTA_VIOLATE_TABLE_PROPERTY_VALIDATION_FAILED — The parent error class for property validation violations.

## Sources

- delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_violate_table_property_validation_failed-error-condition-databricks-on-aws.md](/references/delta_violate_table_property_validation_failed-error-condition-databricks-on-aws-8e86a725.md)
