---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7a0cecad07843d40f3a80bf9ea975ab00fe31fbcc7d62c8a299081d878b447f
  pageDirectory: concepts
  sources:
    - row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filters-unity-catalog
    - RF(C
  citations:
    - file: row-filters-and-column-masks-databricks-on-aws.md
title: Row filters (Unity Catalog)
description: SQL UDFs applied to tables that restrict which rows a user can see at query time based on per-row evaluation.
tags:
  - data-governance
  - unity-catalog
  - security
timestamp: "2026-06-19T20:16:17.978Z"
---

# Row Filters (Unity Catalog)

**Row filters** are a Unity Catalog access control mechanism that restricts which rows a user can see in a table at query time. They enforce row-level security by evaluating a SQL user-defined function (UDF) on each row; rows for which the function returns `FALSE` are excluded from query results. ^[row-filters-and-column-masks-databricks-on-aws.md]

## How Row Filters Work

A row filter is a SQL UDF defined separately from the table and then bound to a table using `ALTER TABLE ... SET ROW FILTER`. The UDF takes one or more table columns as arguments and must return a `BOOLEAN`. The filter is evaluated at query time by the Unity Catalog query engine. Table-level row filters are managed by the table owner. ^[row-filters-and-column-masks-databricks-on-aws.md]

Common use cases include restricting users to records from a specific region, department, or account. ^[row-filters-and-column-masks-databricks-on-aws.md]

## When to Use Alternatives

Unity Catalog provides two other mechanisms for row-level access control that may be preferable in certain scenarios:

- **ABAC policies**: Attach at the catalog or schema level and apply automatically based on governed tags. Use ABAC when you need consistent rules across many tables, separation of duties between policy authors and data stewards, or automatic coverage of new tables. ABAC is the recommended approach for consistent row filtering across many tables. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Dynamic views**: Wrap one or more base tables in a SQL view that filters rows, masks columns, or reshapes data, typically gated by group-membership functions. Use dynamic views when you want to expose a curated, transformed, or joined version of your data to users who lack access to the underlying tables. ^[row-filters-and-column-masks-databricks-on-aws.md]

For a side-by-side comparison, see [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md). ^[row-filters-and-column-masks-databricks-on-aws.md]

## Application Methods

Row filters can be applied in two ways:

- **Using ABAC policies (recommended)**: Apply filters centrally using governed tags and reusable policies. ABAC scales across catalogs and schemas, can be defined by higher-level admins, and is evaluated more efficiently than table-specific UDFs. Table owners cannot override or remove them. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Manual assignment per table**: Assign UDFs directly to individual tables using SQL. This provides fine-grained, table-specific control but is harder to scale and maintain. See [Manually apply row filters and column masks](/concepts/row-filters-and-column-masks.md). ^[row-filters-and-column-masks-databricks-on-aws.md]

## Performance Recommendations

Row filters and column masks always prioritize security over performance, which can affect query speed. To minimize the performance impact of row filters:

- Use simple UDFs (prefer `CASE` expressions over mapping tables or subqueries).
- Avoid row filters with too many `AND` conjuncts; fewer conjuncts allow better optimization.
- Use deterministic expressions that cannot throw errors (e.g., `try_divide` instead of ANSI division).
- Prefer SQL UDFs over Python UDFs; if using Python, mark the UDF as `DETERMINISTIC` when applicable. ^[row-filters-and-column-masks-databricks-on-aws.md]

For full guidance, see [Performance considerations for row filter and column mask policies](/concepts/performance-optimization-for-row-filters-and-column-masks.md). Most of that guidance applies equally to manually-applied row filters. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Data Type Mismatch Behavior

When creating a row filter, the data type of each table column passed to the UDF must match the corresponding parameter type. If there is a mismatch, Databricks implicitly casts the column value to the parameter type. With ANSI mode disabled (`spark.sql.ansi.enabled = false`), uncastable values are silently converted to `NULL`, which can cause the filter to return incorrect results (e.g., returning all rows instead of filtering). Databricks recommends enabling ANSI mode (`spark.sql.ansi.enabled = true`), which raises an error on cast failure, making the problem immediately visible. ^[row-filters-and-column-masks-databricks-on-aws.md]

**Example**: A table with a `STRING` column `department` and a row filter UDF accidentally declared with an `INT` parameter. The values `'exec'` and `'engineering'` cannot be cast to `INT` and become `NULL`. If the filter returns `TRUE` when input is `NULL`, all rows are returned instead of only rows where `department` is actually `NULL`. Fixing the UDF parameter type to `STRING` resolves the issue. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Limitations

Row filters and column masks share a common set of limitations. The following apply specifically to row filters or to both mechanisms:

- Databricks Runtime versions below 12.2 LTS do not support row filters; access fails securely (no data returned).
- You cannot apply row-level security to a view.
- Iceberg REST catalog, Unity REST APIs, and Delta Lake APIs are not supported.
- OpenSharing providers cannot share tables with table-level row filters (ABAC-based filters can be shared if the share owner is exempt).
- OpenSharing recipients can apply row filters only to shared tables and foreign tables, not to streaming tables or materialized views.
- Path-based file access is not supported.
- `MERGE` statements do not support tables with row filter UDFs that contain nesting, aggregations, windows, limits, or non-deterministic functions.
- Databricks Runtime below 17.2 does not support `DELETE`, `UPDATE`, and `MERGE` on partitioned tables with row filters defined on the partition column.
- Circular dependencies between row filter policies and themselves are not supported.
- Row filters cannot reference tables that also have active row filters or column masks.
- Time travel does not work with row-level security.
- Deep and shallow clones are not supported on tables with row-level security.
- You cannot create an AI Search index from a table with row filters. ^[row-filters-and-column-masks-databricks-on-aws.md]

### Dedicated Access Mode Limitation

You cannot access a table with row filters from a dedicated access compute resource on Databricks Runtime 15.3 or below. On Databricks Runtime 15.4 LTS or above (with serverless compute enabled), only read operations are supported up to runtime 16.2; write operations require runtime 16.3 or above. When querying from dedicated access mode, Databricks uses serverless compute to enforce fine-grained access controls (FGAC), which may use Cloud Fetch and cause S3 bucket versioning storage growth issues. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- [Column masks (Unity Catalog)](/concepts/column-masks-unity-catalog.md)
- ABAC policies
- Dynamic views
- [Unity Catalog](/concepts/unity-catalog.md)
- [Manually apply row filters and column masks](/concepts/row-filters-and-column-masks.md)
- [Performance considerations for row filter and column mask policies](/concepts/performance-optimization-for-row-filters-and-column-masks.md)
- Common patterns for row filtering and column masking
- [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md)
- Fine-grained access control on dedicated compute

## Sources

- row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [row-filters-and-column-masks-databricks-on-aws.md](/references/row-filters-and-column-masks-databricks-on-aws-f091f827.md)
