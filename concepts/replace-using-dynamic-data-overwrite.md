---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71bb1a2c50476516021f3bb12ffbc548f649e3c3247edbb4b8457ac54d7f7520
  pageDirectory: concepts
  sources:
    - selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - replace-using-dynamic-data-overwrite
    - RUDDO
    - Dynamic Data Overwrites
  citations:
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
title: REPLACE USING Dynamic Data Overwrite
description: Compute-independent, atomic overwrite that replaces rows when specified columns compare equal under equality, supporting partitioned, unpartitioned, and liquid-clustered tables.
tags:
  - delta-lake
  - data-engineering
  - spark
  - overwrite
timestamp: "2026-06-19T23:02:23.178Z"
---

# REPLACE USING Dynamic Data Overwrite

**REPLACE USING Dynamic Data Overwrite** is a feature of [Delta Lake](/concepts/delta-lake.md) that enables atomic, compute-independent selective overwrites for partitioned and unpartitioned tables. It replaces rows in the target table when the specified columns compare equal under standard equality, leaving all other data unchanged. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

`REPLACE USING` is supported in SQL from Databricks Runtime 16.3 onward, and in Python and Scala from Databricks Runtime 18.2 onward. It works on Databricks SQL warehouses, serverless compute, and classic compute without requiring any Spark session configuration. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Syntax and Usage

To perform a dynamic data overwrite using `REPLACE USING`, set the `replaceUsing` option on a `DataFrameWriter` operation, specifying the column names that define the match condition.

**Python**

```python
(sourceDataDF.write
  .mode("overwrite")
  .option("replaceUsing", "event_id, start_date")
  .saveAsTable("events"))
```

**Scala**

```scala
sourceDataDF.write
  .mode("overwrite")
  .option("replaceUsing", "event_id, start_date")
  .saveAsTable("events")
```

**SQL**

```sql
INSERT OVERWRITE TABLE events REPLACE USING (event_id, start_date)
SELECT * FROM sourceData;
```

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

The column list defines the key columns for matching. Rows in the target table whose values in these columns match the incoming data are replaced. All other rows remain intact.

## Behavior

- **Atomic replacement:** The overwrite is performed atomically. If any row in the source data does not match the predicate (in the case of `REPLACE WHERE`) or if there are failures, the operation fails without partially modifying the table. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]  
  (For `REPLACE USING`, the matching is done on column equality; there is no predicate validation failure as in `REPLACE WHERE` because the match is purely equality-based.)

- **Compute independence:** `REPLACE USING` does not depend on Spark configuration settings like `spark.sql.sources.partitionOverwriteMode`. It works uniformly across all compute types. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

- **Empty source queries:** When the source query produces no rows, `REPLACE USING` does **not** delete any rows from the target table. This contrasts with `REPLACE WHERE`, which may delete rows even with an empty source. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

- **Supported table types:** Partitioned tables, unpartitioned tables, and tables with [Liquid Clustering](/concepts/liquid-clustering.md) are all supported. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

- **Constraints:** In Python and Scala, `replaceUsing` cannot be combined with `replaceWhere`, `partitionOverwriteMode`, or `overwriteSchema` in the same `DataFrameWriter` operation. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Legacy Behavior

In Databricks Runtime versions 16.3 to 17.1, `REPLACE USING` exhibited legacy behavior where it only allowed dynamic partition overwrites — the full set of partition columns had to be specified, and the overwrite replaced entire partitions. From Databricks Runtime 17.2 and above, `REPLACE USING` supports dynamic **data** overwrites, which can replace arbitrary rows based on column equality, not just entire partitions. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

When using the legacy behavior, it is important to validate that the written data touches only the expected partitions; a single row in the wrong partition could unintentionally overwrite the entire partition. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Related Options

### `REPLACE WHERE`

`REPLACE WHERE` is another selective overwrite method that uses an arbitrary boolean expression to determine which rows to replace. It is most suitable when the overwrite condition is based on non-key columns or complex predicates. Unlike `REPLACE USING`, `REPLACE WHERE` enforces a constraint check that all written rows must satisfy the predicate (unless the constraint check is disabled). ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

### `REPLACE ON`

`REPLACE ON` (supported from Databricks Runtime 17.1 for SQL, 18.2 for Python/Scala) provides complex and NULL-safe matching conditions using the `<=>` operator. Use `REPLACE ON` when the equality semantics of `REPLACE USING` (which treats `NULL` as not equal) are insufficient. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

### Dynamic Partition Overwrites (`partitionOverwriteMode`)

Legacy dynamic partition overwrites are available via the Spark configuration `spark.sql.sources.partitionOverwriteMode=dynamic` or the `partitionOverwriteMode` DataFrame option. This method only works on classic compute and is deprecated in favor of `REPLACE USING` because it may use stale data when partitioning changes. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Recovery from Accidental Overwrites

If data has been accidentally overwritten, you can use the [Delta Lake](/concepts/delta-lake.md) [restore](/concepts/metastore.md) functionality to undo the change. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Dynamic Partition Overwrites](/concepts/dynamic-partition-overwrites-with-partitionoverwritemode.md)
- REPLACE WHERE
- [REPLACE ON](/concepts/create-or-replace-clone.md)
- DataFrameWriter
- [Liquid Clustering](/concepts/liquid-clustering.md)
- INSERT Overwrite Semantics

## Sources

- selectively-overwrite-data-with-delta-lake-databricks-on-aws.md

# Citations

1. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
