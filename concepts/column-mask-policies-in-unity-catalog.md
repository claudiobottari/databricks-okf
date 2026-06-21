---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e902e9ca3128bc9a8e71237a289db7b3f8dfaa9a613aa3427c6f29767c725b1
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - tutorial-configure-abac-with-sql-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - column-mask-policies-in-unity-catalog
    - CMPIUC
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - file: tutorial-configure-abac-with-sql-databricks-on-aws.md
title: Column mask policies in Unity Catalog
description: ABAC policy type that supports column-level security on tables, materialized views, and streaming tables.
tags:
  - access-control
  - unity-catalog
  - column-level-security
  - policies
timestamp: "2026-06-19T14:06:21.240Z"
---

# Column Mask Policies in Unity Catalog

**Column Mask Policies** are a type of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy in Unity Catalog that dynamically obscure column values at query time based on governed tag conditions and a user-defined masking function. Unlike traditional table-level column masks that must be applied to each table individually, ABAC column mask policies can be defined once at a catalog or schema scope and automatically apply to all matching columns across many tables. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How Column Mask Policies Work

A column mask policy uses a user-defined function (UDF) registered in Unity Catalog to implement the masking logic. The policy specifies which columns to target, which principals to affect, and within which scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Core Components

- **Column condition (`MATCH COLUMNS`):** Identifies which columns to mask based on governed tag predicates. Use `has_tag()` or `has_tag_value()` to match columns with a specific tag or tag-value pair. You can include up to three column expressions; all must match for the policy to apply. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Masking function (`COLUMN MASK`):** References a UDF that receives the column value as its first argument (bound automatically) and returns either the original value or a masked version. The UDF's return type must be castable to the column's data type. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Scope (`ON` clause):** Where the policy is attached — a catalog, schema, or table. Attaching at a catalog applies the policy to all tables in that catalog; attaching at a schema applies to all tables in that schema; attaching at a table applies only to that table. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Principals (`TO` clause):** Lists the users, groups, or service principals subject to the policy. The optional `EXCEPT` clause exempts specific principals. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Table condition (`WHEN` clause, optional):** Filters which tables within the scope the policy applies to, based on tags on the table itself. If omitted, the policy applies to all tables in scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Additional arguments (`USING COLUMNS`):** Pass extra values to the UDF beyond the masked column. These can be constant values or references to other columns matched by tag expressions. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example SQL Statement

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

This policy scopes to the `hr_catalog` catalog, applies the `mask_ssn` UDF to columns tagged with `pii = ssn`, affects all users except the compliance team, and passes the constant `4` as an additional argument to the UDF. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Creating a Column Mask Policy

### Requirements

- Databricks Runtime 16.4 or above, or serverless compute. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `MANAGE` permission or ownership on the securable object (catalog, schema, or table) where the policy will be attached. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- `EXECUTE` privilege on the UDF that implements the masking logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- [Governed Tags](/concepts/governed-tags.md) applied to the target columns. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using SQL

Use the `CREATE POLICY` statement. The UDF can be an existing Unity Catalog function or a SQL function defined inline. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
-- Step 1: Create a masking UDF
CREATE FUNCTION redact_ssn(ssn STRING) RETURNS STRING
  RETURN '***-**-****';

