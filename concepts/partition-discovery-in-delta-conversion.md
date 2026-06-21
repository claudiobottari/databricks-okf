---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 490c724214002e8beea02a5ba8d24eea431cab08b64d72a9fc1cfdf979652ad3
  pageDirectory: concepts
  sources:
    - convert-to-delta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-discovery-in-delta-conversion
    - PDIDC
  citations:
    - file: convert-to-delta-databricks-on-aws.md
title: Partition Discovery in Delta Conversion
description: How CONVERT TO DELTA handles partitioning information, requiring PARTITIONED BY for path-based conversions and optionally loading from the metastore for registered tables.
tags:
  - delta-lake
  - partitioning
  - data-organization
timestamp: "2026-06-19T17:52:37.894Z"
---

# Partition Discovery in Delta Conversion

**Partition Discovery in Delta Conversion** refers to the process by which the `CONVERT TO DELTA` command identifies and validates the partitioning scheme of an existing Apache Parquet or Apache Iceberg table when converting it to a [Delta Lake](/concepts/delta-lake.md) table. The command must correctly discover the partition columns to build an accurate Delta Lake transaction log.

## Overview

When converting a Parquet table to Delta Lake, the `CONVERT TO DELTA` command needs to know the partitioning structure of the source data. Partition discovery determines which columns define the partitioning scheme and validates that the directory structure on disk matches the expected partition layout. ^[convert-to-delta-databricks-on-aws.md]

## Discovery Methods

### From the [Metastore](/concepts/metastore.md)

When the `table_name` parameter is a qualified table identifier (a table registered in the [Metastore](/concepts/metastore.md)), partition specifications are loaded automatically from the [Metastore](/concepts/metastore.md). The `PARTITIONED BY` clause is optional in this case. ^[convert-to-delta-databricks-on-aws.md]

### From the `PARTITIONED BY` Clause

When the `table_name` is a path to a Parquet file directory (rather than a [Metastore](/concepts/metastore.md) table), the `PARTITIONED BY` clause is **required** for partitioned data. The user must explicitly specify the partition columns and their data types. ^[convert-to-delta-databricks-on-aws.md]

### From Iceberg Manifests

For Iceberg tables whose underlying file format is Parquet, the converter generates the Delta Lake transaction log based on the Iceberg table's native file manifest, schema, and partitioning information. You do not need to provide partitioning information for Iceberg tables. ^[convert-to-delta-databricks-on-aws.md]

## Validation

The conversion process aborts and throws an exception if the directory structure does not conform to the provided or loaded `PARTITIONED BY` specification. This validation ensures that the discovered partition scheme accurately reflects the physical data layout. ^[convert-to-delta-databricks-on-aws.md]

## Historical Behavior

In Databricks Runtime 11.1 and below, `PARTITIONED BY` was a **required** argument for all partitioned data, regardless of whether the table was registered in the [Metastore](/concepts/metastore.md). ^[convert-to-delta-databricks-on-aws.md]

## Related Concepts

- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — The command that performs partition discovery during conversion.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The metadata layer that records partition information after conversion.
- Partitioned Tables in Delta Lake — How Delta Lake manages partitioned data.
- [Liquid Clustering](/concepts/liquid-clustering.md) — A recommended alternative to traditional partitioning for data layout optimization.
- VACUUM — Cleanup operation that removes files not tracked by Delta Lake.

## Sources

- convert-to-delta-databricks-on-aws.md

# Citations

1. [convert-to-delta-databricks-on-aws.md](/references/convert-to-delta-databricks-on-aws-4b099753.md)
