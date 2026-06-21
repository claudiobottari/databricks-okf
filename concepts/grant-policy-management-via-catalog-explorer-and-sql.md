---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2a951280f9d14db18fb10f330de7e0df8cfa5a67779ed30376f9a18c327ac87
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-management-via-catalog-explorer-and-sql
    - SQL and GRANT Policy Management via Catalog Explorer
    - GPMVCEAS
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Management via Catalog Explorer and SQL
description: How to create, edit, delete, list, and describe GRANT policies using the Catalog Explorer UI, SQL statements (CREATE POLICY, DESCRIBE POLICY, SHOW POLICIES), and the Databricks Python SDK.
tags:
  - management
  - catalog-explorer
  - sql
timestamp: "2026-06-18T14:16:27.960Z"
---

# GRANT Policy Management via Catalog Explorer and SQL

**GRANT policies** are attribute-based access control (ABAC) policies in [Unity Catalog](/concepts/unity-catalog.md) that dynamically grant privileges to securable objects whose [Governed Tags](/concepts/governed-tags.md) match a specified condition. This page describes how to create, edit, delete, and view GRANT policies using the Catalog Explorer interface and SQL commands. GRANT policies are currently in **Beta** and support the `EXECUTE` privilege on models attached at the catalog or schema level. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## What Is a GRANT Policy?

A GRANT policy is an ABAC policy that grants privileges to Unity Catalog securable objects based on their governed tags. Unlike direct `GRANT` statements that identify objects by their three-level namespace (`catalog.schema.object`), GRANT policies evaluate a `WHEN` condition against governed tags every time access is checked, granting the privilege on every matching object. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

In Beta, GRANT policies support one privilege on one securable type: `EXECUTE` on models. Both customer-registered MLflow models and Databricks-hosted foundation models in `system.ai` are covered. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Creating a GRANT Policy

### Prerequisites

- You must have `MANAGE` on the catalog or schema where the policy is attached, or own that securable object. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Creating, modifying, or dropping GRANT policies with SQL requires a classic compute cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the catalog or schema where you want to attach the policy.
3. Click the **Policies** tab.
4. Click **New policy**.
5. Under **Policy identification**, enter a **Policy name** and an optional **Description**.
6. Under **Principals and scope**:
   - In **Applied to**, select the principals (users, groups, or service principals).
   - In **Except for**, optionally select principals to exclude.
   - In **Scope**, confirm the catalog or schema.
7. Under **Policy type**, select **Grant access**.
8. Under **Securable objects**, select **Model**.
9. Under **Condition**, choose how to scope the policy:
   - **No condition** applies to all models.
   - **Securables matching any of these tags** applies only to models with selected tags.
   - **Securables matching a custom expression** lets you write a tag-based expression.
10. Under **Privileges**, select **EXECUTE**.
11. Click **Show code** to review the equivalent SQL, then click **Create policy**.

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Using SQL

```sql
CREATE POLICY policy_name
ON { CATALOG | SCHEMA } securable_name
[COMMENT 'description']
TO `principal` [, `principal` ...]
[EXCEPT `principal` [, `principal` ...]]
GRANT EXECUTE FOR MODELS
WHEN condition_expression;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

#### Example: Granting Access Based on Tags

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

#### Example: Granting Access to Foundation Models

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

This policy grants `EXECUTE` on all Anthropic-hosted models in `system.ai` without a separate grant per model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Editing a GRANT Policy

### Using Catalog Explorer

1. Click **Catalog**.
2. Select the catalog or schema the policy is attached to.
3. Click the **Policies** tab.
4. Select the policy you want to edit.
5. Update any fields.
6. Click **Update policy**.

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Deleting a GRANT Policy

### Using Catalog Explorer

1. Click **Catalog**.
2. Select the catalog or schema the policy is attached to.
3. Click the **Policies** tab.
4. Select the policy.
5. Click **Delete policy**.

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Viewing Policies

### SHOW POLICIES

Use `SHOW POLICIES` to list policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to include policies inherited from parent scopes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATATLOG | SCHEMA } securable_name
```

The result includes the policy name, policy type, and scope. GRANT policies are returned with policy type `GRANT`. The `table` column is `NULL` for GRANT policies attached to a catalog or schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### DESCRIBE POLICY

Use `DESCRIBE POLICY` to view details of a specific GRANT policy. Requires `MANAGE` on the target securable object or ownership. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA } securable_name
```

The result shows key-value properties including name, securable type, securable name, principals, privileges, and the `WHEN` condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction with Direct Grants

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` on a model when either: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- A GRANT policy lists the principal in `TO` (and not in `EXCEPT`), and the `WHEN` condition matches the model's tags.
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal.

`SHOW GRANTS` does not return privileges granted by a GRANT policy. To see all `EXECUTE` access on a model, combine `SHOW GRANTS` with `SHOW EFFECTIVE POLICIES`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Use groups in `TO` and `EXCEPT`**, not individual users. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope** that covers the targets. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use tag inheritance** for safe defaults at the parent level, overriding only on specific objects. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Don't mix GRANT policies and direct grants** for the same privilege on the same securable. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`**, GRANT policies for `EXECUTE`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

- Only `EXECUTE` on models is supported in Beta. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- A policy can be attached to the catalog or schema, not to the model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does not return privileges granted by a GRANT policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Deleting a model or model version is not covered by GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- [Delta Sharing](/concepts/delta-sharing.md) cannot be used to share models with GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Audit Logging

GRANT policy create, alter, and drop operations are logged under the same `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` actions as [row filter](/concepts/row-filter-policies.md) and column mask policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — The full concept overview
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform
- [Governed Tags](/concepts/governed-tags.md) — Tags used in policy conditions
- [System Tags](/concepts/system-tags.md) — Predefined tags from Databricks
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data content
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- MLflow Models — Models that can be secured with GRANT policies

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
