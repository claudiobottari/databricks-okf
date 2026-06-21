---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a637bed3a555115f21d63a48f7c35ca203f16fef737e9ec53022a38dd7908f1
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - liquid-clustering-enablement-on-existing-tables
    - LCEOET
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: Liquid Clustering Enablement on Existing Tables
description: Enabling liquid clustering on an existing Delta table requires using overwrite mode with the overwriteSchema option set to true.
tags:
  - delta-lake
  - clustering
  - data-optimization
timestamp: "2026-06-19T18:26:18.242Z"
---

# Liquid Clustering Enablement on Existing Tables

**Liquid Clustering Enablement on Existing Tables** refers to the process of enabling [Liquid Clustering](/concepts/liquid-clustering.md) on a Delta table that was previously created without clustering, or that has an existing partitioning scheme. This operation requires specific write mode settings to avoid the `DELTA_METADATA_MISMATCH` error condition.

## Overview

When attempting to enable liquid clustering on an existing Delta table, Databricks may raise the `DELTA_METADATA_MISMATCH` error with the `ENABLE_LIQUID` sub-condition. This occurs because the table's metadata does not match the clustering configuration being applied during the write operation. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Condition

The specific error message for this scenario is:

```
ENABLE_LIQUID: To enable clustering on the existing table, please use "overwrite" mode and set: '.option("overwriteSchema", "true")'.
```

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Solution

To successfully enable liquid clustering on an existing table, you must use **overwrite mode** with the `overwriteSchema` option set to `true`. This allows the write operation to modify the table's metadata to include the clustering configuration. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### Example

```python
df.write \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .option("clusterBy", ["column1", "column2"]) \
  .saveAsTable("your_table_name")
```

## Related Error Conditions

The `DELTA_METADATA_MISMATCH` error class includes several other sub-conditions that may be encountered during similar operations:

- **ACL_ENABLED**: Table ACLs prevent automatic schema migration; use `ALTER TABLE` instead.
- **OVERWRITE_REQUIRED**: Schema or partitioning changes require `overwriteSchema` to be set to `true`.
- **PARTITIONING_MISMATCH**: Partition columns in the write operation do not match the table's existing partition columns.
- **SCHEMA_MISMATCH**: The schema of the data being written does not match the table schema; use `mergeSchema` or enable auto-merge.

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Liquid Clustering](/concepts/liquid-clustering.md) — The clustering mechanism for optimizing data layout in Delta tables.
- [Delta Table Metadata](/concepts/delta-lake-external-metadata.md) — The schema and configuration information stored with each Delta table.
- Schema Migration — The process of evolving a table's schema to accommodate new data.
- Overwrite Mode — A write mode that replaces existing data in a table.
- [Delta Lake Error Conditions](/concepts/delta-error-sub-conditions.md) — The broader category of error conditions for Delta Lake operations.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
