---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df576b514304037b1118f0d45eaba6473df48f6899fe50ecadb280e2cf2532de
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-command
    - CIC
    - COPY INTO
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO Command
description: A SQL command in Databricks that loads data from file locations into Delta tables with retryable and idempotent semantics.
tags:
  - sql
  - data-ingestion
  - delta-lake
timestamp: "2026-06-19T14:26:46.041Z"
---

# COPY INTO Command

The **COPY INTO** command is a SQL statement in Databricks that loads data from a file location into a [Delta Table](/concepts/delta-lake-table.md). It is a retryable and idempotent operation — files in the source location that have already been loaded are skipped, even if the files have been modified since they were loaded. ^[copy-into-databricks-on-aws.md]

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

Identifies an existing Delta table. The table name must not include a temporal specification or options specification. ^[copy-into-databricks-on-aws.md]

If the table name is provided in form of a location (e.g., `delta.\`/path/to/table\``), [Unity Catalog](/concepts/unity-catalog.md) can govern access to the locations being written to. Writing to an external location requires either `WRITE FILES` permissions on that external location, or `WRITE FILES` permissions on a named storage credential that authorizes writing to the location. ^[copy-into-databricks-on-aws.md]

### BY POSITION | ( col_name [ , ... ] )

Matches source columns to target table columns by ordinal position. Type casting is performed automatically. This parameter is only supported for headerless CSV files, requiring both `FILEFORMAT = CSV` and `FORMAT_OPTIONS ("headers" = "false")`. ^[copy-into-databricks-on-aws.md]

**BY POSITION** matches source columns to target table columns automatically by ordinal position. `IDENTITY` and `GENERATED` columns are ignored during matching. An error is raised if the number of source columns doesn't equal the filtered target table columns. ^[copy-into-databricks-on-aws.md]

The column name list syntax `( col_name [ , ... ] )` matches source columns to specified target columns by relative ordinal position. `IDENTITY` and `GENERATED` columns cannot be specified in this list. Columns not in the list receive default values or `NULL`, and an error is raised if any omitted column is not nullable. ^[copy-into-databricks-on-aws.md]

### source

The file location to load data from, provided as a URI. Files must have the format specified in `FILEFORMAT`. ^[copy-into-databricks-on-aws.md]

Access to the source location can be provided through:
- A named credential (if the file location is not included in an [External location](/concepts/external-location.md))
- Inline temporary credentials
- Defining the source location as an external location with `READ FILES` permissions via Unity Catalog
- A named storage credential with `READ FILES` permissions

If the source file path is a root path, add a trailing slash (`/`), for example `s3://my-bucket/`. ^[copy-into-databricks-on-aws.md]

Accepted credential options include `AWS_ACCESS_KEY`, `AWS_SECRET_KEY`, and `AWS_SESSION_TOKEN` for AWS S3, and `AZURE_SAS_TOKEN` for ADLS and Azure Blob Storage. Accepted encryption options include `TYPE = 'AWS_SSE_C'` with `MASTER_KEY` for AWS S3. ^[copy-into-databricks-on-aws.md]

### SELECT expression_list

Selects specified columns or expressions from the source data before copying into the Delta table. Expressions can include any valid `SELECT` statement elements, including window operations. Aggregation expressions are limited to global aggregates — `GROUP BY` is not supported with this syntax. ^[copy-into-databricks-on-aws.md]

### FILEFORMAT = data_source

The format of the source files to load. Supported formats are `CSV`, `JSON`, `AVRO`, `ORC`, `PARQUET`, `TEXT`, and `BINARYFILE`. ^[copy-into-databricks-on-aws.md]

### VALIDATE

Applies to Databricks Runtime 10.4 LTS and above. Validates that data can be loaded without writing to the table. Validation checks include whether data can be parsed, whether the schema matches the table (or needs evolution), and whether all nullability and check constraints are met. The default validates all data; `VALIDATE num_rows ROWS` validates a specified number of rows. Returns a preview of up to 50 rows (or fewer when a number less than 50 is specified). ^[copy-into-databricks-on-aws.md]

### FILES

A list of file names to load, with a limit of 1000 files. Cannot be specified together with `PATTERN`. ^[copy-into-databricks-on-aws.md]

### PATTERN

A glob pattern that identifies files to load from the source directory. Cannot be specified together with `FILES`. ^[copy-into-databricks-on-aws.md]

### FORMAT_OPTIONS

Options passed to the Apache Spark data source reader for the specified format. See DataFrameReader Options for format-specific options. ^[copy-into-databricks-on-aws.md]

### COPY_OPTIONS

Options controlling the operation of the `COPY INTO` command:

- **`force`**: boolean, default `false`. When set to `true`, idempotency is disabled and files are loaded regardless of whether they've been loaded before.
- **`mergeSchema`**: boolean, default `false`. When set to `true`, the schema can evolve according to the incoming data.

^[copy-into-databricks-on-aws.md]

## Concurrent Invocations

`COPY INTO` supports concurrent invocations against the same table, provided each invocation operates on distinct sets of input files. Otherwise, a transaction conflict occurs. A single `COPY INTO` command with multiple files typically performs better than running concurrent commands with single files. Common use cases for concurrent invocation include when multiple data producers cannot coordinate a single invocation, or when ingesting a very large directory sub-directory by sub-directory. For directories with a very large number of files, Databricks recommends using Auto Loader when possible. ^[copy-into-databricks-on-aws.md]

## Idempotency

By default, `COPY INTO` is idempotent — files that have already been loaded are skipped on subsequent runs. This behavior can be disabled by setting the `force` copy option to `true`. ^[copy-into-databricks-on-aws.md]

## Related Concepts

- [Delta Table](/concepts/delta-lake-table.md)
- Auto Loader
- [External Locations](/concepts/external-location.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Data Ingestion Patterns
- DataFrameReader Options

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
