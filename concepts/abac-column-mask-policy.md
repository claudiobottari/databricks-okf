---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb56941b316b9f133cec5a938c316b79b83b95fb2c1804b79979132c81b34931
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-column-mask-policy
    - ACMP
    - Column Mask Policy
    - Column mask policy
    - column mask policy
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Column Mask Policy
description: A Unity Catalog ABAC policy that masks column values by applying a masking function to columns matched by governed tags or custom expressions.
tags:
  - data-governance
  - unity-catalog
  - abac
  - security
timestamp: "2026-06-18T14:52:15.119Z"
---

# ABAC Column Mask Policy

An **ABAC Column Mask Policy** is a type of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy in Unity Catalog that dynamically masks column values for users based on governed tag conditions. Unlike table-level column masks that must be applied per table, ABAC column mask policies evaluate at query time against the tags on the target column and can be defined once at a catalog or schema scope to cover many tables automatically. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## How It Works

A column mask policy uses a user-defined function (UDF) in Unity Catalog to implement the masking logic. The policy specifies: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **Scope**: The `ON` clause defines the catalog, schema, or table where the policy is attached. Attaching at a catalog applies the policy to all tables in that catalog; attaching at a schema applies to all tables in that schema; attaching at a table applies only to that table. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Principals**: The `TO` clause lists the users, groups, or service principals subject to the policy. The optional `EXCEPT` clause exempts specific principals. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Column condition**: The `MATCH COLUMNS` clause uses built-in tag functions (e.g., `has_tag()`, `has_tag_value()`) to identify which columns the policy should mask. A policy can include up to three column expressions; all must match for the policy to apply. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Masking logic**: The `COLUMN MASK` clause references a UDF that receives the column value as its first argument (bound automatically from the `ON COLUMN` clause) and returns the original value or a masked version. Additional arguments can be passed via `USING COLUMNS`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Table condition**: The optional `WHEN` clause filters which tables within the scope the policy applies to, based on tags on the table itself. If omitted, the policy applies to all tables in scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example

The following example masks SSN columns (tagged with `pii : ssn`) so that non-exempt users see only the last four digits: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
  RETURN CONCAT('***-**-', RIGHT(ssn, show_last));

CREATE POLICY mask_ssn_columns
ON CATALOG hr_catalog
COLUMN MASK mask_ssn
TO `account users` EXCEPT `compliance team`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4);
```

In this example:
- The policy is scoped to the `hr_catalog` catalog.
- All users except the `compliance team` are subject to the mask.
- The policy targets any column tagged with `pii : ssn`.
- The UDF `mask_ssn` receives the column value and the constant `4`, returning the masked string.
- The `USING COLUMNS` clause passes the additional argument (how many digits to show) to the UDF.

## UDF Requirements

- The UDF’s return type must match or be castable to the column’s data type. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- SQL UDFs are recommended for better performance; Python UDFs are supported but cannot be inlined by the query optimizer. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- The first argument to the UDF is always the masked column value (bound automatically from the `ON COLUMN` clause). Additional arguments are supplied via `USING COLUMNS` and can be aliases for other columns matching tag expressions, or constant values. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Tag Inheritance

Columns do **not** inherit tags from their parent table or ancestors. The `has_tag()` and `has_tag_value()` functions in `MATCH COLUMNS` only evaluate tags directly applied to the column, not inherited tags. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

However, tags on parent objects (catalogs, schemas, tables) are inherited by child objects (except columns) and can be used in the `WHEN` clause to filter which tables the policy applies to. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Permissions

To create a column mask policy, a user needs:

- `MANAGE` permission or ownership on the securable object (catalog, schema, or table) where the policy is attached.
- `EXECUTE` privilege on the UDF referenced by the policy. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Users querying masked data must have `SELECT` (or appropriate) privileges on the table. The policy does **not** grant access; it only controls how the data appears to users who already have access. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits

- **Reusable**: One policy can mask the same type of column (e.g., all columns tagged `PII`) across many tables without per-table configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Automatic**: When new tables are created and tagged, existing column mask policies apply automatically. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Consistent**: Ensures uniform masking rules for similar data across the estate. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Lower maintenance**: Updates to masking logic can be done by modifying the UDF or the policy, rather than editing each table’s column mask individually. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## When to Use ABAC Column Mask Policies vs. Table-Level Column Masks

The source material directs readers to [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md) for a comparison. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Creating and Managing Policies

Policies can be created, edited, deleted, and described using the Catalog Explorer UI, SQL statements, the Databricks REST APIs, SDKs, and Terraform. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Requirements

- Databricks Runtime 16.4 or above, or serverless compute.
- A UDF in Unity Catalog on which you have `EXECUTE` (or an inline SQL function).
- [Governed Tags](/concepts/governed-tags.md) applied to target objects. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Creating a Policy (SQL Example)

```sql
CREATE POLICY mask_ssn_columns
ON CATALOG hr_catalog
COLUMN MASK mask_ssn
TO `account users` EXCEPT `compliance team`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4);
```

For UI steps, see [Create and manage row filter and column mask policies](/concepts/row-filter-and-column-mask-policies.md).

### Viewing Effective Policies

Use `SHOW EFFECTIVE POLICIES ON { CATALOG | SCHEMA | TABLE }` to see policies from parent scopes that affect a given object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

Governed tag and ABAC policy operations (create, delete, etc.) are logged in the audit log system table. Example queries are provided in the Databricks documentation. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) – Restrict rows rather than columns.
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) – Dynamically grant privileges (currently for models).
- [Governed Tags](/concepts/governed-tags.md) – The attributes used in policy conditions.
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) – Alternative per-object approach.
- Policy Evaluation Order – How multiple ABAC policies are evaluated together.
- [Create and manage row filter and column mask policies](/concepts/row-filter-and-column-mask-policies.md) – Detailed how-to guide.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
