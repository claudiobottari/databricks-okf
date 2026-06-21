---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af747feec28a41f2df40208278d7ddcf965a5f08b119bffcd5405de12d0df9e0
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policies-abac
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: Policies (ABAC)
description: Core mechanism in Unity Catalog ABAC that uses governed tag attributes in conditions to determine access; attached at catalog, schema, or table level and evaluated dynamically.
tags:
  - access-control
  - unity-catalog
  - policies
timestamp: "2026-06-18T10:48:50.176Z"
---

# Policies (ABAC)

**ABAC policies** are rules in Unity Catalog that use [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) to determine access to data and AI assets. These policies evaluate **attributes** associated with [securable objects](/concepts/unity-catalog-securable-objects.md) — represented through [Governed Tags](/concepts/governed-tags.md) — to identify which data a policy should protect and how access should be restricted or granted.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How ABAC Policies Work

Policies are attached at a level in the Unity Catalog hierarchy, such as a catalog, schema, or table, and are evaluated dynamically. When a securable object has the attributes targeted by a policy, that policy takes effect automatically. This means a single policy can enforce consistent access rules across an entire catalog or schema without requiring individual grants on each object.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Types of ABAC Policies

Unity Catalog supports three types of ABAC policies, each serving a different purpose in the access control model:^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### Row Filter Policies

[Row Filter Policies](/concepts/row-filter-policies.md) restrict the rows of data a user can see when querying a table, materialized view, or streaming table. These policies apply a filter condition that limits which rows are returned based on the user's attributes or other criteria.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### Column Mask Policies

[Column Mask Policies](/concepts/column-mask-policies.md) control the visibility of sensitive columns by applying a masking function that transforms the data returned to the user. These policies are applied to tables, materialized views, and streaming tables.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### GRANT Policies (Beta)

[GRANT policies](/concepts/abac-grant-policy.md) dynamically grant Unity Catalog privileges to securable objects whose governed tags match a specified condition. These policies are currently in Beta and support only the `EXECUTE` privilege on models. Unlike row filter and column mask policies, GRANT policies determine whether a user can access the object at all, rather than restricting the content of data the user can already access.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md, abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Policy Evaluation

When a user attempts to access a securable object, Unity Catalog evaluates all applicable policies attached to that object and its ancestors in the catalog hierarchy. The effect is dynamic — if a securable object's tags change, the policies that apply to it may change as well, without any administrative action.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Differences Between Policy Types

Row filter and column mask policies restrict the content of data a user can already access, whereas GRANT policies determine whether the user can access the object at all. Additionally, row filter and column mask policies require a user-defined function (UDF) to implement the filter or mask, while GRANT policies express conditions inline in the policy definition.^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Best Practices

- **Attach policies at the smallest scope** that covers the target securable objects. Use the narrowest level in the catalog hierarchy that contains all objects the policy should apply to.
- **Use governed tags** to categorize securable objects consistently so that policies can target the right objects automatically.
- **Leverage tag inheritance** by applying default tag values at the parent catalog or schema so descendants inherit them. Override inherited tags only on specific objects that need different values.

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model that policies enforce
- [Governed Tags](/concepts/governed-tags.md) — The attributes used in policy conditions
- [System Tags](/concepts/system-tags.md) — Predefined tags provided by Databricks
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data rows
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — ABAC policies that dynamically grant privileges
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform providing ABAC capabilities

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- abac-grant-policies-for-models-beta-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
