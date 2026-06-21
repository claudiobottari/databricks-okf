---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d014a2fa578e9f862f358baaf13a410b751c5972a610f2d504692dfb986dcafa
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-lake-external-metadata
    - DLEM
    - Delta External Metadata
    - Delta Table Metadata
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Lake External Metadata
description: A mechanism for storing Delta table metadata externally; has compatibility constraints with certain Delta features like column masking, RLS, and unsupported table types.
tags:
  - delta-lake
  - metadata
  - architecture
timestamp: "2026-06-18T11:53:29.500Z"
---

# Delta Lake External Metadata

**Delta Lake External Metadata** refers to the capability in [Delta Lake](/concepts/delta-lake.md) to reference external metadata sources for reconciliation queries on tables. This feature is used to synchronize or validate data against external systems. However, not all table types or configurations are supported; when an unsupported source is encountered, the system raises the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error (SQLSTATE class 0AKDC, Feature Not Supported).^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Unsupported Sources

The following conditions cause External Metadata to reject a source:

| Condition | Description |
|-----------|-------------|
| **COLUMN_MASK** | Tables with Column Mask (CM) policies are not supported. |
| **COLUMN_RENAME_WITHOUT_COLUMN_MAPPING** | Column mapping must be enabled to use an alias in the reconciliation query. |
| **PROJECTION_NOT_SUPPORTED** | The specified projection `<projectionSql>` in the reconciliation query is not supported. |
| **ROW_FILTER** | Tables with Row-level Security (RLS) policies are not supported. |
| **TABLE_TYPE** | Only streaming tables and materialized views are supported; `<tableType>` is not. |

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Supported Table Types

Delta Lake External Metadata supports only:

- Streaming Tables
- [Materialized Views](/concepts/materialized-views-in-databricks.md)

Other Delta table types are unsupported and will trigger the `TABLE_TYPE` error condition.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The foundational storage layer
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data rows
- [Delta Sharing](/concepts/delta-sharing.md) — Data sharing across platforms
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for managing policies and metadata

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
