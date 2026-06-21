---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abb24e579bae42fd595f6ec2b4d11ba2e7b1f1eadf7a6b982510ee5631719f88
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-copy_options
    - CIC
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO COPY_OPTIONS
description: Configuration options for COPY INTO including force (disable idempotency) and mergeSchema (evolve schema for incoming data).
tags:
  - sql
  - configuration
  - data-ingestion
timestamp: "2026-06-19T14:27:15.560Z"
---

# COPY INTO COPY_OPTIONS

**COPY_OPTIONS** is an optional clause of the [`COPY INTO`](/sql/language-manual/delta-copy-into) command that controls the operational behavior of the data loading operation. It specifies a set of key-value pairs that modify how `COPY INTO` handles file loading, schema evolution, and idempotency. ^[copy-into-databricks-on-aws.md]

## Syntax

```sql
COPY_OPTIONS ( { copy_option = value } [, ...] )
```

The clause appears after the `FORMAT_OPTIONS` clause in a `COPY INTO` statement. ^[copy-into-databricks-on-aws.md]

## Available Options

### `force`

- **Type**: Boolean
- **Default**: `false`

When set to `true`, the idempotency guarantee of `COPY INTO` is disabled. Files in the source location are loaded regardless of whether they have been loaded before. Normally, `COPY INTO` automatically tracks which files have already been processed and skips them on subsequent runs to ensure exactly-once semantics. Forcing re-load overwrites existing data in the target Delta table, which can lead to duplicates if the target table does not have a merge key or if duplicate handling is not designed. ^[copy-into-databricks-on-aws.md]

Use `force = true` only in scenarios where you intentionally want to reprocess files, such as after correcting a data quality issue in the source files or when resetting a pipeline.

### `mergeSchema`

- **Type**: Boolean
- **Default**: `false`

When set to `true`, the schema of the target Delta table can evolve to accommodate new columns present in the incoming data. If `mergeSchema` is `false` (the default), `COPY INTO` will fail when the source files have a schema that does not match the target table, unless an explicit column list or `BY POSITION` mapping is used. ^[copy-into-databricks-on-aws.md]

Schema evolution adds new columns to the end of the table schema. It does not drop or rename existing columns. This option is equivalent to enabling schema evolution in [Delta Lake](/concepts/delta-lake.md)'s write operations.

## Usage Recommendations

- Use `force` sparingly and only when you understand the deduplication implications. Production pipelines should rely on the default idempotent behavior.
- Use `mergeSchema` when you expect schema drift in your source data and want `COPY INTO` to adapt automatically. For strict schema control, keep it disabled and manage schema changes through explicit `ALTER TABLE` statements.
- When using both `force` and `mergeSchema` together, ensure that the target table's data quality requirements can tolerate repeated ingestion of the same files.

## Example

```sql
COPY INTO sales_data
FROM '/path/to/sales_files'
FILEFORMAT = CSV
FORMAT_OPTIONS ('header' = 'true')
COPY_OPTIONS ('mergeSchema' = 'true');
```

This loads CSV files from the given path, evolving the target table schema if the incoming files contain new columns.

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) — The full command syntax and parameters
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides schema evolution, idempotency, and transactional guarantees
- Auto Loader — An alternative incremental ingestion tool for large volumes of files
- Schema evolution — The broader concept of adapting table schemas to changing data
- Data loading patterns with COPY INTO — Common use cases and best practices

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
