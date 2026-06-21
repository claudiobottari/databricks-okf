---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb278606f359051d07d20436e43a624b5abaa8626f91ba033d1678254616e4f2
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-partitioning-constraints
    - DTPC
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: Delta Table Partitioning Constraints
description: Delta Lake enforces that partition columns specified during a write must match the existing table's partition columns; a mismatch raises the PARTITIONING_MISMATCH error.
tags:
  - delta-lake
  - partitioning
  - data-validation
timestamp: "2026-06-19T18:26:11.714Z"
---

```yaml
---
title: Delta Table Partitioning Constraints
summary: The requirement that partition columns specified during a write operation must match the existing partition columns of the target Delta table, enforced by the PARTITIONING_MISMATCH error.
sources:
  - delta_metadata_mismatch-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:21:29.653Z"
updatedAt: "2026-06-18T15:21:29.653Z"
tags:
  - delta-lake
  - partitioning
  - constraints
aliases:
  - delta-table-partitioning-constraints
  - DTPC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Table Partitioning Constraints

**Delta Table Partitioning Constraints** are the rules that enforce consistency of the partitioning scheme when writing data to an existing [[Delta Lake Table|Delta table]]. When a write operation specifies partition columns, those columns must exactly match the partition columns already defined on the table; any deviation triggers a `DELTA_METADATA_MISMATCH` error. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Partitioning Mismatch Error

If the partition columns supplied during a write do not match those of the target table, Databricks raises the following error:

```
DELTA_METADATA_MISMATCH.PARTITIONING_MISMATCH
Partition columns do not match the partition columns of the table.
Given: <provided>
Table: <original>
```

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

This constraint prevents accidental changes to the table’s partitioning scheme, which could break data layout and query optimization.

## Changing Partitioning

To alter the partitioning of an existing Delta table — for example, to change which columns are used as partition keys — you must use the `overwriteSchema` option set to `true` in the write operation. This rewrites the table schema and allows the new partitioning to take effect. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

```python
df.write \
  .mode("overwrite") \
  .option("overwriteSchema", "true") \
  .save("/path/to/table")
```

Note that the schema cannot be overwritten when `replaceWhere` is also used. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### Limitation with `replaceWhere`

The `overwriteSchema` option cannot be used together with `replaceWhere`. If you need to replace data based on a condition and also change the schema or partitioning, perform the operations separately or use an alternative approach. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Table Schema Evolution – Managing schema changes in Delta tables.
- Delta Table Overwrite – Replacing data in a Delta table.
- Delta Table Write Modes – Append, overwrite, and merge behaviors.
- DELTA_METADATA_MISMATCH Error Class|Delta Metadata Mismatch Error – The broader error class that includes partitioning mismatch.
- Delta Table Schema – The column definitions that partition columns are part of.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
