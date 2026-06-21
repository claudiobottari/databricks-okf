---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eeab05bd4e056d98847bae3c9ef2611b7a34e5592e9945d09249a391f9eabaea
  pageDirectory: concepts
  sources:
    - selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - replace-on-complex-match-overwrite
    - ROCO
  citations:
    - file: selectively-overwrite-data-with-delta-lake-databricks-on-aws.md
title: REPLACE ON Complex-Match Overwrite
description: Delta Lake overwrite option for user-defined matching conditions including NULL-safe equality, used when REPLACE USING's equality semantics are insufficient.
tags:
  - delta-lake
  - data-engineering
  - spark
  - overwrite
timestamp: "2026-06-19T23:01:54.518Z"
---

# REPLACE ON Complex-Match Overwrite

**REPLACE ON Complex-Match Overwrite** is a [Delta Lake](/concepts/delta-lake.md) selective overwrite operation that replaces rows in a target table when they match a user-defined condition, supporting matching logic beyond simple equality comparisons, including NULL-safe matching. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Overview

`REPLACE ON` enables compute-independent, atomic overwrite behavior that works across Databricks SQL warehouses, serverless compute, and classic compute. Unlike `REPLACE USING`, which replaces rows when specified columns compare equal under standard equality, `REPLACE ON` allows you to define arbitrary matching conditions for determining which rows to replace. This makes it the preferred choice for use cases requiring Complex Match Conditions or NULL-Safe Matching. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## When to Use

Use `REPLACE ON` when you need matching logic that REPLACE USING does not support, such as treating `NULL` values as equal. For most use cases, Databricks recommends using REPLACE USING or REPLACE WHERE. Use `REPLACE ON` only if your use case requires complex or NULL-safe matching conditions. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Availability

- **SQL:** Supported in Databricks Runtime 17.1 and above
- **Python and Scala:** Supported in Databricks Runtime 18.2 and above

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Syntax and Options

`REPLACE ON` accepts a user-defined condition string using the `replaceOn` option. You can optionally use the `targetAlias` option to specify an alias for the target table, and the `.as()` or `.alias()` APIs to specify an alias for the source data. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

### Python Example

```python
(sourceDataDF.alias("s")
  .write
  .mode("overwrite")
  .option("targetAlias", "t")
  .option("replaceOn", "s.event_id <=> t.event_id AND s.start_date <=> t.start_date")
  .saveAsTable("events"))
```

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

For SQL syntax, see the INSERT statement in the SQL language reference. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Behavior

- **Empty source queries:** For empty source queries, `REPLACE ON` does not delete any table rows. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]
- **Atomic replacement:** The operation performs an atomic replacement of matching rows with the source data.
- **NULL-safe matching:** The `<=>` operator in the example condition is a NULL-safe equality operator that treats `NULL` values as equal, unlike standard equality checks.

## Limitations and Constraints

- In Scala and Python, `replaceOn` cannot be used in combination with `replaceWhere`, `partitionOverwriteMode`, or `overwriteSchema`. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Recovery

If data has been accidentally overwritten, you can use the RESTORE command to undo the change and recover the previous table state. ^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Comparison with Other Overwrite Options

| Option | Matching Logic | Use Case |
|--------|---------------|----------|
| `REPLACE WHERE` | Arbitrary boolean expression | Replacing data matching a predicate |
| `REPLACE USING` | Equality comparison on specified columns | Simple column-based replacement |
| `REPLACE ON` | User-defined condition | Complex or NULL-safe matching |

^[selectively-overwrite-data-with-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Selective Overwrite](/concepts/replace-where-selective-overwrite.md)
- REPLACE WHERE
- REPLACE USING
- [Dynamic Data Overwrites](/concepts/replace-using-dynamic-data-overwrite.md)
- INSERT Statement
- [RESTORE Table](/concepts/restore-table-command.md)

## Sources

- selectively-overwrite-data-with-delta-lake-databricks-on-aws.md

# Citations

1. [selectively-overwrite-data-with-delta-lake-databricks-on-aws.md](/references/selectively-overwrite-data-with-delta-lake-databricks-on-aws-3465bfbb.md)
