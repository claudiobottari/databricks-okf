---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 58cd80f9d5d004e348b465afd54f677dbda3cfd2be3de14b32546420d7061ebd
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-level-restrictions
    - Workspace-level access control
    - workspace permissions
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Workspace-Level Restrictions
description: Control over where users can access data by binding securable objects like catalogs and external locations to specific workspaces.
tags:
  - unity-catalog
  - access-control
  - workspace-binding
timestamp: "2026-06-18T10:36:25.256Z"
---

# Workspace-Level Restrictions

**Workspace-level restrictions** control *where* users can access data by limiting securable objects — such as catalogs, schemas, external locations, and storage credentials — to specific workspaces within a Unity Catalog [Metastore](/concepts/metastore.md). ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Workspace-level restrictions are one of four complementary access control models in Unity Catalog, alongside privileges and ownership, [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md), and table-level filtering and masking. ^[access-control-in-unity-catalog-databricks-on-aws.md]

While privileges determine *who* can access *what*, and ABAC policies determine *what data* users can access based on tags, workspace-level restrictions determine *which workspaces* can access specific objects. This allows administrators to enforce data isolation between workspaces, even within the same [Metastore](/concepts/metastore.md). ^[access-control-in-unity-catalog-databricks-on-aws.md]

## How Workspace Binding Works

A [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) attaches a workspace to a catalog, external location, or storage credential. Once bound, only that workspace can access the object. Objects that are not bound to a workspace are accessible from all workspaces in the [Metastore](/concepts/metastore.md) by default. ^[access-control-in-unity-catalog-databricks-on-aws.md]

Workspace bindings evaluate access at the object level, independently from privileges and ABAC policies. All three mechanisms work together to enforce secure, fine-grained access across your data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use Workspace Restrictions

Workspace-level restrictions are appropriate when:

- You need to isolate data for specific teams or projects to dedicated workspaces.
- You want to prevent certain workspaces from accessing sensitive catalogs or external storage.
- Compliance or data governance requirements mandate strict separation of data access by workspace.

They are designed to be used alongside other access control mechanisms. For example, you might bind a catalog to a specific workspace, then use privileges and ABAC policies within that workspace to further control access to individual objects. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Comparison with Other Mechanisms

| Mechanism | Controls | Scope | Evaluated |
|---|---|---|---|
| **Workspace bindings** | *Where* users can access data | Catalogs, external locations, storage credentials | Per workspace |
| **Privileges/ownership** | *Who* can access what | All securable objects | Per principal |
| **ABAC policies** | *What* data users can access | Tagged objects | Per object at access time |
| **Row/column filters** | *What* data users see within tables | Table rows/columns | Per query |

These mechanisms evaluate access at different levels and are designed to be used together. No single mechanism replaces the others. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — The mechanism for attaching workspaces to catalogs
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides workspace-level restrictions
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven access control that complements workspace restrictions
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The permissions model that controls *who* can access objects
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Table-level data filtering and masking

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
