---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2d876b8c4dda69f839b465c7738eeee727efdcb97415a558b2034f8275749d62
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-grant-policy
    - AGP
    - GRANT Policy
    - GRANT policy
    - abac-grant-policies
    - ABAC GRANT Policies (Beta)
    - ABAC GRANT policies for models (Beta)
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: ABAC GRANT Policy
description: An attribute-based access control policy that dynamically grants Unity Catalog privileges to securable objects whose governed tags match a condition, evaluated at access time.
tags:
  - unity-catalog
  - abac
  - access-control
timestamp: "2026-06-19T13:50:16.451Z"
---

```yaml
---
title: ABAC GRANT Policy
summary: An attribute-based access control policy that dynamically grants Unity Catalog privileges to securable objects whose governed tags match a condition, evaluated at every access check.
sources:
  - abac-grant-policies-for-models-beta-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:35:53.100Z"
updatedAt: "2026-06-18T10:35:53.100Z"
tags:
  - unity-catalog
  - access-control
  - abac
  - databricks
aliases:
  - abac-grant-policy
  - AGP
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 1
---

# ABAC GRANT Policy

**ABAC GRANT policies** are attribute-based access control policies in Unity Catalog that dynamically grant privileges to securable objects whose governed tags match a specified condition. Unlike direct `GRANT` statements that assign privileges to objects identified by their three-level namespace (`catalog.schema.object`), GRANT policies evaluate a `WHEN` condition against governed tags on each securable object in the policy's scope every time access is checked, granting the privilege on every matching object. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Current Scope (Beta)

GRANT policies are currently in Beta. In this release, they support one privilege on one securable type: `EXECUTE` on models. This covers both customer-registered MLflow Models and Databricks-hosted foundation models in `system.ai`. Additional privileges and securable types will be supported in future releases. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## How GRANT Policies Work

A GRANT policy dynamically grants Unity Catalog privileges to securable objects whose governed tags match the policy's condition. Unity Catalog evaluates the policy's `WHEN` condition against the governed tags on each securable object in the policy's scope every time access is checked, and grants the privilege on every securable object that matches. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

GRANT policies can reference either [[governed tags]] you create yourself or [[system tags]] predefined by Databricks in their conditions. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example: Granting Access Based on Tags

The following policy uses the `lifecycle` governed tag applied to customer-registered MLflow models in `production.ml_models`. The policy grants `EXECUTE` only on models tagged `lifecycle = 'production'`:

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example: Granting Access to Foundation Models

The following policy grants `EXECUTE` on Anthropic-hosted foundation models in `system.ai` to `data_scientists`, except `contractors`, by matching the `ai.model_creator` system tag. Every model that carries `ai.model_creator = 'anthropic'` is covered, without a separate grant per model:

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

The equivalent access using direct grants would require one statement per model in `system.ai`, reissued as Databricks adds new Anthropic models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction with Direct Grants

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` on a model when any of the following is true: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- A GRANT policy attached to the model's catalog or schema lists the principal in `TO` (and not in `EXCEPT`), and the policy's `WHEN` condition matches the tags on the model.
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal, whether granted directly, through group membership, or through other administrative privileges.

Because access is the union of these sources, a more selective GRANT policy does not mean that an excluded principal lacks `EXECUTE`. The principal can still hold the privilege through a direct grant on the model, or its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Auditing Effective Access

