---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a6419234ff5c629981b2e078ea7bc38acae3eac93c61061b0927f85795dd396
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-metadata-in-databricks
    - EMID
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: External metadata in Databricks
description: A Databricks concept for managing table metadata externally, with limited support only for streaming tables and materialized views.
tags:
  - databricks
  - metadata
  - data-catalog
timestamp: "2026-06-19T18:24:50.696Z"
---

# External Metadata in Databricks

**External Metadata** is a Databricks feature that allows certain table types to provide their metadata from external sources rather than from the Delta Lake transaction log. This enables specific table types to be queried and managed without requiring direct access to the underlying data files. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Supported Table Types

External Metadata only supports **streaming tables** and **materialized views**. Other table types are not supported by this feature. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Unsupported Features

When using External Metadata, several features are not supported and will result in error conditions:

### Column Mask (CM) Policies
Tables with Column Mask policies are not supported when using External Metadata. This includes any table type that has column-level masking applied. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Column Mapping for Renames
Column mapping must be enabled to use an alias in the reconciliation query. If column mapping is not enabled, column renames without column mapping will not work. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Projection in Reconciliation Queries
The projection specified in a reconciliation query is not supported when using External Metadata. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Row Filter (RLS) Policies
Tables with Row-level Security (RLS) policies are not supported when using External Metadata. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Error Conditions

When an unsupported feature is used with External Metadata, Databricks returns the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error condition with specific sub-errors:

| Sub-Error | Description |
|-----------|-------------|
| `COLUMN_MASK` | `<tableType>` with Column Mask (CM) policies |
| `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` | Column mapping must be enabled to use an alias in the reconciliation query |
| `PROJECTION_NOT_SUPPORTED` | The projection '`<projectionSql>`' of reconciliation query is not supported |
| `ROW_FILTER` | `<tableType>` with Row-level Security (RLS) policies |
| `TABLE_TYPE` | `<tableType>` table, only streaming table and materialized view are supported |

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## SQLSTATE Reference

These errors fall under SQLSTATE class **0AKDC**, which covers feature not supported conditions. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- Streaming Tables — Tables that process data incrementally from external sources
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Pre-computed views for query optimization
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Databricks tables
- Column Masking — Access control for hiding sensitive column data
- [Row-Level Security](/concepts/row-level-security-rls-policies.md) — Access control for filtering rows based on user permissions
- [Reconciliation Queries](/concepts/delta-lake-reconciliation-queries.md) — Queries used to reconcile data between sources
- [Column Mapping](/concepts/delta-table-column-mapping.md) — The process of mapping column names between different formats

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
