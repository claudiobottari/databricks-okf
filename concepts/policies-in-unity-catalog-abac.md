---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c5fcbbfe376897207ee5f1d7a9415016b54d2c23ee68076f017f70299339c6e
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policies-in-unity-catalog-abac
    - PIUCA
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: Policies in Unity Catalog ABAC
description: Reusable access rule definitions attached to catalog, schema, or table levels that dynamically evaluate governed tags to determine access
tags:
  - access-control
  - policy-management
  - unity-catalog
timestamp: "2026-06-19T22:08:32.692Z"
---

```markdown
# Policies in Unity Catalog ABAC

In [[Attribute-Based Access Control (ABAC)]] within Unity Catalog, **policies** are the mechanism that defines access rules based on attributes. A policy is attached at a level in the Unity Catalog hierarchy — such as a catalog, schema, or table — and is evaluated dynamically. When a [[Unity Catalog Securable Objects|securable object]] has the attributes targeted by a policy, that policy takes effect automatically, so a single policy can enforce consistent access rules across an entire catalog or schema. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Types of Policies

ABAC supports two primary categories of policies for fine-grained access control:

- **Row filter policies** and **column mask policies** provide row- and column-level security on tables, materialized views, and streaming tables. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]
- **GRANT policies** (Beta) support dynamic privilege grants, currently scoped to the `EXECUTE` privilege on models. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

The attributes used in policy conditions are represented through [[governed tags]], which are associated with securable objects in Unity Catalog. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How Policies Work

Policies are attached to a catalog, schema, or table, and are evaluated at runtime. When a user queries a securable object, any policies attached to that object or a parent in the hierarchy are checked. If the object’s attributes match the conditions in a policy, the policy’s access rules (e.g., row filtering or column masking) are applied automatically. This dynamic evaluation means that a single policy can protect many objects across a catalog or schema without needing to be recreated for each one. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [[Attribute-Based Access Control (ABAC)]] — the overall access control model in Unity Catalog.
- [[Governed Tags]] — the attribute representation used in policy conditions.
- [[ABAC Row Filter Policy|Row Filter Policy]] — a policy type for row-level security.
- [[Column Mask Policies|Column Mask Policy]] — a policy type for column-level security.
- [[GRANT Policies (Beta)|GRANT Policy]] — a policy type for dynamic privilege grants (Beta).
- [[Unity Catalog Securable Objects]] — the objects (catalogs, schemas, tables, models) that policies can be attached to.

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
```

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
