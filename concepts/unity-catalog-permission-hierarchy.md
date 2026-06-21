---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92e7a9b37b612e633a0a58beb5ad0bb18cea7fcf86a153a819c889c1e12ce289
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - unity-catalog-permission-hierarchy
    - UCPH
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Permission Hierarchy
description: Hierarchy of securable objects in Unity Catalog with privilege inheritance, where privileges on parent objects flow down to child objects.
tags:
  - unity-catalog
  - permissions
  - hierarchy
timestamp: "2026-06-19T13:50:41.725Z"
---

# Unity Catalog Permission Hierarchy

**Unity Catalog Permission Hierarchy** refers to the structured, multi-level system of privileges and access control mechanisms that govern who can access what data assets within the Databricks Unity Catalog environment. The hierarchy is organized around securable objects in a parent-child relationship, where privileges flow from higher-level objects to their descendants.

## Overview

Access control in Unity Catalog is built on four complementary models that work together to enforce secure, fine-grained access across your data environment: ^[access-control-in-unity-catalog-databricks-on-aws.md]

1. **Privileges and ownership** — control *who* can access *what*, using grants on securable objects.
2. **Attribute-based policies (ABAC)** — control *what* data users can access, using governed tags and centralized policies.
3. **Table-level filtering and masking** — control *what* data users can see within tables using table-specific filters and views.
4. **Workspace-level restrictions** — control *where* users can access data, by limiting objects to specific workspaces.

## The Object Hierarchy

Unity Catalog organizes data assets into a hierarchical structure. Privileges granted on a parent object are inherited by its child objects, simplifying administration. The hierarchy flows from broad to specific:

1. **Metastore** — The top-level container for all metadata and data assets.
2. **Catalog** — A logical container for schemas (formerly databases).
3. **Schema** — A namespace that contains tables, views, functions, and models.
4. **Tables, Views, Functions, Models** — The actual data assets and logic objects.

Privileges assigned at a higher level (e.g., a catalog) automatically apply to all contained objects (e.g., schemas and tables within that catalog), unless overridden by more specific grants. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Key Concepts

### Privileges and Ownership

Privileges are fine-grained permissions that control actions such as `SELECT`, `CREATE`, `MODIFY`, and `USAGE` on securable objects. Ownership determines who can grant privileges on an object and who bears responsibility for its management. For a complete list of privileges, see the Privileges Reference. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Privilege Inheritance

When a privilege is granted on a parent object, all child objects inherit that privilege by default. For example, granting `SELECT` on a catalog allows a user to read all tables in all schemas within that catalog. This reduces the need for repetitive grants at lower levels. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Attribute-Based Access Control (ABAC)

Databricks recommends using ABAC to centralize and scale access control based on governed tags. ABAC policies dynamically filter and mask data at query time, enabling consistent policy enforcement across the catalog without per-object grants. Use row filters and column masks only when you need per-table logic or haven't adopted ABAC yet. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Workspace-Catalog Binding

Workspace-level restrictions allow administrators to limit which workspaces can access specific catalogs, external locations, and storage credentials. This adds a location-based dimension to permission control, ensuring that data is only accessible from authorized compute environments. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use Each Access Control Mechanism

Workspace bindings, privileges, and ABAC policies evaluate access at different levels and are designed to be used together: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Privileges and Ownership** — Use for basic read/write access control on defined objects.
- **ABAC** — Use for scalable, tag-driven policies that apply across the catalog without per-table configuration.
- **Row Filters and Column Masks** — Use for per-table logic that cannot be expressed through ABAC.
- **Workspace Bindings** — Use to restrict data access based on compute location.

## Admin Roles

Unity Catalog defines several administrative roles with distinct scopes: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Account Admin** — Has full control over the entire Databricks account, including all workspaces and metastores.
- **Workspace Admin** — Manages a single workspace's settings, users, and permissions.
- **Metastore Admin** — Oversees the [Metastore](/concepts/metastore.md), catalogs, and global data governance settings.

Each role has different capabilities and responsibilities for managing the permission hierarchy.

## Managing Access

Administrators manage privileges using [Catalog Explorer](/concepts/catalog-explorer.md) and SQL commands (`GRANT`, `REVOKE`, `SHOW GRANTS`). For detailed guidance, see [Manage Privileges](/concepts/manage-privilege.md). ^[access-control-in-unity-catalog-databricks-on-aws.md]

Access requests can be configured to route through email, Slack, Teams, or webhooks, enabling self-service workflows for data access. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Privileges Reference — Complete list of all Unity Catalog privileges.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven dynamic access policies.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Per-table data masking and filtering.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Restricting catalog access by workspace.
- [Metastore Admin](/concepts/metastore-admin-role.md) — Role responsible for managing the top-level Unity Catalog object.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI tool for managing Unity Catalog objects and permissions.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
