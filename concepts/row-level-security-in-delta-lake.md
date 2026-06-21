---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a0e4fe591ec5c447fc72c82815432431d7788930b409f6291861ce3e8718e852
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-level-security-in-delta-lake
    - RLSIDL
    - Row-level security in Databricks
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Row Level Security in Delta Lake
description: A Delta Lake table feature for filtering rows based on user identity, which is incompatible with REFRESH SYNC UNIFORM.
tags:
  - delta-lake
  - security
  - row-level
timestamp: "2026-06-19T10:09:56.434Z"
---

# Row Level Security in Delta Lake

**Row Level Security (RLS) in Delta Lake** is a security feature that restricts which rows of a Delta table a user can query, filtering data at the row level based on user permissions or attributes. When row-level security is active on a Delta table, certain operations—such as refreshing the table's Uniform (Iceberg) manifest—may fail with a specific error condition. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## How Row Level Security Works

Row Level Security in Delta Lake is typically implemented through [Row Filter Policies](/concepts/row-filter-policies.md) in [Unity Catalog](/concepts/unity-catalog.md). These policies define conditions that are automatically applied to queries, ensuring users only see rows they are authorized to access. The filtering occurs transparently at query execution time without requiring changes to user queries. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Condition with Uniform Refresh

The `REFRESH` identifier `SYNC UNIFORM` is not supported on tables that have row-level security enabled. If you attempt to synchronize the Uniform manifest on such a table, Delta Lake returns the following error: ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

```
ROW_LEVEL_SECURITY
Row level security is not supported by `REFRESH` identifier `SYNC UNIFORM`.
```

This error is part of the broader DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class with SQLSTATE: 0AKDC. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Types of Row-Level Security

Delta Lake supports different mechanisms for implementing row-level security:

- **Row Filter Policies** – The primary mechanism in Unity Catalog, allowing you to define filter conditions that are applied to all queries on a table.
- **Attribute-Based Access Control (ABAC) Row Filters** – A more dynamic approach that uses [Governed Tags](/concepts/governed-tags.md) to automatically apply row filters across multiple tables. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Implications for Operations

If a Delta table has row-level security policies applied:

- You cannot use `REFRESH SYNC UNIFORM` to generate or update the Iceberg manifest for that table.
- To enable [Uniform (Delta Lake)](/concepts/delta-uniform.md) on a table that requires row-level security, you must either remove the row-level security policies before performing the refresh, or choose a different approach to expose the table in Iceberg format without the `SYNC UNIFORM` operation.
- This limitation applies regardless of whether row filters are implemented through Unity Catalog row filter policies or ABAC row filter policies.

This restriction is independent of the row-level security implementation and applies to all forms of row filtering on Delta tables. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Error Conditions

The same error class also includes other reasons why `REFRESH SYNC UNIFORM` may fail, such as:

- [COLUMN_MASK](/concepts/column-mask-policies.md) – When column masks are applied to the table
- COMPATIBILITY_NOT_ENABLED – When Uniform compatibility is not configured
- [UNSUPPORTED_READER_FEATURES](/concepts/unsupported-reader-features-for-delta-uniform-refresh.md) – When unsupported reader table features are present
- UNSUPPORTED_TYPE – When the source type is not supported

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) – The primary mechanism for row-level security in Unity Catalog
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md) – Attribute-based row filters that work across multiple tables
- [Uniform (Delta Lake)](/concepts/delta-uniform.md) – The feature that enables reading Delta tables in Iceberg format
- [REFRESH SYNC UNIFORM](/concepts/refresh-sync-uniform.md) – The SQL command that fails when row-level security is present
- [Column Mask Policies](/concepts/column-mask-policies.md) – Another form of access control that has the same limitation
- Delta Lake Security Features – Overview of security capabilities in Delta Lake
- [Unity Catalog Access Control](/concepts/unity-catalog-access-control-models.md) – The broader access control system

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
