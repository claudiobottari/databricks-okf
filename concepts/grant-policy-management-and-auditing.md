---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f33f63bde5ba4a2d144978ef41308d5c815a0d9e2bb74ab7692d7ed2e2ca15fb
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-management-and-auditing
    - Auditing and GRANT Policy Management
    - GPMAA
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: |-
        abac-grant-policies-for-models-beta-databricks-on-aws.md>

        Note: `SHOW GRANTS` does **not** include privileges granted by a GRANT policy; you must combine it with `SHOW EFFECTIVE POLICIES` to see all sources of `EXECUTE` access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Management and Auditing
description: SQL commands (CREATE POLICY, ALTER POLICY, SHOW POLICIES, DESCRIBE POLICY, DROP POLICY), Catalog Explorer UI operations, and audit logging for managing ABAC GRANT policies in Unity Catalog.
tags:
  - unity-catalog
  - policy-management
  - sql
  - operations
timestamp: "2026-06-19T21:54:34.589Z"
---

# GRANT Policy Management and Auditing

**GRANT Policy Management and Auditing** covers the lifecycle of attribute-based access control (ABAC) GRANT policies on Databricks. GRANT policies dynamically grant Unity Catalog privileges to securable objects whose governed tags match a condition, offering an alternative to static direct grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Overview

A GRANT policy is an ABAC policy that grants a privilege – in Beta, the `EXECUTE` privilege on Model objects – to principals (users, groups, service principals) when the policy’s `WHEN` condition matches the governed tags applied to those models. The policy is attached at either the [Catalog](/concepts/unity-catalog.md) or Schema level, and Unity Catalog evaluates it every time access is checked. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

GRANT policies support both customer-registered MLflow Models and Databricks‑hosted foundation models (for example, those in `system.ai`). Conditions can reference user‑created [Governed Tags](/concepts/governed-tags.md) or [System Tags](/concepts/system-tags.md) predefined by Databricks. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## How GRANT Policies Interact with Direct Grants

The effective privileges on a model are the **union** of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` when:

- A GRANT policy attached to the model’s catalog or schema lists the principal in `TO` (and not in `EXCEPT`), and the policy’s `WHEN` condition matches the model’s tags; or
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect (whether via a direct grant, group membership, or administrative privilege).

Because access is the union of sources, a more selective GRANT policy does **not** prevent a principal from holding `EXECUTE` through a direct grant. To audit effectively, use `SHOW EFFECTIVE POLICIES` to see all GRANT policies that affect a scope, and `SHOW GRANTS` (or the equivalent REST APIs) to enumerate direct grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Creating a GRANT Policy

You can create a GRANT policy through the [Catalog Explorer](/concepts/catalog-explorer.md) UI, the [`CREATE POLICY`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-create-policy) SQL statement, or the Databricks SDK. The creator must have `MANAGE` on the target catalog or schema (or own that securable object). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

In the Catalog Explorer:
1. Navigate to the catalog or schema.
2. Click the **Policies** tab and then **New policy**.
3. Provide a policy name and description.
4. Under **Principals and scope**, specify the users/groups/service principals in `Applied to` and optionally an `Except for` list.
5. Set the policy type to **Grant access**.
6. Under **Securable objects**, select **Model** (the only supported type in Beta).
7. Under **Condition**, choose:
   - **No condition** – applies to all models in the scope.
   - **Securables matching any of these tags** – applies to models with at least one selected governed tag.
   - **Securables matching a custom expression** – lets you write a tag‑based expression using functions such as `has_tag_value`.
8. Under **Privileges**, select **EXECUTE**.
9. Click **Create policy**.

The equivalent SQL syntax uses `CREATE POLICY ... ON SCHEMA ... TO ... GRANT EXECUTE FOR MODELS WHEN has_tag_value(...)`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Editing and Deleting a GRANT Policy

To edit a GRANT policy in the Catalog Explorer, select the policy from the **Policies** tab, modify the fields, and click **Update policy**. In SQL, use `ALTER POLICY`. To delete, click **Delete policy** in the UI or use `DROP POLICY`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Showing and Describing Policies

Use `SHOW POLICIES ON { CATALOG | SCHEMA }` to list policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies inherited from parent scopes (for example, catalog‑level policies that affect a schema). The result includes policy name, type (`GRANT`), and scope. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Use `DESCRIBE POLICY <policy_name> ON { CATALOG | SCHEMA }` to view detailed properties such as the name, securable object, principals, privileges, and `WHEN` condition. Requires `MANAGE` on the target or ownership. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md>

Note: `SHOW GRANTS` does **not** include privileges granted by a GRANT policy; you must combine it with `SHOW EFFECTIVE POLICIES` to see all sources of `EXECUTE` access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Policy Quotas

GRANT policies have independent quotas separate from the quotas for [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Audit Logging

All create, alter, and drop operations on GRANT policies are logged under the same audit actions as row filter and column mask policies: `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies`. Refer to the [Audit Logging](/concepts/abac-policy-audit-logging.md) documentation for example queries. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Use groups** in `TO` and `EXCEPT` instead of individual users to simplify maintenance.
- **Attach policies at the smallest scope** that contains the target models to avoid unintended access.
- **Use tag inheritance** for safe defaults: apply default tag values at the parent catalog or schema, and override on specific objects that need a different value.
- **Don’t mix GRANT policies and direct grants** for the same privilege on the same securable; the union makes reasoning and auditing harder.
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`** (which are prerequisites for model access), and use a GRANT policy to scope `EXECUTE` on individual models by tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations (Beta)

- Only the `EXECUTE` privilege on models is supported. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` must be granted directly.
- The prerequisite permissions `USE SCHEMA` and `USE CATALOG` are not supported by GRANT policies.
- A policy can be attached only to the catalog or schema, not to the model itself.
- `SHOW GRANTS` does not reflect privileges from GRANT policies.
- `INFORMATION_SCHEMA` does not include GRANT policies.
- Deleting a model or model version is not covered by GRANT policies.
- Models with GRANT policies cannot be shared using [Delta Sharing](/concepts/delta-sharing.md).
- Compute requirement: Creating, modifying, or dropping GRANT policies with SQL requires a classic compute cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Governed Tags](/concepts/governed-tags.md)
- [System Tags](/concepts/system-tags.md)
- MLflow Models
- [Direct Grants](/concepts/grant-policy-vs-direct-grant.md)
- Securable Objects
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Databricks SDK
- [Audit Logging](/concepts/abac-policy-audit-logging.md)
- [Delta Sharing](/concepts/delta-sharing.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
2. abac-grant-policies-for-models-beta-databricks-on-aws.md>

Note: `SHOW GRANTS` does **not** include privileges granted by a GRANT policy; you must combine it with `SHOW EFFECTIVE POLICIES` to see all sources of `EXECUTE` access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md
