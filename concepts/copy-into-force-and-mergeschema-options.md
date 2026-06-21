---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc93022d89a5004e3a5f3e9caa6b8cff07a7ce93de8cd4136e9aca4943623f71
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-force-and-mergeschema-options
    - mergeSchema Options and COPY INTO FORCE
    - CIFAMO
  citations:
    - file: copy-into-databricks-on-aws.md
      start: 9
      end: 10
    - file: copy-into-databricks-on-aws.md
      start: 125
      end: 127
    - file: copy-into-databricks-on-aws.md
      start: 128
      end: 130
    - file: L125-L130
title: COPY INTO FORCE and mergeSchema Options
description: Copy options to disable idempotency (force) or enable automatic schema evolution (mergeSchema) during ingestion.
tags:
  - databricks
  - schema-evolution
  - data-ingestion
timestamp: "2026-06-19T17:53:34.856Z"
---

# COPY INTO FORCE and mergeSchema Options

The `COPY INTO` command supports two key `COPY_OPTIONS`: `force` and `mergeSchema`. These options modify the default behavior of the command, which is retryable and idempotent by default — files that have already been loaded are skipped, even if they have been modified since. ^[copy-into-databricks-on-aws.md#L9-L10]

## `force` Option

The `force` option is a boolean (`true`/`false`) with a default value of `false`. When set to `true`, the idempotency guarantee is disabled: files are loaded regardless of whether they have been loaded before. ^[copy-into-databricks-on-aws.md#L125-L127]

```sql
COPY INTO my_table
FROM 's3://my-bucket/data'
FILEFORMAT = CSV
COPY_OPTIONS ('force' = 'true')
```

This option is useful when you need to re-ingest previously loaded files, for example after schema changes or data corrections. However, because it bypasses deduplication, use it with caution to avoid duplicate records. ^[copy-into-databricks-on-aws.md#L125-L127]

## `mergeSchema` Option

The `mergeSchema` option is also a boolean with a default value of `false`. When set to `true`, the schema of the target [Delta Lake](/concepts/delta-lake.md) table can evolve according to the schema of the incoming data. ^[copy-into-databricks-on-aws.md#L128-L130]

```sql
COPY INTO my_table
FROM 's3://my-bucket/data'
FILEFORMAT = JSON
COPY_OPTIONS ('mergeSchema' = 'true')
```

This option allows new columns present in the source files to be added to the target table automatically, enabling schema evolution without manual `ALTER TABLE` statements. It is part of [Delta Lake](/concepts/delta-lake.md)'s schema enforcement and evolution capabilities. ^[copy-into-databricks-on-aws.md#L128-L130]

## Interaction and Best Practices

- When both `force` and `mergeSchema` are set to `true`, existing data is reloaded and the table schema may evolve on each load. This combination can be used for repeated ingestion of evolving source data.
- For typical incremental ingestion, keep `force = false` (the default) to maintain idempotency, and use `mergeSchema = true` only when the source schema changes frequently.
- If you need to re-ingest only a subset of files, specify the file names with the `FILES` option instead of using `force`. ^[copy-into-databricks-on-aws.md#L9-L10, L125-L130]

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) — The complete SQL command reference
- [Delta Lake Schema Enforcement](/concepts/delta-table-schema-requirements.md) — How Delta Lake manages schema validation and evolution
- Auto Loader — An alternative incremental ingestion tool that supports schema evolution and file discovery
- [Idempotent Data Loading](/concepts/idempotent-data-loading.md) — The default behavior of `COPY INTO` that prevents duplicate loads
- Format Options — Additional data source reader options for `COPY INTO`

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md:9-10](/references/copy-into-databricks-on-aws-02102312.md)
2. [copy-into-databricks-on-aws.md:125-127](/references/copy-into-databricks-on-aws-02102312.md)
3. [copy-into-databricks-on-aws.md:128-130](/references/copy-into-databricks-on-aws-02102312.md)
4. L125-L130
