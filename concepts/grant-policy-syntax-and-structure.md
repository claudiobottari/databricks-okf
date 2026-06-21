---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 258fb5ddd1ec2681f5aa7457020f8a33415a527acb99425bd1ab2dba13875638
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-syntax-and-structure
    - Structure and GRANT Policy Syntax
    - GPSAS
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
    - file: |-
        abac-grant-policies-for-models-beta-databricks-on-aws.md>

        ## Related SQL Commands

        ### SHOW POLICIES

        List all policies defined on a securable object (catalog or schema). Use `SHOW EFFECTIVE POLICIES` to also include inherited policies from parent scopes.

        ```sql
        SHOW [EFFECTIVE
    - file: |-
        abac-grant-policies-for-models-beta-databricks-on-aws.md>

        ## Best Practices for Syntax

        - **Use groups in `TO` and `EXCEPT`** rather than individual users. This makes the policy more maintainable and avoids needing to rewrite the policy when people join or leave teams. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy Syntax and Structure
description: The CREATE POLICY SQL syntax for defining GRANT policies, including TO/EXCEPT principals, GRANT EXECUTE FOR MODELS, and WHEN conditions using functions like has_tag_value.
tags:
  - sql
  - syntax
  - unity-catalog
timestamp: "2026-06-18T14:15:39.082Z"
---

# GRANT Policy Syntax and Structure

**ABAC GRANT policies** are defined using the `CREATE POLICY` SQL statement, which specifies the policy name, scope, principals, the privilege to grant, and an inline condition based on [Governed Tags](/concepts/governed-tags.md) or [System Tags](/concepts/system-tags.md). The condition is evaluated every time access is checked against each securable object within the policy's scope. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Syntax

The full syntax for creating a GRANT policy is:

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

### Clauses

- **`policy_name`** – A unique name for the policy within the scope.
- **`ON { CATALOG | SCHEMA } securable_name`** – The scope where the policy is attached. In Beta, policies can only be attached to a catalog or a schema, not directly to a model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`COMMENT`** (optional) – A description of the policy.
- **`TO`** – One or more principals (users, groups, service principals) to whom the privilege is granted. Principal names must be enclosed in backticks (`` ` ``). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`EXCEPT`** (optional) – Principals excluded from the grant. Used alongside `TO` to subtract specific principals from a broader group. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`GRANT EXECUTE FOR MODELS`** – The privilege and securable type. Currently only `EXECUTE` on models is supported. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`WHEN condition_expression`** – A Boolean expression using built-in tag functions (such as `has_tag_value` or `has_tag`) that must match the governed or system tags on the securable object. The condition is evaluated inline; no UDF is required. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Condition Expression

The `WHEN` clause uses the same built-in condition functions available for all ABAC policies. Common functions include `has_tag(tag_name)` and `has_tag_value(tag_name, value)`. The condition is evaluated against the tags on each model in the policy’s scope every time access is checked. For a full list of available functions, see [Core concepts for attribute-based access control (ABAC)](/concepts/attribute-based-access-control-abac.md). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Examples

### Granting access based on a governed tag

The following policy grants `EXECUTE` to the `analysts` group on models tagged `lifecycle = 'production'` in schema `production.ml_models`:

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
COMMENT 'Grant EXECUTE on production MLflow models'
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Granting access based on a system tag with exclusions

The following policy grants `EXECUTE` to `data_scientists` (except `contractors`) on all Anthropic-hosted foundation models in `system.ai` by matching the `ai.model_creator` system tag:

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md>

## Related SQL Commands

### SHOW POLICIES

List all policies defined on a securable object (catalog or schema). Use `SHOW EFFECTIVE POLICIES` to also include inherited policies from parent scopes.

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA } securable_name
```

The result includes the policy name, policy type (`GRANT`), and the scope where each policy is defined. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### DESCRIBE POLICY

View the details of a specific GRANT policy. Requires `MANAGE` on the target securable object or object ownership.

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA } securable_name
```

Outputs key-value pairs including name, securable type and name, principals, privileges, and the `WHEN` condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md>

## Best Practices for Syntax

- **Use groups in `TO` and `EXCEPT`** rather than individual users. This makes the policy more maintainable and avoids needing to rewrite the policy when people join or leave teams. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope** that covers the target securables. A broader scope may unintentionally grant access to unrelated models that match the condition. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use tag inheritance** to apply default tag values at the parent catalog or schema, then override only on specific objects that need different values. Combine with `EXCEPT` for controlled exceptions. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Differences from Other Policy Types

GRANT policies differ syntactically and structurally from [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md):

- GRANT policies use an inline `WHEN` condition instead of referencing a UDF.
- GRANT policies attach to a catalog or schema, not to a table or column.
- GRANT policies **grant** access, whereas row and column policies **restrict** already-granted access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations

- Only `EXECUTE` on models is supported in Beta. Other privileges (e.g., `CREATE MODEL`, `APPLY TAG`) must be granted directly.
- The policy cannot be attached to a model; it must be attached to a catalog or schema.
- `SHOW GRANTS` does not include privileges from GRANT policies; use `SHOW EFFECTIVE POLICIES` instead. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Overview of the policy type
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer providing ABAC
- [Governed Tags](/concepts/governed-tags.md) — User-defined tags used in condition expressions
- [System Tags](/concepts/system-tags.md) — Predefined Databricks tags (e.g., `ai.model_creator`)
- MLflow Models — The securable objects covered in Beta
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data rows
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask column values
- has_tag_value — Built-in function for tag-value matching
- has_tag — Built-in function for tag presence checking

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
2. abac-grant-policies-for-models-beta-databricks-on-aws.md>

## Related SQL Commands

### SHOW POLICIES

List all policies defined on a securable object (catalog or schema). Use `SHOW EFFECTIVE POLICIES` to also include inherited policies from parent scopes.

```sql
SHOW [EFFECTIVE
3. abac-grant-policies-for-models-beta-databricks-on-aws.md>

## Best Practices for Syntax

- **Use groups in `TO` and `EXCEPT`** rather than individual users. This makes the policy more maintainable and avoids needing to rewrite the policy when people join or leave teams. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md
