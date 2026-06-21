---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd90e71312f466b5f93a2fd86ab9b04d1c5ce2befa5048cf4730d5467993c20a
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-row-level-security-rls-policies
    - DLRS(P
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Lake Row-Level Security (RLS) Policies
description: A row-level security feature in Delta Lake that restricts data access at the row level, and is unsupported for external metadata operations.
tags:
  - delta-lake
  - security
  - row-level-security
timestamp: "2026-06-18T15:19:18.172Z"
---

# Delta Lake Row-Level Security (RLS) Policies

**Delta Lake Row-Level Security (RLS) Policies** are a feature that restricts which rows of a Delta table are visible to users based on policy conditions. RLS policies are applied at query time, filtering out rows that the current user is not authorized to see.

## Error Condition: DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE

When using Delta Lake with external metadata systems, certain table types with RLS policies may trigger the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error. This error occurs specifically with the `ROW_FILTER` sub-condition. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Error Message

The error condition for RLS policies is reported as:

```
ROW_FILTER
<tableType> with Row-level Security (RLS) policies.
```

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Cause

External metadata systems do not support Delta tables that have Row-Level Security (RLS) policies applied. When a reconciliation query attempts to access a table with RLS policies through an external metadata source, the system returns this error. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### Related Unsupported Features

External metadata also does not support Delta tables with the following features:

- **Column Mask (CM) policies** — Reported as `COLUMN_MASK` sub-condition. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Column rename without column mapping** — Reported as `COLUMN_RENAME_WITHOUT_COLUMN_MAPPING`. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Unsupported projections** — Reported as `PROJECTION_NOT_SUPPORTED`. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **Unsupported table types** — Only streaming tables and [materialized views](/concepts/materialized-views-in-databricks.md) are supported; reported as `TABLE_TYPE`. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Best Practices

When working with Row-Level Security policies in Delta Lake:

- Use RLS policies directly within a Unity Catalog environment that supports them natively, rather than through external metadata sources.
- If you need to use external metadata, ensure that your Delta tables do not have RLS policies applied. Consider using views or derived tables to apply row-level restrictions instead.
- For tables that require both RLS and external metadata access, evaluate whether the RLS policy can be moved to a higher layer (such as a view) or whether the table can be replicated without RLS policies to the external metadata system.

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) — Attribute-based row-level filtering in Unity Catalog
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) — Table-specific row and column security
- [Column Mask Policies](/concepts/column-mask-policies.md) — Similar security mechanism for columns (also unsupported by external metadata)
- [Delta External Metadata](/concepts/delta-lake-external-metadata.md) — The external metadata integration that has these limitations
- Streaming Tables — Table types supported by external metadata
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Table types supported by external metadata

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
