---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20285e02acf2bbeb07e96567a6a899808e9e1beb5253407dc69c47315312a11c
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-admin-roles-account-workspace-metastore
    - UCAR(WM
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Admin Roles (Account, Workspace, Metastore)
description: The three most important administrative roles in Unity Catalog — account admins, workspace admins, and metastore admins — each operating at different scopes within the Databricks architecture.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T17:28:12.278Z"
---

# Unity Catalog Admin Roles (Account, Workspace, [Metastore](/concepts/metastore.md))

Databricks distinguishes several administrator roles; for Unity Catalog, the three most important are **account admins**, **workspace admins**, and **metastore admins**. Account admins and workspace admins are required in every deployment, while the [Metastore](/concepts/metastore.md) admin role is optional. Understanding each role’s scope and responsibilities helps assign the right privileges to the right people. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Account Admins

Account admins operate at the Databricks **account level**. They can create and link [Unity Catalog](/concepts/unity-catalog.md) metastores to workspaces, manage account-level workspaces, and assign admin roles to users, groups, or service principals. This is a highly privileged role that should be distributed carefully. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Workspace Admins

Workspace admins operate within a single workspace. They manage workspace membership, jobs, workspace objects, and other workspace-level settings. This role is also highly privileged and should be restricted. Account admins can further limit workspace admin privileges using the `RestrictWorkspaceAdmins` setting. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Workspace Admin Privileges (Automatically Enabled Workspaces)

Workspaces created after **November 8, 2023** are automatically enabled for Unity Catalog and attached to a [Metastore](/concepts/metastore.md) by default. In that scenario, workspace admins receive additional default privileges on the attached [Metastore](/concepts/metastore.md), including `CREATE CATALOG`, `CREATE CLEAN ROOM`, `CREATE EXTERNAL LOCATION`, `CREATE SERVICE CREDENTIAL`, `CREATE STORAGE CREDENTIAL`, `CREATE CONNECTION`, `CREATE SHARE`, `CREATE RECIPIENT`, `CREATE PROVIDER`, and `CREATE MATERIALIZED VIEW`. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

These privileges are granted through a system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`, visible in the metastore’s **Permissions** tab in the account console. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

If a **workspace catalog** was provisioned for the workspace, workspace admins become its default owners. Ownership of this catalog grants them the ability to manage privileges or transfer ownership of any object within the catalog (including granting themselves read/write access, which is audit-logged) and to transfer ownership of the workspace catalog itself. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

All workspace users receive the `USE CATALOG` privilege on the workspace catalog, as well as `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema in the catalog. The default privileges granted on the attached [Metastore](/concepts/metastore.md) and workspace catalog are **not** maintained across workspaces (for example, if the workspace catalog is also bound to another workspace). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) Admins (Optional)

A **metastore admin** is an optional but highly privileged user or group within a single Unity Catalog [Metastore](/concepts/metastore.md). [Metastore](/concepts/metastore.md) admins govern data access, ownership, and top-level Unity Catalog securable objects. Their privileges come from two sources: default privileges inherent to the role, and ownership privileges because they are the owners of the [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### When to Assign a [Metastore](/concepts/metastore.md) Admin

For workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins already receive sufficient metastore-level privileges by default. You must assign a [Metastore](/concepts/metastore.md) admin if any of the following actions are needed:

- Change ownership of objects or grant privileges on objects that you do not own (for example, taking over a catalog after the original owner is removed). Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own.
- Remove the default workspace admin permissions described above.
- Add managed storage to the [Metastore](/concepts/metastore.md), if the [Metastore](/concepts/metastore.md) has none (requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- Enable default access request destinations for objects that do not have destinations explicitly set.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Default [Metastore](/concepts/metastore.md) Admin Privileges

[Metastore](/concepts/metastore.md) admins have a set of default privileges on the [Metastore](/concepts/metastore.md). (The full list is defined elsewhere in Databricks documentation; the source material does not enumerate them exhaustively.) ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Ownership Privileges

As owners of the [Metastore](/concepts/metastore.md), [Metastore](/concepts/metastore.md) admins inherit ownership privileges that allow them to manage the [Metastore](/concepts/metastore.md) and its top-level securable objects. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Who Has Initial [Metastore](/concepts/metastore.md) Admin Privileges?

If an account admin creates the [Metastore](/concepts/metastore.md) manually (the case for all metastores created before November 8, 2023), that account admin becomes the metastore’s initial owner and [Metastore](/concepts/metastore.md) admin. Account admins can later assign the role to a different user, group, or service principal and relinquish it themselves. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

If the [Metastore](/concepts/metastore.md) was provisioned automatically (workspaces created after November 8, 2023), it is created without a [Metastore](/concepts/metastore.md) admin. In that case the workspace admins’ default privileges make the role optional; account admins can still assign a [Metastore](/concepts/metastore.md) admin if needed. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Assign a [Metastore](/concepts/metastore.md) Admin

Only account admins can assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends nominating a **group** as the [Metastore](/concepts/metastore.md) admin, so that any member of the group automatically receives the role. To assign:

1. As an account admin, log in to the **account console**.
2. Click **Catalog**.
3. Select the name of a [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Choose a group from the drop-down (search by text).
6. Click **Save**.

The change can take up to 30 seconds to be reflected, and may take longer in some workspaces due to caching. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Metastore](/concepts/metastore.md)
- Privilege Grants
- [Account Admin](/concepts/account-admin-unity-catalog.md)
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md)
- [RestrictWorkspaceAdmins](/concepts/restrictworkspaceadmins-setting.md)
- [Access Request Destinations](/concepts/access-request-destinations.md)

## Sources
- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
