---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 02a721c522bdf52696da09b6f42af9ae1b76dbf5299c19497bedb4602cb407e6
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-schema-migration
    - DLSM
    - Delta Lake schema validation
    - Delta Lake Schema Evolution
    - Delta Lake Table Schema Evolution
    - Delta Lake schema evolution
    - Schema migration
    - schema migration
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: Delta Lake Schema Migration
description: The process of evolving a Delta table's schema to match incoming data, controlled via DataFrameWriter options (mergeSchema, overwriteSchema) or session configurations.
tags:
  - delta-lake
  - schema-evolution
  - data-engineering
timestamp: "2026-06-19T18:26:15.395Z"
---

---
title: Delta Lake Schema Migration
summary: The process of evolving a Delta table's schema to match incoming data, controlled via DataFrameWriter/DataStreamWriter options like mergeSchema and overwriteSchema.
sources:
  - delta_metadata_mismatch-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:21:28.004Z"
updatedAt: "2026-06-22T10:00:00.000Z"
tags:
  - delta-lake
  - schema-evolution
  - databricks
aliases:
  - delta-lake-schema-migration
  - DLSM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Lake Schema Migration

**Delta Lake Schema Migration** is the process of modifying a Delta table’s schema — adding new columns, changing data types, or adjusting partitioning — during write operations. When the schema of incoming data does not match the target table’s schema, Delta Lake raises a `DELTA_METADATA_MISMATCH` error. The error message provides a specific sub‑reason that determines the required corrective action. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## DELTA_METADATA_MISMATCH Error

This error (SQLSTATE: 42KDG) occurs when a metadata mismatch is detected while writing to a Delta table. Each sub‑reason dictates a different resolution. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### ACL_ENABLED

Table ACLs (Access Control Lists) are enabled in the cluster, which disables automatic schema migration. The solution is to use the `ALTER TABLE` command to manually change the table schema. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### ENABLE_LIQUID

An attempt was made to enable [Liquid Clustering](/concepts/liquid-clustering.md) on an existing table without using overwrite mode. The fix is to write using `"overwrite"` mode and set the option `.option("overwriteSchema", "true")`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### OVERWRITE_REQUIRED

Schema overwrite or partition change was attempted without setting `overwriteSchema` to `true`. The solution is to add `.option("overwriteSchema", "true")` to the write operation. Note that the schema cannot be overwritten when using `replaceWhere`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### PARTITIONING_MISMATCH

The partition columns provided in the write operation do not match the partition columns of the existing table. The error shows both the provided and the table’s partition columns. To resolve, ensure partition columns match exactly, or use overwrite mode with `overwriteSchema` to repartition. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### SCHEMA_MISMATCH

The data schema is structurally different from the table schema (e.g., new columns, differing data types). The error includes both the table schema and the data schema for comparison. To enable automatic schema migration:
- For `DataFrameWriter` or `DataStreamWriter`, set `.option("mergeSchema", "true")`.
- For other operations (e.g., SQL inserts), set the session configuration `spark.databricks.delta.schema.autoMerge.enabled` to `"true"`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Schema Migration Options

Delta Lake provides two primary write‑time strategies for handling schema changes:

- **Merge schema** (`mergeSchema`): Automatically adds new columns and resolves compatible type changes. Enabled via the `.option("mergeSchema", "true")` writer option or the session configuration `spark.databricks.delta.schema.autoMerge.enabled`.
- **Overwrite schema** (`overwriteSchema`): Completely replaces the table schema with the data schema. Requires write mode `overwrite` and the option `.option("overwriteSchema", "true")`.

Both strategies are subject to the error conditions described above, and the appropriate sub‑error guides which option to use. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The ACID‑compliant storage layer that provides schema enforcement.
- Schema Evolution – The general practice of adapting a table schema over time.
- [Delta Lake Merge Schema](/concepts/delta-lake-merge-into-upsert.md) – Automatic schema merging via the `mergeSchema` option.
- [Delta Lake Overwrite Schema](/concepts/overwriteschema-option.md) – Full schema replacement via the `overwriteSchema` option.
- [Liquid Clustering](/concepts/liquid-clustering.md) – A clustering technique that requires overwrite mode when enabling on existing tables.
- ALTER TABLE – SQL command for manual schema changes.
- Partitioning in Delta Lake – How partition columns interact with schema migration.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
