---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0cebe588d8d8645cb852e9fc74a751372cc2f0a4c06b885a0e8af1bdacfef7b7
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - enable_liquid-sub-error
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: ENABLE_LIQUID sub-error
description: A DELTA_METADATA_MISMATCH sub-error that occurs when trying to enable liquid clustering on an existing table without using overwrite mode
tags:
  - databricks
  - delta-lake
  - clustering
  - error-messages
timestamp: "2026-06-19T15:06:31.726Z"
---

# ENABLE_LIQUID sub-error

The **ENABLE_LIQUID sub-error** is a specific condition under the broader DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH error class. It occurs when a user attempts to enable [Liquid Clustering](/concepts/liquid-clustering.md) on an existing [Delta table](/concepts/delta-lake-table.md) without using the required overwrite mode. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Description

When writing to a Delta table with a write operation that attempts to enable Liquid Clustering, the engine detects a metadata mismatch because the table’s clustering specification differs from the new write configuration. The error message indicates that the schema or metadata must be overwritten to apply the clustering setting:

> To enable clustering on the existing table, please use "overwrite" mode and set: '.option("overwriteSchema", "true")'. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Cause

Liquid Clustering changes the physical layout of the Delta table by reorganizing data files according to the specified clustering columns. This transformation requires an overwrite of the table’s metadata (schema) to reflect the new clustering configuration. If the write operation is not explicitly configured to overwrite the schema, the engine raises the ENABLE_LIQUID sub-error to prevent unintended metadata changes. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error, the write operation must use **overwrite mode** and include the option `overwriteSchema` set to `true`. For example, when using the DataFrame writer:

```python
df.write \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .saveAsTable("your_table")
```

This instructs Delta Lake to replace the table’s schema and metadata, allowing the new clustering columns to be applied. Note that using `replaceWhere` in the same operation is not supported for schema overwrite. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH error class – The parent error class containing sub-errors like ENABLE_LIQUID.
- [Liquid Clustering](/concepts/liquid-clustering.md) – The feature that reorganizes data by clustering columns for improved query performance.
- [Delta table](/concepts/delta-lake-table.md) – The storage format for Delta Lake, which manages metadata and schema evolution.
- [Overwrite Schema](/concepts/overwriteschema-option.md) – The mode that allows altering a Delta table’s schema during a write operation.
- ALTER TABLE – Alternative DDL for changing table properties, though not sufficient for enabling Liquid Clustering from scratch.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
