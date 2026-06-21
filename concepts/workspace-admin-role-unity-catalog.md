---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a2b9ec8a3f8ccac6a7b5e2e011a105296ecadcca4df51113245120f39e496cc8
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-admin-role-unity-catalog
    - WAR(C
    - Workspace Admin Role
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace Admin Role (Unity Catalog)
description: A highly privileged role operating within a single Databricks workspace, managing workspace membership, jobs, and workspace objects.
tags:
  - unity-catalog
  - admin-roles
  - workspace-administration
timestamp: "2026-06-19T08:54:19.327Z"
---

Based on the provided source material, here is the wiki page for "Workspace Admin Role (Unity Catalog)".

---

## Workspace Admin Role (Unity Catalog)

**Workspace admin** is a highly privileged role in Databricks that operates within a single workspace. From a Unity Catalog permissions perspective, workspace admins manage workspace membership, jobs, and workspace objects. This role is distinct from [Account Admin](/concepts/account-admin-unity-catalog.md) and [Metastore Admin](/concepts/metastore-admin-role.md) roles, which operate at different scopes. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Default [Metastore](/concepts/metastore.md) Privileges

For workspaces created after November 8, 2023 (which are automatically enabled for Unity Catalog), workspace admins are granted specific privileges on the attached [Metastore](/concepts/metastore.md) by default. These are represented in the [Metastore](/concepts/metastore.md)'s **Permissions** tab by an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Default privileges include:

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

### Workspace Catalog Ownership

If a workspace catalog was provisioned for your workspace, workspace admins are its default owners. This ownership grants the ability to manage privileges for or transfer ownership of any object within that workspace catalog. It also allows workspace admins to transfer ownership of the workspace catalog itself. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### User Privileges in the Workspace Catalog

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Additionally, users receive `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema within the catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Role Restrictions

Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### When a [Metastore](/concepts/metastore.md) Admin is Still Needed

The [Metastore](/concepts/metastore.md) admin role is optional for workspaces created after November 8, 2023, because workspace admins have sufficient default privileges. However, a [Metastore](/concepts/metastore.md) admin must be assigned if the workspace needs to: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Change ownership of objects or grant privileges on objects not owned by the workspace admin.
- Remove default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md) if none exists.
- Enable default access request destinations for objects without explicit destinations.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
