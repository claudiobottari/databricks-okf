---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27dd76dbac812e16ff4c85634134649c2930440d58afc661ce492fb91d1e4ac4
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - condition-functions-for-abac
    - CFFA
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Condition Functions for ABAC
description: Built-in functions such as has_tag and has_tag_value used in GRANT policy WHEN clauses to match governed tags on securable objects and determine policy applicability.
tags:
  - access-control
  - unity-catalog
  - sql
  - policy-language
timestamp: "2026-06-19T21:54:32.340Z"
---

# Condition Functions for ABAC

**Condition functions** are built-in expressions used in [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies on Databricks to dynamically grant privileges based on the values of [Governed Tags](/concepts/governed-tags.md) attached to securable objects. In ABAC GRANT policies, the condition is written inline (not as a user-defined function) and is evaluated at access time against the tags on each securable object within the policy’s scope. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Built-in Condition Functions

Two condition functions are referenced in the ABAC GRANT policy documentation:

- `has_tag(tag_key)` — returns `true` if the securable object carries a governed tag with the specified key.
- `has_tag_value(tag_key, tag_value)` — returns `true` if the securable object carries a governed tag whose key equals `tag_key` and whose value equals `tag_value`.

These functions appear in the `WHEN` clause of a GRANT policy. For example:

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

The same functions are used when matching system tags (e.g., `ai.model_creator`). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

For a complete reference of all available condition functions and their syntax, see the core ABAC documentation ([Core concepts for attribute-based access control (ABAC)])—the source material for this page does not list every function, but it explicitly cross‑references that document. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## How Conditions Are Evaluated

Unity Catalog evaluates the `WHEN` condition of a GRANT policy every time access to a securable object is checked. The condition is applied to every object in the policy’s scope (the catalog or schema where the policy is attached). If the tags on the object satisfy the condition, the principal listed in `TO` receives the specified privilege (`EXECUTE` on models, in the current Beta). The policy can also exclude certain principals using the `EXCEPT` clause. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Usage in GRANT Policies

Condition functions are used in two ways:

1. **In SQL** – written directly in the `WHEN` clause of `CREATE POLICY`.
2. **In Catalog Explorer** – when creating a policy, the **Condition** step offers:
   - **No condition** (applies to all objects in scope),
   - **Securables matching any of these tags** (a tag-picker interface that generates a condition using `has_tag`/`has_tag_value` internally),
   - **Securables matching a custom expression** (free‑form text field where you can write arbitrary condition expressions using the built‑in functions).

In all cases, the condition can only reference governed tags (user-created or [System Tags](/concepts/system-tags.md)). UDFs are not allowed; the condition is expressed inline. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations (Beta)

- Only the `EXECUTE` privilege on models is supported. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` cannot be granted via condition functions.
- Condition functions cannot be used to grant prerequisite permissions like `USE CATALOG` or `USE SCHEMA`; those must be granted directly.
- The policy must be attached at the catalog or schema level, never directly to a model.
- `SHOW GRANTS` does not reflect privileges obtained through condition‑based GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [System Tags](/concepts/system-tags.md)
- [GRANT policies (ABAC)](/concepts/grant-policies-abac-beta.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) (related but distinct: GRANT policies control access, not data content)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
