---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b439648b1863bed40cf797553b674f5330b805d9339237957435a6ddb7e57085
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-admins-unity-catalog
    - WA(C
    - Workspace admins
    - workspace admins
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace admins (Unity Catalog)
description: Admin role operating within a single workspace, managing workspace membership, jobs, and workspace objects, with default privileges on automatically-provisioned metastores.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-18T14:19:59.670Z"
---

# Workspace admins (Unity Catalog)

**Workspace admins** are administrative users who operate within a single Databricks workspace. From a Unity Catalog permissions perspective, they are one of the three most important administrator roles, alongside account admins and [Metastore](/concepts/metastore.md) admins. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Responsibilities

Workspace admins manage workspace membership, jobs, and workspace objects. They have admin privileges within a single workspace. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Privileges when workspaces are enabled for Unity Catalog automatically

For workspaces created after November 8, 2023, Unity Catalog is enabled automatically and the workspace is attached to a [Metastore](/concepts/metastore.md) by default. In this scenario, workspace admins receive the following metastore-level privileges by default: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

* `CREATE CATALOG`
* `CREATE CLEAN ROOM`
* `CREATE EXTERNAL LOCATION`
* `CREATE SERVICE CREDENTIAL`
* `CREATE STORAGE CREDENTIAL`
* `CREATE CONNECTION`
* `CREATE SHARE`
* `CREATE RECIPIENT`
* `CREATE PROVIDER`
* `CREATE MATERIALIZED VIEW`

These privilege grants are visible in the [Metastore](/concepts/metastore.md) **Permissions** tab in the account console. Databricks represents them with an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Workspace catalog ownership

If a workspace catalog has been provisioned for the workspace, workspace admins are the default owners of that catalog. Ownership of the workspace catalog grants the following privileges: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

* Manage the privileges for or transfer ownership of any object within the workspace catalog. This includes the ability to grant themselves read and write access to all data in the catalog (no direct access by default; granting permissions is audit-logged).
* Transfer ownership of the workspace catalog itself.

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Additionally, workspace users receive the `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema in the catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

> The default privileges granted on the attached [Metastore](/concepts/metastore.md) and workspace catalog are not maintained across workspaces (e.g., if the workspace catalog is also bound to another workspace).

## Relationship to other admin roles

Workspace admins are separate from [Metastore admin|metastore admins](/concepts/metastore-admin-role.md) and [Account admin|account admins](/concepts/account-admin-unity-catalog.md). Account admins operate at the Databricks account level, creating and linking metastores and workspaces and assigning admin roles. [Metastore](/concepts/metastore.md) admins govern data access, ownership, and top-level Unity Catalog securable objects within a single [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

In workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins receive sufficient metastore-level privileges by default. A [Metastore](/concepts/metastore.md) admin must be assigned if an organization needs to perform actions such as changing ownership of objects they do not own, removing default workspace admin permissions, adding managed storage to the [Metastore](/concepts/metastore.md), or enabling default access request destinations. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Sources

* admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
