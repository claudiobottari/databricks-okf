---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a1397e3bb98e8e9a9a4d620c66a8ce26ff149cc6ea5d091cb7fc532d319f4d6
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-databricks-sql
    - CI(S
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO (Databricks SQL)
description: A SQL command for loading data from file locations into Delta tables, supporting retryable and idempotent ingestion.
tags:
  - sql
  - data-ingestion
  - delta-lake
  - databricks
timestamp: "2026-06-18T11:11:07.861Z"
---

# COPY INTO (Databricks SQL)

**COPY INTO** is a SQL command in Databricks that loads data from a file location into an existing [Delta table](/concepts/delta-lake.md). The operation is designed to be retryable and idempotent — files in the source location that have already been loaded are skipped, even if the file content has been modified since the initial load. This behavior makes `COPY INTO` suitable for incremental ingestion pipelines. ^[copy-into-databricks-on-aws.md]

## Syntax

```sql
COPY INTO target_table
  [ BY POSITION | ( col_name [ , <col_name> ... ] ) ]
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

### `target_table`

Identifies an existing Delta table. The table name must not include a temporal specification or options specification. If the table name is provided as a location (e.g., `delta./path/to/table`), Unity Catalog can govern access to the locations being written to. You can write to an external location by defining it as an external location with `WRITE FILES` permissions, or by having `WRITE FILES` permissions on a named storage credential using `COPY INTO delta./some/location WITH (CREDENTIAL <named-credential>)`. ^[copy-into-databricks-on-aws.md]

### Column matching: `BY POSITION` | `(col_name, ...)`

This parameter matches source columns to target table columns by ordinal position. It is only supported for headerless CSV files (`FILEFORMAT = CSV` with `FORMAT_OPTIONS ("headers" = "false")`, which is the default). ^[copy-into-databricks-on-aws.md]

- **`BY POSITION`**: Automatically matches source columns to target table columns by ordinal position. `IDENTITY` and `GENERATED` columns in the target are ignored. If the number of source columns does not equal the filtered target columns, an error is raised. ^[copy-into-databricks-on-aws.md]
- **`(col_name, ...)`**: Specifies a list of target column names in parentheses, matched by relative ordinal position. `IDENTITY` and `GENERATED` columns cannot be specified. Columns not listed receive default values (or `NULL` if no default exists). An error is raised for non-nullable columns. ^[copy-into-databricks-on-aws.md]

### `source`

The file location (URI) from which to load data. Files must have the format declared in `FILEFORMAT`. Access can be provided through:
- An external location with `READ FILES` permissions in Unity Catalog.
- A named storage credential with `READ FILES` permissions.
- Inline temporary credentials or named credentials if the location is not covered by an external location.

If the source path is a root path, append a trailing slash (`/`). Supported credential options include `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_SESSION_TOKEN` for S3, and `AZURE_SAS_TOKEN` for ADLS/Azure Blob. Encryption options include `TYPE = 'AWS_SSE_C'` with `MASTER_KEY`. ^[copy-into-databricks-on-aws.md]

### `SELECT expression_list`

Allows selecting specified columns or expressions from the source data before copying into the Delta table. Expressions can include window operations and global aggregates (without `GROUP BY`). ^[copy-into-databricks-on-aws.md]

### `FILEFORMAT = data_source`

The format of source files. Supported values: `CSV`, `JSON`, `AVRO`, `ORC`, `PARQUET`, `TEXT`, `BINARYFILE`. ^[copy-into-databricks-on-aws.md]

### `VALIDATE`

Validates the data that would be loaded without writing it to the table. Checks include parseability, schema compatibility (or schema evolution), and nullability/check constraint satisfaction. Default is to validate all data. You can specify a row count (e.g., `VALIDATE 15 ROWS`). Returns a preview of up to 50 rows (or fewer if a smaller number is specified). Available in Databricks Runtime 10.4 LTS and above, and Databricks SQL. ^[copy-into-databricks-on-aws.md]

### `FILES` and `PATTERN`

- **`FILES`**: List of file names to load (max 1000 files). Cannot be used with `PATTERN`.
- **`PATTERN`**: A glob pattern to identify files. Cannot be used with `FILES`. ^[copy-into-databricks-on-aws.md]

### `FORMAT_OPTIONS`

Options passed to the Apache Spark data source reader for the specified format. See the [DataFrameReader options documentation](https://docs.databricks.com/aws/en/spark/api-options#batch-read-options) for format-specific settings (JSON, CSV, XML, Parquet, Avro, text, ORC, binary). ^[copy-into-databricks-on-aws.md]

### `COPY_OPTIONS`

Options controlling the command's behavior:

- `force` (boolean, default `false`): If `true`, disables idempotency and reloads files even if they have been loaded before.
- `mergeSchema` (boolean, default `false`): If `true`, allows schema evolution based on incoming data. ^[copy-into-databricks-on-aws.md]

## Concurrent Invocation

`COPY INTO` supports concurrent invocations against the same table, provided each invocation targets a **distinct** set of input files. Otherwise, a transaction conflict occurs. Concurrent invocations are not recommended for performance improvement; a single invocation with multiple files typically performs better. Common scenarios for concurrency include:
- Multiple data producers that cannot easily coordinate.
- Ingesting a very large directory sub-directory by sub-directory.

For directories with a very large number of files, Databricks recommends using Auto Loader instead. ^[copy-into-databricks-on-aws.md]

## Format Options

For file format-specific options (JSON, CSV, XML, Parquet, Avro, text, ORC, binary), refer to the [DataFrameReader batch read options](https://docs.databricks.com/aws/en/spark/api-options#batch-read-options). Databricks SQL and Databricks Runtime share these format options. ^[copy-into-databricks-on-aws.md]

## Related Articles

- Credentials|Credentials (storage credentials and external locations in Unity Catalog)
- [DELETE (Delta)](/concepts/delete-from-delta-lake.md)
- INSERT (DML)
- [MERGE INTO (Delta)](/concepts/merge-into-delta-lake.md)
- [UPDATE (Delta)](/concepts/update-statement-delta-lake.md)
- Auto Loader — Recommended for very large directories
- File metadata column — Accessing metadata for file-based data sources
- Data loading patterns|Common data loading patterns using COPY INTO

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
