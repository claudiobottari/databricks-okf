---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2562e27ef1c27fd51d384e2d566cf23f7e83e6717092e315885019d02ec34393
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-schema-modification-duplicate-detection
    - DLSMDD
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: Delta Lake schema modification duplicate detection
description: Sub-conditions under DELTA_DUPLICATE_COLUMNS_FOUND that detect duplicate columns during schema-altering operations such as ADDING_COLUMNS, REPLACING_COLUMNS, or when validating EXISTING_SCHEMA, TABLE_SCHEMA, SPECIFIED_COLUMNS, and READ_SCHEMA.
tags:
  - delta-lake
  - schema-evolution
  - validation
timestamp: "2026-06-19T18:24:26.099Z"
---

# Delta Lake Schema Modification Duplicate Detection

**Delta Lake schema modification duplicate detection** refers to the mechanism by which [Delta Lake](/concepts/delta-lake.md) identifies and reports duplicate column names when performing schema modifications or data operations. When duplicate columns are detected, Delta Lake raises a `DELTA_DUPLICATE_COLUMNS_FOUND` error with SQLSTATE 42711. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Error Overview

The `DELTA_DUPLICATE_COLUMNS_FOUND` error occurs when Delta Lake encounters a column name that appears more than once in a schema context. The error message identifies the specific duplicate columns: `Found duplicate column(s): <duplicateCols>`. Delta Lake categorizes the error into specific sub-conditions based on the operation being performed. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Sub-Conditions

Delta Lake reports the `DELTA_DUPLICATE_COLUMNS_FOUND` error under the following specific sub-conditions, each corresponding to a different schema modification context:

- **ADDING_COLUMNS**: The duplicate was found while adding columns to a table. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **CLUSTER_BY**: The duplicate was found in the `CLUSTER BY` clause during table creation or modification. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **CONVERT_TO_DELTA**: The duplicate was found during conversion of a table to Delta format. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **DATA**: The duplicate was found in the data being saved to the table. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **EXISTING_SCHEMA**: The duplicate was found in the existing table schema or during a metadata update. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **PARTITION_COLUMNS**: The duplicate was found in the partition columns specification. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **PARTITION_SCHEMA**: The duplicate was found in the partition schema. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **READ_SCHEMA**: The duplicate was found in the schema of the data being read. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **REPLACING_COLUMNS**: The duplicate was found while replacing existing columns with a new schema. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **SPECIFIED_COLUMNS**: The duplicate was found in a user-specified column list. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **TABLE_SCHEMA**: The duplicate was found in the overall table schema definition. ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Common Scenarios

Duplicate column detection typically occurs when:

- Attempting to add a column with a name that already exists in the table schema (ADDING_COLUMNS). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- Defining partitioning on a column name that appears multiple times in the schema (PARTITION_COLUMNS, PARTITION_SCHEMA). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- Writing data that contains duplicate column names in its schema (DATA). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- Converting a non-Delta table to Delta format when the source has duplicate columns (CONVERT_TO_DELTA). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- Replacing the entire table schema with a new schema containing duplicates (REPLACING_COLUMNS). ^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Resolution

To resolve duplicate column errors, inspect the schema and ensure all column names are unique. This may involve:

- Renaming duplicate columns in the source data before writing.
- Removing duplicate column specifications from schema modification commands.
- Cleaning up the existing table schema if duplicates are found in the metadata.

## Related Concepts

- [Delta Lake schema enforcement](/concepts/delta-table-schema-requirements.md) — The mechanism that validates data against the table schema.
- [Delta Lake schema evolution](/concepts/delta-lake-schema-migration.md) — How Delta Lake handles schema changes over time.
- [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md) — Configuration options for schema management.
- [SQLSTATE 42711](/concepts/sqlstate-42711.md) — The SQL standard error code for duplicate column errors.

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
