---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2259de0b3c0b192237c44516327a285e3eb09aae585a3402162925a4f0248ed6
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-sql-syntax
    - GPSS
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy SQL Syntax
description: SQL syntax for creating, describing, showing, and deleting GRANT policies, including CREATE POLICY, DESCRIBE POLICY, SHOW POLICIES, and SHOW EFFECTIVE POLICIES.
tags:
  - sql
  - unity-catalog
  - reference
timestamp: "2026-06-19T13:50:17.740Z"
---

# GRANT Policy SQL Syntax

**GRANT Policy SQL Syntax** describes the SQL statements used to create, modify, list, and describe attribute-based access control (ABAC) policies in [Unity Catalog](/concepts/unity-catalog.md) that dynamically grant privileges on securable objects based on tag conditions. In the current Beta, GRANT policies support only the `EXECUTE` privilege on models, attached at the catalog or schema level. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

A GRANT policy uses a `CREATE POLICY` statement with a `WHEN` clause that references [Governed Tags](/concepts/governed-tags.md) or [System Tags](/concepts/system-tags.md). The policy is evaluated every time access is checked, granting the specified privilege on every securable object whose tags match the condition. Unlike direct `GRANT` statements, which name specific objects by their three-level namespace, a GRANT policy dynamically applies to all current and future objects that satisfy the tag-based condition within the policy’s scope. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## CREATE POLICY

Use the `CREATE POLICY` statement to define a new GRANT policy. The policy must be attached to a catalog or schema (not directly to a model). The SQL syntax is:

```sql
CREATE POLICY policy_name
  ON { CATALOG | SCHEMA } securable_name
  COMMENT 'optional description'
  TO `principal` [ , ... ]
  [ EXCEPT `principal` [ , ... ] ]
  GRANT EXECUTE FOR MODELS
  WHEN condition_expression;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Components

- **`policy_name`**: A user-chosen name for the policy, unique within the catalog or schema.
- **`ON CATALOG` or `ON SCHEMA`**: Specifies the scope where the policy is attached. In Beta, policies can only be attached at the catalog or schema level. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`TO`**: Lists the principals (users, groups, or service principals) that the policy applies to. Using groups is recommended over individual users for easier maintenance. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`EXCEPT` (optional)**: Excludes specific principals from the policy. If a principal appears in both `TO` and `EXCEPT`, they are excluded. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`GRANT EXECUTE FOR MODELS`**: Specifies the privilege and securable type. Only `EXECUTE` on models is supported in Beta. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **`WHEN condition_expression`**: A condition that uses built-in functions such as `has_tag()` and `has_tag_value()` to match governed tags on models. If the condition evaluates to `true` for a model, the policy grants `EXECUTE` on that model to the `TO` principals (except those in `EXCEPT`). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example 1: Grant EXECUTE on production models

The following policy grants `EXECUTE` on all models in `production.ml_models` that have the governed tag `lifecycle` set to `'production'`:

```sql
CREATE POLICY grant_production_model_access
  ON SCHEMA production.ml_models
  COMMENT 'Grant EXECUTE on production MLflow models'
  TO `analysts`
  GRANT EXECUTE FOR MODELS
  WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Example 2: Grant EXECUTE on Anthropic foundation models with an exception

This policy grants `EXECUTE` on all models in `system.ai` that carry the system tag `ai.model_creator = 'anthropic'`, but excludes the `contractors` group:

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

Without a GRANT policy, equivalent access would require a separate `GRANT EXECUTE ON MODEL` statement per model, and would need to be reissued when new models are added. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Prerequisites

To create a GRANT policy, you must have `MANAGE` on the catalog or schema where the policy is attached, or own that securable object. Compute must be a classic cluster running Databricks Runtime 18.3 or above. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## DESCRIBE POLICY

The `DESCRIBE POLICY` statement returns the properties of an existing GRANT policy as key-value pairs, including name, securable object, principals, privileges, and the `WHEN` condition.

```sql
{ DESC | DESCRIBE } POLICY policy_name ON { CATALOG | SCHEMA } securable_name;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Example:

```sql
DESCRIBE POLICY grant_anthropic_foundation_models ON SCHEMA system.ai;
```

You must have `MANAGE` on the target securable object or own it to use `DESCRIBE POLICY`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## SHOW POLICIES and SHOW EFFECTIVE POLICIES

Use `SHOW POLICIES` to list the policies defined directly on a securable object. Use `SHOW EFFECTIVE POLICIES` to also include policies inherited from parent scopes (e.g., catalog-level policies that apply to a schema).

```sql
SHOW [EFFECTIVE] POLICIES ON { CATALOG | SCHEMA } securable_name;
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The result includes the policy name, policy type (for GRANT policies, the type is `GRANT`), and the catalog or schema where each policy is defined. For GRANT policies, the `table` column is `NULL` because they are not attached at the table level. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Example:

```sql
SHOW EFFECTIVE POLICIES ON SCHEMA system.ai;
```

`SHOW GRANTS` does **not** include privileges granted via a GRANT policy. To see all effective `EXECUTE` access on a model, you must combine the output of `SHOW GRANTS` on the model with the GRANT policies returned by `SHOW EFFECTIVE POLICIES` on its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction with Direct Grants

Effective privileges on an object are the union of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` on a model if:

- A GRANT policy attached to the model’s catalog or schema lists the principal in `TO` (and not in `EXCEPT`), and the policy’s `WHEN` condition matches the tags on the model; or
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal (via direct grant, group membership, or administrative privileges).

Because access is additive, a more selective GRANT policy does not remove `EXECUTE` that a principal already holds through a direct grant. To audit whether direct grants might override a GRANT policy, use `SHOW GRANTS` (or the equivalent REST API / Python SDK) on the model and its ancestors. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations (SQL-relevant)

- Only `EXECUTE` on models is supported in Beta. Other privileges such as `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- The prerequisite permissions `USE SCHEMA` and `USE CATALOG` are not covered by GRANT policies and must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- A policy can be attached only to a catalog or schema, not to an individual model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does not return privileges granted by a GRANT policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices for SQL Usage

- **Use groups in `TO` and `EXCEPT`** rather than individual users. Adding or removing a user from a group changes policy applicability without editing the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope** that contains the target securables to avoid unintended access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Do not mix GRANT policies and direct grants for the same privilege.** Choose one approach for a given privilege on a securable to simplify auditing and reasoning about access. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`**, and use GRANT policies only for `EXECUTE` on models. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
