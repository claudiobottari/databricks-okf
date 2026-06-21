---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0323f58a18faf89fb9029d3e8fbef5885fd1e6d57b71395ce0e3c38c123b5474
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_external_metadata_unsupported_source
    - DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE
description: A Databricks error condition raised when external metadata operations are attempted on unsupported Delta table sources or configurations.
tags:
  - databricks
  - error-handling
  - delta-lake
timestamp: "2026-06-19T15:04:21.576Z"
---

# DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE

**DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE** is a [Delta Lake](/concepts/delta-lake.md) error condition (SQLSTATE `0AKDC`, Feature Not Supported) that occurs when external metadata cannot process a source table or view due to an unsupported feature or configuration.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Error Categories

The error message includes a specific reason that identifies the exact unsupported aspect. Each reason is detailed below.

### COLUMN_MASK

The source table uses a [column mask](/concepts/column-mask-policies.md) policy. The error message displays the `<tableType>` of the affected object.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

```
<tableType> with Column Mask (CM) policies.
```

### COLUMN_RENAME_WITHOUT_COLUMN_MAPPING

[Column mapping](/concepts/column-mapping-in-delta-lake.md) must be enabled before using an alias in a reconciliation query.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

```
Column mapping must be enabled to use an alias in the reconciliation query.
```

### PROJECTION_NOT_SUPPORTED

The projection clause `<projectionSql>` of a reconciliation query is not supported by the external metadata system.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

```
The projection '<projectionSql>' of reconciliation query is not supported.
```

### ROW_FILTER

The source table has a [row-level security (RLS) filter](/concepts/row-filter-policies.md) applied. The error message shows the `<tableType>` of the affected object.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

```
<tableType> with Row-level Security (RLS) policies.
```

### TABLE_TYPE

The source is an unsupported table type. External metadata supports only Streaming Tables and [Materialized Views](/concepts/materialized-views-in-databricks.md). The error message shows the `<tableType>` of the object.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

```
<tableType> table, only streaming table and materialized view are supported.
```

## Related Concepts

- [Delta Lake External Metadata](/concepts/delta-lake-external-metadata.md)
- [Column Mapping](/concepts/delta-table-column-mapping.md)
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md)

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
