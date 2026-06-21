---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d1426862a11774402123d06d382b06a778f6169c5345671340873be46176f661
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - privileges-and-ownership-model
    - Ownership Model and Privileges
    - PAOM
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Privileges and Ownership Model
description: Controls who can access what objects in Unity Catalog through grants on securable objects, with a hierarchy of privileges from account-level to table-level.
tags:
  - unity-catalog
  - privileges
  - ownership
timestamp: "2026-06-19T13:50:36.120Z"
---

# Privileges and Ownership Model

The **Privileges and Ownership Model** is a fundamental access control mechanism in [Unity Catalog](/concepts/unity-catalog.md) that governs *who* can access *what* data objects. It uses grants on securable objects to control permissions across the data platform.

## Overview

Privileges and ownership form one of four complementary access control models in Unity Catalog, alongside attribute-based policies ([ABAC](/concepts/abac-attribute-based-access-control.md)), [Table-Level Filtering and Masking](/concepts/table-level-filtering-and-masking.md), and [Workspace-Level Restrictions](/concepts/workspace-level-restrictions.md). These models work together to enforce secure, fine-grained access across your data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## How It Works

The privileges and ownership model controls access by granting specific permissions on [securable objects](/concepts/unity-catalog-securable-objects.md) to users, groups, or service principals. Ownership determines who can manage and delegate access to each object. ^[access-control-in-unity-catalog-databricks-on-aws.md]

Key concepts include:

- **Securable objects** — The objects in the Unity Catalog hierarchy (catalogs, schemas, tables, views, etc.) that can have privileges granted on them.
- **Privileges** — Specific permissions (such as SELECT, MODIFY, CREATE, USAGE) that control what actions a principal can perform on an object.
- **Inheritance** — Privileges granted on parent objects (e.g., a catalog) flow down to child objects (e.g., schemas and tables within that catalog), unless explicitly overridden.
- **Ownership** — The principal that owns an object has full control over it, including the ability to grant and revoke privileges to other principals.

## Privilege Inheritance

Privileges in Unity Catalog follow a hierarchical inheritance model. When a privilege is granted on a parent object, all child objects inherit that privilege by default. For example, granting USAGE on a catalog allows access to all schemas and tables within that catalog. This inheritance reduces administrative overhead by allowing broad grants at higher levels of the object hierarchy. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Relationship to Other Access Control Models

The privileges and ownership model is designed to work alongside other access control mechanisms:

| Mechanism | What It Controls | When to Use |
|-----------|-----------------|-------------|
| Privileges and ownership | Who can access what objects | Foundation of all access control |
| [ABAC](/concepts/abac-attribute-based-access-control.md) | What data users can access, using tags and policies | Centralized, scalable access control |
| [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) | What data users see within tables | Per-table logic or when ABAC is not adopted |
| [Workspace-Level Restrictions](/concepts/workspace-level-restrictions.md) | Where users can access data | Limiting objects to specific workspaces |

Databricks recommends using [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) to centralize and scale access control based on governed tags. Use row filters and column masks only when you need per-table logic or haven't adopted ABAC yet. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Managing Privileges

Privileges can be managed through:

- **Catalog Explorer** — A graphical interface for granting, revoking, and inspecting privileges on Unity Catalog objects.
- **SQL commands** — Using `GRANT`, `REVOKE`, and `SHOW GRANTS` statements directly.

For complete details on all available privileges, see the privileges reference. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Admin Roles

Unity Catalog defines several administrative roles that have elevated privileges:

- **Account admin** — Manages the entire Databricks account, including metastores and billing.
- **Workspace admin** — Manages workspace-level settings and permissions.
- **Metastore admin** — Manages the Unity Catalog [Metastore](/concepts/metastore.md) and can grant privileges on objects within it.

These roles are described in detail in the admin roles documentation. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md) — The structure of securable objects and how privilege inheritance flows between them.
- ABAC policies — Attribute-based access control for centralized, tag-driven data governance.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Restricting which workspaces can access specific catalogs.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Per-table data filtering using UDFs.
- Access requests — Configuring destinations for access requests on securable objects.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
