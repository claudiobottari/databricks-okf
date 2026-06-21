---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9280c58026ebf7a11be96044769561d9f89fd3cec74e76eb3199bb3183886ab3
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-data-loading-copy-into
    - IDL(I
  citations:
    - file: copy-into-databricks-on-aws.md
title: Idempotent Data Loading (COPY INTO)
description: The property of COPY INTO that skips already-loaded files, making it safe to retry without duplicate data even if source files have been modified.
tags:
  - data-ingestion
  - reliability
  - delta-lake
timestamp: "2026-06-19T14:27:04.425Z"
---

# Idempotent Data Loading (COPY INTO)

**Idempotent Data Loading (COPY INTO)** refers to the `COPY INTO` SQL command in Databricks that loads data from a file location into a [Delta Lake](/concepts/delta-lake.md) table, designed as a retryable and idempotent operation. Files in the source location that have already been loaded are automatically skipped, even if those files have been modified since they were initially loaded. ^[copy-into-databricks-on-aws.md]

## Overview

`COPY INTO` is a SQL statement that loads data from a file location into a Delta table. Its idempotent behavior makes it well-suited for batch ingestion pipelines where the same command may be run multiple times — for example, after a transient failure — without duplicating data. ^[copy-into-databricks-on-aws.md]

Because `COPY INTO` tracks which files have already been consumed, it can be safely retried. The command compares incoming files against its internal metadata and loads only new, unseen files. ^[copy-into-databricks-on-aws.md]

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
```

^[copy-into-databricks-on-aws.md]

## Key Parameters

- **`target_table`** — Identifies an existing Delta table. The table must not include a temporal specification or options specification. ^[copy-into-databricks-on-aws.md]
- **`source_clause`** — The URI of the file location to load data from. Access to the source can be provided through an external location, a named credential, or inline temporary credentials. ^[copy-into-databricks-on-aws.md]
- **`FILEFORMAT`** — Specifies the format of the source files. Supported formats include `CSV`, `JSON`, `AVRO`, `ORC`, `PARQUET`, `TEXT`, and `BINARYFILE`. ^[copy-into-databricks-on-aws.md]
- **`FILES`** — A list of up to 1,000 file names to load. Cannot be combined with `PATTERN`. ^[copy-into-databricks-on-aws.md]
- **`PATTERN`** — A glob pattern to identify files to load from the source directory. Cannot be combined with `FILES`. ^[copy-into-databricks-on-aws.md]
- **`VALIDATE`** — (Applies to Databricks Runtime 10.4 LTS and above) Validates that the data can be parsed, that the schema matches the target table, and that all nullability and check constraints are met, without writing the data. ^[copy-into-databricks-on-aws.md]

## Copy Options

- **`force`** (boolean, default `false`) — When set to `true`, idempotency is disabled and all files are loaded regardless of whether they have been loaded before. ^[copy-into-databricks-on-aws.md]
- **`mergeSchema`** (boolean, default `false`) — When set to `true`, the schema can be evolved to match the incoming data. ^[copy-into-databricks-on-aws.md]

## Concurrent Invocations

`COPY INTO` supports concurrent invocations against the same table, as long as each invocation operates on a **distinct** set of input files. If concurrent invocations try to load overlapping file sets, a transaction conflict may occur. ^[copy-into-databricks-on-aws.md]

Concurrent `COPY INTO` is useful when:
- Multiple data producers cannot coordinate into a single invocation.
- A very large directory is ingested sub-directory by sub-directory.

A single `COPY INTO` command with multiple files typically performs better than running many concurrent commands each with a single file. When ingesting directories with a very large number of files, Databricks recommends using Auto Loader when possible. ^[copy-into-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying table format that makes `COPY INTO` idempotent.
- Auto Loader — An alternative incremental ingestion tool for large-scale file ingestion.
- Data ingestion patterns — Common patterns for loading data into Delta tables.
- Cloud object storage — The source locations that can be read with `COPY INTO`.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
