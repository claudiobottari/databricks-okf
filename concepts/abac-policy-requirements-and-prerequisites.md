---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6740953656ffbe62c965671cf31987e0832a724c1839ba41f7fec92de816253a
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-requirements-and-prerequisites
    - Prerequisites and ABAC Policy Requirements
    - APRAP
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC Policy Requirements and Prerequisites
description: Requirements for creating ABAC policies including MANAGE privilege or ownership on the securable object, Databricks Runtime 16.4+ or serverless compute, EXECUTE on a UDF, and governed tags applied to target objects.
tags:
  - data-governance
  - unity-catalog
  - abac
  - requirements
timestamp: "2026-06-18T11:20:30.031Z"
---

# ABAC Policy Requirements and Prerequisites

**ABAC Policy Requirements and Prerequisites** outlines the necessary permissions, compute environments, and supporting configurations required to create, edit, and manage [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in [Unity Catalog](/concepts/unity-catalog.md).

## Permission Requirements

### Manage Privilege Requirement

All policy operations — including creating, editing, deleting, showing, and describing policies — require the `MANAGE` privilege on the securable object (catalog, schema, or table) where the policy is attached, or ownership of the securable object.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Additional Requirements for Creating Policies

Creating an ABAC policy also requires:^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- Execute privilege on the user-defined function (UDF) that implements the filtering or masking logic, or a SQL function defined inline when creating the policy.
- [Governed Tags](/concepts/governed-tags.md) applied to target objects that the policy conditions reference.
- An appropriate compute environment (see [#Compute Requirements](/concepts/abac-compute-requirements.md) below).

For [ABAC GRANT Policy](/concepts/abac-grant-policy.md) (Beta), you must have `MANAGE` on the catalog or schema where the policy is attached, or own that securable object. GRANT policies do not use UDFs — the condition is expressed inline in the policy definition.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Compute Requirements

### Row Filter and Column Mask Policies

Creating, modifying, or dropping row filter and column mask policies requires:^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- Databricks Runtime 16.4 or above, or serverless compute.

### ABAC GRANT Policies

Creating, modifying, or dropping GRANT policies with SQL requires a classic compute cluster running Databricks Runtime 18.3 or above.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## UDF Requirements

For row filter and column mask policies, the UDF that implements the filtering or masking logic must:^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- Be registered in Unity Catalog.
- Be accessible via `EXECUTE` privilege to the policy creator.
- For row filters, return a boolean value — rows where the function returns `FALSE` are excluded from query results.
- For column masks, the return type must be castable to the target column's data type.

## Tagging Requirements

### Governed Tags

ABAC policies require [Governed Tags](/concepts/governed-tags.md) applied to the securable objects (catalogs, schemas, or tables) that the policy conditions evaluate against. Tags must be properly configured and applied before policies can function correctly.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

For GRANT policies, conditions can reference either governed tags created by the organization or [System Tags](/concepts/system-tags.md) predefined by Databricks.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Tag Naming and Taxonomy

Tags used in ABAC policies should follow a consistent taxonomy. Best practices include:^[best-practices-for-abac-policies-databricks-on-aws.md]

- Use a single `sensitivity` tag with controlled values such as `public`, `internal`, `confidential`, and `restricted`.
- Avoid multiple overlapping tags like `is_sensitive`, `data_class`, and `pii_level`.
- Restrict tag creation and modification to authorized data stewards or governance admins.

## Viewing and Describing Policies

### Show Policies

Use `SHOW POLICIES` to list policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to include policies inherited from parent scopes (e.g., catalog-level policies that affect a schema or table).^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA | TABLE } securable_name
```

Viewing effective policies for a table does not require permissions on the parent catalog or schema. This allows a table admin to see the rules that apply without having read access to sibling tables' policies.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Describe Policy

Use `DESCRIBE POLICY` to view the details of a specific policy. Requires `MANAGE` on the target securable object or object ownership.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA | TABLE } securable_name
```

The result shows the policy's properties as key-value pairs, including name, securable object type, securable object name, principals, conditions, function name, and timestamps.^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Audit Logging

Databricks logs governed tag and ABAC policy operations in the audit log system table. Key actions logged include:^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- `createEntityTagAssignment` and `deleteEntityTagAssignment` for tag operations.
- `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` for policy CRUD operations.

GRANT policy operations are logged under the same `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` actions as row filter and column mask policies.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Prerequisites by Policy Type

| Requirement | Row Filter / Column Mask | GRANT Policy (Beta) |
|---|---|---|
| Manage privilege | Yes | Yes |
| Runtime | Databricks Runtime 16.4+ or serverless | Databricks Runtime 18.3+ (classic compute) |
| UDF with Execute | Yes (for filtering/masking logic) | No (condition inline) |
| Governed Tags | Yes | Yes (or system tags) |
| Supported Securables | Catalogs, schemas, tables | Catalogs, schemas (models only) |

## Related Concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Dynamic privilege grants based on tag conditions
- [Governed Tags](/concepts/governed-tags.md) — Tags used in ABAC policy conditions
- [System Tags](/concepts/system-tags.md) — Predefined tags provided by Databricks
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data rows
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- [Unity Catalog UDFs](/concepts/unity-catalog.md) — User-defined functions for policy logic
- ABAC Performance Considerations — Performance implications of ABAC policy design
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) — Best practices for policy design

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
3. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
