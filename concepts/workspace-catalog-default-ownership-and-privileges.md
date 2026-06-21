---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a106692f2c380e3b8d9331d284b12e38b16d03d7ac33e0bc59f8f0a62b34ec5
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-catalog-default-ownership-and-privileges
    - Privileges and Workspace Catalog Default Ownership
    - WCDOAP
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace Catalog Default Ownership and Privileges
description: When a workspace is auto-enabled for Unity Catalog, a workspace catalog is provisioned with workspace admins as default owners, granting them privilege management and ownership transfer capabilities over objects in that catalog.
tags:
  - unity-catalog
  - workspace-catalog
  - permissions
timestamp: "2026-06-19T13:54:40.921Z"
---

# Workspace Catalog Default Ownership and Privileges

**Workspace Catalog Default Ownership and Privileges** describes the automatic ownership and permission grants that apply when a workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md) automatically (all workspaces created after November 8, 2023). In this scenario, a workspace catalog is provisioned and assigned to the workspace, and both [workspace admins](/concepts/workspace-admins-unity-catalog.md) and all workspace users receive a set of default privileges on that catalog.

## Default Ownership

Workspace admins are the **default owners** of the workspace catalog. As owners, they have the following capabilities with respect to the catalog:

- Manage privileges for or transfer ownership of **any object within the workspace catalog**. This includes the ability to grant themselves read and write access to all data in the catalog (such grants are audit-logged, and no direct access is given by default).
- Transfer ownership of the workspace catalog itself. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default Privileges for Workspace Admins

In addition to catalog ownership, workspace admins receive a set of metastore-level privileges automatically on the [Metastore](/concepts/metastore.md) attached to the workspace. These privileges are represented by an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>` and include: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- `CREATE CATALOG`
- `CREATE CLEAN ROOM`
- `CREATE EXTERNAL LOCATION`
- `CREATE SERVICE CREDENTIAL`
- `CREATE STORAGE CREDENTIAL`
- `CREATE CONNECTION`
- `CREATE SHARE`
- `CREATE RECIPIENT`
- `CREATE PROVIDER`
- `CREATE MATERIALIZED VIEW`

These grants are visible in the [Metastore](/concepts/metastore.md) **Permissions** tab in the account console. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default Privileges for All Workspace Users

All workspace users receive the following default privileges on the workspace catalog: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- `USE CATALOG` on the workspace catalog itself.
- On the `default` schema within that catalog: `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW`.

These grants enable users to interact with the catalog immediately without requiring any additional privilege assignments.

## Important Notes

- The default privileges described above are **not maintained across workspaces** – for example, if the workspace catalog is also bound to another workspace, the default grants do not carry over. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- Because workspace admins receive sufficient metastore-level privileges by default, the optional [metastore admin](/concepts/metastore-admin-role.md) role is typically unnecessary in workspaces that were automatically enabled for Unity Catalog. A [Metastore](/concepts/metastore.md) admin must be assigned only when specific actions are needed, such as taking ownership of objects the workspace admin does not own, removing default workspace admin permissions, or adding managed storage to the [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Workspace admins](/concepts/workspace-admins-unity-catalog.md)
- [Metastore admin](/concepts/metastore-admin-role.md)
- Admin privileges in Unity Catalog
- [Workspace catalog](/concepts/workspace-catalog-binding.md)

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
