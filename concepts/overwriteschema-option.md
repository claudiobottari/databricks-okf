---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dcbbe099653afdbd9b65b6f833a934586beadf591d3d83ef14d485fdd1a682c
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - overwriteschema-option
    - Overwrite schema option
    - Delta Lake Overwrite Schema
    - Overwrite Schema
    - overwriteschema-option-for-delta-tables
    - OOFDT
    - overwriteschema-option-pattern
    - OOP
    - Overwrite Schema Option Pattern
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: overwriteSchema Option
description: A Spark/Delta Lake DataFrameWriter option that allows overwriting the schema or changing partitioning of an existing Delta table.
tags:
  - delta-lake
  - configuration
  - spark
timestamp: "2026-06-18T15:21:19.736Z"
---

# overwriteSchema Option

The **overwriteSchema Option** is a DataFrame writer configuration used with [Delta Lake](/concepts/delta-lake.md) tables to allow automatic schema migration when the provided data schema does not match the existing table schema. Setting this option to `true` instructs the write operation to overwrite the table schema with the schema of the incoming data, enabling changes such as adding new columns or altering partitioning. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## When to Use overwriteSchema

The `overwriteSchema` option is required when a DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition occurs with the following sub‑conditions:

- **ENABLE_LIQUID** – To enable [Liquid Clustering](/concepts/liquid-clustering.md) on an existing table, you must use `overwrite` mode and set `overwriteSchema` to `true`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- **OVERWRITE_REQUIRED** – To overwrite the table schema (for example, to add or remove columns) or to change the partitioning columns, you must set `overwriteSchema` to `true`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- **PARTITIONING_MISMATCH** – When the partition columns of the incoming data do not match the existing table’s partition columns, the error message recommends using `overwriteSchema` as part of the solution. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## How to Set the Option

When using `DataFrameWriter` or `DataStreamWriter` in Apache Spark, include the option as follows:

```python
df.write \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .saveAsTable("my_table")
```

The option must be used together with `mode("overwrite")` or `mode("overwrite")` for the operation to succeed. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Limitations

The `overwriteSchema` option **cannot be used** alongside the `replaceWhere` option. If you attempt to overwrite the schema while using `replaceWhere`, the operation will fail with an error. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Schema Migration](/concepts/delta-lake-schema-migration.md) – General strategies for evolving Delta table schemas.
- [mergeSchema Option](/concepts/mergeschema-option.md) – An alternative option for automatic schema merging during append operations.
- DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition – The error class that triggers the need for this option.
- [Liquid Clustering](/concepts/liquid-clustering.md) – A clustering technique that may require `overwriteSchema` to enable on an existing table.
- replaceWhere – A write option that conflicts with `overwriteSchema`.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
