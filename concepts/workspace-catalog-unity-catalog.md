---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c469a71a859bca7f3fd72907c737ff2be391031bed5fc4bbb14c922257b2b617
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - workspace-catalog-unity-catalog
    - WC(C
    - Upgrade a workspace to Unity Catalog
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace Catalog (Unity Catalog)
description: A catalog provisioned for a workspace during automatic Unity Catalog enablement, where workspace admins are default owners and all workspace users receive USE CATALOG privilege.
tags:
  - unity-catalog
  - data-governance
  - databricks
timestamp: "2026-06-19T21:59:45.706Z"
---

# Workspace catalog (Unity Catalog)

A **workspace catalog** is a Unity Catalog catalog provisioned automatically for a single Databricks workspace that has been enabled for Unity Catalog. It serves as a default, workspace-scoped namespace and provides baseline access to workspace users without requiring separate [Metastore](/concepts/metastore.md) admin grants. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Overview

When a workspace is automatically enabled for Unity Catalog—which applies to all workspaces created after November 8, 2023—Databricks may provision a workspace catalog for that workspace. This catalog provides a default location for storing and managing data assets within the workspace. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Ownership and privileges

Workspace admins are the default owners of the workspace catalog. Ownership grants them the following privileges:

- Manage privileges for or transfer ownership of any object within the workspace catalog.
- Grant themselves read and write access to all data in the catalog (no direct access by default; granting permissions is audit‑logged).
- Transfer ownership of the workspace catalog itself.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default user privileges

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. In addition, workspace users receive the following privileges on the `default` schema within the catalog:

- `USE SCHEMA`
- `CREATE TABLE`
- `CREATE VOLUME`
- `CREATE MODEL`
- `CREATE FUNCTION`
- `CREATE MATERIALIZED VIEW`

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Cross-workspace considerations

The default privileges granted on the workspace catalog are not maintained across workspaces. For example, if the workspace catalog is also bound to another workspace, the default grants apply only within the workspace where the catalog was provisioned. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship to other catalogs

The workspace catalog is one of the catalogs in the [Metastore](/concepts/metastore.md). Workspace admins can also create additional catalogs using the `CREATE CATALOG` privilege they have on the [Metastore](/concepts/metastore.md). Other catalogs (such as user‑created catalogs) do not automatically inherit the default privileges that apply to the workspace catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides cataloging and access control.
- [Metastore admin](/concepts/metastore-admin-role.md) — The role that governs data access at the [Metastore](/concepts/metastore.md) level.
- Workspace admin — The role that manages workspace membership and objects within a workspace.
- [Account admin](/concepts/account-admin-unity-catalog.md) — The role that operates at the Databricks account level.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
