---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04bb8c07c5024e0787f8112f48afa1d8ad992a74dc009c50bfa43aa500a4971f
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-privileges-and-ownership
    - Ownership and Unity Catalog Privileges
    - UCPAO
    - Unity Catalog privilege hierarchy
    - Unity Catalog privileges (CREATE RECIPIENT, USE RECIPIENT)
    - Unity Catalog privileges reference
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Privileges and Ownership
description: Grant-based model controlling who can access what on securable objects using a hierarchical permission system with privilege inheritance.
tags:
  - unity-catalog
  - permissions
  - privileges
timestamp: "2026-06-19T21:54:45.181Z"
---

# Unity Catalog Privileges and Ownership

**Unity Catalog Privileges and Ownership** form the foundational access control model in [Unity Catalog](/concepts/unity-catalog.md), determining *who* can access *what* securable objects through grants on the object hierarchy. This model works alongside [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md), [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md), and [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) to enforce secure, fine-grained access across a Databricks data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Privileges and ownership control access using grants on securable objects. The [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md) defines how privileges are inherited from parent to child objects, and ownership determines who can manage and transfer control of objects. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Key Concepts

### Object Hierarchy and Privilege Inheritance

Unity Catalog organizes securable objects in a hierarchy — from [Metastore](/concepts/metastore.md) down to catalog, schema, table, and view. Privileges granted on a parent object are inherited by its child objects, simplifying administration. Understanding this hierarchy is essential for designing an effective permission strategy. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Ownership

Ownership is a special privilege that grants full control over a securable object. The owner can manage permissions, alter the object, and transfer ownership to another principal. Ownership is distinct from other privileges and carries administrative authority over the object. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Privileges Reference

Unity Catalog provides a comprehensive set of privileges that can be granted on different securable objects. These include:

- **Read privileges** such as `SELECT`, `READ_METADATA`, and `BROWSE`
- **Write privileges** such as `MODIFY`, `CREATE`, and `WRITE`
- **Administrative privileges** such as `OWNERSHIP`, `ALL_PRIVILEGES`, and `MANAGE`
- **Usage privileges** such as `USAGE` on schemas and catalogs

Each privilege has specific applicability to different object types. For detailed descriptions of every privilege, see the Privileges Reference page. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Managing Privileges

### Granting and Revoking

Privileges are managed using SQL statements (`GRANT`, `REVOKE`) or through [Catalog Explorer](/concepts/catalog-explorer.md). The `GRANT` statement assigns a privilege on a securable object to a principal (user, service principal, or group). The `REVOKE` statement removes a previously granted privilege. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Inspecting Privileges

You can view current privilege assignments using the `SHOW GRANTS` SQL command or through Catalog Explorer's permissions interface. This allows administrators to audit who has access to what objects. ^[access-control-in-unity-catalog-databricks-on-aws.md]

### Access Requests

Unity Catalog supports configuring access request destinations on securable objects. When users lack access, they can request it through configured channels including email, Slack, Teams, and webhooks. This streamlines the process of granting appropriate access. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Admin Roles

Unity Catalog defines several administrative roles with different scopes:

- **Account admin** — Full administrative access across all workspaces in the account
- **Metastore admin** — Administrative access to the [Metastore](/concepts/metastore.md) and its objects
- **Workspace admin** — Administrative access within a specific workspace

These roles have elevated privileges and can manage permissions on objects within their scope. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use Privileges and Ownership

Privileges and ownership are the primary mechanism for controlling access to Unity Catalog objects. They are designed to work alongside other access control mechanisms:

- Use **privileges and ownership** to control *who* can access *what* objects
- Use **ABAC** to centralize and scale access control based on governed tags
- Use **row filters and column masks** for per-table logic when ABAC is not adopted
- Use **workspace bindings** to restrict *where* users can access data

Databricks recommends using ABAC to centralize and scale access control based on governed tags, with row filters and column masks reserved for cases requiring per-table logic. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Privileges Reference — Detailed descriptions of every privilege in Unity Catalog
- Admin Roles — Account admin, workspace admin, and [Metastore](/concepts/metastore.md) admin roles
- [Manage Privileges](/concepts/manage-privilege.md) — Grant, revoke, and inspect privileges using Catalog Explorer and SQL
- Access Requests — Configure destinations for access requests on securable objects
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Restrict which workspaces can access specific catalogs
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven, centralized access control
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Per-table row and column filtering using UDFs

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
