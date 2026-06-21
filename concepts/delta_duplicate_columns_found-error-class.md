---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c34c79a059526abfa76bb1d7ea58ae4b5f9710893c773b77d56888812735762d
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_duplicate_columns_found-error-class
    - DEC
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: DELTA_DUPLICATE_COLUMNS_FOUND error class
description: A Databricks Delta Lake error (SQLSTATE 42711) raised when duplicate column names are detected in a Delta operation, with multiple sub-condition variants pinpointing the exact operation context.
tags:
  - delta-lake
  - error-handling
  - databricks
timestamp: "2026-06-19T18:24:46.179Z"
---

# DELTA_DUPLICATE_COLUMNS_FOUND error class

The **DELTA_DUPLICATE_COLUMNS_FOUND** error class is a [Delta Lake](/concepts/delta-lake.md) error condition that occurs when duplicate column names are detected during schema definitions, data operations, or metadata operations. The error has SQLSTATE `42711`, which falls under Class 42 (syntax error or access rule violation).^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Error Message

The error returns the following message template, where `<duplicateCols>` is replaced at runtime with the actual duplicate column names:

```
[SQLSTATE: 42711] Found duplicate column(s): <duplicateCols>.
```

^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Sub-Conditions

The error class includes several sub-conditions that identify the specific operation context where the duplicate was detected:

| Sub-Condition | Description |
|---------------|-------------|
| `ADDING_COLUMNS` | Duplicate found while adding columns to the table schema. |
| `CLUSTER_BY` | Duplicate found in the `CLUSTER BY` clause. |
| `CONVERT_TO_DELTA` | Duplicate found during conversion to Delta format. |
| `DATA` | Duplicate found in the data being saved. |
| `EXISTING_SCHEMA` | Duplicate found in the existing table schema or metadata update. |
| `PARTITION_COLUMNS` | Duplicate found in the partition columns specification. |
| `PARTITION_SCHEMA` | Duplicate found in the partition schema. |
| `READ_SCHEMA` | Duplicate found in the schema of data being read. |
| `REPLACING_COLUMNS` | Duplicate found while replacing columns. |
| `SPECIFIED_COLUMNS` | Duplicate found in the specified columns list. |
| `TABLE_SCHEMA` | Duplicate found in the table schema definition. |

All sub-conditions are defined in the source material.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Common Causes

This error typically occurs in the following scenarios:

- **Schema definition errors**: Creating a table or adding columns with duplicate column names, such as `CREATE TABLE t (a INT, a STRING)`.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **Data source issues**: Reading data from files (e.g., Parquet) that contain duplicate column names.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **Conversion operations**: Converting existing data formats to Delta when the source data has duplicate columns.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **Metadata operations**: Operations like `REPLACE COLUMNS` or `ALTER TABLE` that introduce duplicate column names.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **Partitioning issues**: Specifying duplicate column names in partition column lists.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Troubleshooting

To resolve this error:

1. **Identify the duplicate columns**: The error message lists the duplicate column names found.
2. **Review the operation**: Check whether you're adding columns, reading data, converting to Delta, or performing another operation.
3. **Remove or rename duplicates**: Ensure all column names in the schema, data, or operation are unique.
4. **Validate source data**: If reading from external files, verify the source data doesn't have duplicate column names.

## Related Concepts

- [Delta Lake schema enforcement](/concepts/delta-table-schema-requirements.md) — Schema validation that prevents duplicate columns
- [SQLSTATE 42711](/concepts/sqlstate-42711.md) — The SQL state associated with this error
- Delta Lake error conditions — Other Delta Lake errors and their resolutions
- [ALTER TABLE operations](/concepts/alter-table-set-managed-operation.md) — Operations that can trigger this error

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
