---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 222f625293b3ad03560f5629f9cea581718299892df2c6dc16abd166f7934339
  pageDirectory: concepts
  sources:
    - selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - replace-where-selective-overwrite
    - RWSO
    - Delta Lake Selective Overwrite
    - Delta Lake selective overwrite
    - replaceWhere Write Option
    - replaceWhere option
  citations:
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
title: REPLACE WHERE Selective Overwrite
description: Delta Lake option to atomically replace data matching an arbitrary boolean expression, with optional constraint validation to ensure all written rows fall within the predicate.
tags:
  - delta-lake
  - data-engineering
  - spark
  - overwrite
timestamp: "2026-06-19T23:01:36.532Z"
---

# REPLACE WHERE Selective Overwrite

**REPLACE WHERE Selective Overwrite** is a [Delta Lake](/concepts/delta-lake.md) feature that allows you to atomically replace only the data matching an arbitrary boolean expression in a target table, leaving all other data unchanged. It is one of several selective overwrite options available in [Delta Lake](/concepts/delta-lake.md), alongside REPLACE USING and [REPLACE ON](/concepts/create-or-replace-clone.md).

## Overview

The `REPLACE WHERE` operation enables precise, predicate-based data replacement. When you write data with this option, [Delta Lake](/concepts/delta-lake.md) validates that all rows in the source data match the specified predicate, then performs an atomic replacement using overwrite semantics. If any values in the operation fall outside the predicate, the operation fails with an error by default. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Syntax and Usage

To atomically replace events in January in a target table partitioned by `start_date`:

```python
(replace_data.write
  .mode("overwrite")
  .option("replaceWhere", "start_date >= '2017-01-01' AND end_date <= '2017-01-31'")
  .saveAsTable("events"))
```

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

The `REPLACE WHERE` option accepts a `boolean_expression` with some restrictions. See the INSERT SQL language reference for details. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Behavior with Empty Source Queries

For empty source queries, `REPLACE WHERE` might delete table rows. This differs from `REPLACE USING` and `REPLACE ON`, which do not delete data when the source is empty. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Constraint Checking

By default, [Delta Lake](/concepts/delta-lake.md) enforces that all written data matches the `replaceWhere` predicate. To change this behavior so that values within the predicate range are overwritten and records outside the range are inserted, you can disable the constraint check:

```python
spark.conf.set("spark.databricks.delta.replaceWhere.constraintCheck.enabled", False)
```

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

This configuration is only available on classic compute. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Legacy Behavior

Legacy `replaceWhere` behavior is only available on classic compute. In legacy mode, queries overwrite data that matches a predicate only over partition columns. The following command atomically replaces the month January in a target table partitioned by `date`:

```python
(df.write
  .mode("overwrite")
  .option("replaceWhere", "birthDate >= '2017-01-01' AND birthDate <= '2017-01-31'")
  .saveAsTable("people10m"))
```

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

To enable legacy behavior, set the following configuration:

```python
spark.conf.set("spark.databricks.delta.replaceWhere.dataColumns.enabled", False)
```

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Comparison with Other Selective Overwrite Options

| Feature | `REPLACE WHERE` | `REPLACE USING` | `REPLACE ON` |
|---------|-----------------|-----------------|--------------|
| Matching logic | Arbitrary boolean expression | Column equality | User-defined condition |
| Empty source behavior | May delete rows | Does not delete | Does not delete |
| NULL-safe matching | No | No | Yes (via `<=>` operator) |

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

For most use cases, Databricks recommends using `REPLACE USING` or `REPLACE WHERE`. Use `REPLACE ON` only if your use case requires complex or NULL-safe matching conditions. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Important Considerations

- In Scala and Python, `replaceOn` and `replaceUsing` cannot be used in combination with `replaceWhere`, `partitionOverwriteMode`, or `overwriteSchema`. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]
- If data has been accidentally overwritten, you can use the RESTORE command to undo the change. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]
- `REPLACE WHERE` supports partitioned tables, unpartitioned tables, and tables with [Liquid Clustering](/concepts/liquid-clustering.md). ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing ACID transactions and [Scalable Metadata Handling](/concepts/scalable-metadata-handling.md)
- REPLACE USING — Dynamic data overwrite using column equality matching
- [REPLACE ON](/concepts/create-or-replace-clone.md) — Dynamic data overwrite using user-defined conditions
- INSERT — SQL language reference for DML operations
- [Dynamic Partition Overwrites](/concepts/dynamic-partition-overwrites-with-partitionoverwritemode.md) — Legacy partition-level overwrite behavior
- Table History and Restore — Recovering from accidental overwrites

## Sources

- selectively-overwrite-data-with-delta-lake-databricks-on-aws.md

# Citations

1. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
