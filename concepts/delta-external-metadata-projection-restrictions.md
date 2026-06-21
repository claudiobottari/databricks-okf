---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af41fcfec8e5a9db6107df809dfadf3b8eab246810e17efd69193e538c3acffc
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-external-metadata-projection-restrictions
    - DEMPR
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta External Metadata Projection Restrictions
description: The reconciliation query for external metadata operations has unsupported projection expressions that trigger a PROJECTION_NOT_SUPPORTED error.
tags:
  - databricks
  - delta-lake
  - projection
  - reconciliation
timestamp: "2026-06-19T15:05:03.023Z"
---

# Delta External Metadata Projection Restrictions

**Delta External Metadata Projection Restrictions** refers to limitations on the `SELECT` projections that can be used in reconciliation queries when a table is accessed through external metadata (for example, via [Delta Sharing](/concepts/delta-sharing.md) or a catalog integration). When the projection of a reconciliation query is not supported, the system raises the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error with the sub‑condition `PROJECTION_NOT_SUPPORTED`. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Error Condition

The full error message is:

```
The projection '<projectionSql>' of reconciliation query is not supported.
```

This error indicates that the specific column expression or select list used in a reconciliation query against a table with external metadata is not allowed. The system does not enumerate the exact set of unsupported projection forms; it only signals that the given projection is incompatible. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Context

The `PROJECTION_NOT_SUPPORTED` condition is one of several restrictions enforced when external metadata acts as the source for a table. Other restrictions in the same error class include:

- **COLUMN_MASK** – Tables with column mask policies.
- **COLUMN_RENAME_WITHOUT_COLUMN_MAPPING** – Column renaming without column mapping enabled.
- **ROW_FILTER** – Tables with row‑level security policies.
- **TABLE_TYPE** – Unsupported table types; only streaming tables and materialized views are allowed.

These restrictions apply broadly to any operation that requires external metadata to interpret the table schema or enforce access controls. For the projection restriction, it specifically governs the shape of the reconciliation query used to verify or synchronize data. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Resolution

To resolve the error, adjust the projection of the reconciliation query so that it matches one of the supported forms. Because the documentation does not provide a list of supported projections, you may need to:

- Simplify expressions (e.g., avoid complex calculations or subqueries in the select list).
- Use only direct column references.
- Check whether the projection is needed for reconciliation; if not, remove unsupported elements.

If the problem persists, consult the [Delta Lake](/concepts/delta-lake.md) documentation or your external metadata provider for guidance on supported reconciliation query syntax. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [External Metadata](/concepts/external-metadata-api.md) – Catalogs or schemas external to the Delta table’s own metadata.
- [Reconciliation Query](/concepts/delta-lake-reconciliation-queries.md) – A query used to compare or synchronize table state with an external source.
- Column Masking – Access control feature that can conflict with external metadata usage.
- [Row‑Level Security](/concepts/row-level-security-rls-policies.md) – Another access control feature that can cause compatibility issues.
- Streaming Tables and [Materialized Views](/concepts/materialized-views-in-databricks.md) – The only table types currently supported when using external metadata as a source.

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
