---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f335bb06be07d76e32b504e8a8f56d49b287a1f27d761fd78321f7d873e1bbc5
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.6
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - reconciliation-query-projections
    - RQP
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Reconciliation Query Projections
description: Query projections used in metadata reconciliation that have specific support limitations in Databricks
tags:
  - databricks
  - queries
  - delta-lake
timestamp: "2026-06-19T10:05:46.718Z"
---

# Reconciliation Query Projections

**Reconciliation Query Projections** refer to the projection clause of a reconciliation query used in the context of Delta Lake’s external metadata feature. When such a projection is not supported, Delta Lake raises a specific error condition.

## Error Condition

The `PROJECTION_NOT_SUPPORTED` sub‑type of the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error class indicates that the projection clause of a reconciliation query is not supported. Delta Lake returns the message:

```
The projection '<projectionSql>' of reconciliation query is not supported.
```

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

This error is one of several conditions that can occur when external metadata sources are used with Delta tables. Other related conditions include `COLUMN_MASK`, `ROW_FILTER`, `TABLE_TYPE`, and `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING`, all of which trigger the same general error class. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

The error occurs when a reconciliation query’s projection (the `SELECT` list of columns and expressions) uses syntax or functions that Delta Lake’s external metadata reader does not support. The exact unsupported projection is included in the error message as `<projectionSql>`. The source documentation does not specify which projections are allowed or prohibited, but the error implies that only a limited set of projections can be used in reconciliation queries for external metadata sources. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [External Metadata](/concepts/external-metadata-api.md) — The feature that allows Delta tables to read metadata from external sources.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format and engine.
- [Column Mapping](/concepts/delta-table-column-mapping.md) — Required for some operations like column aliasing in reconciliation queries; the `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` error indicates when column mapping is missing.
- [Reconciliation Query](/concepts/delta-lake-reconciliation-queries.md) — The query used to reconcile external metadata with Delta table state.
- DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE error|Delta External Metadata Unsupported Source Error — The parent error class containing all sub‑types.

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
