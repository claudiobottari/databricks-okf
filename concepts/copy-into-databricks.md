---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db5a7fc45b630db3b48c1debf6177f64ffe440663a0788db2cda6b4fec574b3f
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-databricks
    - CI(
    - Copy Into Data Loading (Databricks)
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO (Databricks)
description: A SQL command for idempotently loading data from file storage into Delta tables, skipping previously loaded files.
tags:
  - databricks
  - sql
  - data-ingestion
timestamp: "2026-06-18T14:45:57.657Z"
---

# COPY INTO (Databricks)

**COPY INTO** is a SQL command in Databricks that incrementally loads data from cloud object storage into a Delta table. It is designed to be idempotent and retryable: files that have already been loaded from the source location are automatically skipped, even if they have been modified since they were last loaded. ^[copy-into-databricks-on-aws.md]

## Syntax

```sql
COPY INTO target_table [ BY POSITION | ( col_name [ , <col_name> ... ] ) ]
  FROM { source_clause |
         ( SELECT expression_list FROM source_clause ) }
  FILEFORMAT = data_source
  [ VALIDATE [ ALL | num_rows ROWS ] ]
  [ FILES = ( file_name [, ...] ) | PATTERN = glob_pattern ]
  [ FORMAT_OPTIONS ( { data_source_reader_option = value } [, ...] ) ]
  [ COPY_OPTIONS ( { copy_option = value } [, ...] ) ]

source_clause
  source [ WITH ( [ CREDENTIAL { credential_name |
                                (temporary_credential_options) } ]
                  [ ENCRYPTION (encryption_options) ] ) ]
```

^[copy-into-databricks-on-aws.md]

## Parameters

### target_table

The target must be an existing Delta table. Table names with temporal specifications or options specifications are not permitted. If the table name is provided as a location path, such as `delta.'/path/to/table'`, Unity Catalog can govern access to the written locations. Writing to an external location requires either:

- `WRITE FILES` permissions on the defined external location, or
- `WRITE FILES` permissions on a named storage credential authorizing writes via `COPY INTO delta.'/some/location' WITH (CREDENTIAL <named-credential>)`.

^[copy-into-databricks-on-aws.md]

### BY POSITION | (col_name [, ...])

Controls how source columns are mapped to target table columns. This parameter is only supported for headerless CSV files and requires `FILEFORMAT = CSV` with `FORMAT_OPTIONS ("headers" = "false")`.

**BY POSITION** automatically matches source columns to target columns by ordinal position. `IDENTITY` and `GENERATED` columns in the target are ignored during matching. If the number of source columns does not equal the filtered target columns, an error is raised.

**(col_name [, ...])** matches source columns to the specified target column names in list order, ignoring the table's original column order and names. `IDENTITY` and `GENERATED` columns cannot appear in this list. Columns not in the list receive default values (if defined) or `NULL`; if any omitted column is non-nullable, an error is raised.

^[copy-into-databricks-on-aws.md]

### source

The file location URI from which data is loaded. Files at this location must match the format specified in `FILEFORMAT`. Access to the source can be provided through:

- An external location defined in Unity Catalog with `READ FILES` permissions.
- A named storage credential with `READ FILES` permissions.
- Inline temporary credentials (e.g., `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_SESSION_TOKEN` for S3; `AZURE_SAS_TOKEN` for ADLS and Azure Blob Storage).
- Inline encryption options (e.g., `TYPE = 'AWS_SSE_C'` with `MASTER_KEY` for S3).

If the source path is a root path, a trailing slash (`/`) must be added (e.g., `s3://my-bucket/`).

^[copy-into-databricks-on-aws.md]

### SELECT expression_list

Selects specified columns or expressions from the source data before copying into the Delta table. Any expressions valid in `SELECT` statements are allowed, including window operations. Aggregation expressions are permitted only for global aggregates—`GROUP BY` on columns is not supported with this syntax.

^[copy-into-databricks-on-aws.md]

### FILEFORMAT

Specifies the format of source files. Supported values: `CSV`, `JSON`, `AVRO`, `ORC`, `PARQUET`, `TEXT`, `BINARYFILE`.

^[copy-into-databricks-on-aws.md]

### VALIDATE

Validates data without writing to the table. Checks include parseability, schema compatibility (including schema evolution needs), and constraint compliance (nullability and check constraints). By default, all data is validated; `VALIDATE num_rows ROWS` limits validation to a specified row count. The command returns a preview of up to 50 rows (or fewer if `num_rows` is less than 50).

^[copy-into-databricks-on-aws.md]

### FILES and PATTERN

**FILES** specifies a list of file names to load (limit: 1000 files). Cannot be used with `PATTERN`.

**PATTERN** specifies a glob pattern to identify files in the source directory. Cannot be used with `FILES`.

^[copy-into-databricks-on-aws.md]

### FORMAT_OPTIONS

Options passed to the Apache Spark data source reader for the specified format. Available options vary by file format and correspond to DataFrameReader options for batch reads.

^[copy-into-databricks-on-aws.md]

### COPY_OPTIONS

Controls the operation of the `COPY INTO` command:

- `force`: boolean, default `false`. When `true`, idempotency is disabled and all files are loaded regardless of prior ingestion history.
- `mergeSchema`: boolean, default `false`. When `true`, the target table's schema can evolve based on incoming data.

^[copy-into-databricks-on-aws.md]

## Concurrent Invocations

`COPY INTO` supports concurrent invocations against the same table as long as each invocation operates on a **distinct** set of input files. If concurrent invocations process overlapping file sets, a transaction conflict occurs. Running concurrent `COPY INTO` commands is not recommended for performance improvement—a single command with multiple files typically performs better than multiple single-file commands.

Concurrent invocations are useful when:
- Multiple data producers cannot coordinate into a single invocation.
- A very large directory is ingested sub-directory by sub-directory.

For ingesting directories with a very large number of files, Databricks recommends using Auto Loader when possible.

^[copy-into-databricks-on-aws.md]

## Idempotency

By default, `COPY INTO` is idempotent: files already loaded from the source location are skipped on subsequent runs, even if the files have been modified. This behavior can be overridden by setting `COPY_OPTIONS ('force' = 'true')`, which causes all files to be reloaded regardless of prior ingestion history.

^[copy-into-databricks-on-aws.md]

## Related Concepts

- Auto Loader — Alternative incremental ingestion method for very large directories.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for target tables.
- Unity Catalog External Locations — Access control mechanism for cloud storage.
- DataFrameReader Options — Format-specific read options for each file type.
- File Metadata Column — Accessing metadata for file-based data sources.
- Common Data Loading Patterns Using COPY INTO — Practical examples and patterns.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — Upsert operation for merging source data into Delta tables.
- INSERT INTO — Standard row insertion into Delta tables.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
