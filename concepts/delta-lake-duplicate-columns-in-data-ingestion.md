---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f650dadf1238d2eddbe6335828f973bee75cbbc0e4f0cf185957c73ba14f4d91
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-duplicate-columns-in-data-ingestion
    - DLDCIDI
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: Delta Lake Duplicate Columns in Data Ingestion
description: Scenarios where duplicate columns are detected during data ingestion operations such as saving data or converting to Delta format.
tags:
  - delta-lake
  - data-ingestion
  - error-messages
timestamp: "2026-06-19T10:05:33.953Z"
---

# Delta Lake Duplicate Columns in Data Ingestion

**Delta Lake Duplicate Columns in Data Ingestion** refers to the `DELTA_DUPLICATE_COLUMNS_FOUND` error condition that occurs when duplicate column names are detected during data ingestion operations into Delta Lake tables. This error prevents the write or update operation from completing, ensuring data integrity and schema consistency.

## Overview

When ingesting data into Delta Lake, the engine validates that no duplicate column names exist in the incoming data or the target schema. If duplicates are found, the operation fails with the `DELTA_DUPLICATE_COLUMNS_FOUND` error (SQLSTATE: 42711), returning the message: "Found duplicate column(s): `<duplicateCols>`." ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Common Scenarios

The error can occur in several specific contexts during ingestion:

### DATA

The duplicate is found in the data being saved. This happens when the source data contains columns with the same name — for example, when joining or unioning datasets that have overlapping column names without proper aliasing. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### ADDING_COLUMNS

The duplicate is detected while adding columns to an existing table, such as when an `ALTER TABLE ADD COLUMNS` statement specifies a column name that already exists in the schema. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### REPLACING_COLUMNS

The duplicate is found while replacing columns, such as during an `ALTER TABLE REPLACE COLUMNS` operation where the new schema contains duplicate column names. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### SPECIFIED_COLUMNS

The duplicate exists in columns explicitly specified by the user in a `SELECT` statement or column list during a write operation. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Schema-Related Errors

### EXISTING_SCHEMA

The duplicate is found in the existing table schema, meaning the table itself has duplicate column definitions — an inconsistent state that should not normally occur. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### TABLE_SCHEMA

The duplicate is found in the table schema definition, such as when creating a table with duplicate column names. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### READ_SCHEMA

The duplicate is found in the schema of the data being read, such as when a `SELECT *` from a source with duplicate column names is used for ingestion. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Partition-Related Errors

### PARTITION_COLUMNS

The duplicate exists among the partition columns specified for the table. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### PARTITION_SCHEMA

The duplicate is found in the partition schema definition, such as specifying the same column as both a data column and a partition column. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Other Contexts

### CLUSTER_BY

The duplicate is found in the `CLUSTER BY` clause, when the same column is specified multiple times for clustering. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

### CONVERT_TO_DELTA

The duplicate is detected during conversion from a non-Delta format (such as Parquet) to Delta Lake format. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Resolution

To resolve the `DELTA_DUPLICATE_COLUMNS_FOUND` error, identify and eliminate duplicate column names from the operation. Common approaches include:

- **Use explicit column selection**: Replace `SELECT *` with explicit column lists.
- **Rename duplicate columns**: Use `SELECT col1 AS unique_name` to disambiguate.
- **Clean source data**: Deduplicate columns in the source dataset before ingestion.
- **Review schema modifications**: Ensure `ALTER TABLE` operations don't introduce duplicate column names.

## Related Concepts

- [Delta Lake Schema Enforcement](/concepts/delta-table-schema-requirements.md) — How Delta Lake validates schema during writes
- [Delta Lake Table Schema Evolution](/concepts/delta-lake-schema-migration.md) — Managing schema changes over time
- Delta Lake Write Operations — Available write modes and behaviors
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) — Configuring partition columns
- Delta Lake Clustering — Using liquid clustering with CLUSTER BY

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
