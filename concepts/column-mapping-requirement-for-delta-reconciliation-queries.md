---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 235bb215a81e3db8b71a72a0c2f36a63a153a06ceb895313a3382a01faf30be5
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-mapping-requirement-for-delta-reconciliation-queries
    - CMRFDRQ
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Column Mapping Requirement for Delta Reconciliation Queries
description: Column mapping must be enabled on a Delta table to use an alias in a reconciliation query, otherwise a COLUMN_RENAME_WITHOUT_COLUMN_MAPPING error occurs.
tags:
  - databricks
  - delta-lake
  - column-mapping
  - reconciliation
timestamp: "2026-06-19T15:04:53.319Z"
---

# Column Mapping Requirement for Delta Reconciliation Queries

**Column Mapping Requirement for Delta Reconciliation Queries** refers to a precondition enforced by [Delta External Metadata](/concepts/delta-lake-external-metadata.md) reconciliation queries: column mapping must be enabled before an alias can be used in the reconciliation query. If column mapping is not enabled, the system raises the `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` error.

## Error Condition

When a reconciliation query attempts to use a column alias without column mapping being enabled on the table, Databricks returns the following error:

```
DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE error class
COLUMN_RENAME_WITHOUT_COLUMN_MAPPING
```

The error message states: *"Column mapping must be enabled to use an alias in the reconciliation query."* ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Cause

The `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` condition occurs when a [reconciliation query](/concepts/delta-lake-reconciliation-queries.md) includes a column alias, but the underlying table does not have [column mapping](/concepts/column-mapping-in-delta-lake.md) enabled. Delta Lake requires column mapping to be active to properly interpret and apply column aliases during reconciliation operations.

## Solution

Enable column mapping on the table before using aliases in reconciliation queries. Column mapping can be enabled on existing Delta tables using `ALTER TABLE` commands with the appropriate column mapping mode setting.

## Related Error Conditions

The `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error class also includes other conditions related to reconciliation queries, such as:

- [COLUMN_MASK](/concepts/column-mask-policies.md) – When the table has column mask policies
- PROJECTION_NOT_SUPPORTED – When the reconciliation query projection is not supported
- [ROW_FILTER](/concepts/row-filter-policies.md) – When the table has row-level security policies
- TABLE_TYPE – When the table type is not supported (only streaming tables and materialized views are supported)

## Related Concepts

- [Delta External Metadata](/concepts/delta-lake-external-metadata.md) — The feature that enables external metadata synchronization
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md) — The feature that allows column renaming and aliasing
- [Delta Reconciliation Queries](/concepts/delta-lake-reconciliation-queries.md) — Queries used to reconcile data between Delta tables and external systems
- NOT_DELTA_TABLE error reason|Delta Lake Error Messages — Reference for Delta Lake error conditions and SQL states

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
