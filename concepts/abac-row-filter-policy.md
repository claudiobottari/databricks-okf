---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a4bea58a626c0862d4693f8ebb90e686350fcd0aa9c127fe7d4cf43a85b4179
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-row-filter-policy
    - ARFP
    - Row Filter Policy
    - Row filter policy
    - row filter policy
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Row Filter Policy
description: A Unity Catalog ABAC policy that filters rows from query results using a boolean user-defined function (UDF), excluding rows where the function returns FALSE.
tags:
  - data-governance
  - unity-catalog
  - abac
  - security
timestamp: "2026-06-18T14:52:43.270Z"
---

# ABAC Row Filter Policy

**ABAC Row Filter Policy** is a type of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy in Unity Catalog that dynamically restricts which rows are visible to users at query time based on [Governed Tags](/concepts/governed-tags.md) applied to tables and their properties. Unlike table-level row filters that must be configured per table, ABAC row filter policies are defined once at a catalog or schema scope and automatically apply to all matching tables within that scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## How Row Filter Policies Work

A row filter policy uses a user-defined function (UDF) in Unity Catalog that returns a boolean value for each row. Rows where the function returns `TRUE` are included in query results; rows where it returns `FALSE` are excluded. The policy defines:

- **Scope**: The catalog, schema, or table where the policy is attached (using the `ON` clause). Attaching at a catalog applies the policy to all tables in that catalog; attaching at a schema applies to all tables in that schema; attaching at a table applies only to that table. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Principals**: The `TO` clause lists the users, groups, or service principals subject to the policy. The optional `EXCEPT` clause exempts specific principals. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Filtering logic**: A UDF that evaluates row attributes and returns a boolean. The UDF receives column values or constant arguments as inputs. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Table condition**: The optional `WHEN` clause filters which tables within the scope the policy applies to, based on tags on the table itself. If omitted, the policy applies to all tables in scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example

The following example creates a row filter that hides customer records from the EU region for non-admin users: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE FUNCTION filter_eu_customers(region STRING) RETURNS BOOLEAN
  RETURN region != 'EU';

CREATE POLICY hide_eu_customers
ON SCHEMA prod.customers
ROW FILTER filter_eu_customers
TO `all users` EXCEPT `admin`
FOR TABLES
WHEN has_tag_value('data_classification', 'pii');
```

In this example:
- The policy is scoped to the `prod.customers` schema.
- All users except the `admin` group are subject to the filter.
- The policy applies only to tables within the schema that are tagged with `data_classification : pii` (the `WHEN` clause).
- The UDF `filter_eu_customers` receives the `region` column value and returns `FALSE` for rows where the region is `'EU'`, effectively hiding EU customer data.

## UDF Requirements for Row Filters

- The UDF must return a boolean value (`TRUE` or `FALSE`). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- SQL UDFs are recommended for better performance; Python UDFs are supported but cannot be inlined by the query optimizer. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- The UDF's input parameters correspond to columns in the target table or constant expressions supplied in the policy definition. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Creating a Policy

You can create a row filter policy using the Catalog Explorer UI, the CREATE POLICY SQL statement, or the Databricks REST APIs, SDKs, and Terraform. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Requirements

- Databricks Runtime 16.4 or above, or serverless compute. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `MANAGE` permission or ownership on the securable object (catalog, schema, or table) where the policy is attached. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `EXECUTE` privilege on the UDF referenced by the policy. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- Governed tags applied to target objects. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Creating in Catalog Explorer

1. Navigate to the catalog, schema, or table that will be the policy scope.
2. Click the **Policies** tab.
3. Click **New policy**.
4. Complete the **Policy identification** section (name, description).
5. In the **Principals and scope** section, specify the users/groups subject to the policy and any exemptions.
6. For **Policy type**, select **Row filter**.
7. In the **Row filter function** section, either select an existing UDF or define a new SQL function inline.
8. In the **Function inputs** section, provide values for each UDF parameter — these can be column names, matched tags, or constant values.
9. Click **Create policy**.

## Editing and Deleting Policies

Policies can be edited or deleted through Catalog Explorer, SQL, or the Python SDK. When editing, you can modify the description, principals, policy type, conditions, and function input mappings. The policy name and the securable object where the policy is applied cannot be changed after creation. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Viewing Policies

Use `SHOW POLICIES` to list policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies from parent scopes, such as catalog-level policies that affect a table. Use `DESCRIBE POLICY` to view the details of a specific policy. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Tag Inheritance

Tables inherit tags from their parent [Catalog and Schema](/concepts/catalog-and-schema.md). The `has_tag()` and `has_tag_value()` functions in the `WHEN` clause evaluate tags on the table, including inherited tags. This allows policies to be applied automatically to new tables that inherit the right tags. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Permissions Model

Users querying filtered tables must have `SELECT` (or appropriate) privileges on the table. The policy does **not** grant access; it only controls which rows are visible to users who already have access. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits

- **Automatic enforcement**: When new tables are created with the appropriate tags, existing row filter policies apply automatically without manual configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Consistent rules**: Ensures uniform filtering for similar data types across the data estate. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Lower maintenance**: Updates to filtering logic can be done by modifying the UDF or the policy, rather than editing each table's row filter individually. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## When to Use ABAC Row Filter Policies vs. Table-Level Row Filters

The source material directs readers to [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md) for a comparison. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) – Restrict or transform column values rather than rows.
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) – Dynamically grant privileges (currently for models).
- [Governed Tags](/concepts/governed-tags.md) – The attributes used in policy conditions.
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) – Alternative per-object approach.
- Policy Evaluation Order – How multiple ABAC policies are evaluated together.
- CREATE POLICY – SQL statement for creating policies.
- SHOW POLICIES – SQL statement for listing policies.
- DESCRIBE POLICY – SQL statement for viewing policy details.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
