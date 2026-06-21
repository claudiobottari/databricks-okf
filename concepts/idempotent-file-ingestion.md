---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a57071e496ba74c5da9f6e4357b2ebb960806179544759cacd0362c0ebabd350
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-file-ingestion
    - IFI
  citations:
    - file: copy-into-databricks-on-aws.md
title: Idempotent file ingestion
description: The property that files already loaded via COPY INTO are skipped on subsequent runs, even if modified, enabling safe retries.
tags:
  - data-ingestion
  - reliability
  - delta-lake
timestamp: "2026-06-18T11:11:00.807Z"
---

# Idempotent file ingestion

**Idempotent file ingestion** is a data loading pattern that guarantees that running the same ingestion operation multiple times produces the same result — no duplicate records are created and no data is lost. In Databricks, this is a core property of the `COPY INTO` SQL command, which tracks which files have already been loaded and skips them on subsequent executions.^[copy-into-databricks-on-aws.md]

## How idempotency works

`COPY INTO` maintains a internal journal of files that have been successfully loaded into the target [Delta table](/concepts/delta-lake-table.md). When the command is re-run against the same source location, it compares the set of files present against the journal and loads only the files that have not been processed before.^[copy-into-databricks-on-aws.md]

This tracking is persistent across retries: even if a file has been modified since it was first loaded, `COPY INTO` still skips it. The command is designed to be retryable and safe to run on a schedule without manual deduplication logic.^[copy-into-databricks-on-aws.md]

## Disabling idempotency

Idempotency can be disabled by setting the `force` copy option to `true`. When `force` is enabled, all files in the source location are loaded regardless of whether they have been loaded before. This is useful for reprocessing scenarios but should be used with caution to avoid duplicate data.^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table
FROM 's3://my-bucket/data/'
FILEFORMAT = PARQUET
COPY_OPTIONS ('force' = 'true');
```

^[copy-into-databricks-on-aws.md]

## Concurrent invocations

`COPY INTO` supports concurrent invocations against the same table, as long as each invocation operates on a **distinct** set of input files. If concurrent invocations attempt to load the same files, a transaction conflict occurs.^[copy-into-databricks-on-aws.md]

Concurrent `COPY INTO` is useful when:
- Multiple data producers cannot coordinate and cannot make a single invocation.
- A very large directory is ingested sub-directory by sub-directory.

However, a single `COPY INTO` command with multiple files typically performs better than running concurrent commands with one file each. For directories with a very large number of files, Databricks recommends using Auto Loader when possible.^[copy-into-databricks-on-aws.md]

## Validation without ingestion

The `VALIDATE` clause allows you to test whether data can be loaded without actually writing to the table. This is useful for verifying that files are parseable, that the schema matches the target table, and that all nullability and check constraints are met — all while preserving idempotency for the actual load.^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table
FROM 's3://my-bucket/data/'
FILEFORMAT = CSV
VALIDATE 10 ROWS;
```

^[copy-into-databricks-on-aws.md]

## Related concepts

- [COPY INTO](/concepts/copy-into-command.md) — The SQL command that implements idempotent file ingestion
- [Delta table](/concepts/delta-lake-table.md) — The target storage format for idempotent loads
- Auto Loader — An alternative ingestion tool for large-scale file processing
- Incremental data ingestion — Broader patterns for loading only new or changed data
- Schema evolution — How `COPY INTO` handles schema changes via the `mergeSchema` option

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
