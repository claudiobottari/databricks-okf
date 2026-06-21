---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ccf6dbab3987baa3be52126bfc7da4ea794cc1c2220c5495e58293091a7c78be
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-unity-catalog-enablement-and-workspace-admin-default-privileges
    - Workspace Admin Default Privileges and Automatic Unity Catalog Enablement
    - AUCEAWADP
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Automatic Unity Catalog Enablement and Workspace Admin Default Privileges
description: For workspaces created after November 8, 2023, Unity Catalog is auto-enabled and workspace admins receive default metastore-level privileges (CREATE CATALOG, CREATE EXTERNAL LOCATION, etc.) represented by the auto-generated _workspace_admins_databricks system group.
tags:
  - unity-catalog
  - auto-enablement
  - workspace-admins
timestamp: "2026-06-19T13:54:34.012Z"
---

---
title: Automatic Unity Catalog Enablement and Workspace Admin Default Privileges
summary: Workspaces created after November 8, 2023 are automatically enabled for Unity Catalog, granting workspace admins default [Metastore](/concepts/metastore.md) privileges that make the [Metastore](/concepts/metastore.md) admin role optional.
sources:
  - admin-privileges-in-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - databricks
  - unity-catalog
  - workspace-admin
  - privileges
aliases:
  - automatic-unity-catalog-enablement-and-workspace-admin-default-privileges
  - AUCWADP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Automatic Unity Catalog Enablement and Workspace Admin Default Privileges

**Automatic Unity Catalog Enablement** is a Databricks behavior for all workspaces created after November 8, 2023. These workspaces are automatically attached to a Unity Catalog [Metastore](/concepts/metastore.md) by default, and workspace admins receive a set of default metastore-level privileges that make the [Metastore](/concepts/metastore.md) admin role optional. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Scope of Automatic Enablement

Workspaces created after November 8, 2023 are enabled for Unity Catalog automatically, meaning they are attached to a [Metastore](/concepts/metastore.md) without requiring manual setup by an account admin. This contrasts with older workspaces, where an account admin had to manually create and assign a [Metastore](/concepts/metastore.md). See Get started with Unity Catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default Workspace Admin Privileges on the [Metastore](/concepts/metastore.md)

When a workspace is automatically enabled, workspace admins receive the following privileges on the attached [Metastore](/concepts/metastore.md) by default:

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

Databricks represents these privilege grants using an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. They appear in the [Metastore](/concepts/metastore.md) **Permissions** tab of the account console. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Workspace Catalog Ownership

If a workspace catalog was provisioned for the workspace, workspace admins become its default owners. Ownership of this catalog grants the following capabilities:

- Manage privileges for or transfer ownership of any object within the workspace catalog, including granting themselves read and write access to all data in the catalog. Granting permissions is audit-logged.
- Transfer ownership of the workspace catalog itself.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. In addition, workspace users receive `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema within the catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

> **Note:** The default privileges granted on the attached [Metastore](/concepts/metastore.md) and workspace catalog are not maintained across workspaces — for example, if the workspace catalog is also bound to another workspace. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) Admin Role Optionality

Because workspace admins receive sufficient metastore-level privileges through automatic enablement, the [Metastore](/concepts/metastore.md) admin role is optional for workspaces created after November 8, 2023. The [Metastore](/concepts/metastore.md) was originally created without a [Metastore](/concepts/metastore.md) admin when provisioned automatically. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

However, a [Metastore](/concepts/metastore.md) admin must be assigned if you need to perform actions not covered by workspace admin defaults:

- Change ownership of objects or grant privileges on objects you do not own (e.g., taking over a catalog after the original owning account is removed).
- Remove default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md) (requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- Enable default access request destinations for objects that don't have destinations explicitly set.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Account admins can assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group. Databricks strongly recommends nominating a group. See [Assign a metastore admin](/concepts/assigning-a-metastore-admin.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for data governance.
- Workspace admin — Admin role operating within a single workspace.
- [Account admin](/concepts/account-admin-unity-catalog.md) — Admin role operating at the Databricks account level.
- [Metastore admin](/concepts/metastore-admin-role.md) — Optional admin role governing data access in a [Metastore](/concepts/metastore.md).
- [Restrict workspace admins](/concepts/restrictworkspaceadmins-setting.md) — Account-level setting that can limit workspace admin privileges.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
