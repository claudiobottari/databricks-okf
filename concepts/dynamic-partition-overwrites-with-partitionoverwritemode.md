---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f7258bc833c77807feb2a207bef04b740fd880acfebeaeaf9bc0fac693559c5
  pageDirectory: concepts
  sources:
    - selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-partition-overwrites-with-partitionoverwritemode
    - DPOWP
    - Dynamic Partition Overwrites
    - partitionOverwriteMode
  citations:
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
title: Dynamic Partition Overwrites with partitionOverwriteMode
description: Legacy approach using spark.sql.sources.partitionOverwriteMode=dynamic to replace only affected partitions during INSERT OVERWRITE operations.
tags:
  - delta-lake
  - data-engineering
  - spark
  - partitioning
timestamp: "2026-06-19T23:01:56.653Z"
---

# Dynamic Partition Overwrites with `partitionOverwriteMode` (Legacy)

**Dynamic Partition Overwrites with `partitionOverwriteMode`** is a legacy [Delta Lake](/concepts/delta-lake.md) data‑write mode available on classic Databricks compute. It allows you to overwrite only the partitions that are touched by the new data, leaving all other partitions unchanged. This mode is intended for **partitioned tables only** and is a subset of the newer dynamic data overwrite behavior. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Availability

This feature is supported in **Databricks Runtime 11.3 LTS and above**, but only on **classic compute** (not Databricks SQL warehouses or serverless compute). ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## How to Use

To enable dynamic partition overwrites, set the Spark session configuration `spark.sql.sources.partitionOverwriteMode` to `dynamic`. Alternatively, you can set the `DataFrameWriter` option `partitionOverwriteMode` to `dynamic` on a per‑write basis. If both are present, the query-specific option overrides the session-level configuration. The default value for this configuration is `static`. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

The following examples use partition overwrite mode:

- **SQL**:
  ```sql
  SET spark.sql.sources.partitionOverwriteMode = dynamic;
  INSERT OVERWRITE TABLE default.people10m SELECT * FROM morePeople;
  ```

- **Python**:
  ```python
  (df.write
    .mode("overwrite")
    .option("partitionOverwriteMode", "dynamic")
    .saveAsTable("default.people10m"))
  ```

- **Scala**:
  ```scala
  df.write
    .mode("overwrite")
    .option("partitionOverwriteMode", "dynamic")
    .saveAsTable("default.people10m")
  ```

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Constraints and Behaviors

Keep the following limitations in mind when using `partitionOverwriteMode`:

- You **cannot** set `overwriteSchema` to `true` in the same operation.
- You **cannot** specify both `partitionOverwriteMode` and `replaceWhere` in the same `DataFrameWriter` operation. If a `replaceWhere` condition is provided, it takes precedence over the partition overwrite mode.
- Always validate that the data you are writing touches only the expected partitions. A single row in the wrong partition can unintentionally overwrite the entire partition.
- This mode works **only for partitioned tables**. Unpartitioned tables are not supported.

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Legacy Status and Recommendation

The `partitionOverwriteMode` approach is a **legacy feature**. It is superseded by the modern [Dynamic Data Overwrites](/concepts/replace-using-dynamic-data-overwrite.md) provided by the REPLACE USING statement (supported in Databricks Runtime 16.3+) and the [REPLACE ON](/concepts/create-or-replace-clone.md) statement (supported in 17.1+). These newer methods are compute‑independent, atomic, and work on Databricks SQL warehouses, serverless compute, and classic compute. They do not require setting a Spark session configuration. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

> **Warning**: When possible, use `INSERT REPLACE USING` instead of `INSERT OVERWRITE PARTITION` with `spark.sql.sources.partitionOverwriteMode=dynamic`. Partition overwrite may use stale data when partitioning changes. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Dynamic Data Overwrites](/concepts/replace-using-dynamic-data-overwrite.md) – The modern, generalised replacement for dynamic partition overwrites.
- REPLACE USING – Recommended atomic overwrite for matching key columns.
- [REPLACE ON](/concepts/create-or-replace-clone.md) – Recommended atomic overwrite for custom matching conditions, including NULL-safe equality.
- REPLACE WHERE – Selective overwrite based on an arbitrary boolean expression.
- INSERT OVERWRITE – The SQL command that can be combined with partition overwrite mode.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer providing these write capabilities.
- [Classic Compute](/concepts/classic-compute-forecasting.md) – The compute environment where the legacy `partitionOverwriteMode` is supported.
- [partitionOverwriteMode](/concepts/dynamic-partition-overwrites-with-partitionoverwritemode.md) – The Spark configuration and DataFrameWriter option that controls dynamic partition overwrites.

## Sources

- selectively-overwrite-data-with-delta-lake-databricks-on-aws.md

# Citations

1. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
