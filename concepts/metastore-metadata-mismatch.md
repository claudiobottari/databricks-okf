---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2619669a9cad571c6d2baa0c3e64af8ec08443d84151b4d9b8d042feb44fcf3
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-metadata-mismatch
    - MMM
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Metastore Metadata Mismatch
description: An error (convertMetastoreMetadataMismatchException) thrown when the catalog metadata differs from the Delta Lake transaction log metadata during conversion, which can be overridden with a configuration flag.
tags:
  - delta-lake
  - error-handling
  - metadata
timestamp: "2026-06-19T17:52:38.030Z"
---

# [Metastore](/concepts/metastore.md) Metadata Mismatch

**Metastore Metadata Mismatch** is an error condition that occurs when running the `CONVERT TO DELTA` command on a directory that has already been converted to a [Delta Lake](/concepts/delta-lake.md) table, but the metadata stored in the [Hive metastore](/concepts/built-in-hive-metastore.md) (catalog) differs from the metadata recorded in the Delta transaction log. ^[convert-to-delta-databricks-on-aws.md]

## Error Behavior

When a `CONVERT TO DELTA` operation is executed on a path that already contains a Delta transaction log, the command normally detects this and should skip the conversion. However, if the catalog metadata (such as schema or table properties) disagrees with the Delta log’s own metadata, the command throws a `convertMetastoreMetadataMismatchException`. ^[convert-to-delta-databricks-on-aws.md]

This exception is thrown because the conversion process populates catalog information into the Delta transaction log at conversion time, and a mismatch indicates that the catalog has been updated independently without updating the Delta log. ^[convert-to-delta-databricks-on-aws.md]

## Workaround

If you are using Databricks Runtime and want `CONVERT TO DELTA` to overwrite the existing metadata in the Delta transaction log (in effect, forcing the log to match the catalog), you can set the SQL configuration:

```sql
SET spark.databricks.delta.convert.metadataCheck.enabled = false;
```

^[convert-to-delta-databricks-on-aws.md]

Setting this to `false` disables the metadata consistency check and allows the conversion to proceed, overwriting the Delta transaction log metadata with the catalog’s current metadata. This should be used with caution, as it may cause inconsistencies if the catalog metadata is not the intended source of truth. ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) – The command that converts Parquet or Iceberg tables to Delta Lake format.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format providing ACID transactions and metadata management.
- VACUUM – A Delta Lake command that removes files not tracked by the transaction log; files made invisible by a metadata mismatch could be removed.
- [Liquid Clustering](/concepts/liquid-clustering.md) – A recommended method to reorganize data and generate statistics after conversion.
- [Delta transaction log](/concepts/delta-transaction-log.md) – The core metadata store for Delta Lake tables.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
