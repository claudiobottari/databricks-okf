---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 461358cdb16eef1db479cf3b6ecc369d41c4546ac8834cc7657048122f4989d5
  pageDirectory: concepts
  sources:
    - selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-replacewhere-partition-only-overwrite
    - LRPO
  citations:
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
title: Legacy replaceWhere Partition-Only Overwrite
description: Older Delta Lake behavior where replaceWhere only works on partition columns, enabled by setting spark.databricks.delta.replaceWhere.dataColumns.enabled to false.
tags:
  - delta-lake
  - data-engineering
  - spark
  - legacy
timestamp: "2026-06-19T23:02:04.264Z"
---

# Legacy `replaceWhere` Partition-Only Overwrite

The **Legacy `replaceWhere` Partition-Only Overwrite** is a deprecated [Delta Lake](/concepts/delta-lake.md) write mode that restricts overwrite predicates to partition columns only. It is available only on **classic compute** (not on Databricks SQL warehouses or serverless compute). ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Behavior

When the legacy behavior is active, a `replaceWhere` option in a `DataFrameWriter` overwrites data that matches a predicate, but only over **partition columns**. Non‑partition columns cannot be used in the predicate. For example, the following code atomically replaces the month of January in a table partitioned by `date`:

```python
df.write.mode("overwrite") \
  .option("replaceWhere", "birthDate >= '2017-01-01' AND birthDate <= '2017-01-31'") \
  .saveAsTable("people10m")
```

Because `birthDate` is a partition column, this command succeeds. If the predicate referred to a non‑partition column, the operation would fail by default unless constraint checking is disabled. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Enabling Legacy Behavior

Legacy `replaceWhere` is disabled by default in modern Databricks runtimes. To enable it (on classic compute), set the Spark configuration property `spark.databricks.delta.replaceWhere.dataColumns.enabled` to `false`:

- Python
- Scala
- SQL

```python
spark.conf.set("spark.databricks.delta.replaceWhere.dataColumns.enabled", False)
```

Once set, all `replaceWhere` predicates are restricted to partition columns. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Constraint Checking

By default, the legacy mode validates that every row being written satisfies the `replaceWhere` predicate. If any row falls outside the predicate, the operation fails. To change this behavior so that rows outside the predicate are inserted instead of overwritten, disable constraint checking:

```python
spark.conf.set("spark.databricks.delta.replaceWhere.constraintCheck.enabled", False)
```

This setting is available only on classic compute. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Limitations

- Legacy `replaceWhere` cannot be used together with `partitionOverwriteMode`, `overwriteSchema`, or the newer `replaceUsing`/`replaceOn` options in the same `DataFrameWriter` operation. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]
- It works only on **partitioned tables**. Unpartitioned tables and tables with [Liquid Clustering](/concepts/liquid-clustering.md) are not supported under legacy behavior. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]
- For empty source queries, `REPLACE WHERE` (including the legacy variant) **may delete rows** matching the predicate, even if the source is empty. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Migration to Modern Alternatives

Databricks recommends using [`REPLACE USING`](/wiki/REPLACE_USING) or [`REPLACE WHERE`](/wiki/REPLACE_WHERE) (the modern, predicate‑based version) instead of legacy `replaceWhere`. These newer options support non‑partition columns and work on all compute types. [Selective overwrite](/wiki/Selectively_overwrite_data_with_Delta_Lake) provides a full comparison. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Related Concepts

- REPLACE WHERE – Modern selective overwrite with arbitrary predicates.
- REPLACE USING – Dynamic data overwrite based on key columns.
- [Dynamic Partition Overwrites](/concepts/dynamic-partition-overwrites-with-partitionoverwritemode.md) – Legacy `partitionOverwriteMode` alternative.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer providing these overwrite modes.
- [Classic Compute](/concepts/classic-compute-forecasting.md) – The only compute type that supports legacy behavior.

## Sources

- selectively-overwrite-data-with-delta-lake-databricks-on-aws.md

# Citations

1. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
