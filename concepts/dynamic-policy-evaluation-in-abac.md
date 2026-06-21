---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 57ab211af953ce30920e7b57fe47ae88eb109a5b02b008206c7b0edfcfed803f
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-policy-evaluation-in-abac
    - DPEIA
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Dynamic Policy Evaluation in ABAC
description: ABAC policies evaluate at query time based on user identity, group memberships, and object tags, making transparency a challenge
tags:
  - data-governance
  - abac
  - policy-design
  - unity-catalog
timestamp: "2026-06-19T22:13:29.950Z"
---

# Dynamic Policy Evaluation in ABAC

**Dynamic policy evaluation** is a core characteristic of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) in [Unity Catalog](/concepts/unity-catalog.md) where access rules are determined at query time based on attributes rather than being statically attached to a specific table or view. ABAC policies are attached at a level in the Unity Catalog hierarchy—such as a catalog, schema, or table—and are evaluated dynamically when a securable object carries the [Governed Tags](/concepts/governed-tags.md) targeted by the policy. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md, best-practices-for-abac-policies-databricks-on-aws.md]

## How Dynamic Evaluation Works

When a user queries a table, ABAC policies in the table's scope are evaluated using three inputs:

1. The **user's identity and group memberships** (e.g., which roles or groups the user belongs to).
2. The **tags on the data object** (e.g., `sensitivity = confidential`).
3. The **policy conditions** defined in the ABAC policy (row filter, column mask, or GRANT policy).

If the object's tags match the conditions defined in the policy, that policy takes effect automatically. A single policy defined at the catalog or schema level can enforce consistent access rules across all objects in that scope, without needing to attach the policy to each individual table. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md, best-practices-for-abac-policies-databricks-on-aws.md]

## Dynamic vs. Static Policies

Unlike table-level [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md), which are directly visible on the table definition and apply equally to all queries, ABAC policies are not attached to individual tables. They evaluate at query time based on the user's identity and group memberships, and the tags on the data object in the policy scope. This means the same table can produce different access outcomes for different users and at different times as tags change, without any modification to the table schema. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Challenges

Because ABAC policies are not directly visible on the table definition, data consumers and table owners may not immediately know which access rules apply to a given table. The same table may be subject to different policies depending on the tags it carries, and those tags may be inherited or overridden at different levels of the catalog hierarchy. This opacity can lead to confusion, especially in environments where multiple teams manage tagging and access rules independently. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices for Managing Dynamic Policies

To mitigate the challenges of dynamic policy evaluation, Databricks recommends the following practices: ^[best-practices-for-abac-policies-databricks-on-aws.md]

- **Use [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies)** to determine which ABAC policies apply to a specific table or schema. This command returns the union of policies defined on the table and any inherited from parent scopes.
- **Document your tagging taxonomy, policies, and group management approach** so that teams can understand the governance model without inspecting each policy individually. Good documentation reduces the surprise factor of dynamic evaluation.
- **When transparency is critical for a specific table**, consider using table-level row filters and column masks for that isolated case instead of relying solely on ABAC policies. These static filters are visible in the table definition and behave predictably, though care must be taken to address possible conflicts with existing ABAC policies.

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
