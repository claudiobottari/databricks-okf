---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f10a66e9079e7823fdc885c3a0e7fd4606092850c3276435e5aa019c1899600
  pageDirectory: concepts
  sources:
    - row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-row-filters-and-column-masks
    - column masks and Limitations of row filters
    - LORFACM
  citations:
    - file: row-filters-and-column-masks-databricks-on-aws.md
title: Limitations of row filters and column masks
description: Comprehensive set of constraints including runtime version requirements, unsupported operations (MERGE, time travel, clones, views), and dedicated access mode restrictions.
tags:
  - data-governance
  - unity-catalog
  - limitations
timestamp: "2026-06-19T20:16:43.140Z"
---

# Limitations of Row Filters and Column Masks

**Limitations of row filters and column masks** encompass the runtime, data source, operation, and compute-mode restrictions that apply when using these [Unity Catalog](/concepts/unity-catalog.md) access controls on Databricks. Understanding these limitations is essential for planning secure data access patterns without encountering unexpected failures or data exposure.

## Runtime Version Restrictions

Row filters and column masks are not supported on Databricks Runtime versions below 12.2 LTS. When users attempt to access tables with these policies from unsupported runtimes, the system fails securely — no data is returned. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Data Source and Sharing Limitations

Row filters and column masks cannot be applied to views. ^[row-filters-and-column-masks-databricks-on-aws.md]

Tables with row filters or column masks cannot be accessed using the Iceberg REST catalog or Unity REST APIs. ^[row-filters-and-column-masks-databricks-on-aws.md]

[Delta Lake](/concepts/delta-lake.md) APIs are not supported for tables with these policies. ^[row-filters-and-column-masks-databricks-on-aws.md]

OpenSharing providers cannot share tables that have table-level row filters or column masks. However, tables with [ABAC](/concepts/abac-attribute-based-access-control.md)-based row filters or column masks can be shared if the share owner is exempt from the policy. ^[row-filters-and-column-masks-databricks-on-aws.md]

OpenSharing recipients can only apply row filters and column masks to shared tables and foreign tables — not to streaming tables or materialized views. ^[row-filters-and-column-masks-databricks-on-aws.md]

Path-based access to files in tables with policies is not supported. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Operation Limitations

`MERGE` statements do not support tables with row filter or column-mask policies that contain nesting, aggregations, windows, limits, or non-deterministic functions. ^[row-filters-and-column-masks-databricks-on-aws.md]

On Databricks Runtime versions below 17.2, `DELETE`, `UPDATE`, and `MERGE` operations are not supported on partitioned tables when a row filter or column-mask policy is defined on the partition column. ^[row-filters-and-column-masks-databricks-on-aws.md]

Row-filter or column-mask policies with circular dependencies back to the original policies are not supported. ^[row-filters-and-column-masks-databricks-on-aws.md]

Row filters and column masks cannot reference tables that also have active row filters or column masks. In [ABAC](/concepts/abac-attribute-based-access-control.md) configurations, this can be worked around by excluding the policy function owner from the referenced table's policy. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Time Travel and Clone Limitations

[Time Travel](/concepts/delta-lake-time-travel.md) does not work with row-level security or column masks. In ABAC configurations, users explicitly excluded from a policy can still run time travel queries on the underlying data. ^[row-filters-and-column-masks-databricks-on-aws.md]

Deep and shallow clones are not supported on tables that have row-level security or column masks. In ABAC configurations, users explicitly excluded from a policy can still perform clone operations on the underlying data. ^[row-filters-and-column-masks-databricks-on-aws.md]

## AI Search and Generated Columns

You cannot create an AI Search index from a table that has row filters or column masks applied. ^[row-filters-and-column-masks-databricks-on-aws.md]

Column masks cannot be applied to columns that are referenced by generated columns. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Dedicated Access Mode Limitation

You cannot access a table with row filters or column masks from a dedicated access compute resource on Databricks Runtime 15.3 or below. Dedicated access mode is supported on Databricks Runtime 15.4 LTS or above if your workspace is enabled for serverless compute. ^[row-filters-and-column-masks-databricks-on-aws.md]

On Databricks Runtime 15.4 through 16.2, only read operations are supported from dedicated access mode. Write operations (including `INSERT`, `UPDATE`, and `DELETE`) require Databricks Runtime 16.3 or above and must use supported patterns such as `MERGE INTO`. ^[row-filters-and-column-masks-databricks-on-aws.md]

When querying tables with row filters or column masks from dedicated access mode compute, Databricks uses [serverless compute](/concepts/serverless-gpu-compute.md) to enforce fine-grained access controls (FGAC). All FGAC limitations and considerations apply as a result. ^[row-filters-and-column-masks-databricks-on-aws.md]

FGAC uses Cloud Fetch to write temporary result sets to internal workspace storage. If you have S3 bucket versioning enabled, this can lead to exponential storage growth. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- [Row filters](/concepts/row-filter-policies.md) — Restrict which rows a user can see in a table
- [Column masks](/concepts/column-mask-policies.md) — Control what values a user sees for specific columns
- ABAC policies — Recommended alternative for consistent policies across many tables
- Dynamic views — Alternative mechanism for row-level and column-level access control
- Fine-grained access control — Broader category of security controls

## Sources

- row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [row-filters-and-column-masks-databricks-on-aws.md](/references/row-filters-and-column-masks-databricks-on-aws-f091f827.md)
