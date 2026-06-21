---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7400fc37866a696388a52fd2629354f3d2579ece081fd797d0728c513e6c3c7
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filter-policies-and-column-mask-policies
    - column mask policies and Row filter policies
    - RFPACMP
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: Row filter policies and column mask policies
description: ABAC policy types providing row-level and column-level security on tables, materialized views, and streaming tables in Unity Catalog.
tags:
  - access-control
  - data-security
  - unity-catalog
timestamp: "2026-06-19T09:04:14.969Z"
---

# Row Filter Policies and Column Mask Policies

**Row filter policies** and **column mask policies** are two types of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in Unity Catalog that provide dynamic, tag-driven data security at the row and column level respectively. Unlike traditional table-level row filters and column masks that must be applied per table, ABAC policies can be defined once at a catalog or schema scope and automatically apply to all matching tables based on governed tag conditions. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Overview

Both policy types use [Governed Tags](/concepts/governed-tags.md) as attributes to identify which data a policy should protect. Policies are attached at a level in the Unity Catalog hierarchy (catalog, schema, or table) and are evaluated dynamically at query time. When a securable object has the attributes targeted by a policy, that policy takes effect automatically, enabling a single policy to enforce consistent access rules across an entire catalog or schema. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

ABAC row filter and column mask policies apply to tables, materialized views, and streaming tables. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Row Filter Policies

**ABAC Row Filter Policies** restrict which rows users can see in query results by applying a filter condition based on tag-based conditions. The policy specifies:

- **Scope**: The catalog, schema, or table where the policy is attached (using the `ON` clause). Attaching at a catalog applies the policy to all tables in that catalog; attaching at a schema applies to all tables in that schema; attaching at a table applies only to that table. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Principals**: The `TO` clause lists the users, groups, or service principals subject to the policy. The optional `EXCEPT` clause exempts specific principals. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Row condition**: The `WHERE` clause defines the filter logic, which can reference tag functions (e.g., `has_tag()`, `has_tag_value()`) to dynamically determine which rows to include. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Table condition**: The optional `WHEN` clause filters which tables within the scope the policy applies to, based on tags on the table itself. If omitted, the policy applies to all tables in scope. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### Example

The following example restricts access to rows tagged with a specific sensitivity level, except for members of the compliance team: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

```sql
CREATE POLICY restrict_sensitive_rows
ON CATALOG hr_catalog
TO `account users` EXCEPT `compliance team`
FOR TABLES
WHEN has_tag_value('sensitivity', 'confidential')
WHERE has_tag_value('department', user());
```

In this example:
- The policy is scoped to the `hr_catalog` catalog.
- All users except the `compliance team` are subject to the filter.
- The policy only applies to tables tagged with `sensitivity : confidential` (the `WHEN` clause).
- Users only see rows where the `department` tag matches their username (the `WHERE` clause).

## Column Mask Policies

**ABAC Column Mask Policies** dynamically mask column values for users based on governed tag conditions. Unlike table-level column masks that must be applied per table, ABAC column mask policies evaluate at query time against the tags on the target column and can be defined once at a catalog or schema scope to cover many tables automatically. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### How They Work

A column mask policy uses a user-defined function (UDF) in Unity Catalog to implement the masking logic. The policy specifies:

- **Scope**: The catalog, schema, or table where the policy is attached (using the `ON` clause). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Principals**: The `TO` clause lists the users, groups, or service principals subject to the policy. The optional `EXCEPT` clause exempts specific principals. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Column condition**: The `MATCH COLUMNS` clause uses built-in tag functions (e.g., `has_tag()`, `has_tag_value()`) to identify which columns the policy should mask. A policy can include up to three column expressions. All must match for the policy to apply. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
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
- The policy targets any column tagged with `pii : ssn` (the `MATCH COLUMNS` condition).
- The UDF `mask_ssn` receives the column value and the constant `4`, returning the masked string.
- The `USING COLUMNS` clause passes the additional argument (how many digits to show) to the UDF.

### UDF Requirements

- The UDF's return type must match or be castable to the column's data type. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- SQL UDFs are recommended for better performance; Python UDFs are supported but cannot be inlined by the query optimizer. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- The first argument to the UDF is always the masked column value (bound automatically from the `ON COLUMN` clause). Additional arguments are supplied via `USING COLUMNS` and can be aliases for other columns matching tag expressions, or constant values. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Tag Inheritance

Columns do **not** inherit tags from their parent table or ancestors. The `has_tag()` and `has_tag_value()` functions in `MATCH COLUMNS` only evaluate tags directly applied to the column, not inherited tags. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

However, tags on parent objects (catalogs, schemas, tables) are inherited by child objects (except columns) and can be used in the `WHEN` clause to filter which tables the policy applies to. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Permissions

To create a row filter or column mask policy, a user needs:

- `MANAGE` permission or ownership on the securable object (catalog, schema, or table) where the policy is attached.
- For column mask policies: `EXECUTE` privilege on the UDF referenced by the policy. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Users querying data protected by these policies must have `SELECT` (or appropriate) privileges on the table. The policy does **not** grant access; it only controls how the data appears to users who already have access. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Benefits

- **Reusable**: One policy can protect the same type of data (e.g., all columns tagged `PII` or all rows tagged `confidential`) across many tables without per-table configuration. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Automatic**: When new tables are created and tagged, existing policies apply automatically. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Consistent**: Ensures uniform security rules for similar data across the estate. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Lower maintenance**: Updates to masking or filtering logic can be done by modifying the UDF or the policy, rather than editing each table individually. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## When to Use ABAC Policies vs. Table-Level Row Filters and Column Masks

For guidance on choosing between ABAC policies and traditional table-level row filters and column masks, see [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) – Dynamically grant privileges (currently for models).
- [Governed Tags](/concepts/governed-tags.md) – The attributes used in policy conditions.
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md) – Alternative per-object approach.
- Policy Evaluation Order – How multiple ABAC policies are evaluated together.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The overarching access control model.

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
2. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
