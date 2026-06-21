---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c440372303a1319fb73277886e9e5f3043c5532c8dd089f35b7b4d45ab13f0ef
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-column-mask-compatibility-with-external-metadata
    - DCMCWEM
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Column Mask Compatibility with External Metadata
description: Tables with Column Mask (CM) policies are unsupported sources for Delta external metadata operations.
tags:
  - databricks
  - delta-lake
  - column-masking
  - security
timestamp: "2026-06-19T15:04:27.803Z"
---

# Delta Column Mask Compatibility with External Metadata

**Delta Column Mask Compatibility with External Metadata** refers to the error condition that occurs when attempting to use [External Metadata](/concepts/external-metadata-api.md) with a Delta table that has [Column Mask (CM)](/concepts/column-mask-policies.md) policies applied. This combination is not supported and results in a `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error.

## Error Overview

When a Delta table with Column Mask policies is used as a source for External Metadata operations, the system raises the error condition `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` with the specific sub-error `COLUMN_MASK`. The error message indicates that the table type with Column Mask policies is not supported as a source for External Metadata. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Error Details

The full error condition is classified under SQLSTATE class `0A` (Feature Not Supported). The specific error code is `0AKDC`. When triggered, the error message takes the form:

```
<tableType> with Column Mask (CM) policies.
```

This indicates that the table type in question has Column Mask policies applied, which are incompatible with External Metadata operations. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Unsupported Features

Column Mask is one of several features that are incompatible with External Metadata. Other related unsupported features include:

- **ROW_FILTER**: Tables with [Row-level Security (RLS)](/concepts/row-level-security-rls-policies.md) policies are also unsupported.
- **TABLE_TYPE**: Only Streaming Tables and [Materialized Views](/concepts/materialized-views-in-databricks.md) are supported as source types for External Metadata.
- **COLUMN_RENAME_WITHOUT_COLUMN_MAPPING**: Column mapping must be enabled to use an alias in the reconciliation query.
- **PROJECTION_NOT_SUPPORTED**: Certain projections in reconciliation queries are not supported.

^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Workarounds

To use External Metadata with tables that have Column Mask policies, consider the following approaches:

1. **Remove Column Mask policies** from the table before using it as an External Metadata source.
2. **Use an alternative source** that does not have Column Mask policies applied.
3. **Create a view or materialized view** without Column Mask policies that can serve as the External Metadata source.

## Related Concepts

- [External Metadata](/concepts/external-metadata-api.md) — The feature that is incompatible with Column Mask policies
- [Column Mask (CM)](/concepts/column-mask-policies.md) — The security feature that causes the incompatibility
- [Row-level Security (RLS)](/concepts/row-level-security-rls-policies.md) — Another security feature with similar compatibility limitations
- Streaming Tables — Supported source type for External Metadata
- [Materialized Views](/concepts/materialized-views-in-databricks.md) — Supported source type for External Metadata
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format
- SQLSTATE 0A — Feature Not Supported error class

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
