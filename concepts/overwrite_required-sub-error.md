---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e22e5d6c33ef9ab93fb3406ffdca1a4efe4b5a671a4cb71993da5b3f7f1ab2d
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - overwrite_required-sub-error
    - OVERWRITE_REQUIRED sub-error
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: OVERWRITE_REQUIRED sub-error
description: A DELTA_METADATA_MISMATCH sub-error that occurs when schema or partitioning changes require setting overwriteSchema to true
tags:
  - databricks
  - delta-lake
  - schema-migration
  - error-messages
timestamp: "2026-06-19T15:06:43.503Z"
---

# OVERWRITE_REQUIRED Sub-Error

The `OVERWRITE_REQUIRED` sub-error is a specific condition of the DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition in [Delta Lake](/concepts/delta-lake.md) on Databricks. It occurs when a write operation attempts to change the table schema or partitioning without explicitly enabling schema overwrite. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Message

When this sub-error is triggered, Delta Lake returns the following guidance:

> To overwrite your schema or change partitioning, please set: '.option("overwriteSchema", "true")'.

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Cause

The `OVERWRITE_REQUIRED` sub-error is raised when a write operation to a Delta table would result in either:

- A change to the table schema (adding, removing, or modifying columns)
- A change to the table partitioning scheme

Delta Lake prevents automatic schema or partitioning changes during a write operation unless explicitly permitted by the user. This safeguard prevents accidental schema corruption or data loss. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Solution

To resolve the error, set the `.option("overwriteSchema", "true")` on the write operation. This explicitly allows Delta Lake to overwrite the existing schema with the new schema provided by the DataFrame being written.

For example, using the DataFrame API:

```python
df.write \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .saveAsTable("your_table")
```

Or using Spark SQL:

```sql
INSERT OVERWRITE TABLE your_table
  OPTIONS (overwriteSchema = true)
  SELECT * FROM source_data
```

## Important Limitation

The schema cannot be overwritten when using `replaceWhere`. If you are using `replaceWhere` for targeted data replacement, you must use alternative approaches to modify the schema. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Error Conditions

- DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition — The parent error class containing this sub-error
- `SCHEMA_MISMATCH` — A related sub-error for schema differences that can be resolved using schema merging
- `PARTITIONING_MISMATCH` — Another sub-error when partition columns do not match
- `ENABLE_LIQUID` — A sub-error for enabling clustering on existing tables
- `ACL_ENABLED` — A sub-error triggered when table ACLs prevent automatic schema migration

## Related Concepts

- [Delta Lake Schema Evolution](/concepts/delta-lake-schema-migration.md) — Overview of schema management in Delta tables
- DataFrame Write Modes — Different write modes in Spark DataFrames
- Table Partitioning in Delta Lake — How partitioning works and how to manage it

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
