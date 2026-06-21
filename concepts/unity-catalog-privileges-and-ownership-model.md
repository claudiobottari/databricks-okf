---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60402f73434a61070471122d667ef93e9f4af0fea91b19b1fe949dc2692a9794
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-privileges-and-ownership-model
    - Ownership Model and Unity Catalog Privileges
    - UCPAOM
    - Unity Catalog Privilege Model
    - Unity Catalog Privileges#CREATE MODEL VERSION|CREATE MODEL VERSION
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Privileges and Ownership Model
description: Grant-based model controlling who can access what securable objects, with privilege inheritance through the object hierarchy.
tags:
  - access-control
  - unity-catalog
  - privileges
  - ownership
timestamp: "2026-06-19T17:23:46.573Z"
---

# Unity Catalog Privileges and Ownership Model

**Unity Catalog Privileges and Ownership Model** is the foundational access-control mechanism in [Unity Catalog](/concepts/unity-catalog.md) that governs _who_ can perform _what_ actions on securable objects. It determines access through explicit grants of privileges on objects arranged in a hierarchical namespace (catalog → schema → object), combined with ownership that conveys administrative rights over each object. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Role within Unity Catalog Access Control

Access control in Unity Catalog is built on four complementary models. The privileges and ownership model is the primary layer that controls basic access; it is complemented by:

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – tag-driven policies that dynamically filter or mask data.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) – per-table filters and views that restrict visible rows and columns.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) – restrictions on which workspaces can access specific catalogs, external locations, and storage credentials.

Together these models enforce secure, fine-grained access. Databricks recommends using ABAC to centralize and scale access control based on governed tags, and resorting to row filters and column masks only when per-table logic is required or ABAC has not yet been adopted. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Key Components

The privileges and ownership model is documented across several sub-topics within the Unity Catalog documentation:

- **Permissions concepts** – explains the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md), privilege inheritance, and how access flows from parent to child objects.
- **Privileges reference** – provides detailed descriptions of every privilege available in Unity Catalog.
- **[Admin roles](/concepts/unity-catalog-admin-roles.md)** – describes the account admin, workspace admin, and [Metastore](/concepts/metastore.md) admin roles and their scopes.
- **[Manage privileges](/concepts/manage-privilege.md)** – covers granting, revoking, and inspecting privileges using Catalog Explorer and SQL.

These resources provide the full specification of how grants, ownership, and privilege inheritance work in practice. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Using the Model

Administrators grant privileges (such as `SELECT`, `CREATE`, `MODIFY`, `READ`, `WRITE`, `EXECUTE`, etc.) on securable objects to principals (users, service principals, or groups). Ownership of an object conveys full administrative control, including the ability to grant privileges to others. Access can be further refined by combining privilege grants with workspace bindings, ABAC policies, and row/column-level filters. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Permissions concepts
- Privileges reference
- [Admin roles](/concepts/unity-catalog-admin-roles.md)
- [Manage privileges](/concepts/manage-privilege.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)
- Access requests – configurable destinations (email, Slack, Teams, webhooks) for requesting access on Unity Catalog securable objects.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
