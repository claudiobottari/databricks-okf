---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c80af3d0a321e49f821f5e8aa47844787023b46ce00af47e1e2eed4a3eec240
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-abac-attribute-based-access-control
    - UCA(AC
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog ABAC (Attribute-Based Access Control)
description: Centralized, tag-driven policies that dynamically filter and mask data across the catalog, recommended by Databricks over per-table filters for scalability.
tags:
  - access-control
  - unity-catalog
  - abac
  - tag-based-policies
timestamp: "2026-06-19T17:24:02.860Z"
---

# Unity Catalog ABAC (Attribute-Based Access Control)

**Unity Catalog ABAC (Attribute-Based Access Control)** is an access control model in [Unity Catalog](/concepts/unity-catalog.md) that uses governed tags and centralized policies to dynamically control what data users can access. Unlike traditional role-based access control (RBAC), ABAC evaluates access decisions based on attributes of the user, the data, and the environment at query time. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

ABAC is one of the complementary access control models in Unity Catalog. It works alongside privileges and ownership (controlling *who* can access *what*), table-level filtering and masking (controlling *what* data users see within tables), and workspace-level restrictions (controlling *where* users can access data). These models are designed to be used together to enforce secure, fine-grained access across a data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use ABAC

Databricks recommends using ABAC to centralize and scale access control based on governed tags. Row filters and column masks should be used only when per-table logic is needed or when ABAC has not yet been adopted. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## How It Works

ABAC policies are defined centrally and reference governed tags that are applied to data objects (such as tables, columns, or schemas). When a user queries data, Unity Catalog evaluates the relevant ABAC policies against the attributes of the querying principal and the target data objects. This evaluation can dynamically filter rows or mask columns without requiring per-table configuration. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Relationship to Other Access Control Mechanisms

Workspace bindings, privileges, and ABAC policies evaluate access at different levels and are designed to be used together. The following table summarizes when each mechanism is appropriate:

| Mechanism | Purpose |
|-----------|---------|
| Privileges and ownership | Control *who* can access *what* using grants on securable objects |
| Attribute-based policies (ABAC) | Control *what* data users can access using governed tags and centralized policies |
| Row filters and column masks | Control *what* data users can see within tables using table-specific filters and views |
| Workspace-level restrictions | Control *where* users can access data by limiting objects to specific workspaces |

^[access-control-in-unity-catalog-databricks-on-aws.md]

## Key Benefits

- **Centralized management:** Policies are defined once and applied across the catalog, reducing per-table configuration overhead.
- **Dynamic evaluation:** Access decisions are computed at query time based on current user and data attributes.
- **Scalability:** Tag-driven policies scale across thousands of tables without manual per-object grants.
- **Tag-driven governance:** Leverages governed tags, which are managed through [Unity Catalog](/concepts/unity-catalog.md)'s tagging system.

## Related Concepts

- [Privileges and Ownership in Unity Catalog](/concepts/privileges-and-ownership.md) – Controls *who* can access *what* using grants on securable objects.
- [Row Filters and Column Masks in Unity Catalog](/concepts/row-filters-and-column-masks.md) – Per-table row and column filters using UDFs.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) – Workspace-level restrictions on data access.
- [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md) – The underlying object model that privileges, policies, and tags operate on.
- [Governed Tags in Unity Catalog](/concepts/governed-tags-in-unity-catalog.md) – Tags used by ABAC policies to drive access decisions.
- [Databricks Catalog Explorer](/concepts/catalog-explorer.md) – UI tool for managing privileges, policies, and tags.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
