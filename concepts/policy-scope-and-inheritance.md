---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71a9200d0485b90932430b4b0e43cf600367b5537d033d6db10f14025bc7bd42
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-scope-and-inheritance
    - Inheritance and Policy Scope
    - PSAI
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Policy Scope and Inheritance
description: ABAC policies can be attached at the catalog, schema, or table level, and effective policies include inherited policies from parent scopes (e.g., catalog-level policies affecting a table).
tags:
  - data-governance
  - unity-catalog
  - abac
timestamp: "2026-06-19T09:34:47.189Z"
---

# Policy Scope and Inheritance

**Policy Scope and Inheritance** describes how [ABAC row filter and column mask policies](/concepts/row-filter-and-column-mask-policies.md) are attached to Unity Catalog objects and how those policies propagate to child objects. Understanding scope and inheritance is essential for designing a maintainable access-control strategy that minimises redundant policy definitions without unintended overrides.

## Scope

ABAC policies are attached to one of three securable levels: a **catalog**, a **schema**, or a **table**. The attachment point defines the scope of the policy:

- **Catalog** – A policy attached to a catalog applies to **all tables** in that catalog. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Schema** – A policy attached to a schema applies to **all tables** in that schema. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Table** – A policy attached to a table applies **only to that table**. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

Both row filter policies and column mask policies follow the same scoping rules. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Specifying Scope in SQL

When creating a policy with `CREATE POLICY`, the `ON { CATALOG | SCHEMA | TABLE }` clause determines the scope. For example: ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md, create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
-- Catalog-level column mask policy
CREATE POLICY mask_ssn_columns
ON CATALOG hr_catalog
COLUMN MASK mask_ssn
TO `account users` EXCEPT `compliance team`
FOR TABLES
MATCH COLUMNS has_tag_value('pii', 'ssn') AS ssn_col
ON COLUMN ssn_col
USING COLUMNS (4);
```

```sql
-- Schema-level row filter policy
CREATE POLICY hide_eu_customers
ON SCHEMA prod.customers
ROW FILTER is_eu_customer
TO `analysts`;
```

## Inheritance

Policies defined at a higher scope are **inherited** by all child objects within that scope. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md] For example, a catalog-level column mask policy automatically applies to every table in the catalog, even if those tables are created after the policy is defined. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md] This inheritance eliminates the need to attach the same policy to each table individually.

Multiple policies can apply to a single table when they are defined at different scopes. To see all policies that affect a given table – including those inherited from parent catalogs and schemas – use `SHOW EFFECTIVE POLICIES`: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SHOW EFFECTIVE POLICIES ON TABLE hr_catalog.employees.employee_data;
```

The result lists each policy along with its scope (the catalog, schema, or table where it was defined). No special permissions on parent objects are required to view effective policies for a table. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Evaluation Order

When multiple ABAC policies of the same type (e.g., two column mask policies) apply to the same table, the order of evaluation determines which policy takes effect. See Policy Evaluation Order for details.

## Tag Inheritance and Column Mask Policies

Columns **do not** inherit tags from their parent table, schema, or catalog. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md] Therefore, column mask policies that use `MATCH COLUMNS has_tag()` or `has_tag_value()` can only match columns that have governed tags directly applied to them. Tags on parent objects (catalogs, schemas, tables) **are** inherited by all child objects **except columns**; those inherited tags can be used in the `WHEN` clause to filter which tables a policy applies to, but not to match columns. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

## Best Practices

- **Prefer broader scopes** (catalog or schema) for policies that apply universally, such as masking all PII columns across the estate. This reduces maintenance and ensures consistent enforcement. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]
- **Use table-level scope** only for exceptional rules that deviate from the broader policy.
- **Review effective policies** regularly to avoid unintended combinations of inherited and locally attached policies.
- **Apply governed tags consistently** at the column level when using column mask policies, since tags are not inherited for columns.

## Related Concepts

- [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md)
- [ABAC Row Filter Policies](/concepts/abac-row-filter-policies.md)
- [Governed Tags](/concepts/governed-tags.md)
- Policy Evaluation Order
- [Create and Manage Row Filter and Column Mask Policies](/concepts/row-filter-and-column-mask-policies.md)

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
2. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
