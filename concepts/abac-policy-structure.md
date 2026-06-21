---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a807b012a5a3b18982a8642b5d9b748b53f83098dea8d585d80410b20dfb409
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-structure
    - APS
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: ABAC Policy Structure
description: Every ABAC policy specifies a scope (catalog/schema/table), principals (TO/EXCEPT clauses), actions (row filter, column mask, or grant), and tag-based conditions (WHEN and MATCH COLUMNS clauses).
tags:
  - abac
  - policies
  - syntax
timestamp: "2026-06-19T17:53:49.086Z"
---

# ABAC Policy Structure

**ABAC Policy Structure** defines the formal syntax and components used to create attribute-based access control (ABAC) policies in Unity Catalog. ABAC policies are dynamic access control rules that reference [Governed Tags](/concepts/governed-tags.md) to grant or restrict access based on object attributes rather than per-object grants. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Policy Anatomy

An ABAC policy consists of several required and optional clauses that together specify the scope, principals, actions, and conditions for access control. The following example illustrates the complete structure: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE POLICY mask_pii_for_hr
ON CATALOG catalog_a
COLUMN MASK mask_pii
TO `account users` EXCEPT `HR admins`
FOR TABLES
WHEN has_tag('HR')
MATCH COLUMNS has_tag('PII') AS pii_col
ON COLUMN pii_col;
```

### Scope (`ON` clause)

The `ON` clause specifies the securable object where the policy is attached. This determines the scope over which the policy conditions are evaluated. Supported scopes are: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **`CATALOG`** — The policy evaluates against all objects of the specified type across the entire catalog.
- **`SCHEMA`** — The policy evaluates against all objects of the specified type within that schema.
- **`TABLE`** — The policy evaluates only against that specific table.

Databricks recommends attaching policies at the highest applicable level, typically the catalog, to maximize governance efficiency. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Object Type (`FOR` clause)

The `FOR` clause specifies the type of securable object the policy targets: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **`FOR TABLES`** — Used for row filter and column mask policies. Tables, including streaming tables and materialized views, are the only supported securable object type for these policies.
- **`GRANT EXECUTE FOR MODELS`** — Used for GRANT policies (Beta), which support models only.

### Principals (`TO` and `EXCEPT` clauses)

The `TO` clause specifies which users, groups, or service principals are subject to the policy. The optional `EXCEPT` clause excludes specific principals from the policy's effects. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Actions

The action clause determines what the policy does when its conditions match. ABAC supports three action types: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

- **`ROW FILTER`** — Restricts which rows a user can see by referencing a user-defined function (UDF) that evaluates each row.
- **`COLUMN MASK`** — Controls what values a user sees for specific columns by referencing a UDF that transforms column values.
- **`GRANT`** (Beta) — Dynamically grants a Unity Catalog privilege without using a UDF.

## Conditions and Built-in Functions

### Table Conditions (`WHEN` clause)

Boolean expressions that match tables based on their tags. If omitted, defaults to `TRUE`, meaning the policy applies to all tables in scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Column Conditions (`MATCH COLUMNS` clause)

One or more comma-separated boolean expressions that identify which columns the policy targets. Each expression can be a single built-in function or a combination using logical operators. Each expression can be assigned an alias (specified after `AS`) that can be referenced in `ON COLUMN` and `USING COLUMNS` clauses. A policy can include up to 3 column expressions, and all must match for the policy to apply. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Built-in Tag Functions

Conditions use the following built-in functions, evaluated by Unity Catalog against securable metadata: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

| Function | Purpose |
|----------|---------|
| `has_tag('key')` | Checks whether a given governed tag key is present on the target object. |
| `has_tag_value('key', 'value')` | Checks whether a governed tag with the specified key-value pair exists. |

Both functions use snake_case naming. The older camelCase forms (`hasTag`, `hasTagValue`) continue to work but are not recommended for new policies. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Policy Types in Detail

### Row Filter Policies

Row filter policies use a UDF in the `ROW FILTER` clause to evaluate each row. Arguments are passed to the UDF through the `USING COLUMNS` clause. Rows where the function returns `FALSE` are excluded from query results. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE POLICY regional_access_emea
ON CATALOG sales
ROW FILTER filter_by_region
TO `emea team`
FOR TABLES
MATCH COLUMNS has_tag('region') AS rgn
USING COLUMNS (rgn, 'EMEA');
```

### Column Mask Policies

Column mask policies use a UDF in the `COLUMN MASK` clause to transform column values. The masked column value is bound automatically as the first argument from the `ON COLUMN` clause. Additional arguments can be passed through `USING COLUMNS`. The return type must match or be castable to the column's data type. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

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

### GRANT Policies (Beta)

GRANT policies dynamically grant a Unity Catalog privilege when their tag-based condition matches a securable object's tags. They use the same evaluation model as row filter and column mask policies but do not use UDFs. The condition is expressed inline in the policy definition. The effective privileges on an object are the union of direct grants and any applicable GRANT policies. GRANT policies only add access — they cannot revoke access that was granted directly. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## User-Defined Functions (UDFs)

Row filter and column mask policies require UDFs registered in Unity Catalog to implement filtering or masking logic. SQL UDFs are recommended for better performance. Python UDFs are also supported, though the query optimizer cannot inline or optimize them as effectively. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

The `USING COLUMNS` clause passes arguments to the UDF. It accepts aliases for columns that match a tag-based expression, or constant values (quoted strings, numeric literals, boolean values, or `NULL`), supplied in the order the function expects them. For column mask policies, these are additional arguments beyond the masked column, which is bound automatically from `ON COLUMN`. This allows a single UDF to be reused across policies with different parameters. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Policy Creation and Management

Policies are created and managed through the UI or programmatically with SQL statements (`CREATE POLICY`, `DROP POLICY`, `SHOW POLICIES`, `DESCRIBE POLICY`), REST APIs, Databricks SDKs, or Terraform. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The attribute system that ABAC policies reference
- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that restrict row-level access
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that control column-level visibility
- [GRANT Policies](/concepts/grant-policies-beta.md) — Dynamic privilege grant policies (Beta)
- [ABAC Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) — How Unity Catalog evaluates policies at query time
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — Objects that can have policies attached
- [ABAC vs Table-Level Row Filters and Column Masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md) — Comparison of ABAC with direct object-level controls

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
