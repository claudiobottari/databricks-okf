---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fb408bd02efa7f04189383b14c9756b7f8691aa6df25784e64bcd5c2bef3bee
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - effective-policy-visibility-via-show-effective-policies
    - EPVVSEP
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: Effective Policy Visibility via SHOW EFFECTIVE POLICIES
description: The ability to view all policies affecting a securable object including inherited policies from parent scopes (catalog → schema → table) without requiring permissions on parent objects.
tags:
  - data-governance
  - unity-catalog
  - abac
  - visibility
timestamp: "2026-06-19T14:34:43.496Z"
---

# Effective Policy Visibility via SHOW EFFECTIVE POLICIES

The `SHOW EFFECTIVE POLICIES` command provides visibility into all active [ABAC policy|ABAC policies](/concepts/abac-policy-types.md) that apply to a given securable object, including policies inherited from parent scopes. This is essential for understanding the complete access control landscape without requiring permissions on every parent object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Overview

`SHOW EFFECTIVE POLICIES` is a SQL command for [Unity Catalog](/concepts/unity-catalog.md) that lists the row filter and column mask policies defined on a catalog, schema, or table. Unlike `SHOW POLICIES`, which only shows policies directly attached to the specified object, `SHOW EFFECTIVE POLICIES` also includes policies from parent scopes — such as catalog-level policies that affect a table within that catalog. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Syntax

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name
```

The `EFFECTIVE` keyword is optional; including it expands the result set to include inherited policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Result

The command returns policy name, policy type, and the catalog, schema, or table where each policy is defined. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Permissions Model

A key benefit of `SHOW EFFECTIVE POLICIES` is that viewing effective policies for a table does not require permissions on the parent catalog or schema. This enables a table admin to see all rules that apply to their table without needing read access to sibling tables' policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Example

```sql
SHOW EFFECTIVE POLICIES ON SCHEMA prod.customers;
```

This returns all policies defined on the `prod.customers` schema, including any policies inherited from the `prod` catalog. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Use Cases

- **Compliance auditing**: Quickly identify all policies that affect a specific table or schema.
- **Troubleshooting**: Understand why certain rows are filtered or columns are masked.
- **Policy management**: Verify that inherited policies are applied as intended before making changes.

## Related Commands

- `SHOW POLICIES` — Lists only policies directly attached to the specified object.
- `DESCRIBE POLICY` — Shows detailed properties of a specific policy.
- `CREATE POLICY` — Creates new ABAC policies.

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) — Policies that exclude rows from query results.
- [Column Mask Policies](/concepts/column-mask-policies.md) — Policies that modify column values.
- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) — The access control model underlying these policies.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance system where policies are defined.

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
