---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2667ac6caf83c8e9342483c71b791b01623f65cdece2e302d617f78e2caca516
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - materialized-views-in-databricks
    - MVID
    - Materialized View
    - Materialized Views
    - Materialized Views|materialized view
    - Materialized Views|materialized views
    - Materialized view
    - Materialized views
    - materialized view
    - materialized views
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Materialized views in Databricks
description: Pre-computed views that refresh on a schedule or on demand, one of the two table types supported for external metadata.
tags:
  - databricks
  - views
  - delta-lake
timestamp: "2026-06-19T18:24:53.192Z"
---

# Materialized views in Databricks

**Materialized views** in Databricks are pre-computed, incrementally maintained views that store the results of a query as a physical table. They are designed to improve query performance for complex or frequently accessed aggregations by avoiding recomputation of the underlying data on each query. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Overview

A materialized view in Databricks is a type of table that persists the output of a SQL query. Unlike standard views, which execute the query each time they are accessed, materialized views store the results physically and update them incrementally as the source data changes. This makes them particularly useful for dashboards, reporting, and other workloads where query latency is critical. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Supported Table Types

Databricks supports materialized views as one of the table types that can be used with external metadata systems. When working with external metadata, only **streaming tables** and **materialized views** are supported as valid table types. Other table types may trigger the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error condition. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Limitations and Constraints

### External Metadata Support

When using external metadata with materialized views, the following constraints apply:

- **Column masks (CM):** Materialized views with column mask policies are not supported by external metadata systems. Attempting to use such a view will result in a `COLUMN_MASK` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Row filters (RLS):** Materialized views with row-level security policies are not supported by external metadata systems. Attempting to use such a view will result in a `ROW_FILTER` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Column renaming without column mapping:** If column mapping is not enabled, using an alias in the reconciliation query is not supported. This will result in a `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Unsupported projections:** Certain projection expressions in reconciliation queries are not supported by external metadata, resulting in a `PROJECTION_NOT_SUPPORTED` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Table Type Validation

Only streaming tables and materialized views are supported when working with external metadata. Other table types will trigger the `TABLE_TYPE` error condition. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Streaming tables in Databricks](/concepts/streaming-tables-in-databricks.md) — Another supported table type for external metadata
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for materialized views
- [External metadata in Databricks](/concepts/external-metadata-in-databricks.md) — Systems that integrate with Databricks table metadata
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md) — Required for certain rename operations
- [Row-level security in Databricks](/concepts/row-level-security-in-delta-lake.md) — Access control policies that may conflict with external metadata
- [Column masks in Databricks](/concepts/column-masks-in-delta-lake.md) — Data masking policies that may conflict with external metadata

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
