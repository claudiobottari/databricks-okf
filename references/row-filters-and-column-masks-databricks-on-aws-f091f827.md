---
title: Row filters and column masks | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/
ingestedAt: "2026-06-18T08:04:30.900Z"
---

Row filters and column masks are Unity Catalog access controls that restrict the rows and column values a user can see at query time. This page describes the _table-level_ form of these controls, which are configured directly on individual tables using SQL and managed by the table owner. For consistent row filtering and column masking across many tables, [ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies) are the recommended approach. They attach at the catalog or schema level and apply automatically based on governed tags.

tip

Databricks recommends [ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies) when you need consistent row filtering and column masking across many tables. ABAC policies attach at the catalog or schema level and apply automatically based on governed tags, rather than requiring per-table configuration.

## What are row filters?[​](#what-are-row-filters "Direct link to What are row filters?")

Row filters restrict which rows a user can see in a table. The filter is a SQL user-defined function (UDF) that evaluates each row at query time. Rows where the function returns `FALSE` are excluded from query results. This is commonly used for row-level security. For example, you can restrict users to records from a specific region, department, or account.

Table-level row filters are bound to a single table using `ALTER TABLE ... SET ROW FILTER` and managed by the table owner. For consistent row filtering across many tables, use [ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies) instead.

## What are column masks?[​](#what-are-column-masks "Direct link to What are column masks?")

Column masks control what values a user sees for specific columns. The mask is a SQL UDF that takes the column value as input and returns the original value or a masked version. The return type must match or be castable to the column's data type. Each column can have one mask. Column masks can take other columns as inputs to vary behavior based on multiple attributes.

Table-level column masks are bound to a column using `ALTER TABLE ... ALTER COLUMN ... SET MASK` and managed by the table owner. They apply only to that column on that table. For consistent column masking across many tables, use [ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies) instead.

## When to use ABAC policies or dynamic views instead[​](#when-to-use-abac-policies-or-dynamic-views-instead "Direct link to When to use ABAC policies or dynamic views instead")

Unity Catalog provides two related mechanisms for row-level and column-level access control:

