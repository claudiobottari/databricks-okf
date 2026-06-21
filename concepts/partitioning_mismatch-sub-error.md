---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8888633a691a9a0dc2f91500536d3e3a7f2a5ac8c2dddda194e207a018ec06d6
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partitioning_mismatch-sub-error
    - PARTITIONING_MISMATCH Error
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: PARTITIONING_MISMATCH sub-error
description: A DELTA_METADATA_MISMATCH sub-error that occurs when provided partition columns do not match the table's partition columns
tags:
  - databricks
  - delta-lake
  - partitioning
  - error-messages
timestamp: "2026-06-19T15:06:38.864Z"
---

# PARTITIONING_MISMATCH Sub-Error

**PARTITIONING_MISMATCH** is a sub-error of the DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition that occurs when writing to a Delta table where the partition columns specified in the write operation do not match the partition columns defined in the target table. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Message

The error returns the following message structure:

```
Partition columns do not match the partition columns of the table.

Given: <provided>
Table: <original>
```

where `<provided>` shows the partition columns from the write operation and `<original>` shows the existing partition columns of the table. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Cause

This error occurs when a write operation attempts to use a different set of partition columns than those already defined on the Delta table. For example, writing to a table partitioned by `date` with a DataFrame that specifies partitioning by `region` would trigger this sub-error. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Resolution

To resolve the PARTITIONING_MISMATCH error, set the `overwriteSchema` option to `true` in the write operation. This allows the schema and partitioning to be overwritten: ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

```python
df.write \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .save("/path/to/table")
```

Note that the schema cannot be overwritten when using `replaceWhere`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition — The parent error class for partitioning and schema conflicts.
- OVERWRITE_REQUIRED sub-error — A related sub-error that also requires `overwriteSchema` to be set.
- SCHEMA_MISMATCH sub-error — Another sub-error for schema differences that uses `mergeSchema` instead.
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) — Best practices for defining and managing partitions in Delta tables.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
