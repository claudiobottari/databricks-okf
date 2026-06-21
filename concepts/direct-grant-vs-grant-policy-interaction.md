---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 469db028e2c8e5bc9bea66834fb48b5b3fd0fe9bd4bf9d74ae788503e140b531
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - direct-grant-vs-grant-policy-interaction
    - DGVGPI
    - Direct Grants vs. GRANT Policies
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Direct Grant vs GRANT Policy Interaction
description: The effective privileges on an object are the union of direct grants and applicable GRANT policies; mixing both for the same privilege complicates reasoning about access.
tags:
  - unity-catalog
  - access-control
  - abac
  - databricks
timestamp: "2026-06-18T10:36:02.120Z"
---

# Direct Grant vs GRANT Policy Interaction

In Unity Catalog, the effective privileges on a securable object are determined by the union of direct grants and any applicable GRANT policies. Understanding how these two mechanisms interact is essential for designing a coherent access control strategy. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## How Interaction Works

A principal holds a privilege (such as `EXECUTE`) on a model when **any** of the following conditions is true:

- A [GRANT Policy](/concepts/grant-policies-beta.md) attached to the model's catalog or schema lists the principal in its `TO` clause (and not in `EXCEPT`), and the policy's `WHEN` condition matches the tags on the model.
- A direct `GRANT` statement on the model, its parent schema, or its parent catalog is in effect for that principal — whether granted directly to the principal, through group membership, or through other administrative privileges. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

Because access is the union of these sources, a more selective GRANT policy does **not** mean that an excluded principal lacks the privilege. The principal can still hold the privilege through a direct grant on the model, or on its parent schema or catalog. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Determining Effective Privileges

If you intend to use GRANT policies as the primary way to control `EXECUTE` on models, first determine whether any direct grants already in place might override the policy: ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA <parent_schema>` (or `ON CATALOG <parent_catalog>`) to list every GRANT policy whose scope covers the models in that schema or catalog. `SHOW EFFECTIVE POLICIES` does **not** support `ON MODEL` directly. The equivalent REST API is `GET /api/2.1/unity-catalog/policies/{on_securable_type}/{on_securable_fullname}?include_inherited=true` (Python SDK: `w.policies.list_policies(..., include_inherited=True)`). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

- Use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. The equivalent REST API for direct grants on a securable object is `GET /api/2.1/unity-catalog/permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get(...)`). For the union of direct and inherited grants, use `GET /api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}` (Python SDK: `w.grants.get_effective(...)`). ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Key Differences Between Direct Grants and GRANT Policies

| Aspect | Direct Grant | GRANT Policy |
|---|---|---|
| **Targeting** | Identifies objects by three-level namespace (`catalog.schema.object`) | Identifies objects dynamically by matching governed tags on the object |
| **Scope** | Can be applied at the object, schema, or catalog level | Attached at the catalog or schema level (Beta limitation) |
| **Maintenance** | Requires one statement per object; must be re-issued when new objects are added | Single policy covers all matching objects automatically |
| **Visibility** | Visible in `SHOW GRANTS` output | **Not** visible in `SHOW GRANTS` output; shown via `SHOW EFFECTIVE POLICIES` |
| **Conditional logic** | No condition — privilege applies unconditionally | `WHEN` condition based on governed tags or system tags |

## Best Practices for Using Both Mechanisms

### Use Groups in Policies, Not Individual Users

Adding or removing users from a group named in a policy changes who the policy applies to, without editing the policy itself. Groups should be used in both `TO` and `EXCEPT` clauses of GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Use Separate Mechanisms for Different Privileges

Use direct grants for `USE CATALOG` and `USE SCHEMA` — the prerequisite permissions required to reach a model. Use GRANT policies for `EXECUTE` on individual models by tag. GRANT policies do not grant the `USE` privileges needed to access a model, so those must always be handled through direct grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Avoid Mixing GRANT Policies and Direct Grants for the Same Privilege

For a given privilege on a securable, choose either GRANT policies or direct grants, not both. GRANT policies union with direct grants, so mixing them on the same securable makes it harder to reason about who has access and to audit changes. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Use Direct Grants for Non-Supported Operations

GRANT policies in Beta only support the `EXECUTE` privilege on models. Operations such as `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` are not supported by GRANT policies and must be granted directly. Similarly, the prerequisite permissions `USE SCHEMA` and `USE CATALOG` must be granted directly. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Example: GRANT Policy vs Direct Grants

The following GRANT policy uses the `ai.model_creator` system tag to grant `EXECUTE` on all Anthropic-hosted foundation models in `system.ai` to `data_scientists`:

```sql
CREATE POLICY grant_anthropic_foundation_models
ON SCHEMA system.ai
COMMENT 'Grant EXECUTE on Anthropic foundation models'
TO `data_scientists`
EXCEPT `contractors`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('ai.model_creator', 'anthropic');
```

The equivalent access using direct grants requires one statement per model, reissued as Databricks adds new Anthropic models:

```sql
GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-sonnet-4-6` TO `data_scientists`;
GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-opus-4-7` TO `data_scientists`;
GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-haiku-4-5` TO `data_scientists`;
```

Even when the GRANT policy is in place, if a direct grant exists on a model (for example, to a specific user), that user retains `EXECUTE` regardless of the policy's tag conditions or `EXCEPT` clause. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations of GRANT Policies

- `SHOW GRANTS` does **not** return privileges granted by a GRANT policy. To see all `EXECUTE` access on a model, combine `SHOW GRANTS` output with the GRANT policies returned by `SHOW EFFECTIVE POLICIES`. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Deleting a model or model version is not covered by GRANT policies — these operations require direct grants. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- You cannot use [Delta Sharing](/concepts/delta-sharing.md) to share models that have GRANT policies defined on them. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- Unity Catalog ABAC — Attribute-based access control framework in Unity Catalog
- [Governed Tags](/concepts/governed-tags.md) — Tags used in GRANT policy conditions for dynamic privilege assignment
- [System Tags](/concepts/system-tags.md) — Predefined tags that can be referenced in GRANT policy conditions
- [Row Filter Policies](/concepts/row-filter-policies.md) — Related policy mechanism that restricts data content rather than object access
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full set of privileges available in Unity Catalog

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