-- Step 2: Create the column mask policy
CREATE POLICY redact_ssn_policy
ON SCHEMA abac_tutorial.customers
COLUMN MASK redact_ssn
TO `account users`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col;
```
^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

### Using Catalog Explorer UI

1. In your Databricks workspace, click **Catalog**.
2. Select the target catalog, schema, or table.
3. Click the **Policies** tab.
4. Click **New policy**.
5. Under **Policy type**, choose **Mask column data**.
6. Configure the general settings (name, description, principals, scope).
7. In **Conditions**, choose how to identify columns to mask (by tag or custom expression) and select the masking function.
8. Optionally test the masking function with sample input.
9. In **Function inputs**, provide values for additional UDF parameters (e.g., a constant or another column).
10. Click **Create policy**.
^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Using Python SDK

The SDK provides equivalent operations to create and manage policies programmatically. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Managing Policies

### Editing

You can modify the description, principals, policy type, column conditions, masking function, and function input mappings. The policy name and the securable object where the policy is applied cannot be edited. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- In the UI: Navigate to the Policies tab on the target object, select the policy, update fields, and click **Update policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- With SQL: Use `ALTER POLICY` (not detailed in sources but implied by management capabilities).

### Deleting

- In the UI: Select the policy and click **Delete policy**. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- With SQL: Use `DROP POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name`. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Showing Effective Policies

`SHOW EFFECTIVE POLICIES ON TABLE securable_name` lists all policies that apply to a table, including those inherited from parent scopes. Viewing effective policies does not require permissions on parent catalogs or schemas. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Describing a Policy

`DESCRIBE POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name` returns the policy's properties including name, scope, principals, conditions, function name, and timestamps. Requires `MANAGE` on the target securable object or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Examples

### Example 1: Basic SSN Masking

Mask all columns tagged `pii = ssn` with a static placeholder. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

```sql
-- UDF
CREATE FUNCTION mask_SSN(ssn STRING) RETURN '***-**-****';

-- Policy
CREATE POLICY mask_ssn
ON CATALOG abac
COLUMN MASK mask_SSN
TO `All account users`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col;
```

### Example 2: Conditional Email Masking

Show full email for users who have consented; otherwise show only the first character and domain. ^[tutorial-configure-abac-with-sql-databricks-on-aws.md]

```sql
-- UDF with two arguments
CREATE FUNCTION mask_email_by_consent(email STRING, consent BOOLEAN) RETURNS STRING
RETURN CASE
  WHEN consent = TRUE THEN email
  ELSE CONCAT(LEFT(email, 1), '***@', SUBSTRING_INDEX(email, '@', -1))
END;

-- Policy
CREATE POLICY mask_email_by_consent_policy
ON SCHEMA abac_tutorial.customers
COLUMN MASK mask_email_by_consent
TO `account users`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'email') AS email_col,
  has_tag('consent') AS consent_col
ON COLUMN email_col
USING COLUMNS (consent_col);
```

## Tag Inheritance and UDF Requirements

- Columns do **not** inherit tags from their parent table or ancestors. The `has_tag()` and `has_tag_value()` functions only evaluate tags directly applied to the column. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- Tags on parent objects (catalogs, schemas, tables) are inherited by child objects (except columns) and can be used in the `WHEN` clause of a policy. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **UDF requirements:** The return type must match or be castable to the target column's data type. SQL UDFs are recommended for better performance; Python UDFs are supported but cannot be inlined by the query optimizer. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- The first argument to the UDF is always the masked column value (bound automatically from the `ON COLUMN` clause). Additional arguments are supplied via `USING COLUMNS` and can be column aliases or constants. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## When to Use ABAC Column Mask Policies vs. Table-Level Column Masks

For guidance on choosing between ABAC policies and traditional table-level column masks, see [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md) – Restrict rows rather than columns.
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) – Dynamically grant privileges (currently for models).
- [Governed Tags](/concepts/governed-tags.md) – The attributes used in policy conditions.
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) – Alternative per-object approach.
- [Unity Catalog User-Defined Functions](/concepts/abac-user-defined-functions-udfs.md) – Required for masking logic.
- Policy Evaluation Order – How multiple ABAC policies are evaluated together.
- [Performance Considerations for Row Filter and Column Mask Policies](/concepts/row-filter-and-column-mask-policies.md) – Guidelines for maintaining query performance.

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
- tutorial-configure-abac-with-sql-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
3. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
4. [tutorial-configure-abac-with-sql-databricks-on-aws.md](/references/tutorial-configure-abac-with-sql-databricks-on-aws-99ec3df0.md)
