---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ebcda2a29cdde705f92a8161e3c367557c4e9ede8601d8f067b6282e1e07e5b
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-admin-unity-catalog
    - WA(C
    - Workspace Admin
    - Workspace Administration
    - Workspace administrator
    - workspace admin
    - workspace-admin-role-unity-catalog
    - WAR(C
    - Workspace Admin Role
    - workspace-admins-in-unity-catalog
    - WAIUC
    - workspace-admins-unity-catalog
    - Workspace admins
    - workspace admins
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace Admin (Unity Catalog)
description: An admin role operating within a single Databricks workspace, managing workspace membership, jobs, and workspace objects, with default metastore privileges on auto-enabled workspaces.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T22:00:10.802Z"
---

# Workspace Admin (Unity Catalog)

**Workspace admin** is a highly privileged role within a single Databricks workspace. Workspace admins manage workspace membership, jobs, and workspace objects, and they have specific privileges in Unity Catalog depending on whether the workspace was enabled for Unity Catalog automatically or manually.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Overview

Workspace admins operate within the scope of one workspace. They are distinct from [account admins](/concepts/account-admin-unity-catalog.md), who manage the entire Databricks account, and from [metastore admins](/concepts/metastore-admin-role.md), who govern a Unity Catalog [Metastore](/concepts/metastore.md) at the account level. Workspace admins are required in every deployment, while the [Metastore](/concepts/metastore.md) admin role is optional.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Workspace admin privileges in Unity Catalog

Workspace admins' Unity Catalog privileges depend on whether the workspace was enabled for Unity Catalog automatically (all workspaces created after November 8, 2023) or manually.

### Default privileges on the [Metastore](/concepts/metastore.md) (automatic-enablement workspaces)

If the workspace was enabled for Unity Catalog automatically, the workspace is attached to a [Metastore](/concepts/metastore.md) by default. Workspace admins automatically receive the following privileges on that [Metastore](/concepts/metastore.md):

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

These grants are represented by an auto‑generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`, visible in the [Metastore](/concepts/metastore.md) **Permissions** tab in the account console.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Ownership of the workspace catalog

If a workspace catalog was provisioned for the workspace, workspace admins are its default owners. Ownership of this catalog grants the following capabilities:

- Manage privileges for or transfer ownership of any object within the workspace catalog (including the ability to grant themselves read and write access to all data in the catalog – granting permissions is audit‑logged).
- Transfer ownership of the workspace catalog itself.

All workspace users receive `USE CATALOG` on the workspace catalog, as well as `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` on the `default` schema in the catalog.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Restriction of workspace admin privileges

Account admins can restrict workspace admin privileges by enabling the `RestrictWorkspaceAdmins` setting. See [Restrict workspace admins](https://docs.databricks.com/aws/en/admin/workspace-settings/restrict-workspace-admins).^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship with the [Metastore](/concepts/metastore.md) admin role

For workspaces enabled for Unity Catalog automatically, the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins receive sufficient metastore‑level privileges by default. However, a [Metastore](/concepts/metastore.md) admin must be assigned to perform the following actions:

- Change ownership of objects or grant privileges on objects that the workspace admin does not own (for example, taking over a catalog after the original owning account is removed).
- Remove default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md) if it has none (requires an account admin).
- Enable default access request destinations for objects.

Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Best practices

- Distribute the workspace admin role carefully; it is a highly privileged role.
- Use groups rather than individual users to manage workspace admin assignments when possible.
- Account admins should consider enabling `RestrictWorkspaceAdmins` to limit the scope of workspace admin actions.
- In automatic‑enablement workspaces, the [Metastore](/concepts/metastore.md) admin role can remain unassigned unless specific advanced operations are needed.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Account admin](/concepts/account-admin-unity-catalog.md) — Admin role for the entire Databricks account
- [Metastore admin](/concepts/metastore-admin-role.md) — Optional admin role for a Unity Catalog [Metastore](/concepts/metastore.md)
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform underlying these admin roles
- [RestrictWorkspaceAdmins](/concepts/restrictworkspaceadmins-setting.md) — A setting to limit workspace admin permissions

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
