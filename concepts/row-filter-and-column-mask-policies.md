---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f2c1ba247a2a9b30ef7386a3593e43ee8bf60d21fd969c5bfc64fbd3e5e04af
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - row-filter-and-column-mask-policies
    - Column Mask Policies and Row Filter
    - RFACMP
    - ABAC row filter and column mask policies
    - Quotas for Row Filter and Column Mask Policies
    - Row Filter and Column Mask Policy
    - Create and Manage Row Filter and Column Mask Policies
    - Create and manage row filter and column mask policies
    - Performance Considerations for Row Filter and Column Mask Policies
    - Row Filter and Column Mask Policy Evaluation
    - Row Filter and Column Mask Policy Evaluation and Runtime Behavior
    - Row Filters and Column Masks (ABAC)|row filter and column mask policies
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
title: Row Filter and Column Mask Policies
description: ABAC-supported policy types for row and column-level security on tables, materialized views, and streaming tables in Unity Catalog.
tags:
  - security
  - unity-catalog
  - data-filtering
timestamp: "2026-06-19T17:36:09.428Z"
---

# Row Filter and Column Mask Policies

**Row Filter Policies** and **Column Mask Policies** are two types of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in [Unity Catalog](/concepts/unity-catalog.md) that implement row-level and column-level security on data objects. They allow access to be restricted or transformed based on attributes from [Governed Tags](/concepts/governed-tags.md) or other context, rather than granting direct permissions per user or group. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Supported Objects

Both policy types can be applied to the following securable objects within Unity Catalog:

- **Tables**
- **Materialized Views**
- **Streaming Tables**

^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## How They Work

Row filter policies control which rows a user can see by evaluating attributes on the data or session variables. Column mask policies control what value is returned for a column, often by obfuscating the original value. Both are defined as SQL functions and are attached to a specific securable object (catalog, schema, or table). When a query accesses the object, the policy is evaluated dynamically based on the requesting principal’s attributes. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The overarching access control model that evaluates attributes to enforce policies.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform where these policies are defined and attached.
- [Governed Tags](/concepts/governed-tags.md) — The attribute source used in policy conditions.
- Securable Objects — The entities (catalog, schema, table, etc.) to which policies can be attached.

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
