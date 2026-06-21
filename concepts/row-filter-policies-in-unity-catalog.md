---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38bdcb947fb02b6b61ed1316a7acf86a21874bb5c1512eac74eb454adebcacfa
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - tutorial-configure-abac-with-sql-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - row-filter-policies-in-unity-catalog
    - RFPIUC
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - file: tutorial-configure-abac-with-sql-databricks-on-aws.md
title: Row filter policies in Unity Catalog
description: ABAC policy type that supports row-level security on tables, materialized views, and streaming tables.
tags:
  - access-control
  - unity-catalog
  - row-level-security
  - policies
timestamp: "2026-06-19T14:04:37.459Z"
---

# Row Filter Policies in Unity Catalog

**Row Filter Policies** in Unity Catalog are a type of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy that dynamically exclude rows from query results based on governed tag conditions. Unlike table-level row filters that must be applied individually to each table, ABAC row filter policies can be defined once at a catalog or schema scope and automatically apply to all matching tables within that scope. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How Row Filter Policies Work

A row filter policy uses a user-defined function (UDF) in Unity Catalog that evaluates each row and returns a boolean value. Rows where the function returns `FALSE` are excluded from query results, while rows returning `TRUE` are visible to the user. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

The policy specifies:

- **Scope**: The catalog, schema, or table where the policy is attached (using the `ON` clause). Attaching at a catalog applies the policy to all tables in that catalog; attaching at a schema applies to all tables in that schema; attaching at a table applies only to that table. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Principals**: The `TO` clause lists the users, groups, or service principals subject to the policy. The optional `EXCEPT` clause exempts specific principals. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Filtering logic**: The `ROW FILTER` clause references a UDF that receives column values as arguments and returns a boolean for each row. The UDF’s first argument is bound automatically from the `ON COLUMN` clause. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Column matching**: The `MATCH COLUMNS` clause uses built-in tag functions (e.g., `has_tag()`, `has_tag_value()`) to identify which columns to pass to the filtering UDF. A policy can include up to three column expressions. All must match for the policy to apply. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Table condition**: The optional `WHEN` clause filters which tables within the scope the policy applies to, based on tags on the table itself. If omitted, the policy applies to all tables in scope. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Example

The following example hides rows containing EU addresses from `account users` (except the `compliance team`): ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

```sql
CREATE FUNCTION is_not_eu_address(address STRING) RETURNS BOOLEAN
  RETURN CASE
    WHEN LOWER(address) LIKE '%eu%' 
      OR LOWER(address) LIKE '%e.u.%' 
      OR LOWER(address) LIKE '%europe%'
    THEN FALSE
    ELSE TRUE
  END;

CREATE POLICY hide_eu_customers
ON SCHEMA abac_tutorial.customers
ROW FILTER is_not_eu_address
TO `account users`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'address') AS addr_col
USING COLUMNS (addr_col);
```

In this example:
- The policy is scoped to the schema `abac_tutorial.customers`.
- All users are subject to the row filter.
- The policy targets any column tagged with `pii : address` (the `MATCH COLUMNS` condition).
- The UDF `is_not_eu_address` receives the address value and returns `FALSE` (hide row) if the address references the EU. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

## UDF Requirements

- The UDF must return a `BOOLEAN` type. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- SQL UDFs are recommended for better performance; Python UDFs are supported but cannot be inlined by the query optimizer. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- The first argument to the UDF is always the column value identified by the `ON COLUMN` clause. Additional arguments are supplied via `USING COLUMNS` and can be aliases for other columns matching tag expressions, or constant values. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Creating a Row Filter Policy

To create a row filter policy, you must have `MANAGE` permission or ownership on the securable object (catalog, schema, or table) where the policy is attached, and `EXECUTE` privilege on the UDF that implements the filtering logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using SQL

```sql
CREATE POLICY policy_name
ON { CATALOG | SCHEMA | TABLE } securable_name
ROW FILTER function_name
TO principals [EXCEPT exempted_principals]
[FOR TABLES [WHEN (table_condition)]]
MATCH COLUMNS tag_expression [AS alias] [, ...]
[USING COLUMNS (alias [, ...] | constant [, ...])];
```

^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Catalog Explorer

1. Navigate to the catalog, schema, or table in the Catalog Explorer.
2. Click the **Policies** tab.
3. Click **New policy**.
4. For **Purpose**, choose **Hide table rows**.
5. Select or create the row filter function.
6. Configure function parameters by mapping columns matched by tags.
7. Click **Create policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Editing and Deleting Policies

Editing and deleting policies require `MANAGE` on the securable object or object ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Edit**: In Catalog Explorer, select the policy and update any fields except the policy name and the securable object where it is applied. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- **Delete**: In Catalog Explorer, select the policy and click **Delete policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Viewing Policies

Use the `SHOW POLICIES` command to list policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies from parent scopes, such as catalog-level policies that affect a table. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name;
```

Use `DESCRIBE POLICY` to view details of a specific policy: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
DESCRIBE POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name;
```

## Benefits of ABAC Row Filter Policies

- **Reusable**: One policy can filter rows based on the same type of column (e.g., all columns tagged `PII`) across many tables without per-table configuration. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Automatic**: When new tables are created and tagged, existing row filter policies apply automatically. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Consistent**: Ensures uniform filtering rules for similar data across the estate. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **Lower maintenance**: Updates to filtering logic can be done by modifying the UDF or the policy, rather than editing each table’s row filter individually. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use ABAC Row Filter Policies vs. Table-Level Row Filters

The source material directs readers to [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md) for a comparison. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Requirements

- Databricks Runtime 16.4 or above, or serverless compute. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- [Governed Tags](/concepts/governed-tags.md) applied to target objects. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `MANAGE` permission on the target securable object or object ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `EXECUTE` privilege on the UDF referenced by the policy. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – Restrict columns rather than rows.
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) – Dynamically grant privileges (currently for models).
- [Governed Tags](/concepts/governed-tags.md) – The attributes used in policy conditions.
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) – Alternative per-object approach.
- Policy Evaluation Order – How multiple ABAC policies are evaluated together.
- Using Columns in ABAC Policies – How to pass additional column values to masking or filtering functions.

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
- tutorial-configure-abac-with-sql-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
3. [tutorial-configure-abac-with-sql-databricks-on-aws.md](/references/tutorial-configure-abac-with-sql-databricks-on-aws-99ec3df0.md)
