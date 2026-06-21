---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef93923dc76ec03bed816ad12372bb044f1e25d3de915b3e3bdb674f97c10b5c
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-syntax-and-management
    - Management and GRANT Policy Syntax
    - GPSAM
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Syntax and Management
description: SQL syntax (CREATE POLICY, DESCRIBE POLICY, SHOW POLICIES, SHOW EFFECTIVE POLICIES, DROP POLICY) and Catalog Explorer UI for creating, editing, deleting, and inspecting ABAC GRANT policies.
tags:
  - unity-catalog
  - sql
  - abac
  - databricks
timestamp: "2026-06-18T10:36:25.949Z"
---

Here is the wiki page for "GRANT Policy Syntax and Management".

---

ABAC GRANT policies are in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). In Beta, GRANT policies can grant the `EXECUTE` privilege on models, attached at the catalog or schema level. Additional privileges and securable types will be supported in future releases.

---

# GRANT Policy Syntax and Management

**GRANT policies** are an [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) mechanism within [Unity Catalog](/concepts/unity-catalog.md) that dynamically grant privileges to securable objects based on governed tags. Instead of granting permissions on individually named objects, a GRANT policy defines a tag-matching condition; Unity Catalog evaluates the condition against every object in the policy's scope and grants the specified privilege on every object whose tags match.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## What is a GRANT Policy?

A GRANT policy is a Unity Catalog policy object that dynamically grants privileges to Securable Objects whose [Governed Tags](/concepts/governed-tags.md) satisfy a condition. The policy is defined with a `WHEN` clause that uses built-in functions—such as `has_tag` and `has_tag_value`—to match against the governed tags on each securable object. Unlike direct `GRANT` statements, which assign privileges on specific objects identified by their three-level namespace (`catalog.schema.object`), a GRANT policy covers all current and future objects within its scope that meet the tag condition.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

In Beta, GRANT policies support one privilege on one securable type: `EXECUTE` on models. This includes both customer-registered MLflow models and Databricks-hosted foundation models in the `system.ai` schema.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

GRANT policies differ from row filter and column mask policies in two important ways:
- Row filter and column mask policies restrict the content of data a user can already access; GRANT policies determine whether the user can access the object at all.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Row filter and column mask policies require a user-defined function (UDF) to implement the filter or mask; GRANT policies do not use UDFs—the condition is expressed inline in the policy definition.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## SQL Syntax

GRANT policies are managed using Data Definition Language (DDL) statements. The primary syntax for creating a policy is the `CREATE POLICY` statement.

### CREATE POLICY

```sql
CREATE POLICY policy_name
ON { CATALOG | SCHEMA } securable_name
[COMMENT 'description']
TO `principal_list`
[EXCEPT `exception_principal_list`]
GRANT EXECUTE FOR MODELS
WHEN condition_expression;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The components of the statement are:
- **`policy_name`**: A unique name for the policy within the scope.
- **`ON CATALOG | SCHEMA`**: Specifies the scope—the catalog or schema where the policy is attached.
- **`TO`**: The principals (users, groups, or service principals) to whom the privilege is granted.
- **`EXCEPT`**: (Optional) Principals to exclude from the grant.
- **`GRANT EXECUTE FOR MODELS`**: The privilege and securable type. In Beta, only `EXECUTE` on models is supported.
- **`WHEN`**: A Condition Expression using built-in functions to match governed tags on securable objects.

### Example: Granting Access by Own Tag

The following policy grants `EXECUTE` on models in `production.ml_models` that are tagged with `lifecycle = 'production'` to the `analysts` group:

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example: Granting Access by System Tag

The following policy grants `EXECUTE` on all Anthropic-hosted foundation models in `system.ai` to `data_scientists`, except `contractors`:

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

This single policy replaces the need for multiple direct `GRANT` statements—one for each model—and automatically covers new Anthropic models as Databricks adds them to `system.ai`.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### DESCRIBE POLICY

To view the details of a specific GRANT policy:

```sql
DESC | DESCRIBE POLICY policy_name ON { CATALOG | SCHEMA } securable_name;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The output shows the policy's properties, including name, securable object type, securable object name, principals, privileges, and the `WHEN` condition.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### SHOW POLICIES

To list the policies defined directly on a securable object:

```sql
SHOW POLICIES ON { CATALOG | SCHEMA } securable_name;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

To include policies inherited from parent scopes (for example, catalog-level policies that affect a schema):

```sql
SHOW EFFECTIVE POLICIES ON { CATALOG | SCHEMA } securable_name;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The output includes the policy name, policy type (`GRANT`), and the catalog or schema where each policy is defined. Note that `SHOW GRANTS` does not include privileges granted via a GRANT policy.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Management Operations

### Create

You can create a GRANT policy using:
- **Catalog Explorer UI**: Navigate to a catalog or schema, click the **Policies** tab, then **New policy**. Select **Grant access** as the policy type, and configure the condition, scope, and principals.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **SQL**: Use the `CREATE POLICY` statement as described above.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Databricks SDK**: Use the Python SDK's policy management API.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

**Prerequisite**: You must have `MANAGE` on the catalog or schema where the policy is attached, or own that securable object.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Edit

To edit a GRANT policy:
- **Catalog Explorer UI**: Navigate to the catalog or schema, select the **Policies** tab, click the policy, update the fields, and click **Update policy**.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **SQL**: Use the `ALTER POLICY` statement (not detailed in the source material).

### Delete

To delete a GRANT policy:
- **Catalog Explorer UI**: Navigate to the catalog or schema, select the **Policies** tab, click the policy, and click **Delete policy**.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **SQL**: Use the `DROP POLICY` statement.

## Compute Requirements

Creating, modifying, or dropping GRANT policies using SQL requires a Classic Compute Cluster running Databricks Runtime 18.3 or above.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction with Direct Grants

The effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` on a model when any of the following is true:
- A GRANT policy lists the principal in `TO` (and not in `EXCEPT`), and the policy's condition matches the model's tags.
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Because access is the union of these sources, a more selective GRANT policy does not guarantee that an excluded principal lacks `EXECUTE`. To audit effective access, combine:
- `SHOW EFFECTIVE POLICIES` on the parent schema or catalog to list applicable GRANT policies. The equivalent REST API is `GET /api/2.1/unity-catalog/policies/{on_securable_type}/{on_securable_fullname}?include_inherited=true`.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. The equivalent REST API is `GET /api/2.1/unity-catalog/permissions/{securable_type}/{full_name}` for direct grants, and `GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}` for the union of direct and inherited grants.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Use groups in `TO` and `EXCEPT`**: Add or remove users from a group rather than editing the policy.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach at the smallest scope**: Use the narrowest catalog or schema that covers the intended securables. A broader scope may inadvertently match unrelated objects.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use tag inheritance**: Apply default tag values at the parent scope and override them only on objects that need different access.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Don't mix GRANT policies and direct grants for the same privilege**: GRANT policies union with direct grants, making it harder to reason about who has access.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`**: GRANT policies do not grant these prerequisite permissions. Grant them directly, and use GRANT policies only for `EXECUTE` on models.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

- Only the `EXECUTE` privilege on models is supported. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` must be granted directly.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Policies can be attached at the catalog or schema level, not directly to a model.
- `SHOW GRANTS` and `INFORMATION_SCHEMA` do not include privileges granted by a GRANT policy.
- Deleting a model or model version is not covered by GRANT policies.
- [Delta Sharing](/concepts/delta-sharing.md) cannot share models that have GRANT policies defined on them.

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Securable Objects
- Condition Expression
- [Databricks Runtime Requirements](/concepts/databricks-ai-runtime-requirements.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
