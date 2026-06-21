---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb4f554fa18a20cabdef8d02a629075159653021c0fd2b58e7f2a6e4b606f63f
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - tutorial-configure-abac-databricks-on-aws.md
    - tutorial-configure-abac-with-sql-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - row-filter-policies
    - RFP
    - ROW_FILTER
    - Row Filter
    - Row Filter Policy|row filter policies
    - Row Filters
    - Row Filter|row filters
    - Row filter
    - Row filter policy
    - Row filtering
    - Row filters
    - row filter
    - row filter policy
    - row filter policy|row filter
    - row filters
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: tutorial-configure-abac-with-sql-databricks-on-aws.md
    - file: tutorial-configure-abac-databricks-on-aws.md
title: Row Filter Policies
description: ABAC policy type that enforces row-level security on tables, materialized views, and streaming tables by filtering rows based on attributes
tags:
  - access-control
  - row-level-security
  - unity-catalog
timestamp: "2026-06-19T22:08:48.203Z"
---

# Row filter policies

**Row filter policies** are a type of attribute-based access control (ABAC) policy in [Unity Catalog](/concepts/unity-catalog.md) that dynamically restrict which rows a user can see in a table, materialized view, or streaming table. The policy evaluates a user-defined function (UDF) against each row; rows for which the function returns `FALSE` are excluded from query results. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

Row filter policies are one of three ABAC policy types supported by Unity Catalog, alongside [Column Mask Policies](/concepts/column-mask-policies.md) and GRANT policies (Beta). They rely on [Governed Tags](/concepts/governed-tags.md) to identify which tables and columns the policy should apply to, enabling consistent, tag-driven row-level security across entire catalogs or schemas. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How row filter policies work

A row filter policy is attached to a securable object — a catalog, schema, or table — and specifies:

- **Scope** (`ON` clause): The catalog, schema, or table where the policy is evaluated. A policy attached at the catalog level applies to all tables in that catalog; at schema level, to all tables in that schema; at table level, only to that table. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]
- **Principals** (`TO` and optional `EXCEPT` clause): Which users, groups, or service principals are subject to the policy, and which are exempt. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]
- **UDF**: A user-defined function (written in SQL or Python) that implements the row-filtering logic. The function must be registered in Unity Catalog and the policy creator must have `EXECUTE` privilege on it. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]
- **Table conditions** (`WHEN` clause): Boolean expressions using `has_tag()` or `has_tag_value()` that identify which tables the policy targets. If omitted, defaults to `TRUE` (all tables in scope). ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]
- **Column conditions** (`MATCH COLUMNS` clause): One or more tag-based expressions that identify which columns provide arguments to the UDF. Each expression can be aliased and referenced in the `USING COLUMNS` clause. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]
- **UDF arguments** (`USING COLUMNS` clause): The arguments passed to the UDF. These can be column values identified by matching tags, constant literals, or boolean values. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

When a user queries a table within the policy's scope, Unity Catalog evaluates the policy dynamically against that table and its columns. If the table’s tags match the `WHEN` condition and the columns match the `MATCH COLUMNS` conditions, the UDF is applied to each row. Rows for which the UDF returns `FALSE` are hidden from the user. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

### Tag inheritance

Tags automatically propagate from parent catalogs and schemas to their children. This means a policy referencing a tag on a schema will match tables inside that schema (unless overridden). Columns, however, do not inherit tags from parent tables — column-level tags must be applied directly. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Syntax

The SQL syntax for creating a row filter policy is:

```sql
CREATE POLICY policy_name
ON { CATALOG | SCHEMA | TABLE } securable_name
ROW FILTER function_name
TO `principal` [, `principal` ...]
[EXCEPT `principal` [, `principal` ...]]
FOR TABLES
[WHEN condition_expression]
[MATCH COLUMNS column_expression_1 AS alias_1 [, column_expression_2 AS alias_2, ...]]
[USING COLUMNS (alias_or_constant [, ...])];
```

- `function_name` is the name of the UDF used for filtering.
- `WHEN condition_expression` targets tables by their tags. Example: `WHEN has_tag('HR')`.
- `MATCH COLUMNS` identifies columns based on tags. Example: `MATCH COLUMNS has_tag('region') AS rgn`.
- `USING COLUMNS` passes the matched column values or constants to the UDF. Example: `USING COLUMNS (rgn, 'EMEA')`.

You can also create a row filter policy using the Catalog Explorer UI (see the Tutorial: Configure ABAC).

## Example

The following policy ensures that only rows matching the EMEA region are visible to the `emea team` group, for all tables in the `sales` catalog that have a column tagged `region`:

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING) RETURNS BOOLEAN
  RETURN region = allowed;

CREATE POLICY regional_access_emea
ON CATALOG sales
ROW FILTER filter_by_region
TO `emea team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'EMEA');
```

^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

In the tutorial example, a row filter policy called `hide_eu_customers` uses the UDF `is_not_eu_address` to exclude rows where the address column (tagged `pii : address`) contains EU-related substrings. ^[tutorial-configure-abac-databricks-on-aws.md]

## Permissions

To create a row filter policy on a securable object, you must have `MANAGE` permission on that object or own it. You also need `EXECUTE` privilege on the UDF that the policy references. The UDF must be registered in Unity Catalog. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

Row filter policies do **not** grant `SELECT` or any other data access privilege on their own. The user must already have `SELECT` (or equivalent) on the table from a direct grant or role membership. The policy only filters rows for users who already have access to the table. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Best practices

- **Attach policies at the highest applicable level** (usually catalog) to maximize governance efficiency and automatically cover all tables within the scope. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]
- **Use groups in `TO` and `EXCEPT`** rather than individual users, so membership changes automatically propagate.
- **Leverage tag inheritance** to apply consistent policies across many tables with minimal configuration.
- **Write UDFs as SQL functions** for better performance; Python UDFs are supported but cannot be inlined by the query optimizer. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Limitations

- Row filter policies currently apply only to tables, materialized views, and streaming tables. They do not apply to other securable types such as models or volumes. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- The `has_tag` and `has_tag_value` functions use snake_case naming; the older camelCase forms (`hasTag`, `hasTagValue`) continue to work but are not recommended for new policies. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## Related concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The overarching access control model
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask column values
- [GRANT policies](/concepts/grant-policies-beta.md) — ABAC policies that dynamically grant privileges
- [Governed Tags](/concepts/governed-tags.md) — The attributes used in policy conditions
- User-defined functions — The filtering logic used by row filter policies
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages policies

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- tutorial-configure-abac-databricks-on-aws.md
- tutorial-configure-abac-with-sql-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [tutorial-configure-abac-with-sql-databricks-on-aws.md](/references/tutorial-configure-abac-with-sql-databricks-on-aws-99ec3df0.md)
3. [tutorial-configure-abac-databricks-on-aws.md](/references/tutorial-configure-abac-databricks-on-aws-cbba5828.md)
