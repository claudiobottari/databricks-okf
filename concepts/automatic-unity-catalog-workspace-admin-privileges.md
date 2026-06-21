---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fa919cc8314e5d18634c806f672611b50b1a6a84dab443464e8dd298c63ec22
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-unity-catalog-workspace-admin-privileges
    - AUCWAP
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Automatic Unity Catalog Workspace Admin Privileges
description: Default metastore-level privileges (CREATE CATALOG, CREATE EXTERNAL LOCATION, etc.) automatically granted to workspace admins in workspaces created after November 8, 2023, making the metastore admin role optional.
tags:
  - unity-catalog
  - workspace-admin
  - auto-enablement
  - privileges
timestamp: "2026-06-19T17:28:09.094Z"
---

## Automatic Unity Catalog Workspace Admin Privileges

**Automatic Unity Catalog Workspace Admin Privileges** refers to the set of default permissions that workspace admins receive when a workspace is automatically enabled for Unity Catalog. This automatic enablement applies to all workspaces created after November 8, 2023, and makes the [Metastore](/concepts/metastore.md) admin role optional by granting workspace admins sufficient metastore-level privileges out of the box. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Default Privileges on the Attached [Metastore](/concepts/metastore.md)

When automatic Unity Catalog enablement is in effect, workspace admins are granted the following metastore-level privileges by default:

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

These grants allow workspace admins to manage key [Unity Catalog](/concepts/unity-catalog.md) securable objects without requiring a separate [Metastore Admin](/concepts/metastore-admin-role.md) role. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Workspace Catalog Ownership

If a workspace catalog has been provisioned for the workspace, workspace admins become its default owners. Ownership of the catalog conveys the following abilities:

- Manage privileges for or transfer ownership of any object within the workspace catalog. This includes the ability to grant themselves read and write access to all data in that catalog; granting such permissions is audit-logged.
- Transfer ownership of the workspace catalog itself.

Additionally, all workspace users receive the `USE CATALOG` privilege on the workspace catalog, and on the `default` schema within that catalog they receive `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW`. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

These default privileges apply only to the workspace where the workspace catalog is bound; they are not maintained across workspaces if the catalog is bound to another workspace. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### [Metastore](/concepts/metastore.md) Admin Optionality

Because workspace admins receive the above privileges automatically, the [Metastore](/concepts/metastore.md) admin role becomes **optional** for workspaces created after November 8, 2023. A [Metastore](/concepts/metastore.md) admin must still be assigned if any of the following actions are needed:

- Change ownership of objects or grant privileges on objects that are not owned by the workspace admin (e.g., taking over a catalog after the original owning account is removed).
- Remove any of the default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md) (requires an [Account Admin](/concepts/account-admin-unity-catalog.md) to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- Enable default access request destinations for objects without explicit destinations.

Account admins can assign the [Metastore](/concepts/metastore.md) admin role when such operations are required. Databricks recommends using a group as the [Metastore](/concepts/metastore.md) admin to simplify access management. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Auto-Generated System Group

Databricks represents the default privilege grants on the attached [Metastore](/concepts/metastore.md) via an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. These grants are visible in the [Metastore](/concepts/metastore.md) **Permissions** tab in the account console. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Metastore Admin](/concepts/metastore-admin-role.md)
- [Account Admin](/concepts/account-admin-unity-catalog.md)
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md)
- [Workspace Catalog](/concepts/workspace-catalog-binding.md)
- [Admin roles in Unity Catalog](/concepts/account-admin-role-in-unity-catalog.md)

### Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
