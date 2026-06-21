---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d72a456f09549d7421ee059f72df75c09e61ac695eca6ffbdf868413e35daaa4
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-catalog-ownership
    - WCO
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace Catalog Ownership
description: Workspace admins are default owners of the workspace catalog when one is provisioned, granting them the ability to manage privileges and transfer ownership within that catalog.
tags:
  - unity-catalog
  - workspace-catalog
  - ownership
  - privileges
timestamp: "2026-06-19T17:28:16.019Z"
---

# Workspace Catalog Ownership

**Workspace Catalog Ownership** refers to the default ownership and privileges automatically granted to Workspace Admins for the workspace catalog in a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). When a workspace is automatically enabled for Unity Catalog (all workspaces created after November 8, 2023), a dedicated workspace catalog is provisioned, and workspace admins become its default owners. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Ownership Privileges

As default owners of the workspace catalog, workspace admins receive the following privileges: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- **Manage privileges or transfer ownership** of any object within the workspace catalog. This includes the ability to grant themselves read and write access to all data in the catalog. By default, they have no direct data access; any self‑grant is audit‑logged. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Transfer ownership** of the workspace catalog itself to another user, group, or service principal. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

These privileges are represented in the metastore’s **Permissions** tab in the account console through an auto‑generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default User Privileges on the Workspace Catalog

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Additionally, on the `default` schema within that catalog, users are granted the following privileges: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- `USE SCHEMA`
- `CREATE TABLE`
- `CREATE VOLUME`
- `CREATE MODEL`
- `CREATE FUNCTION`
- `CREATE MATERIALIZED VIEW`

The default privileges granted on the workspace catalog are not maintained if the catalog is bound to another workspace. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Role of the [Metastore](/concepts/metastore.md) Admin

The [Metastore Admin](/concepts/metastore-admin-role.md) is an optional role in workspaces with automatic Unity Catalog enablement. Workspace admins already receive sufficient metastore‑level privileges by default, making a [Metastore](/concepts/metastore.md) admin unnecessary for routine operations. However, if a [Metastore](/concepts/metastore.md) admin is assigned (by an [Account Admin](/concepts/account-admin-unity-catalog.md)), they have additional ownership privileges because they are the owners of the [Metastore](/concepts/metastore.md) itself. Workspace catalog ownership remains separate; the [Metastore](/concepts/metastore.md) admin’s scope is the entire [Metastore](/concepts/metastore.md), not just the workspace catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Transferring Ownership

Workspace admins can transfer ownership of the workspace catalog to another user, group, or service principal. After transfer, the new owner gains the same management privileges over the catalog’s contents. The previous workspace admin retains any privileges granted separately (e.g., through the workspace admin role) but loses catalog‑specific ownership rights. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Admin Privileges in Unity Catalog — Overview of account, workspace, and [Metastore](/concepts/metastore.md) admin roles.
- [Workspace Catalog](/concepts/workspace-catalog-binding.md) — The default catalog provisioned for each Unity Catalog‑enabled workspace.
- [Metastore Admin](/concepts/metastore-admin-role.md) — Optional role with metastore‑wide privileges and ownership.
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — How privileges are managed on Unity Catalog securable objects.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
