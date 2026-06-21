---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 346f015862b3423304bf4441ddb98d3fbbe7834a99939cb2bfa99895e8f3d882
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-schema-migration-via-mergeschema
    - DSMVM
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: Delta Schema Migration via mergeSchema
description: The mechanism to enable automatic schema migration when writing to Delta tables using the mergeSchema option or session configuration.
tags:
  - delta-lake
  - schema-evolution
  - data-ingestion
timestamp: "2026-06-19T10:07:31.933Z"
---

# Delta Schema Migration via mergeSchema

**Delta Schema Migration via mergeSchema** is a technique for resolving schema mismatches when writing data to an existing [Delta Lake](/concepts/delta-lake.md) table. When the schema of incoming data does not match the table's schema, Delta Lake raises a `DELTA_METADATA_MISMATCH` error condition with subtype `SCHEMA_MISMATCH`. Enabling `mergeSchema` allows automatic schema evolution, merging the data schema into the table schema during the write operation. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## How It Works

When writing to a Delta table, Delta Lake compares the schema of the incoming data against the existing table schema. If the schemas differ, Delta Lake raises a `SCHEMA_MISMATCH` error. To enable automatic schema migration, set the `mergeSchema` option to `true` on the DataFrameWriter or DataStreamWriter: ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

```python
df.write.option("mergeSchema", "true").mode("append").save("/path/to/table")
```

With `mergeSchema` enabled, Delta Lake automatically merges the schema of the incoming data into the existing table schema. This includes:
- Adding new columns present in the data but not in the table
- Updating column types where compatible
- Preserving existing columns that are not present in the incoming data

## When to Use `mergeSchema`

Use `mergeSchema` when you need to write data to an existing Delta table and the incoming data has:
- Additional columns not yet present in the table
- Evolving column types that are compatible with existing types

This is common in streaming scenarios, ETL pipelines, and data ingestion workflows where the schema may evolve naturally over time. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Alternative: Automatic Schema Merge via Session Configuration

For operations other than DataFrameWriter and DataStreamWriter, you can enable automatic schema merging by setting the session configuration: ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

```python
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
```

This setting enables schema migration across all operations in the session. See the [Delta Lake documentation](/concepts/databricks-delta-lake-documentation.md) specific to the operation for details. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Error Subtypes

The `DELTA_METADATA_MISMATCH` error condition includes several subtypes that describe different metadata conflicts: ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

| Error Subtype | Description |
|--------------|-------------|
| `SCHEMA_MISMATCH` | Schema of incoming data does not match table schema. Resolved by `mergeSchema`. |
| `PARTITIONING_MISMATCH` | Partition columns do not match the table's partition columns. |
| `OVERWRITE_REQUIRED` | Schema or partitioning changes require `.option("overwriteSchema", "true")`. |
| `ACL_ENABLED` | Table ACLs prevent automatic schema migration; use `ALTER TABLE` instead. |
| `ENABLE_LIQUID` | To enable clustering, use overwrite mode with `.option("overwriteSchema", "true")`. |

## Related Concepts

- [Delta Lake Schema Evolution](/concepts/delta-lake-schema-migration.md) – Broader strategies for handling schema changes over time
- Delta Lake Write Operations – Append, overwrite, and merge operations
- [Delta Table Partitioning](/concepts/delta-table-partitioning-mismatch.md) – How partitioning interacts with schema changes
- DataFrameWriter Options – Complete list of write configuration options
- Streaming Ingestion with Delta Lake – Schema evolution in streaming contexts

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
