---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3770f616164c8deb05eb7040644f641b52c4aa9c9392a5f37ce4bdc22a6f051b
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - show-effective-policies
    - SEP
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: SHOW EFFECTIVE POLICIES
description: A SQL command that lists all policies affecting a securable object, including inherited policies from parent scopes like catalog-level policies affecting a table.
tags:
  - sql
  - unity-catalog
  - auditing
  - abac
timestamp: "2026-06-19T17:59:29.108Z"
---

---
title: SHOW EFFECTIVE POLICIES
summary: A SQL command that lists all ABAC policies effective on a securable object, including inherited policies from parent scopes (e.g., catalog-level policies affecting a table), without requiring permissions on parent objects.
sources:
  - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:52:17.842Z"
updatedAt: "2026-06-18T14:52:17.842Z"
tags:
  - data-governance
  - unity-catalog
  - abac
  - sql
aliases:
  - show-effective-policies
  - SEP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# SHOW EFFECTIVE POLICIES

**SHOW EFFECTIVE POLICIES** is a SQL command in Unity Catalog that displays all [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies — including row filters, column masks, and GRANT policies — that apply to a given securable object. Unlike `SHOW POLICIES`, which only lists policies defined directly on that object, `SHOW EFFECTIVE POLICIES` also includes policies inherited from parent scopes such as catalogs and schemas. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Syntax

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name
```

The `EFFECTIVE` keyword is optional. When omitted, the command behaves identically to plain `SHOW POLICIES` (listing only direct policies). When included, it additionally resolves policies defined on ancestor catalogs or schemas that might affect the named child object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Result

The command returns the following columns for each policy:

- **policy_name** – Name of the policy as defined in Unity Catalog.
- **policy_type** – One of `ROW_FILTER`, `COLUMN_MASK`, or `GRANT`.
- **securable_object** – The catalog, schema, or table where the policy is defined (its attachment point).

Policies inherited from parent scopes appear as separate rows with the same policy name but a different `securable_object` column value. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Example

To see all policies — both direct and inherited — that apply to the `prod.customers` schema:

```sql
SHOW EFFECTIVE POLICIES ON SCHEMA prod.customers;
```

To see the same for a table:

```sql
SHOW EFFECTIVE POLICIES ON TABLE hr_catalog.employees.employee_data;
```

## Permissions

Viewing effective policies for a table does not require `MANAGE` or `SELECT` permissions on the parent catalog or schema. A table admin can see the rules that apply to their table without having read access to sibling tables' policies. The only privilege required is `MANAGE` on the securable object itself, or object ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Use Cases

- **Audit compliance**: Quickly determine which row filter and column mask policies are active for a given dataset.
- **Troubleshooting**: Identify why a user sees unexpected results by listing inherited policies that might be applying additional restrictions.
- **Policy management**: Understand the full policy surface before editing or deleting a policy to avoid breaking inherited protections.

## Related Commands

- `SHOW POLICIES` – Lists only policies defined directly on the named object (no inheritance).
- `DESCRIBE POLICY` – Shows the full details of a single policy (name, principals, conditions, function name, timestamps).
- `CREATE POLICY` – Creates a new ABAC row filter or column mask policy.
- `DROP POLICY` – Removes a policy (requires `MANAGE` on the securable object).

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md)
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md)
- Policy Evaluation Order
- [Row Filters and Column Masks (table-level)](/concepts/row-filters-and-column-masks.md)

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
