---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 148cdc3819f9b73f89cb27ccc39990c107a2922806bca1f7906b49b4241afbe4
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-admins-in-unity-catalog
    - WAIUC
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace Admins in Unity Catalog
description: Workspace-scoped admin role managing workspace membership, jobs, and objects, with additional default privileges on the attached metastore when Unity Catalog is auto-enabled.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T13:55:43.935Z"
---

# Workspace Admins in Unity Catalog

**Workspace Admins** in Unity Catalog are administrator roles that operate within a single Databricks workspace. They manage workspace membership, jobs, and workspace objects, and have specific privileges on the Unity Catalog [Metastore](/concepts/metastore.md) depending on how the workspace was configured. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Role Overview

Workspace admins are one of the three most important admin roles from a Unity Catalog permissions perspective, alongside account admins and [Metastore](/concepts/metastore.md) admins. Account admins and workspace admins are required for all deployments, while the [Metastore](/concepts/metastore.md) admin role is optional. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Workspace admins have admin privileges within a single workspace, which includes the following key capabilities:

- Managing workspace membership
- Managing jobs
- Managing workspace objects

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

For more detailed information, see the documentation on [What are workspace admins?](https://docs.databricks.com/aws/en/admin/admin-concepts#what-are-workspace-admins).

Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. See [Restrict workspace admins](https://docs.databricks.com/aws/en/admin/workspace-settings/restrict-workspace-admins). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Automatic Unity Catalog Enablement

If your workspace was enabled for Unity Catalog automatically — which applies to all workspaces created after November 8, 2023 — the workspace is attached to a [Metastore](/concepts/metastore.md) by default. In this configuration, workspace admins receive additional privileges on the attached [Metastore](/concepts/metastore.md) by default: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

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

These privilege grants are visible in the [Metastore](/concepts/metastore.md) **Permissions** tab in the account console. Databricks represents them with an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Workspace Catalog Ownership

Workspace admins are the default owners of the workspace catalog, if a workspace catalog was provisioned for your workspace. Ownership of this catalog grants the following privileges: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Manage the privileges for or transfer ownership of any object within the workspace catalog. This includes the ability to grant themselves read and write access to all data in the catalog (no direct access by default; granting permissions is audit-logged).
- Transfer ownership of the workspace catalog itself.

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Workspace users also receive the `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema in the catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

**Note:** The default privileges granted on the attached [Metastore](/concepts/metastore.md) and workspace catalog are not maintained across workspaces (if, for example, the workspace catalog is also bound to another workspace). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Comparison with Other Admin Roles

| Role | Scope | Key Responsibilities |
|------|-------|---------------------|
| **Account Admin** | Account level | Create and link metastores and workspaces, assign admin roles |
| **Workspace Admin** | Single workspace | Manage workspace membership, jobs, and workspace objects |
| **Metastore Admin** | Single [Metastore](/concepts/metastore.md) (optional) | Govern data access, ownership, and top-level Unity Catalog securable objects |

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Account admins and [Metastore](/concepts/metastore.md) admins are separate roles. When an account admin creates a [Metastore](/concepts/metastore.md), they become its initial [Metastore](/concepts/metastore.md) admin by default. They can then assign the [Metastore](/concepts/metastore.md) admin role to a different user, group, or service principal and relinquish it themselves. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When the [Metastore](/concepts/metastore.md) Admin Role Is Still Needed

For workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins receive sufficient metastore-level privileges by default. However, you must assign a [Metastore](/concepts/metastore.md) admin if you need to perform the following actions: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- [Change ownership](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/#manage-ownership) of objects or grant privileges on objects that you do not own. For example, this is required when taking over a catalog after the original owning account is removed. Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own.
- Remove default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md), if it has none. This requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition. See [Add managed storage to an existing [Metastore](/concepts/metastore.md)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-metastore#add-storage).
- Enable default access request destinations for objects that don't have destinations explicitly set. See [Enable default email destinations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/access-request-destinations#default-destinations).

## Related Concepts

- [Account Admins in Unity Catalog](/concepts/account-admins-in-unity-catalog.md) – The account-level admin role that creates metastores and workspaces
- [Metastore Admins in Unity Catalog](/concepts/metastore-admins-in-unity-catalog.md) – The optional role governing data access within a [Metastore](/concepts/metastore.md)
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) – The container for data assets governed by Unity Catalog
- [Workspace Catalog](/concepts/workspace-catalog-binding.md) – The default catalog provisioned for workspaces with automatic Unity Catalog enablement
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) – The permission model for governing data access

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
