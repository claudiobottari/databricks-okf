---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7299f0ae320a167892ae030bdfcd17fff75b09c636dc48442013e32ba5186992
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policy-vs-direct-grants
    - GPVDG
    - Direct Grants
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policy vs Direct Grants
description: Comparison between dynamic attribute-based GRANT policies that match on tags versus traditional explicit GRANT statements that name specific objects in their three-level namespace.
tags:
  - access-control
  - unity-catalog
  - authorization-patterns
timestamp: "2026-06-19T21:54:22.089Z"
---

# GRANT Policy vs Direct Grants

**GRANT policies** and **direct grants** are two approaches for assigning privileges in [Unity Catalog](/concepts/unity-catalog.md). Both can grant the `EXECUTE` privilege on models, but they differ in how the target objects are identified and how access is evaluated at runtime.

## Overview

A **direct grant** is a traditional privilege assignment that uses the three-level namespace of a securable object (*catalog.schema.object*). For example, `GRANT EXECUTE ON MODEL system.ai.databricks-claude-sonnet-4-6 TO data_scientists` explicitly names the model and the principal. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

A **GRANT policy** is an [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy that dynamically grants privileges to all securable objects whose [Governed Tags](/concepts/governed-tags.md) match a condition. The policy is attached to a catalog or schema rather than to individual objects. Unity Catalog evaluates the policy's `WHEN` condition against the tags on each securable object every time access is checked. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Key Differences

| Aspect | Direct Grant | GRANT Policy |
|--------|--------------|--------------|
| **Target identification** | Three-level namespace (*catalog.schema.object*) | Tag-based condition evaluated on objects within a scope |
| **Scope** | A single securable object (or its parent with `INHERIT`) | A catalog or schema; covers all objects matching the tag condition |
| **Condition** | None (always applies if granted) | Inline `WHEN` clause using tag functions such as `has_tag_value()` |
| **Maintenance** | A new grant is needed for every new object that should be accessible | Automatically covers new objects added with matching tags |
| **Auditability via `SHOW GRANTS`** | Yes | Not returned by `SHOW GRANTS` |
| **Supports `EXCEPT`** | No | Yes – principals can be excluded from the policy |
| **Requires a UDF** | No | No (unlike row filter and column mask policies) |
| **Purpose** | Grants access to a specific object | Grants access to all objects that meet a tag condition |

## Interaction

The effective privileges on an object are the **union** of direct grants and any applicable GRANT policies. A principal holds `EXECUTE` on a model when any of the following is true:

- A GRANT policy attached to the model's catalog or schema lists the principal in `TO` (and not in `EXCEPT`), and the policy's `WHEN` condition matches the tags on the model.
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal (including through group membership or other administrative privileges). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Because the union applies, a more selective GRANT policy does **not** guarantee that an excluded principal lacks `EXECUTE` — that principal might still hold the privilege through a direct grant on the model or its ancestors. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Auditing and Inspection

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA <schema>` (or `ON CATALOG <catalog>`) to list all GRANT policies whose scope covers models in that schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does **not** include privileges granted by a GRANT policy. To see all `EXECUTE` access on a model, combine the output of `SHOW GRANTS` with the policies returned by `SHOW EFFECTIVE POLICIES`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Use groups in `TO` and `EXCEPT`, not individual users.** This allows membership changes without editing the policy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope** that covers the intended securables. A broader scope may unintentionally grant access to unrelated objects. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Don't mix GRANT policies and direct grants for the same privilege.** Mixing makes it harder to reason about who has access and to audit changes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`; use GRANT policies for `EXECUTE`.** GRANT policies do not grant prerequisite permissions, so those must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations of GRANT Policies (Beta)

- Only the `EXECUTE` privilege on models is supported. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- A policy can be attached only at the catalog or schema level, not to an individual model. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Models with GRANT policies cannot be shared via [Delta Sharing](/concepts/delta-sharing.md). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) (restrict content; differ from GRANT policies that determine access)
- EXECUTE privilege
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md)
- [GRANT Policy for Models (Beta)](/concepts/grant-policies-beta.md)
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
