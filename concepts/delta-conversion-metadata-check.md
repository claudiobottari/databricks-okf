---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d0fcce7c91710903d5d8324f72bb8faf719c3aeb4faf7def30f08f55c6d01a5
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-conversion-metadata-check
    - DCMC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Delta Conversion Metadata Check
description: A validation mechanism in CONVERT TO DELTA that compares catalog metadata with existing Delta Lake transaction log metadata, throwing a convertMetastoreMetadataMismatchException on mismatch, which can be overridden via Spark configuration.
tags:
  - delta-lake
  - metadata
  - configuration
timestamp: "2026-06-19T14:26:21.900Z"
---

# Delta Conversion Metadata Check

**Delta Conversion Metadata Check** is a Databricks SQL configuration parameter that controls how the `CONVERT TO DELTA` command handles metadata conflicts between an existing Delta Lake transaction log and external catalog metadata.

## Overview

When you run `CONVERT TO DELTA` on an Apache Parquet table that has already been converted to a Delta table, Databricks checks whether the metadata in the underlying Delta Lake transaction log matches the metadata stored in the catalog (such as schema and table properties). If the directory has already been converted to Delta Lake and its metadata differs from the catalog metadata, the conversion process throws a `convertMetastoreMetadataMismatchException` to prevent data inconsistency.^[convert-to-delta-databricks-on-aws.md]

## Configuration

By default, the metadata check is **enabled** (`true`). This means that when the underlying directory has already been converted to Delta Lake, Databricks validates that the transaction log metadata matches the catalog metadata before proceeding. If a mismatch is detected, the conversion fails with an error.^[convert-to-delta-databricks-on-aws.md]

### Overriding the Check

To override the existing metadata in the Delta Lake transaction log and force a conversion to proceed, set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to `false`:^[convert-to-delta-databricks-on-aws.md]

```sql
SET spark.databricks.delta.convert.metadataCheck.enabled = false;
```

As noted in the [Databricks documentation](https://docs.databricks.com/aws/en/sql/language-manual/delta-convert-to-delta): "While using Databricks Runtime, if you want `CONVERT` to overwrite the existing metadata in the Delta Lake transaction log, set the SQL configuration `spark.databricks.delta.convert.metadataCheck.enabled` to false."

## When to Use

You should only disable the metadata check when you are certain that:

- The existing Delta transaction log metadata is outdated or incorrect
- You want to overwrite it with the catalog metadata
- You understand the risks of potential data inconsistency

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The command that performs the conversion
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The metadata created during conversion
- [ConvertMetastoreMetadataMismatchException](/concepts/metastore-metadata-mismatch.md) — The error thrown when metadata mismatches occur
- [Metastore catalog](/concepts/metastore.md) — External table metadata storage
- VACUUM — Cleanup operation for untracked files after conversion

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
