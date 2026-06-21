---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5b3f46436dab372a0c06b810d5f37a5611f24acc89efbf0cfcb215826f2004c
  pageDirectory: concepts
  sources:
    - attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - abac-policies-in-unity-catalog
    - APIUC
    - ABAC in Unity Catalog
  citations:
    - file: attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
    - file: when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md
title: ABAC Policies in Unity Catalog
description: Policies attached at a level in the Unity Catalog hierarchy (catalog, schema, table) that are evaluated dynamically — when a securable object has targeted attributes, the policy takes effect automatically.
tags:
  - policies
  - unity-catalog
  - access-control
timestamp: "2026-06-19T17:36:50.648Z"
---

# ABAC Policies in Unity Catalog

**ABAC (Attribute-Based Access Control) Policies in Unity Catalog** is an access control model where access decisions are determined by evaluating **attributes** associated with securable objects. These attributes are represented through [Governed Tags](/concepts/governed-tags.md) and are used in policy conditions to identify which data a policy should protect. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

In Unity Catalog, ABAC policies use attributes — represented through [Governed Tags](/concepts/governed-tags.md) — to determine access rules. Policies are attached at a level in the Unity Catalog hierarchy (such as a catalog, schema, or table) and are evaluated dynamically. When a securable object has the attributes targeted by a policy, that policy takes effect automatically, allowing a single policy to enforce consistent access rules across an entire catalog or schema. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Policy Types

ABAC supports the following policy types for granular data security:

### Row Filter Policies

Row filter policies provide row-level security on tables by filtering which rows are visible to a user based on their attributes. These policies can be applied to tables, materialized views, and streaming tables. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### Column Mask Policies

Column mask policies provide column-level security by masking or redacting sensitive column values. Like row filters, these can be applied to tables, materialized views, and streaming tables. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

### Grant Policies (Beta)

Grant policies support dynamic privilege grants. Currently scoped to `EXECUTE` on models, these policies enable fine-grained control over who can execute specific models based on their attributes. ^[attribute-based-access-control-in-unity-catalog-databricks-on-aws.md]

## Comparison with Table-Level Row Filters and Column Masks

Unity Catalog supports two approaches for row-level and column-level security: ABAC policies and [Table-Level Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md). Neither approach grants access to data on its own — both add restrictions on top of existing object-level privileges. You must grant base table access separately through object-level permissions (`GRANT`). ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

### Key Differences

The core difference is where the restrictions are defined. **Table-level row filters and column masks** apply sensitivity controls directly on individual tables using `ALTER TABLE`. Table owners manage their own data protection without needing a governed tag system. This is straightforward for a small number of tables, but each table must be configured individually, and table owners can modify or remove their own filters and masks. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

**ABAC policies** attach at the catalog, schema, or table level and match tables and columns dynamically based on governed tags. A policy defined at the catalog level applies to all tables in that catalog, and individual table owners can't remove, modify, or bypass it. The policy lives on the catalog and is evaluated by Unity Catalog before the query reaches the runtime. This lets higher-level administrators enforce organization-wide rules and ensure that lower-level administrators and owners can't circumvent them. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

### When to Use Each Approach

Use **ABAC policies** when:
- You need consistent access rules across many tables, schemas, or catalogs
- Your organization separates duties (e.g., policy authors define rules, data stewards classify data with tags)
- Your data estate is growing and you want new tables covered automatically when they are tagged
- You need the `EXCEPT` clause to allow operations like time travel, OpenSharing, or full query optimization for specific principals

Use **table-level row filters and column masks** when:
- Each table has strict, specific logic that doesn't generalize to other tables
- Table owners should manage their own filters and masks directly, without a centralized tag system
- You have a small, stable set of tables that change infrequently

^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

### Combining Both Approaches

ABAC and table-level row filters and column masks can co-exist on the same table. At query time, the policies are evaluated independently for the querying user with the following rules:
- Only one distinct row filter can apply
- Only one distinct column mask can be resolved per column

Databricks evaluates conflict by comparing the functions applied, not the data output. If both an ABAC policy and a table-level filter or mask apply the same row filter or column mask function for the same user, Databricks allows execution. If they apply different functions, Databricks blocks access and returns an error, even if those functions produce identical data output. ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

For details on conflict resolution and troubleshooting, see [Rules for multiple filters and masks](/concepts/row-filters-and-column-masks.md). ^[when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) — The mechanism for representing attributes on securable objects
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — The hierarchy of objects that can have policies attached
- [Row Filters](/concepts/row-filter-policies.md) — Row-level security policies in Unity Catalog
- Column Masks — Column-level security policies in Unity Catalog
- [Grant Policies](/concepts/grant-policies-beta.md) — Dynamic privilege grant policies (Beta)
- [Unity Catalog](/concepts/unity-catalog.md) — The overall data governance platform
- Dynamic Views — An alternative approach for row-level and column-level security
- [Table-Level Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — The table-level approach to data protection

## Sources

- attribute-based-access-control-in-unity-catalog-databricks-on-aws.md
- when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md

# Citations

1. [attribute-based-access-control-in-unity-catalog-databricks-on-aws.md](/references/attribute-based-access-control-in-unity-catalog-databricks-on-aws-23c11bc2.md)
2. [when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws.md](/references/when-to-use-abac-vs-table-level-row-filters-and-column-masks-databricks-on-aws-d92860b7.md)
