---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1a1d6aa37c7599412418734a1a26313165795120901cacbc9ac347bca6295cf
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-validate
    - CIV
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO VALIDATE
description: A validation-only mode of COPY INTO that checks whether data can be parsed, schema matches, and constraints are met without writing to the table.
tags:
  - sql
  - validation
  - data-ingestion
timestamp: "2026-06-19T14:26:55.651Z"
---

# COPY INTO VALIDATE

**COPY INTO VALIDATE** is an option of the [COPY INTO](/concepts/copy-into-command.md) command in Databricks that validates the data to be loaded into a Delta table without actually writing any rows. It is a dry-run mechanism for checking data quality, schema compatibility, and constraint satisfaction before committing an ingestion job. ^[copy-into-databricks-on-aws.md]

## Overview

`COPY INTO` is a retryable, idempotent SQL command that loads data from a file location into a Delta table. The `VALIDATE` clause modifies this command so that all checks performed during a normal load – parsing, schema matching, and constraint validation – are executed, but no data is written to the target table. This lets you preview potential issues without side effects. ^[copy-into-databricks-on-aws.md]

Validation is supported on Databricks SQL and Databricks Runtime 10.4 LTS and above. ^[copy-into-databricks-on-aws.md]

## Syntax

```sql
COPY INTO target_table
  FROM source_clause
  FILEFORMAT = data_source
  VALIDATE [ ALL | num_rows ROWS ]
  [ FORMAT_OPTIONS (...) ]
  [ COPY_OPTIONS (...) ]
```

The `VALIDATE` keyword can be followed by `ALL` (the default) to validate all files that would be loaded, or by a specific number of rows (for example `VALIDATE 15 ROWS`) to limit validation to a sample of the data. ^[copy-into-databricks-on-aws.md]

## Validation Checks

When `VALIDATE` is specified, `COPY INTO` performs the same checks that would occur during a real load:

- **Parsability** – whether the source files can be read and parsed according to the specified file format (CSV, JSON, Parquet, etc.).
- **Schema compatibility** – whether the schema of the incoming data matches the schema of the target Delta table, or whether schema evolution would be required.
- **Constraints** – whether all nullability constraints and check constraints defined on the target table are satisfied by the incoming data. ^[copy-into-databricks-on-aws.md]

If any of these checks fail, the command returns an error describing the problem, allowing you to correct the data or adjust the table schema before performing the actual load.

## Return Value

When validating a number of rows less than 50 (for example `VALIDATE 15 ROWS`), `COPY INTO` returns a preview of the data of up to 50 rows. This preview shows how the data would look after being loaded, which can be helpful for inspecting sample records. When validating all files or a number greater than or equal to 50, no data preview is returned; only a success or error status is shown. ^[copy-into-databricks-on-aws.md]

## Usage Notes

- `VALIDATE` does not write any data to the target table; it is purely a dry-run operation.
- If validation passes, you can run the same `COPY INTO` command without `VALIDATE` to actually load the data. Because `COPY INTO` is idempotent and tracks previously loaded files, the same files will be skipped on the real load (unless the `force` copy option is used).
- Validation is particularly useful in ETL pipelines where data quality must be verified before committing to a [Delta Lake](/concepts/delta-lake.md) table, and in scenarios where schema evolution policies need to be evaluated.
- The `VALIDATE` clause does not accept the `FILES` or `PATTERN` options in a different way than normal; they are still used to determine which files to validate.

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) – The base command for loading data into Delta tables.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer underlying the target table.
- Schema Validation and Schema Evolution – Mechanisms for ensuring data compatibility.
- Delta Table Constraints – Nullability and check constraints validated during `COPY INTO VALIDATE`.
- COPY INTO Format Options – `FORMAT_OPTIONS` that influence parsing and validation behavior.
- [Idempotent Data Ingestion](/concepts/idempotent-data-loading.md) – The retryable nature of `COPY INTO` that makes validation useful.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
