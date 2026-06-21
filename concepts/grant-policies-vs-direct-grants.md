---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 045874c9691e38258aec20002b6e1b123ff245e179be71355df7d2d5eb238010
  pageDirectory: concepts
  sources:
    - abac-grant-policies-for-models-beta-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policies-vs-direct-grants
    - GPVDG
  citations:
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: GRANT Policies vs Direct Grants
description: The interaction model between dynamic tag-based GRANT policies and explicit direct grants, where effective privileges are the union of both mechanisms.
tags:
  - data-governance
  - access-control
  - unity-catalog
  - permissions
timestamp: "2026-06-19T17:23:22.256Z"
---

# GRANT Policies vs Direct Grants

GRANT policies and direct grants are two mechanisms in [Unity Catalog](/concepts/unity-catalog.md) for granting privileges on securable objects. They differ in how they identify target objects, how they are evaluated, and how they interact.

## What Is a Direct Grant?

A direct grant is an explicit `GRANT` statement that assigns a privilege on a specific securable object identified by its three-level namespace (`catalog.schema.object`). For example:

```sql
GRANT EXECUTE ON MODEL `system`.`ai`.`databricks-claude-sonnet-4-6` TO `data_scientists`;
```

Direct grants must be issued for each object individually. When new objects are added (for example, new foundation models in `system.ai`), a separate grant statement is required for each one.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## What Is a GRANT Policy?

A GRANT policy is an [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy that dynamically grants Unity Catalog privileges to securable objects whose governed tags match a condition expressed in the policy. Unity Catalog evaluates the policy’s `WHEN` condition against the governed tags on every securable object in the policy’s scope each time access is checked. The privilege is granted on every object that matches.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

In Beta, GRANT policies support only one privilege on one securable type: `EXECUTE` on models (both customer-registered MLflow models and Databricks-hosted foundation models in `system.ai`). The policy can be attached only at the catalog or schema level, not on the model itself.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

The following policy grants `EXECUTE` on all models in `production.ml_models` that carry the governed tag `lifecycle = 'production'` to the `analysts` group:

```sql
CREATE POLICY grant_production_model_access
ON SCHEMA production.ml_models
TO `analysts`
GRANT EXECUTE FOR MODELS
WHEN has_tag_value('lifecycle', 'production');
```

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Key Differences

| Aspect | Direct Grants | GRANT Policies |
|--------|---------------|----------------|
| Object identification | Explicit three-level name (`catalog.schema.object`) | Dynamic tag-based condition evaluated on all objects in scope |
| Maintenance effort | Requires separate grant per object | One policy covers all matching objects automatically |
| Update behavior | New objects need new grants | New objects that match the condition are covered automatically |
| Scope | Can be granted on model, schema, or catalog | Attached only at catalog or schema (not model) |
| Supported privileges in Beta | All privileges | Only `EXECUTE` on models |

^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Interaction Between the Two

The effective privileges on a model are the **union** of direct grants and GRANT policies. A principal holds `EXECUTE` on a model if:

- A GRANT policy attached to the model’s catalog or schema lists the principal in `TO` (and not in `EXCEPT`) **and** the policy’s `WHEN` condition matches the tags on the model, **or**
- A direct `GRANT EXECUTE` on the model, its schema, or its catalog is in effect for that principal, whether granted directly, through group membership, or through other administrative privileges.

Because access is the union, a more selective GRANT policy does **not** mean that an excluded principal lacks `EXECUTE` — the principal may still hold the privilege through a direct grant on the model or one of its ancestors.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

### Determining Effective Access

To understand who has `EXECUTE` on models in a schema or catalog:

- Use `SHOW EFFECTIVE POLICIES ON SCHEMA <schema>` (or `ON CATALOG <catalog>`) to list every GRANT policy whose scope covers the models.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Use `SHOW GRANTS` on the model and its ancestors to enumerate direct grants. For the union of direct and inherited grants, query the effective permissions API (`/api/2.1/unity-catalog/effective-permissions/{securable_type}/{full_name}`).^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

`SHOW GRANTS` does **not** include privileges granted via a GRANT policy.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Do not mix GRANT policies and direct grants for the same privilege.** Because the effective access is the union, mixing them on the same securable makes it harder to reason about who has access and to audit changes.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use direct grants for `USE CATALOG` and `USE SCHEMA`.** GRANT policies cannot grant these prerequisite permissions. Use a direct grant for `USE` privileges on the [Catalog and Schema](/concepts/catalog-and-schema.md), and use a GRANT policy to scope `EXECUTE` on individual models by tag.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Use groups in `TO` and `EXCEPT`, not individual users.** This simplifies maintenance when personnel change.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- **Attach policies at the smallest scope that covers the targets.** A broader scope may unintentionally grant access to unrelated objects.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Limitations of GRANT Policies (Beta)

- Only the `EXECUTE` privilege on models is supported. `CREATE MODEL`, `CREATE MODEL VERSION`, and `APPLY TAG` must be granted directly.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Policies can be attached only to a catalog or schema, not to a model directly.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `SHOW GRANTS` does not return privileges granted by a GRANT policy.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- `INFORMATION_SCHEMA` does not include GRANT policies.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Deleting a model or model version is not covered by GRANT policies.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]
- Models with GRANT policies defined on them cannot be shared via [Delta Sharing](/concepts/delta-sharing.md).^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)
- [MLflow Models in Unity Catalog](/concepts/models-in-unity-catalog.md)
- [Foundation Models in Unity Catalog](/concepts/models-in-unity-catalog.md)

## Sources

- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
