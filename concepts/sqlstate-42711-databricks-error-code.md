---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 61629646e98a9dc5913c5e632dd190d0425dbe64a0a191b64a76928c683df897
  pageDirectory: concepts
  sources:
    - delta_duplicate_columns_found-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-42711-databricks-error-code
    - S4(EC
  citations:
    - file: delta_duplicate_columns_found-error-condition-databricks-on-aws.md
title: SQLSTATE 42711 (Databricks Error Code)
description: The SQL standard error state code (class 42, syntax error or access rule violation) associated with the DELTA_DUPLICATE_COLUMNS_FOUND error in Databricks.
tags:
  - sql
  - error-codes
  - databricks
timestamp: "2026-06-19T10:05:31.961Z"
---

Here is the wiki page for "SQLSTATE 42711 (Databricks Error Code)", based solely on the provided source material.

---

## SQLSTATE 42711 (Databricks Error Code)

**SQLSTATE 42711** is a Databricks error condition associated with the `DELTA_DUPLICATE_COLUMNS_FOUND` error class. This error occurs when duplicate column names are detected during a Delta Lake operation. The error message includes the specific duplicate column(s) identified: `Found duplicate column(s): <duplicateCols>`.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Causes (Sub-conditions)

The `DELTA_DUPLICATE_COLUMNS_FOUND` error can be triggered in various contexts, depending on the specific operation being performed. The following sub-conditions are defined:

- **ADDING_COLUMNS:** The duplicate was found while adding columns.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **CLUSTER_BY:** The duplicate was found in a `CLUSTER BY` clause.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **CONVERT_TO_DELTA:** The duplicate was found during conversion to Delta format.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **DATA:** The duplicate was found in the data being saved.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **EXISTING_SCHEMA:** The duplicate was found in the existing table schema or in the metadata update.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **PARTITION_COLUMNS:** The duplicate was found in the partition columns.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **PARTITION_SCHEMA:** The duplicate was found in the partition schema.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **READ_SCHEMA:** The duplicate was found in the schema of the data being read.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **REPLACING_COLUMNS:** The duplicate was found while replacing columns.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **SPECIFIED_COLUMNS:** The duplicate was found in the specified columns.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]
- **TABLE_SCHEMA:** The duplicate was found in the table schema.^[delta_duplicate_columns_found-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer where this error is encountered.
- SQLSTATE – The standard SQL state code classification system.
- [Error Handling in Databricks](/concepts/error-handling-in-databricks-notebook-workflows.md) – General guidance on managing errors.

## Sources

- delta_duplicate_columns_found-error-condition-databricks-on-aws.md

# Citations

1. [delta_duplicate_columns_found-error-condition-databricks-on-aws.md](/references/delta_duplicate_columns_found-error-condition-databricks-on-aws-42950ac1.md)