*   **[ABAC policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/)** attach at the catalog or schema level and apply automatically to tables and columns based on governed tags. Use ABAC when you need consistent rules across many tables, separation of duties between policy authors and data stewards, or automatic coverage of new tables as they are tagged. For a side-by-side comparison with table-level row filters and column masks, see [When to use ABAC vs table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/abac-vs-rls-cm).
*   **[Dynamic views](https://docs.databricks.com/aws/en/views/dynamic)** wrap one or more base tables in a SQL view that filters rows, masks columns, or reshapes data, typically gated by group-membership functions like `is_account_group_member()`. Use dynamic views when you want to expose a curated, transformed, or joined version of your data to users who don't have access to the underlying tables. Example use cases include sharing a redacted slice of a fact table with an analyst group, or combining columns from multiple tables into a single secure layer.

For a more detailed comparison with dynamic views and ABAC policies, see [When to use ABAC vs table-level row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/abac-vs-rls-cm).

## How to apply row filters and column masks[​](#how-to-apply-row-filters-and-column-masks "Direct link to How to apply row filters and column masks")

Apply row filters and column masks in one of the following ways:

*   **Using ABAC policies** (recommended): Apply filters and masks centrally using governed tags and reusable policies. ABAC scales across catalogs and schemas and can be defined by higher-level admins, so table owners can't override or remove them. Policy logic is also evaluated more efficiently than table-specific UDFs. See [Attribute-based access control in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/).
*   **Manual assignment per table**: Apply filters and masks by assigning UDFs directly to individual tables and columns. This allows fine-grained, table-specific control but is harder to scale and maintain. See [Manually apply row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply).

## Performance recommendations[​](#performance-recommendations "Direct link to performance-recommendations")

Row filters and column masks control data visibility by ensuring that users cannot view base table values before filtering or masking is applied. When the query engine must choose between optimization and protecting against information leakage from filtered or masked values, it always makes the secure choice, which can affect query performance. To minimize that impact:

*   **Use simple UDFs.** Functions with fewer expressions perform better. Prefer simple `CASE` expressions over mapping tables or expression subqueries.
*   **Limit the number of distinct column masks on large tables.** Each distinct mask is evaluated during queries. Apply masks only to truly sensitive columns and reuse masking functions where possible.
*   **Reduce the number of UDF arguments.** Databricks cannot optimize away column references that come from UDF arguments, even if those columns are not used in the query. Use UDFs with fewer arguments where possible.
*   **Avoid row filters with too many `AND` conjuncts.** Only one distinct row filter can resolve at runtime for a given user and table, so a common pattern is to combine logic with `AND`. The more conjuncts you add, the more likely the combined filter includes one of the patterns warned about above. Use fewer conjuncts where possible.
*   **Use deterministic expressions that cannot throw errors.** Expressions that can throw errors (such as ANSI division) prevent the SQL compiler from pushing operations down in the query plan, because errors like "division by zero" could reveal information about values before filtering or masking. Use deterministic expressions that never throw errors, such as `try_divide`.
*   **Prefer SQL to Python UDFs.** Python UDFs are less performant than SQL and offer fewer optimization opportunities. If you must use Python, mark the UDF as `DETERMINISTIC` when applicable.

For full UDF performance guidance (including predicate pushdown and engine-level optimization details), see [Performance considerations for row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/performance). Most of the guidance there applies equally to manually-applied row filters and column masks. For example UDFs, see [Common patterns for row filtering and column masking](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/common-patterns).

## Data type mismatch behavior[​](#data-type-mismatch-behavior "Direct link to data-type-mismatch-behavior")

When you create a row filter or column mask, the data type of each table column passed to the function must match the corresponding parameter type in the UDF. If there is a type mismatch, such as a `STRING` column passed to an `INT` parameter, Databricks implicitly casts the column value to the parameter type, which can cause unexpected behavior when the column contains values that can't be converted.

With ANSI mode disabled (`spark.sql.ansi.enabled = false`), uncastable values are silently converted to `NULL`, no error is raised, and the UDF receives `NULL` instead of the actual column value. This can produce incorrect results, such as a row filter that returns all rows instead of filtering them, or a column mask that masks the wrong values. Databricks recommends enabling ANSI mode (`spark.sql.ansi.enabled = true`), which raises an error when a cast fails, making the problem immediately visible, instead of silently returning `NULL`.

### Example: Row filter with a type mismatch[​](#example-row-filter-with-a-type-mismatch "Direct link to Example: Row filter with a type mismatch")

Consider a table with a `STRING` column and a row filter whose parameter is accidentally declared as `INT` instead of `STRING`:

SQL

    SET spark.sql.ansi.enabled = false;CREATE TABLE employees (  id INT,  salary INT,  department STRING);INSERT INTO employees VALUES  (91, 200000, null),  (1, 200000, 'exec'),  (2, 50000, 'engineering'),  (3, 150000, 'exec');-- Bug: parameter type is INT, but the column is STRINGCREATE FUNCTION salary_filter(dept INT) RETURNS BOOLEANRETURN dept IS NULL;ALTER TABLE employees SET ROW FILTER salary_filter ON (department);

When queried, the `department` values `'exec'` and `'engineering'` can't be cast to `INT`, so they are silently converted to `NULL`. Because the filter returns `true` when the input is `NULL`, all rows are returned instead of only the rows where `department` is actually `NULL`:

The correct UDF definition uses `STRING` as the parameter type to match the column:

SQL

    CREATE FUNCTION salary_filter(dept STRING) RETURNS BOOLEANRETURN dept IS NULL;

With this fix, the query returns only the row where `department` is `NULL`.

## Limitations[​](#limitations "Direct link to limitations")

*   Databricks Runtime versions below 12.2 LTS do not support row filters or column masks. These runtimes fail securely, meaning that if you try to access tables from these runtimes, no data is returned.
*   You cannot apply row-level security or column masks to a view.
*   You cannot use Iceberg REST catalog or Unity REST APIs to access tables with row filters or column masks.
*   Delta Lake APIs are not supported.
*   OpenSharing providers cannot share tables with table-level row filters or column masks. Tables with ABAC-based row filters or column masks can be shared if the share owner is exempt from the policy. See [OpenSharing tables with ABAC policies or views that reference them](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements#delta-sharing).
*   OpenSharing recipients can apply row filters and column masks only to shared tables and foreign tables, not to streaming tables or materialized views.
*   Path-based access to files in tables with policies is not supported.
*   `MERGE` statements do not support tables with row filter or column-mask policies that contain nesting, aggregations, windows, limits, or non-deterministic functions.
*   Databricks Runtime versions below 17.2 do not support `DELETE`, `UPDATE`, and `MERGE` on partitioned tables with row filter or column-mask policies defined on the partition column.
*   Row-filter or column-mask policies with circular dependencies back to the original policies are not supported.
*   Row filters and column masks cannot reference tables that also have active row filters or column masks. In ABAC configurations, you can work around this by excluding the policy function owner from the referenced table's policy.
*   Time travel does not work with row-level security or column masks. In ABAC configurations, users who are explicitly excluded from a policy can still run time travel queries on the underlying data.
*   Deep and shallow clones are not supported on tables that have row-level security or column masks. In ABAC configurations, users who are explicitly excluded from a policy can still perform clone operations on the underlying data.
*   You cannot create an AI Search index from a table that has row filters or column masks applied.
*   Column masks cannot be applied to columns that are referenced by generated columns. See [Generated columns and column masks](https://docs.databricks.com/aws/en/tables/features/generated-columns#gen-col-masks).

### Dedicated access mode limitation[​](#dedicated-access-mode-limitation "Direct link to dedicated-access-mode-limitation")

You cannot access a table with row filters or column masks from a dedicated access compute resource on Databricks Runtime 15.3 or below. You can use dedicated access mode on Databricks Runtime 15.4 LTS or above if your workspace is enabled for serverless compute. However, only read operations are supported on Databricks Runtime 15.4 through 16.2. Write operations (including `INSERT`, `UPDATE`, and `DELETE`) require Databricks Runtime 16.3 or above and must use supported patterns such as `MERGE INTO`.

When you query tables with row filters or column masks from dedicated access mode compute, Databricks uses serverless compute to enforce fine-grained access controls (FGAC). As a result, all FGAC limitations and considerations apply. See [Fine-grained access control on dedicated compute](https://docs.databricks.com/aws/en/compute/single-user-fgac).

FGAC uses [Cloud Fetch](https://docs.databricks.com/aws/en/integrations/jdbc/capability#cloud-fetch-in-jdbc) to write temporary result sets to internal workspace storage. If you have S3 bucket versioning enabled, this can lead to exponential storage growth. See [S3 bucket versioning considerations](https://docs.databricks.com/aws/en/integrations/jdbc/capability#advanced-configurations) for configuration recommendations.
