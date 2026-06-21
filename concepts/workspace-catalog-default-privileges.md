---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0332619e39bc67e6566a82cfa50efc219a6f2c5928efe5e313dc1284a677981f
  pageDirectory: concepts
  sources:
    - manage-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-catalog-default-privileges
    - WCDP
  citations:
    - file: manage-privileges-in-unity-catalog-databricks-on-aws.md
title: Workspace Catalog Default Privileges
description: When a workspace is automatically enabled for Unity Catalog, a workspace catalog is created where workspace admins are default owners and all workspace users get USE CATALOG on the catalog plus several privileges on the default schema.
tags:
  - unity-catalog
  - workspace
  - defaults
  - privileges
timestamp: "2026-06-19T19:27:28.958Z"
---

# Workspace Catalog Default Privileges

The **Workspace Catalog Default Privileges** are the initial set of permissions automatically granted to workspace users when a [Unity Catalog](/concepts/unity-catalog.md) workspace catalog is created. These defaults ensure that all workspace users have basic access to the catalog and its default schema, while workspace admins retain full ownership and management authority.

## Overview

When a workspace is enabled for Unity Catalog automatically, it is attached to a [Metastore](/concepts/metastore.md) by default, and a dedicated workspace catalog is created in that [Metastore](/concepts/metastore.md). Workspace admins become the default owners of this catalog. As owners, they have all privileges on the catalog and all its child objects and can manage those privileges. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

All workspace users receive a set of default privileges on the workspace catalog and its `default` schema, allowing them to immediately work with data within that catalog without any manual grant.

## Default Privileges Granted

The following privileges are granted by default to every workspace user:

| Scope | Privilege |
|-------|-----------|
| On the workspace catalog itself | `USE CATALOG` |
| On the `default` schema in the catalog | `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, `CREATE MATERIALIZED VIEW` |

^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

These privileges enable users to browse the catalog, create tables and volumes, register models and functions, and build materialized views within the default schema. No additional grant is required for these basic operations.

## Ownership and Management

Workspace admins are the default owners of the workspace catalog. As owners, they can:

- Manage privileges on the workspace catalog and all child objects (schemas, tables, views, volumes, etc.).
- Grant or revoke privileges to users, service principals, and groups.
- Transfer ownership of the catalog to another principal.

Other principals—such as [Metastore](/concepts/metastore.md) admins, account admins, or users with the `MANAGE` privilege on the catalog—can also manage privileges. See Manage Privileges in Unity Catalog for details. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Changing the Defaults

The default privileges can be altered by any principal with sufficient permissions (e.g., a workspace admin, a [Metastore](/concepts/metastore.md) admin, or the catalog owner). For example, an admin could revoke the default `USE CATALOG` privilege from a specific group or grant additional privileges to certain users. The workspace catalog is treated like any other Unity Catalog securable object, so standard GRANT and REVOKE SQL commands or Catalog Explorer can be used to modify its permissions. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Implications

These default privileges are designed to give all workspace users immediate read and basic write access to the workspace catalog's default schema. In many environments, this is sufficient for collaborative data exploration and development. For production environments that require stricter access control, workspace admins should review and adjust these defaults as needed.

Because the workspace catalog is created automatically, no manual setup is required for users to start working with Unity Catalog in that workspace. For further guidance, see Get Started with Unity Catalog.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution providing the permissions model.
- Privileges in Unity Catalog – Full list of privilege types and their meanings.
- USE CATALOG Privilege – The privilege that allows a principal to see and use a catalog.
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) – The role that owns the workspace catalog by default.
- [Metastore](/concepts/metastore.md) – The top-level container for Unity Catalog metadata.
- Default Schema – The schema created automatically in the workspace catalog.

## Sources

- manage-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-privileges-in-unity-catalog-databricks-on-aws.md](/references/manage-privileges-in-unity-catalog-databricks-on-aws-f0868c6d.md)
