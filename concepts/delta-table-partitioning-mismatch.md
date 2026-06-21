---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 114fd007c134dbb296f7f4a041e6e66f9e21d9c2a089edbbfadb185568f87437
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-partitioning-mismatch
    - DTPM
    - Delta Table Partitioning
    - Delta table partitioning
    - Table partitioning
    - partitioning
    - partitioning scheme
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: Delta Table Partitioning Mismatch
description: An error subtype indicating that the partition columns provided during a write do not match the existing partition columns of the Delta table.
tags:
  - delta-lake
  - partitioning
  - error-handling
timestamp: "2026-06-19T10:07:06.228Z"
---

# Delta Table Partitioning Mismatch

**Delta Table Partitioning Mismatch** is a specific sub-condition of the DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH error that occurs when the partition columns specified in a write operation do not match the existing partition columns of the target [Delta Lake](/concepts/delta-lake.md) table. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, the system reports:

```
DELTA_METADATA_MISMATCH
PARTITIONING_MISMATCH
Partition columns do not match the partition columns of the table.
Given: <provided>
Table: <original>
```

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Cause

The error is raised during a write to a Delta table when the partitioning specification in the write operation (e.g., `partitionBy`) differs from the partitioning already defined on the table. Because Delta Lake enforces schema consistency by default, any attempt to change the partitioning after the table is created will trigger this error unless the write explicitly allows schema and partitioning changes. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Solution

To change the partitioning of an existing Delta table, use the `overwrite` mode with the `.option("overwriteSchema", "true")` setting. This tells Delta Lake to overwrite both the data and the table metadata, including the partitioning scheme. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

```python
df.write \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .save("/path/to/table")
```

Note that when using `replaceWhere`, the schema cannot be overwritten. For partitioning changes, avoid `replaceWhere` and use a full overwrite instead. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH — The parent error class that includes other mismatch conditions (e.g., `SCHEMA_MISMATCH`, `ACL_ENABLED`, `ENABLE_LIQUID`).
- Delta Table Schema Evolution — General mechanisms for modifying table schemas.
- Partitioning in Delta Lake — Best practices for choosing partition columns.
- [overwriteSchema Option](/concepts/overwriteschema-option.md) — The Spark DataFrameWriter option used to permit schema and partitioning changes.
- replaceWhere — A partial overwrite option that prevents schema changes.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
