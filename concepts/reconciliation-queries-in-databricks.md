---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64701f8af66a38ff057ed347067b40181059e68d7a9c517ea4137d57f3fc0ca1
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - reconciliation-queries-in-databricks
    - RQID
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Reconciliation queries in Databricks
description: Queries that reconcile or validate external metadata against a source table, with restrictions on projections and aliasing.
tags:
  - databricks
  - query
  - data-validation
timestamp: "2026-06-19T18:24:48.754Z"
---

# Reconciliation Queries in Databricks

**Reconciliation queries** in Databricks are SQL queries used to compare and validate data between source tables and their external metadata representations. These queries are essential for ensuring data consistency and integrity when working with [Delta Lake](/concepts/delta-lake.md) tables that have external metadata enabled.

## Overview

Reconciliation queries allow you to verify that the data in your source tables matches the data stored in external metadata systems. They are particularly important when using [External Metadata](/concepts/external-metadata-api.md) features, as they help detect discrepancies between the actual table data and the metadata that describes it. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Supported Table Types

Reconciliation queries support specific table types. Only Streaming Tables and [Materialized Views](/concepts/materialized-views-in-databricks.md) are supported for reconciliation operations. Other table types will result in errors when reconciliation queries are attempted. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Error Conditions

Several error conditions can occur when working with reconciliation queries:

### COLUMN_MASK

Tables with Column Mask (CM) policies are not supported as sources for reconciliation queries. If you attempt to use a table with column masking enabled, Databricks returns a `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### COLUMN_RENAME_WITHOUT_COLUMN_MAPPING

Column mapping must be enabled to use an alias in the reconciliation query. If you attempt to use column aliases without first enabling [Column Mapping](/concepts/delta-table-column-mapping.md), the reconciliation query will fail. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### PROJECTION_NOT_SUPPORTED

The projection specified in the reconciliation query may not be supported. When you receive this error, the specific unsupported projection SQL is included in the error message, allowing you to identify and correct the issue. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### ROW_FILTER

Tables with Row-level Security (RLS) policies are not supported as sources for reconciliation queries. If you attempt to use a table with row filters enabled, Databricks returns a `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### TABLE_TYPE

Only streaming tables and materialized views are supported for reconciliation queries. Attempting to use other table types will result in an error indicating that the table type is not supported. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Best Practices

When working with reconciliation queries in Databricks:

1. **Verify table type**: Ensure your source table is a streaming table or materialized view before attempting reconciliation.
2. **Enable column mapping**: If you need to use column aliases in your reconciliation query, enable column mapping on the table first.
3. **Avoid security policies**: Tables with column masks or row filters cannot be used as sources for reconciliation queries.
4. **Check projections**: Verify that your projection SQL is compatible with the reconciliation query requirements.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports reconciliation queries
- [External Metadata](/concepts/external-metadata-api.md) — The metadata system that reconciliation queries validate against
- Streaming Tables — One of the supported table types for reconciliation
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Another supported table type for reconciliation
- [Column Mapping](/concepts/delta-table-column-mapping.md) — Required for using aliases in reconciliation queries
- Column Mask — A security feature incompatible with reconciliation queries
- [Row Filter](/concepts/row-filter-policies.md) — A security feature incompatible with reconciliation queries

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
