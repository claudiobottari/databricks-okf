---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0f644d709732d295fe0307181ec1cbd2889ab01930bab54d969effd9d175919
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - idempotent-data-loading
    - IDL
    - Idempotent Data Ingestion
  citations:
    - file: copy-into-databricks-on-aws.md
title: Idempotent Data Loading
description: COPY INTO automatically skips files that have already been loaded, even if they were modified, ensuring safe retry and avoiding duplicate data.
tags:
  - data-ingestion
  - reliability
  - delta-lake
timestamp: "2026-06-19T17:53:28.584Z"
---

```yaml
---
title: Idempotent Data Loading
summary: The property that files already loaded are skipped on subsequent executions, even if modified
sources:
  - copy-into-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:45:23.180Z"
updatedAt: "2026-06-19T09:25:17.620Z"
tags:
  - data-ingestion
  - reliability
aliases:
  - idempotent-data-loading
  - IDL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Idempotent Data Loading

**Idempotent Data Loading** is a data ingestion pattern where repeating the same load operation multiple times produces the same result — no duplicate data is added, even if the operation is executed repeatedly. This property is essential for building reliable, retryable data pipelines, especially when dealing with intermittent failures or concurrent writers.

## Overview

In idempotent data loading, files that have already been loaded from a source location are automatically skipped on subsequent executions. This holds true even if the files have been modified since they were initially loaded.^[copy-into-databricks-on-aws.md]

The primary use case is to enable safe retry of data ingestion operations. If a load fails partway through (due to network issues, cluster failures, or other transient errors), the pipeline can be re-run without risk of duplicating records.

## Implementation: `COPY INTO` Command

The [[COPY INTO Command|COPY INTO]] command in Databricks SQL and Databricks Runtime implements idempotent data loading as a core feature.^[copy-into-databricks-on-aws.md]

### Basic Syntax

```sql
COPY INTO target_table
FROM source_location
FILEFORMAT = data_source
```

The command automatically tracks which files have been loaded and skips them on subsequent runs.^[copy-into-databricks-on-aws.md]

### Disabling Idempotency

The idempotent behavior can be overridden using the `force` copy option:

```sql
COPY INTO target_table
FROM source_location
FILEFORMAT = data_source
COPY_OPTIONS ('force' = 'true')
```

When `force` is set to `true`, all files are loaded regardless of whether they have been loaded before.^[copy-into-databricks-on-aws.md]

## How It Works

`COPY INTO` maintains metadata about which files from the source location have been successfully loaded into the target Delta table. On each invocation, it compares the set of files in the source location against its internal tracking, loading only new files that have not been previously ingested.^[copy-into-databricks-on-aws.md]

Key characteristics:

- **File-level deduplication**: Skipping is based on file identity, not content hash. Modified files are still skipped.^[copy-into-databricks-on-aws.md]
- **Persistent tracking**: The ingestion history persists across cluster restarts and sessions, as it is stored in the Delta table metadata.
- **Transactional guarantees**: The load operation is atomic — if a `COPY INTO` fails, any files that were partially loaded are not marked as complete, allowing clean retry.

## Concurrent Invocations

`COPY INTO` supports concurrent invocations against the same table, provided that each invocation operates on a **distinct set of input files**. If concurrent invocations target overlapping files, a transaction conflict may occur.^[copy-into-databricks-on-aws.md]

Concurrent usage is appropriate when:

- Multiple data producers cannot easily coordinate and must write independently
- A very large directory is ingested sub-directory by sub-directory

For optimal performance, a single `COPY INTO` command processing multiple files generally outperforms running multiple concurrent commands with one file each. For directories with very large numbers of files, Auto Loader is recommended over `COPY INTO`.^[copy-into-databricks-on-aws.md]

## Validation Mode

`COPY INTO` supports a `VALIDATE` mode that checks whether data can be parsed and whether the schema matches the target table — without actually writing data to the table. This allows users to verify the correctness of a load before committing it.^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table
FROM source_location
FILEFORMAT = data_source
VALIDATE ALL
```

Validation checks include:^[copy-into-databricks-on-aws.md]

- Whether the data can be parsed
- Whether the schema matches the table or requires schema evolution
- Whether all nullability and check constraints are met

A subset of rows can be validated using `VALIDATE num_rows ROWS` (e.g., `VALIDATE 15 ROWS`), which returns a preview of up to 50 rows.^[copy-into-databricks-on-aws.md]

## Schema Evolution

By default, `COPY INTO` requires the source data schema to match the target table schema. Schema evolution can be enabled using the `mergeSchema` copy option:^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table
FROM source_location
FILEFORMAT = data_source
COPY_OPTIONS ('mergeSchema' = 'true')
```

When enabled, the target table schema evolves according to the incoming data, adding new columns as needed.^[copy-into-databricks-on-aws.md]

## Best Practices

### Use for Retryable Pipelines

Idempotent loading is the foundation of robust data pipelines. Schedule `COPY INTO` to run on a regular cadence (e.g., hourly or daily) — if one run fails, the next run will pick up only the new files, and no data is lost or duplicated.^[copy-into-databricks-on-aws.md]

### Validate Before Loading

Use the `VALIDATE` option in development or when adding new data sources to catch schema mismatches or parsing errors before they affect production tables.^[copy-into-databricks-on-aws.md]

### Avoid Overlapping Concurrent Loads

When using concurrent `COPY INTO` invocations, ensure each invocation operates on a distinct set of files to avoid transaction conflicts.^[copy-into-databricks-on-aws.md]

## Limitations

- **Modified files are skipped**: If a file in the source location is updated after being loaded, `COPY INTO` does not re-load it. For use cases requiring re-ingestion of changed files, use `force = true` or consider Auto Loader's change detection.
- **File limit with `FILES` keyword**: When specifying files explicitly with `FILES`, the list is limited to 1000 files. For larger sets, use a glob `PATTERN` instead.^[copy-into-databricks-on-aws.md]

## Related Concepts

- [[COPY INTO Command|COPY INTO]] — The SQL command that implements idempotent data loading
- Auto Loader — An alternative incremental ingestion tool with change detection and schema inference
- [[Delta Lake]] — The storage layer that provides transactional guarantees for idempotent loads
- Data Ingestion Patterns — Broader strategies for loading data into data lakes and warehouses
- Idempotency — The general computing concept of operations that produce the same result regardless of how many times they are applied
- Schema Evolution — Techniques for handling changing data schemas during ingestion

## Sources

- copy-into-databricks-on-aws.md
```

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
