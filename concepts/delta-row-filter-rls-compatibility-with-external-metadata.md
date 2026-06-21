---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5bf60792b7155ed22e06160b47d6e3919aa3b734c4a70510c34ecb86e4e53ea9
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-row-filter-rls-compatibility-with-external-metadata
    - DRF(CWEM
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Row Filter (RLS) Compatibility with External Metadata
description: Tables with Row-level Security (RLS) policies are unsupported sources for Delta external metadata operations.
tags:
  - databricks
  - delta-lake
  - row-level-security
  - security
timestamp: "2026-06-19T15:04:34.661Z"
---

# Delta Row Filter (RLS) Compatibility with External Metadata

**Delta Row Filter (RLS) Compatibility with External Metadata** refers to the limitation that tables with [Row-Level Security (RLS)](/concepts/row-level-security-rls-policies.md) policies are not supported when using [External Metadata](/concepts/external-metadata-api.md) in Databricks. When a table has an RLS policy defined, operations that rely on external metadata will fail with the `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error.

## Error Condition

When a table with Row Filter (RLS) policies is used with external metadata, Databricks raises the following error:

```
DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE
```

The error message specifies that the source is a `<tableType>` with Row-level Security (RLS) policies. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Affected Table Types

The error applies to any table type that has RLS policies defined. This includes both streaming tables and materialized views, as well as other table types that may have row filters applied. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Unsupported Features

The `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` error class also covers other unsupported features when using external metadata:

- **COLUMN_MASK**: Tables with [Column Mask (CM)](/concepts/column-mask-policies.md) policies are not supported. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **COLUMN_RENAME_WITHOUT_COLUMN_MAPPING**: Column mapping must be enabled to use an alias in the reconciliation query. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **PROJECTION_NOT_SUPPORTED**: The projection of the reconciliation query is not supported. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- **TABLE_TYPE**: Only streaming tables and materialized views are supported as table types. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Workarounds

To use external metadata with tables that have RLS policies, you must remove the row filter from the table before performing operations that require external metadata. Alternatively, consider using [Delta Sharing](/concepts/delta-sharing.md) or other access control mechanisms that are compatible with external metadata.

## Related Concepts

- [External Metadata](/concepts/external-metadata-api.md) — The feature that allows Databricks to read metadata from external systems
- [Row-Level Security (RLS)](/concepts/row-level-security-rls-policies.md) — Security policies that filter rows based on user identity
- [Column Mask (CM)](/concepts/column-mask-policies.md) — Security policies that mask column values based on user identity
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for Delta tables
- DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE error|DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE error class — The full error class covering all unsupported features

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
