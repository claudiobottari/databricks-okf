---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99b3d2fe5c4d8b1b1da38598986ad9211bef83588e67ed7273219bf73118f509
  pageDirectory: concepts
  sources:
    - row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-masks-unity-catalog
    - CM(C
    - Column Mask Functions
  citations:
    - file: row-filters-and-column-masks-databricks-on-aws.md
title: Column masks (Unity Catalog)
description: SQL UDFs applied to specific columns that transform or redact column values at query time based on user identity or other attributes.
tags:
  - data-governance
  - unity-catalog
  - security
  - masking
timestamp: "2026-06-19T20:16:19.820Z"
---

# Column masks (Unity Catalog)

**Column masks** are a Unity Catalog access control mechanism that restricts the values a user can see for specific columns in a table at query time. A column mask is a SQL user-defined function (UDF) that takes the column value as input and returns either the original value or a masked version. The return type must match or be castable to the column's data type. Each column can have one mask, and masks can take other columns as inputs to vary behavior based on multiple attributes. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Overview

Column masks are configured directly on individual tables using SQL and are managed by the table owner. They are bound to a column using `ALTER TABLE ... ALTER COLUMN ... SET MASK`. Table-level column masks apply only to that specific column on that specific table. ^[row-filters-and-column-masks-databricks-on-aws.md]

For consistent column masking across many tables, Databricks recommends using ABAC policies instead. ABAC policies attach at the catalog or schema level and apply automatically based on governed tags, rather than requiring per-table configuration. ^[row-filters-and-column-masks-databricks-on-aws.md]

## When to use ABAC policies or dynamic views instead

Unity Catalog provides two related mechanisms for column-level access control:

- **ABAC policies**: Attach at the catalog or schema level and apply automatically to tables and columns based on governed tags. Use ABAC when you need consistent rules across many tables, separation of duties between policy authors and data stewards, or automatic coverage of new tables as they are tagged. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Dynamic views**: Wrap one or more base tables in a SQL view that masks columns, filters rows, or reshapes data, typically gated by group-membership functions like `is_account_group_member()`. Use dynamic views when you want to expose a curated, transformed, or joined version of your data to users who don't have access to the underlying tables. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Performance recommendations

Column masks control data visibility by ensuring that users cannot view base table values before masking is applied. When the query engine must choose between optimization and protecting against information leakage from masked values, it always makes the secure choice, which can affect query performance. To minimize that impact: ^[row-filters-and-column-masks-databricks-on-aws.md]

- **Use simple UDFs.** Functions with fewer expressions perform better. Prefer simple `CASE` expressions over mapping tables or expression subqueries. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Limit the number of distinct column masks on large tables.** Each distinct mask is evaluated during queries. Apply masks only to truly sensitive columns and reuse masking functions where possible. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Reduce the number of UDF arguments.** Databricks cannot optimize away column references that come from UDF arguments, even if those columns are not used in the query. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Use deterministic expressions that cannot throw errors.** Expressions that can throw errors (such as ANSI division) prevent the SQL compiler from pushing operations down in the query plan, because errors could reveal information about values before masking. Use deterministic expressions that never throw errors, such as `try_divide`. ^[row-filters-and-column-masks-databricks-on-aws.md]
- **Prefer SQL to Python UDFs.** Python UDFs are less performant than SQL and offer fewer optimization opportunities. If you must use Python, mark the UDF as `DETERMINISTIC` when applicable. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Data type mismatch behavior

When you create a column mask, the data type of each table column passed to the function must match the corresponding parameter type in the UDF. If there is a type mismatch, Databricks implicitly casts the column value to the parameter type, which can cause unexpected behavior when the column contains values that can't be converted. ^[row-filters-and-column-masks-databricks-on-aws.md]

With ANSI mode disabled (`spark.sql.ansi.enabled = false`), uncastable values are silently converted to `NULL`, no error is raised, and the UDF receives `NULL` instead of the actual column value. This can produce incorrect results, such as a column mask that masks the wrong values. Databricks recommends enabling ANSI mode (`spark.sql.ansi.enabled = true`), which raises an error when a cast fails, making the problem immediately visible, instead of silently returning `NULL`. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Limitations

- Databricks Runtime versions below 12.2 LTS do not support column masks. These runtimes fail securely, meaning that if you try to access tables from these runtimes, no data is returned. ^[row-filters-and-column-masks-databricks-on-aws.md]
- You cannot apply column masks to a view. ^[row-filters-and-column-masks-databricks-on-aws.md]
- You cannot use Iceberg REST catalog or Unity REST APIs to access tables with column masks. ^[row-filters-and-column-masks-databricks-on-aws.md]
- Delta Lake APIs are not supported. ^[row-filters-and-column-masks-databricks-on-aws.md]
- OpenSharing providers cannot share tables with table-level column masks. Tables with ABAC-based column masks can be shared if the share owner is exempt from the policy. ^[row-filters-and-column-masks-databricks-on-aws.md]
- Path-based access to files in tables with policies is not supported. ^[row-filters-and-column-masks-databricks-on-aws.md]
- `MERGE` statements do not support tables with column-mask policies that contain nesting, aggregations, windows, limits, or non-deterministic functions. ^[row-filters-and-column-masks-databricks-on-aws.md]
- Column-mask policies with circular dependencies back to the original policies are not supported. ^[row-filters-and-column-masks-databricks-on-aws.md]
- Column masks cannot reference tables that also have active column masks. ^[row-filters-and-column-masks-databricks-on-aws.md]
- Time travel does not work with column masks. ^[row-filters-and-column-masks-databricks-on-aws.md]
- Deep and shallow clones are not supported on tables that have column masks. ^[row-filters-and-column-masks-databricks-on-aws.md]
- You cannot create an AI Search index from a table that has column masks applied. ^[row-filters-and-column-masks-databricks-on-aws.md]
- Column masks cannot be applied to columns that are referenced by generated columns. ^[row-filters-and-column-masks-databricks-on-aws.md]

### Dedicated access mode limitation

You cannot access a table with column masks from a dedicated access compute resource on Databricks Runtime 15.3 or below. You can use dedicated access mode on Databricks Runtime 15.4 LTS or above if your workspace is enabled for serverless compute. However, only read operations are supported on Databricks Runtime 15.4 through 16.2. Write operations (including `INSERT`, `UPDATE`, and `DELETE`) require Databricks Runtime 16.3 or above and must use supported patterns such as `MERGE INTO`. ^[row-filters-and-column-masks-databricks-on-aws.md]

When you query tables with column masks from dedicated access mode compute, Databricks uses serverless compute to enforce fine-grained access controls (FGAC). FGAC uses Cloud Fetch to write temporary result sets to internal workspace storage. If you have S3 bucket versioning enabled, this can lead to exponential storage growth. ^[row-filters-and-column-masks-databricks-on-aws.md]

## Related concepts

- [Row filters (Unity Catalog)](/concepts/row-filters-unity-catalog.md) — The companion mechanism for restricting which rows a user can see
- ABAC policies — The recommended approach for consistent column masking across many tables
- Dynamic views — An alternative mechanism for column-level access control using SQL views
- [Unity Catalog](/concepts/unity-catalog.md) — The overall data governance platform
- [Fine-grained access control (FGAC)](/concepts/dynamic-views-for-fine-grained-access-control.md) — The broader category of access controls that includes column masks

## Sources

- row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [row-filters-and-column-masks-databricks-on-aws.md](/references/row-filters-and-column-masks-databricks-on-aws-f091f827.md)
