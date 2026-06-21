---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62b05ec62d7b557507ff70b30ae5ebbc87cbe96150df6d4242203f3252a44cdd
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-management-operations
    - GPMO
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Management Operations
description: SQL and UI operations for creating, editing, deleting, showing, and describing GRANT policies, including the USE CATALOG/SCHEMA prerequisites and SHOW EFFECTIVE POLICIES for inherited policies.
tags:
  - administration
  - unity-catalog
  - sql
  - databricks
timestamp: "2026-06-19T08:49:06.821Z"
---

# GRANT Policy Management Operations

**GRANT Policy Management Operations** refers to the set of actions used to create, edit, delete, describe, and list attribute-based access control (ABAC) GRANT policies in Unity Catalog. These operations dynamically grant Unity Catalog privileges (currently `EXECUTE` on models) to securable objects whose governed tags match a policy's condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Overview

GRANT policies are a type of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy that differs from [Row Filter and Column Mask Policies](/concepts/row-filter-policies.md). While row filters and column masks restrict the content of data a user can already access, GRANT policies determine whether the user can access the object at all. Additionally, GRANT policies do not require a user-defined function (UDF) — the condition is expressed inline in the policy definition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Creating a GRANT Policy

You can create a GRANT policy through the [Catalog Explorer](/concepts/catalog-explorer.md) UI, with the `CREATE POLICY` SQL statement, or with the Databricks SDK. To create a GRANT policy, you must have `MANAGE` permission on the catalog or schema where the policy is attached, or own that securable object. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Using SQL

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The `TO` clause lists the principals (users, groups, or service principals) subject to the policy, with an optional `EXCEPT` clause to exclude specific principals. The `WHEN` clause uses built-in tag functions like `has_tag()` and `has_tag_value()` to determine which models the policy applies to. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the catalog or schema where you want to attach the policy.
3. Click the **Policies** tab.
4. Click **New policy**.
5. Under **Policy identification**, enter a **Policy name** and optional **Description**.
6. Under **Principals and scope**, select the principals and optionally exclude some.
7. Under **Policy type**, select **Grant access**.
8. Under **Securable objects**, select **Model**.
9. Under **Condition**, choose how to scope the policy — no condition (applies to all models), matching specific tags, or a custom tag-based expression.
10. Under **Privileges**, select **EXECUTE**.
11. Click **Create policy**.

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Editing a GRANT Policy

You can edit a GRANT policy through Catalog Explorer, SQL (`ALTER POLICY`), or the Databricks SDK. In Catalog Explorer, select the policy from the **Policies** tab, update any fields, and click **Update policy**. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Deleting a GRANT Policy

To delete a GRANT policy, use `DROP POLICY` in SQL, the Databricks SDK, or the Catalog Explorer UI by selecting the policy and clicking **Delete policy**. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Listing and Describing Policies

### SHOW POLICIES

Use `SHOW POLICIES` to list the policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies inherited from parent scopes, such as catalog-level policies that affect a schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA } securable_name
```

The result includes the policy name, policy type (GRANT policies are returned with policy type `GRANT`), and the catalog or schema where each policy is defined. For GRANT policies attached to a catalog or schema, the `table` column is `NULL`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### DESCRIBE POLICY

Use `DESCRIBE POLICY` to view the details of a specific GRANT policy. Requires `MANAGE` on the target securable object or object ownership. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA } securable_name
```

The result shows the policy's properties including name, securable object type and name, principals, privileges, and the `WHEN` condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction with Direct Grants

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` on a model when any of the following is true: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- A GRANT policy attached to the model's catalog or schema lists the principal in `TO` (and not in `EXCEPT`), and the policy's `WHEN` condition matches the tags on the model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

`SHOW GRANTS` does not include privileges granted via a GRANT policy. To see all `EXECUTE` access on a model, combine `SHOW GRANTS` output with the GRANT policies returned by `SHOW EFFECTIVE POLICIES` on its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Compute Requirements

Creating, modifying, or dropping GRANT policies with SQL requires a classic compute cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Use groups in `TO` and `EXCEPT`**, not individual users, to simplify maintenance. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope** that covers the targets to avoid unintended access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use tag inheritance for safe defaults** and override only on specific objects that need different values. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Don't mix GRANT policies and direct grants** for the same privilege, as they union together and make auditing harder. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`**, which are prerequisites to access a model, and use GRANT policies for `EXECUTE`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Audit Logging

GRANT policy create, alter, and drop operations are logged under the same `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` actions as row filter and column mask policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md)
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md)
- [Governed Tags](/concepts/governed-tags.md)
- Policy Evaluation Order
- Manage privileges in Unity Catalog

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
