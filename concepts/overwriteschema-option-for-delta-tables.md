---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 338540e5dc1b67009aeff22b00a5d7597fc3088f4ad78804e1c181c628746b11
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - overwriteschema-option-for-delta-tables
    - OOFDT
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: overwriteSchema Option for Delta Tables
description: A Spark DataFrameWriter option used to overwrite an existing Delta table's schema or change its partitioning.
tags:
  - delta-lake
  - schema-evolution
  - spark
timestamp: "2026-06-19T10:07:08.302Z"
---

---
title: overwriteSchema Option for Delta Tables
summary: The `overwriteSchema` option controls whether a Delta table's schema or partitioning can be replaced during a write, and is required for enabling liquid clustering on existing tables.
sources:
  - delta_metadata_mismatch-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:00:00.000Z"
updatedAt: "2026-06-19T14:00:00.000Z"
tags:
  - delta-lake
  - schema-evolution
  - write-options
aliases:
  - overwriteschema-option-for-delta-tables
  - OSOFDT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# overwriteSchema Option for Delta Tables

The **`overwriteSchema`** option is a configuration flag used with `DataFrameWriter` or `DataStreamWriter` when writing to a [Delta table](/concepts/delta-lake-table.md). Setting this option to `true` allows the write operation to replace the target table's schema or partitioning scheme.

## Use Cases

### Overwriting Schema or Changing Partitioning

To overwrite the existing schema of a Delta table, or to change its partitioning columns, you must set `overwriteSchema` to `true`. The standard syntax is:

```scala
df.write
  .option("overwriteSchema", "true")
  .mode("overwrite")
  .save("/path/to/table")
```

If `overwriteSchema` is not set when attempting to overwrite the schema or change partitioning, the write fails with a `DELTA_METADATA_MISMATCH` error (subtype `OVERWRITE_REQUIRED`). ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### Enabling Liquid Clustering on an Existing Table

When enabling [Liquid Clustering](/concepts/liquid-clustering.md) on a Delta table that already exists, the write must use `overwrite` mode and include `overwriteSchema = true`. The error message for this case (subtype `ENABLE_LIQUID`) explicitly instructs users to set `.option("overwriteSchema", "true")`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Limitations

- **`replaceWhere` conflict**: The `overwriteSchema` option cannot be used together with the `replaceWhere` option. If both are specified, the write fails with `OVERWRITE_REQUIRED` and a note that "the schema can't be overwritten when using 'replaceWhere'." ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- **ACL‑enabled clusters**: When Table ACLs are enabled on a cluster, automatic schema migration (including `overwriteSchema`) is not allowed. Use `ALTER TABLE` instead to change the schema. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Relationship to `mergeSchema`

`overwriteSchema` is distinct from [mergeSchema](/concepts/mergeschema-option.md), which handles schema evolution when appending data. The `mergeSchema` option is recommended for schema migration when the write is not in overwrite mode. For overwrite operations, `overwriteSchema` must be explicitly set. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Error Subtypes

When write operations cause a metadata mismatch, the Delta engine returns one of the following subtypes of `DELTA_METADATA_MISMATCH`:

- `OVERWRITE_REQUIRED` – Schema or partitioning mismatch; set `overwriteSchema` to `true`.
- `ENABLE_LIQUID` – Enable clustering on an existing table; set `overwriteSchema` to `true`.
- `SCHEMA_MISMATCH` – Schema evolution needed; use `mergeSchema` instead.
- `PARTITIONING_MISMATCH` – Partition columns differ; use `overwriteSchema`.
- `ACL_ENABLED` – ACLs prevent automatic migration; use `ALTER TABLE`.

## Related Concepts

- Delta table schema evolution
- [mergeSchema Option](/concepts/mergeschema-option.md)
- [replaceWhere option](/concepts/replace-where-selective-overwrite.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- Delta table partitioning
- DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH error

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
