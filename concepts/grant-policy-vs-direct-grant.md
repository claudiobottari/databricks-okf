---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d5bca832ddd05ca7be80f0d5b65bd3274f0f90e0385b559787a0b4a10c80c9e
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-vs-direct-grant
    - GPVDG
    - Direct Grant
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy vs Direct Grant
description: Key distinction between dynamic tag-based GRANT policies that match by governed tags versus static direct GRANT statements that identify objects by their three-level namespace.
tags:
  - unity-catalog
  - access-control
  - comparison
timestamp: "2026-06-19T13:49:57.792Z"
---

# GRANT Policy vs Direct Grant

**GRANT Policy vs Direct Grant** describes two distinct approaches to granting privileges on securable objects in [Unity Catalog](/concepts/unity-catalog.md). A GRANT policy dynamically grants privileges based on tag-matching conditions, while a direct grant assigns privileges to explicitly named objects using their three-level namespace (`catalog.schema.object`). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Overview

Both mechanisms control access to securable objects, but they differ fundamentally in how privileges are assigned and maintained. The effective privileges on an object are the union of direct grants and any applicable GRANT policies — a principal holds a privilege when either source grants it. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Direct Grant

A direct grant uses the SQL `GRANT` statement to assign a privilege on a specific securable object identified by its full name. For example, granting `EXECUTE` on individual models in `system.ai` requires one statement per model: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-sonnet-4-6` TO `data_scientists`;
GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-opus-4-7` TO `data_scientists`;
GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-haiku-4-5` TO `data_scientists`;
```

Direct grants must be reissued as new objects are added. They are the traditional approach and are required for certain privileges that GRANT policies do not support, such as `USE CATALOG`, `USE SCHEMA`, `CREATE MODEL`, and `CREATE MODEL VERSION`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## GRANT Policy

A GRANT policy is an [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy that dynamically grants Unity Catalog privileges to securable objects whose [Governed Tags](/concepts/governed-tags.md) match the policy's condition. Unity Catalog evaluates the policy's `WHEN` condition against the governed tags on each securable object in the policy's scope every time access is checked, and grants the privilege on every securable object that matches. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

For example, the following policy grants `EXECUTE` on all Anthropic-hosted foundation models in `system.ai` to `data_scientists` (except `contractors`) by matching the `ai.model_creator` system tag — without a separate grant per model: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

GRANT policies can reference either governed tags you create yourself or system tags predefined by Databricks. They differ from row filter and column mask policies in two ways: they determine whether the user can access the object at all (rather than restricting content), and they express conditions inline without requiring a user-defined function (UDF). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Key Differences

| Aspect | Direct Grant | GRANT Policy |
|--------|-------------|--------------|
| **Object identification** | Explicit three-level namespace (`catalog.schema.object`) | Tag-based condition matching |
| **Maintenance** | Requires reissuing grants as objects are added or removed | Automatically covers new objects that match the tag condition |
| **Scope** | Can be applied at object, schema, or catalog level | Attached at catalog or schema level only (Beta) |
| **Supported privileges (Beta)** | All privileges on all securable types | Only `EXECUTE` on models |
| **Visibility in `SHOW GRANTS`** | Yes | No |
| **Visibility in `INFORMATION_SCHEMA`** | Yes | No |

## Interaction Between the Two

Because effective privileges are the union of both sources, a more selective GRANT policy does not mean that an excluded principal lacks the privilege. The principal can still hold the privilege through a direct grant on the object or its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

To audit access on a model, combine two sources of information: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA <parent_schema>` (or `ON CATALOG <parent_catalog>`) to list every GRANT policy whose scope covers the models in that schema or catalog.
- Use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants.

## Best Practices

- **Don't mix GRANT policies and direct grants for the same privilege.** GRANT policies union with direct grants, so mixing them on the same securable makes it harder to reason about who has access and to audit changes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`, GRANT policies for `EXECUTE`.** GRANT policies do not grant the prerequisite permissions required to access a model. Grant those directly, and use a GRANT policy to scope `EXECUTE` on individual models by tag. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use groups in `TO` and `EXCEPT`, not individual users.** Adding or removing users from a group named in a policy changes who the policy applies to, without editing the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope that covers the targets.** A broader scope brings unrelated securables into the policy's tag-matching and may grant access where you didn't intend. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations of GRANT Policies (Beta)

- Only the `EXECUTE` privilege on models is supported. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- The prerequisite permissions `USE SCHEMA` and `USE CATALOG` are not supported by GRANT policies and must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- A policy can be attached to the catalog or the schema, not to the model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does not return privileges granted by a GRANT policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- You cannot use [Delta Sharing](/concepts/delta-sharing.md) to share models that have GRANT policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [System Tags](/concepts/system-tags.md)
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)
- [Row Filter and Column Mask Policies](/concepts/row-filter-and-column-mask-policies.md)
- Manage Privileges in Unity Catalog

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
