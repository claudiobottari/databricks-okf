---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a727f27470a401489f3ddfa16382f465fe7b414dbf3d7ee38644d5427981fdd
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-workspace-admin-privileges-on-metastore
    - DWAPOM
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Default Workspace Admin Privileges on Metastore
description: The set of privileges (CREATE CATALOG, CREATE EXTERNAL LOCATION, etc.) automatically granted to workspace admins on the attached metastore in auto-enabled workspaces.
tags:
  - unity-catalog
  - privileges
  - workspace-admins
timestamp: "2026-06-19T08:54:01.976Z"
---

Here is the wiki page for "Default Workspace Admin Privileges on [Metastore](/concepts/metastore.md)".

---

## Default Workspace Admin Privileges on [Metastore](/concepts/metastore.md)

**Default Workspace Admin Privileges on Metastore** refers to a set of privileges automatically granted to workspace admins on the attached Unity Catalog [Metastore](/concepts/metastore.md) when a workspace is enabled for Unity Catalog automatically. This model applies to all workspaces created after November 8, 2023. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Overview

When a workspace is automatically enabled for Unity Catalog, the workspace is attached to a [Metastore](/concepts/metastore.md) by default. In this scenario, workspace admins receive specific metastore-level privileges that make the [Metastore](/concepts/metastore.md) admin role optional. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Granted Privileges

Workspace admins are granted the following privileges on the attached [Metastore](/concepts/metastore.md) by default:

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

Databricks represents these grants using an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. These privilege grants are visible on the [Metastore](/concepts/metastore.md) **Permissions** tab in the account console. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Workspace Catalog Ownership

If a workspace catalog was provisioned for the workspace, workspace admins are its default owners. Ownership of the workspace catalog grants workspace admins the ability to:

- Manage privileges for or transfer ownership of any object within the workspace catalog (including granting themselves read and write access to all data in the catalog, though granting permissions is audit-logged).
- Transfer ownership of the workspace catalog itself.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Additionally, workspace users receive `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema in the catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Scope Limitations

The default privileges granted on the attached [Metastore](/concepts/metastore.md) and workspace catalog are not maintained across workspaces. For example, if the workspace catalog is also bound to another workspace, these privileges do not carry over. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### When a [Metastore](/concepts/metastore.md) Admin Is Still Required

Even with these default privileges, a [Metastore](/concepts/metastore.md) admin is still required for certain actions:

- Changing ownership of objects or granting privileges on objects that the workspace admin does not own.
- Removing default workspace admin permissions.
- Adding managed storage to the [Metastore](/concepts/metastore.md) if it has none (requires an account admin).
- Enabling default access request destinations for objects without explicitly set destinations.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Metastore Admin](/concepts/metastore-admin-role.md) – A separate, highly privileged role within Unity Catalog; optional when default workspace admin privileges are sufficient.
- [Account Admin](/concepts/account-admin-unity-catalog.md) – An account-level role that creates and links metastores and workspaces, and can assign admin roles.
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) – The top-level container for metadata and data governance in Unity Catalog.
- [Workspace Catalog](/concepts/workspace-catalog-binding.md) – A catalog provisioned for a specific workspace, often owned by workspace admins by default.
- [Restrict Workspace Admins](/concepts/restrictworkspaceadmins-setting.md) – A setting that account admins can use to limit workspace admin capabilities.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
