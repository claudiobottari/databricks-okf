---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47dcf57692bb248634f51ddd66410b2b6d8e7f1251c57b018856da627740d7a9
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-delta-lake
    - CI(L
    - copy-into-databricks-sql
    - CI(S
    - copy-into-databricks
    - CI(
    - Copy Into Data Loading (Databricks)
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO (Delta Lake)
description: A SQL command in Databricks that loads data from file locations into Delta tables with idempotent, retryable semantics.
tags:
  - databricks
  - delta-lake
  - sql
  - data-ingestion
timestamp: "2026-06-19T17:53:21.443Z"
---

# COPY INTO (Delta Lake)

**COPY INTO** is a SQL command that loads data from a file location into an existing [Delta table](/concepts/delta-lake.md). The operation is retryable and idempotent: files in the source location that have already been loaded are skipped, even if those files have been modified since they were loaded. This behavior makes `COPY INTO` suitable for incremental batch ingestion from cloud object storage. ^[copy-into-databricks-on-aws.md]

`COPY INTO` supports both direct file listing and glob patterns, and it can validate incoming data before committing to the table. It is available in Databricks SQL and Databricks Runtime. ^[copy-into-databricks-on-aws.md]

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

### `target_table`
Identifies an existing Delta table. The table name must not include a temporal specification or options specification. If the table name is provided as a location path (e.g., `` delta.`/path/to/table` ``), [Unity Catalog](/concepts/unity-catalog.md) can govern access to the written location. Writing to an external location requires `WRITE FILES` permissions on that external location, or `WRITE FILES` permissions on a named storage credential that authorizes the path. ^[copy-into-databricks-on-aws.md]

### `BY POSITION` | `( col_name [ , ... ] )`
Matches source columns to target table columns by ordinal position. This parameter is only supported for headerless CSV files (`FILEFORMAT = CSV` with `FORMAT_OPTIONS ("headers" = "false")`). Two syntax variants exist:

- **`BY POSITION`**: automatically matches source columns to target table columns by ordinal position. `IDENTITY` and `GENERATED` columns in the target are ignored. If the number of source columns does not equal the filtered target columns, an error is raised.
- **`( col_name [ , ... ] )`**: specifies a list of target column names to match by relative ordinal position. `IDENTITY` and `GENERATED` columns cannot be listed. Unspecified columns receive default values or `NULL`; if any such column is non-nullable, an error is raised. ^[copy-into-databricks-on-aws.md]

### `source`
The file location (URI) containing data files of the specified `FILEFORMAT`. Access to the source can be provided through:
- An [External location](/concepts/external-location.md) defined in Unity Catalog with `READ FILES` permissions.
- A named [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) with `READ FILES` permissions.
- Inline temporary credentials (AWS access keys, Azure SAS tokens etc.).
- No credential is needed if the path is already an external location the user has permission to use.

For root paths, a trailing slash (`/`) should be appended. Accepted credential options include `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_SESSION_TOKEN` for S3, and `AZURE_SAS_TOKEN` for ADLS or Azure Blob Storage. Encryption options include `TYPE = 'AWS_SSE_C'` with `MASTER_KEY` for S3 server-side encryption with customer keys. ^[copy-into-databricks-on-aws.md]

### `SELECT expression_list`
Selects specific columns or expressions from the source data before copying. Supports any `SELECT` expressions, including window operations. Aggregation expressions are allowed only for global aggregates (no `GROUP BY`). ^[copy-into-databricks-on-aws.md]

### `FILEFORMAT = data_source`
The format of the source files. Accepted values: `CSV`, `JSON`, `AVRO`, `ORC`, `PARQUET`, `TEXT`, `BINARYFILE`. ^[copy-into-databricks-on-aws.md]

### `VALIDATE`
(Applies to Databricks Runtime 10.4 LTS and above.) Validates the data that would be loaded but does not write to the table. Validations include parseability, schema compatibility (including potential evolution), and constraint checks (nullability, check constraints). The default validates all data; you can specify a number of rows, e.g., `VALIDATE 15 ROWS`. The statement returns a preview of the data (up to 50 rows when a number less than 50 is used with `ROWS`). ^[copy-into-databricks-on-aws.md]

### `FILES`
A list of file names to load, with a limit of 1000 files. Cannot be used together with `PATTERN`. ^[copy-into-databricks-on-aws.md]

### `PATTERN`
A glob pattern to identify files to load from the source directory. Cannot be used together with `FILES`. ^[copy-into-databricks-on-aws.md]

### `FORMAT_OPTIONS`
Options passed to the Apache Spark data source reader for the given format. See the DataFrameReader Options reference for format-specific options. ^[copy-into-databricks-on-aws.md]

### `COPY_OPTIONS`
Options controlling the `COPY INTO` operation:

- **`force`** (boolean, default `false`): when `true`, disables idempotency; all files are loaded regardless of whether they have been loaded before.
- **`mergeSchema`** (boolean, default `false`): when `true`, allows schema evolution according to the incoming data. ^[copy-into-databricks-on-aws.md]

## Concurrent Invocations

`COPY INTO` supports concurrent invocations against the same table, provided each invocation targets a **distinct** set of input files. If concurrent commands attempt to load overlapping file sets, a transaction conflict occurs and one invocation will fail. For best performance, use a single `COPY INTO` command with multiple files rather than multiple concurrent commands with single files. Concurrent invocation is useful when multiple data producers cannot easily coordinate or when a very large directory is ingested sub‑directory by sub‑directory. For very large directories, Auto Loader is recommended over `COPY INTO`. ^[copy-into-databricks-on-aws.md]

## Format Options

For options specific to each file format (JSON, CSV, XML, Parquet, Avro, text, ORC, binary), refer to the DataFrameReader Options documentation. ^[copy-into-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The table format targeted by `COPY INTO`.
- Auto Loader – Recommended alternative for streaming or very large directory ingestion.
- [Unity Catalog](/concepts/unity-catalog.md) – Governs access to external locations and storage credentials.
- [External location](/concepts/external-location.md) – A Unity Catalog object that defines access to cloud storage.
- [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) – Named credential used to authenticate to cloud storage.
- File Metadata Column – How to access metadata about ingested files.
- Common data loading patterns using COPY INTO – Practical examples.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
