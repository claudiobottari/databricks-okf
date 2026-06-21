---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 989aa0ad8811a951ad995fd3421f396b4735fbb7726e153497c3d43b4f7c53fb
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-column-mapping
    - DTCM
    - Delta column mapping
    - Column Mapping
    - Delta Lake Column Mapping
    - Delta Lake column mapping
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Table Column Mapping
description: A Delta Lake feature that must be enabled to use column aliases in reconciliation queries; related to external metadata constraints.
tags:
  - delta-lake
  - schema-management
timestamp: "2026-06-18T11:53:27.970Z"
---

# Delta Table Column Mapping

**Delta Table Column Mapping** is a [Delta Lake](/concepts/delta-lake.md) feature that allows columns to be renamed without rewriting the underlying data files. In the context of reconciliation queries used with Delta Live Tables or external metadata operations, column mapping must be enabled to use an alias in the query; otherwise, a `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` error is raised.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Overview

Column mapping decouples a Delta table’s logical column names from its physical storage names. This enables schema evolution operations—such as renaming or dropping columns—that were previously rewrite-heavy. When column mapping is not enabled, certain operations that rely on logical column aliases (e.g., in a reconciliation query) are unsupported.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Error Condition

### COLUMN\_RENAME\_WITHOUT\_COLUMN\_MAPPING

The error condition `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING` occurs when a reconciliation query attempts to use an alias for a column, but the Delta table does not have column mapping enabled. The error message states: *Column mapping must be enabled to use an alias in the reconciliation query.*^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

This is one of several errors reported under the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error class, which also includes conditions for column mask policies, row-level security policies, unsupported table types, and unsupported projections.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Requirements

To use aliases in reconciliation queries—or to perform column renames without data rewriting—column mapping must be enabled on the Delta table. This is typically configured at table creation time or via an `ALTER TABLE` command that sets the table property `delta.columnMapping.mode` to `name` or `id`.^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md] (Note: the source material does not specify the exact property name; the above is a commonly known attribute, but to stay strictly factual: the source states that column mapping must be enabled. The exact method is inferred.)

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The open-source storage layer that provides column mapping
- Delta Live Tables — A framework that may use reconciliation queries affected by this requirement
- [Reconciliation Queries](/concepts/delta-lake-reconciliation-queries.md) — Queries that compare data sets and may require column aliases
- [Column Mask Policies](/concepts/column-mask-policies.md) — Another metadata feature that can raise unsupported-source errors
- [Row-Level Security Policies](/concepts/row-level-security-rls-policies.md) — Another feature that can cause similar errors

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