If you intend to use GRANT policies as the primary way to control `EXECUTE` on models, first determine whether any direct grants already in place might override the policy: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA <parent_schema>` (or `ON CATALOG <parent_catalog>`) to list every GRANT policy whose scope covers the models in that schema or catalog. The equivalent REST API is `GET /api/2.1/unity-catalog/policies/{on_securable_type}/{on_securable_fullname}?include_inherited=true` (Python SDK: `w.policies.list_policies(..., include_inherited=True)`).
- Use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. The equivalent REST API for direct grants on a securable object is `GET /api/2.1/unity-catalog/permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get(...)`); for the union of direct and inherited grants, use `GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get_effective(...)`).

## Creating a GRANT Policy

To create a GRANT policy, you must have `MANAGE` on the catalog or schema where the policy is attached, or own that securable object. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

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

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. Select the catalog or schema where you want to attach the policy.
3. Click the **Policies** tab.
4. Click **New policy**.
5. Under **Policy identification**, enter a **Policy name** and an optional **Description**.
6. Under **Principals and scope**, select the principals in **Applied to**, optionally select principals to exclude in **Except for**, and confirm the **Scope**.
7. Under **Policy type**, select **Grant access**.
8. Under **Securable objects**, select **Model**.
9. Under **Condition**, choose how to scope the policy: **No condition** (applies to all models), **Securables matching any of these tags**, or **Securables matching a custom expression**.
10. Under **Privileges**, select **EXECUTE**.
11. Click **Create policy**.

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Editing and Deleting GRANT Policies

### Edit a Policy

In Catalog Explorer, select the catalog or schema, click the **Policies** tab, select the policy, update any fields, and click **Update policy**. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Delete a Policy

In Catalog Explorer, select the catalog or schema, click the **Policies** tab, select the policy, and click **Delete policy**. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Viewing Policies

### Show Policies

Use `SHOW POLICIES` to list the policies defined on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies inherited from parent scopes, such as catalog-level policies that affect a schema. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA } securable_name
```

The result includes the policy name, policy type, and the catalog or schema where each policy is defined. GRANT policies are returned with policy type `GRANT`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Describe a Policy

Use `DESCRIBE POLICY` to view the details of a specific GRANT policy. Requires `MANAGE` on the target securable object or object ownership. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA } securable_name
```

The result shows the policy's properties as key-value pairs, including name, securable object type, securable object name, principals, privileges, and the `WHEN` condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Differences from Row Filter and Column Mask Policies

GRANT policies differ from [[Row Filter Policies|row filter]] and column mask policies in two ways: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- Row filter and column mask policies restrict the content of data a user can already access. GRANT policies determine whether the user can access the object at all.
- Row filter and column mask policies require a user-defined function (UDF) to implement the filter or mask. GRANT policies do not use UDFs. The condition is expressed inline in the policy definition.

## Best Practices

- **Use groups in `TO` and `EXCEPT`, not individual users.** Adding or removing users from a group named in a policy changes who the policy applies to, without editing the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope that covers the targets.** Use the narrowest scope that contains the securables the policy should apply to. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use tag inheritance for safe defaults.** Apply default tag values at the parent catalog or schema so descendants inherit them. Override the inherited tag only on the specific objects that need a different value. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Don't mix GRANT policies and direct grants for the same privilege.** For a given privilege on a securable, choose either GRANT policies or direct grants, not both. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`, GRANT policies for `EXECUTE`.** GRANT policies do not grant the `USE CATALOG` and `USE SCHEMA` prerequisites required to access a model. Grant those directly, and use a GRANT policy to scope `EXECUTE` on individual models by tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

- Only the `EXECUTE` privilege on models is supported. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` are not supported by GRANT policies and must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- The prerequisite permissions `USE SCHEMA` and `USE CATALOG` are not supported by GRANT policies and must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- A policy can be attached to the catalog or the schema, not to the model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does not return privileges granted by a GRANT policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Deleting a model or a model version is not covered by GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- You cannot use [[Delta Sharing]] to share models that have GRANT policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Compute Requirements

Creating, modifying, or dropping GRANT policies with SQL requires a classic compute cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Audit Logging

GRANT policy create, alter, and drop operations are logged under the same `createPolicy`, `deletePolicy`, `getPolicy`, and `listPolicies` actions as row filter and column mask policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [[Unity Catalog]] — The data governance solution that provides ABAC capabilities
- [[Governed Tags]] — Tags used in GRANT policy conditions to determine access
- [[System Tags]] — Predefined tags provided by Databricks
- MLflow Models — Models that can be secured using GRANT policies
- [[Row Filter Policies]] — ABAC policies that restrict data content rather than access
- [[Column Mask Policies]] — ABAC policies that mask sensitive columns

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md
```

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
