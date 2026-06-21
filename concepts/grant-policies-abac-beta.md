---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c8a8a447e9aa034639139ccc372a70cfefd82e54039687ea2ffa26da0e7db03
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grant-policies-abac-beta
    - GP(B
    - GRANT policies (ABAC)
    - GRANT policies|ABAC GRANT policies
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: GRANT policies (ABAC Beta)
description: A beta feature in Unity Catalog ABAC supporting dynamic privilege grants through GRANT policies, currently scoped to EXECUTE on models.
tags:
  - access-control
  - unity-catalog
  - privileges
  - beta
timestamp: "2026-06-18T10:49:05.031Z"
---

<!-- TODO: Verify Beta status and scope. Source material is limited to a single overview page; cross-reference with dedicated GRANT policy documentation if available. -->

# GRANT policies (ABAC Beta)

**GRANT policies** are an attribute‑based access control (ABAC) feature in [Unity Catalog](/concepts/unity-catalog.md) that dynamically grants privileges to securable objects based on the [Governed Tags](/concepts/governed-tags.md) attached to those objects. Instead of using static `GRANT` statements tied to a fixed object identifier, a GRANT policy defines a condition that is evaluated at access time against the tags of each securable object in the policy’s scope. Any object whose tags match the condition automatically receives the privilege.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Current scope (Beta)

GRANT policies are currently in Beta. In this release they support only the `EXECUTE` privilege on models.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How policies are attached and evaluated

Policies are attached at a level in the Unity Catalog hierarchy — a catalog, a schema, or a table — and are evaluated dynamically. When a securable object has the attributes (governed tags) targeted by a policy, that policy takes effect automatically. A single policy can therefore enforce consistent access rules across an entire catalog or schema without requiring individual grants on each object.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Relationship to other ABAC policy types

ABAC in Unity Catalog supports several policy types. Row filter policies and column mask policies provide row‑ and column‑level security on tables, materialized views, and streaming tables. GRANT policies, by contrast, provide dynamic privilege grants — they control *whether* a user can access an object (e.g., execute a model) rather than filtering the content of an object the user already has permission to access.^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The overarching access model
- [Governed Tags](/concepts/governed-tags.md) — The attributes used in policy conditions
- [Row Filter Policies](/concepts/row-filter-policies.md) — Another ABAC policy type for data filtering
- [Column Mask Policies](/concepts/column-mask-policies.md) — Another ABAC policy type for masking columns
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that hosts ABAC policies
- Securable objects — The entities (catalogs, schemas, tables, models) that policies protect

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
