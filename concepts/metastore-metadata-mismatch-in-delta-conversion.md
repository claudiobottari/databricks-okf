---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f23d81212954fae65b4bd59d45b55cbba2450a9318f695081e2eef1f08df0285
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-metadata-mismatch-in-delta-conversion
    - MMMIDC
    - ConvertMetastoreMetadataMismatchException
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Metastore Metadata Mismatch in Delta Conversion
description: An error condition (convertMetastoreMetadataMismatchException) that occurs when catalog metadata differs from the Delta Lake transaction log metadata during or after CONVERT TO DELTA.
tags:
  - delta-lake
  - error-handling
  - metadata
timestamp: "2026-06-19T09:24:25.919Z"
---

# [Metastore](/concepts/metastore.md) Metadata Mismatch in Delta Conversion

**Metastore Metadata Mismatch in Delta Conversion** is an error that occurs when running `CONVERT TO DELTA` on a directory that has already been converted to a Delta table, but the schema or table properties stored in the Unity Catalog (or Hive [Metastore](/concepts/metastore.md)) differ from those recorded in the existing Delta Lake transaction log. The error is raised as a `convertMetastoreMetadataMismatchException`. ^[convert-to-delta-databricks-on-aws.md]

## Cause

The `CONVERT TO DELTA` command populates the Delta Lake transaction log with catalog information, such as the schema and table properties from the [Metastore](/concepts/metastore.md). If the underlying directory was previously converted and already contains a Delta transaction log whose metadata is inconsistent with the current [Metastore](/concepts/metastore.md) metadata, the conversion process cannot reconcile the differences. This protects against accidental overwrites of existing Delta metadata that might break downstream readers. ^[convert-to-delta-databricks-on-aws.md]

## Solution

If you are certain that the [Metastore](/concepts/metastore.md) metadata should override the existing Delta transaction log metadata, you can disable the metadata consistency check by setting the following SQL configuration before running the `CONVERT` statement:

```sql
SET spark.databricks.delta.convert.metadataCheck.enabled = false;
```

This configuration is available only in Databricks Runtime. After setting it, `CONVERT TO DELTA` will overwrite the existing Delta metadata with the catalog information. Note that this bypasses a safety check, so use it with caution. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – The command that triggers this error.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that maintains the transaction log.
- VACUUM – Cleanup operation that may be affected by metadata inconsistencies.
- [Delta transaction log](/concepts/delta-transaction-log.md) – The central source of truth for Delta table metadata.
- [Liquid Clustering](/concepts/liquid-clustering.md) – Recommended after conversion to reorganize data and generate statistics.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
