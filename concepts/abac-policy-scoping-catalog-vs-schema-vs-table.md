---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: acf9eb606549f3d5e48320f896ae20594ed2a4c55cf40b5b1e364365248a7597
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-scoping-catalog-vs-schema-vs-table
    - APS(VSVT
  citations:
    - file: best-practices-for-abab-policies-databricks-on-aws.md
    - file: abac-grant-policies-for-models-beta-databricks-on-aws.md
title: ABAC Policy Scoping (Catalog vs Schema vs Table)
description: Attaching ABAC policies at the highest applicable scope (catalog or schema) rather than table level to maximize reuse and simplify management.
tags:
  - abac
  - policy-design
  - unity-catalog
timestamp: "2026-06-18T14:32:29.859Z"
---

Here is the wiki page for "ABAC Policy Scoping (Catalog vs Schema vs Table)", written based solely on the provided source material.

---

## ABAC Policy Scoping (Catalog vs Schema vs Table)

**ABAC Policy Scoping** refers to the best practice of attaching [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies—including both [row filter](/concepts/row-filter-policies.md) / [column mask](/concepts/column-mask-policies.md) policies and [ABAC GRANT policies](/concepts/abac-grant-policy.md)—at the highest possible level within the [Unity Catalog](/concepts/unity-catalog.md) three-level namespace (`catalog.schema.object`) to simplify governance and reduce the number of access control rules.

## Best Practice: Attach at the Highest Applicable Scope

ABAC policies should be defined at the **catalog or schema level** whenever possible. Table-level policies are rare and should be the exception. ^[best-practices-for-abab-policies-databricks-on-aws.md]

- **Catalog-scoped** policies evaluate against all tables and securable objects in that catalog.
- **Schema-scoped** policies evaluate against all tables and securable objects in that schema.
- Policies scoped at a higher level are automatically inherited by all children within that scope, provided their [Governed Tags](/concepts/governed-tags.md) match the policy's conditions.

When new tables are added to a catalog or schema, any existing policies attached at that parent level can automatically apply to the new tables, as long as the table's tags match the policy's conditions. This eliminates the need to grant a separate policy on each individual table. ^[best-practices-for-abab-policies-databricks-on-aws.md]

## Why Scoping Matters

Attaching policies at the **catalog** or **schema** level (rather than the **table** level) provides two key benefits: ^[best-practices-for-abab-policies-databricks-on-aws.md]

- **Automatic coverage.** When a new table is created inside a catalog or schema that already has a policy attached, that policy can apply to the new table immediately, without requiring a separate policy creation or explicit grant.
- **Reduced management overhead.** A single catalog- or schema-level policy can govern many tables at once, avoiding ABAC Policy Sprawl|policy sprawl and the complexity of managing dozens of individual table-level policies.

## Scoping for ABAC GRANT Policies

For [ABAC GRANT policies](/concepts/abac-grant-policy.md) (which dynamically grant `EXECUTE` on models), the policy can only be attached to the **catalog** or the **schema**, not directly to the model. This limitation means that a GRANT policy covers all models in its scope that match its `WHEN` condition, but model-level scoping is not available in the current release. ^[abac-grant-policies-for-models-beta-databricks-on-aws.md]

## Scoping for Row Filter and Column Mask Policies

Row filter and column mask policies are typically scoped at the **table** level. However, even for these, the recommendation is to use the `TO` and `EXCEPT` clauses within the policy definition to target principals, rather than creating a separate UDF (user-defined function) for each distinct group of users. This keeps the UDF logic simple and reduces policy count. ^[best-practices-for-abab-policies-databricks-on-aws.md]

## Scope and Tags

The tag on an object is what determines whether a policy applies, not the policy's parent scope. A catalog-level policy evaluates against every table in that catalog, but only applies to those tables whose tags match the policy's conditions. Similarly, a schema-level policy evaluates against every table in that schema. Tags are the mechanism that links the policy to the object. ^[best-practices-for-abab-policies-databricks-on-aws.md]

The key exception is when a tag is inherited from the parent object. If a schema is tagged, all tables in that schema inherit that tag, and a policy that matches on that tag will apply to all of them. ^[best-practices-for-abab-policies-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that provides the namespace for policy scoping
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model that uses tags and policies
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Grant policies that dynamically grant `EXECUTE` on models based on tags
- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data content based on a UDF
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- ABAC Policy Sprawl — The risk of creating too many policies, which ABAC scoping practices help avoid
- [Governed Tags](/concepts/governed-tags.md) — The tag mechanism that links policies to objects
- [Tag Inheritance](/concepts/tag-inheritance.md) — How tags propagate from parent to child objects in Unity Catalog

## Sources

- best-practices-for-abab-policies-databricks-on-aws.md

# Citations

1. best-practices-for-abab-policies-databricks-on-aws.md
2. [abac-grant-policies-for-models-beta-databricks-on-aws.md](/references/abac-grant-policies-for-models-beta-databricks-on-aws-49466796.md)
