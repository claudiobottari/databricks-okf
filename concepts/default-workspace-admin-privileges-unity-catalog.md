---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a008d680c9f7d0d5b296aa506400a584f5db5cca731965a4834c38e6846b244d
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-workspace-admin-privileges-unity-catalog
    - DWAP(C
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Default workspace admin privileges (Unity Catalog)
description: A set of metastore-level privileges (CREATE CATALOG, CREATE EXTERNAL LOCATION, CREATE SHARE, etc.) auto-granted to workspace admins in automatically-enabled Unity Catalog workspaces, represented via a system group.
tags:
  - privileges
  - unity-catalog
  - workspace-admins
timestamp: "2026-06-18T10:41:18.881Z"
---

# Default workspace admin privileges (Unity Catalog)

**Default workspace admin privileges** are the set of permissions automatically granted to [Workspace admin|workspace admins](/concepts/restrictworkspaceadmins-setting.md) on their workspace's attached [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) when the workspace is enabled for Unity Catalog automatically. This applies to all workspaces created after November 8, 2023. These default privileges make the [Metastore admin](/concepts/metastore-admin-role.md) role optional in many scenarios.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Overview

When a workspace is automatically enabled for Unity Catalog, it is attached to a [Metastore](/concepts/metastore.md) by default. Workspace admins in this configuration receive a baseline set of metastore-level privileges that allow them to perform essential data governance and management tasks without requiring a separate [Metastore](/concepts/metastore.md) admin assignment.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

These default privileges are granted through an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. The grants are visible in the [Metastore](/concepts/metastore.md) **Permissions** tab in the account console.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Granted privileges

By default, workspace admins on automatically enabled workspaces receive the following privileges on the attached [Metastore](/concepts/metastore.md):

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

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Workspace admins also become the default owners of the workspace catalog (if one was provisioned for the workspace). Ownership of this catalog grants the following additional privileges:

- Manage the privileges for or transfer ownership of any object within the workspace catalog, including the ability to grant themselves read and write access to all data in the catalog (note: no direct access is granted by default; granting access is audit-logged).
- Transfer ownership of the workspace catalog itself.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## User access within the workspace catalog

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Workspace users also receive the following privileges on the `default` schema in the catalog:

- `USE SCHEMA`
- `CREATE TABLE`
- `CREATE VOLUME`
- `CREATE MODEL`
- `CREATE FUNCTION`
- `CREATE MATERIALIZED VIEW`

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Comparison with [Metastore](/concepts/metastore.md) admin

The default workspace admin privileges provide sufficient capabilities for most day-to-day operations, making the [Metastore](/concepts/metastore.md) admin role optional for workspaces created after November 8, 2023. However, a [Metastore](/concepts/metastore.md) admin must still be assigned if you need to:^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Change ownership of objects or grant privileges on objects you do not own (for example, taking over a catalog after the original owner is removed).
- Remove default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md) (requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- Enable default access request destinations for objects that don't have destinations explicitly set.

[Metastore](/concepts/metastore.md) admin privileges differ from workspace admin privileges in that they include default permissions on the [Metastore](/concepts/metastore.md) itself (such as the ability to manage all securable objects) and ownership privileges over the [Metastore](/concepts/metastore.md).^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Important notes

These default privilege grants are not maintained across workspaces. If, for example, the workspace catalog is also bound to another workspace, the privileges do not automatically transfer.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

If needed, account admins can assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group. Databricks strongly recommends using groups for role assignments to ensure any member of the group automatically inherits the role.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- Workspace admin — The administrator role within a single workspace
- [Metastore admin](/concepts/metastore-admin-role.md) — The optional role for governing a Unity Catalog [Metastore](/concepts/metastore.md)
- [Account Admin (Unity Catalog)](/concepts/account-admin-unity-catalog.md) — The account-level administrator who creates and links metastores
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance system these roles manage
- [Metastore](/concepts/metastore.md) — The metadata container for Unity Catalog objects

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
