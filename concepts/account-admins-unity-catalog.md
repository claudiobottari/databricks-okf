---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 93c0fb570c58f2a7107a0b44fd60311127f9b894aae717e3d38d6322c77dcd1f
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-admins-unity-catalog
    - AA(C
    - Account Admins
    - Account admins
    - account admins
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Account admins (Unity Catalog)
description: Highly privileged role operating at the Databricks account level, responsible for creating and linking metastores and workspaces, and assigning admin roles.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-18T14:19:58.553Z"
---

Here is the wiki page for "Account admins (Unity Catalog)".

---

## Account admins (Unity Catalog)

**Account admins** are the highest-privilege role in the [Unity Catalog](/concepts/unity-catalog.md) permission model, operating at the Databricks account level rather than within a single workspace. They are one of three critical admin roles from a Unity Catalog perspective — alongside [workspace admins](/concepts/workspace-admins-unity-catalog.md) and [metastore admins](/concepts/metastore-admin-role.md) — and are required for all Databricks deployments. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Responsibilities

Account admins have privileges over the entire Databricks account. Their key capabilities include creating and linking Unity Catalog metastores and workspaces, and assigning other admin roles. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Role scope

Account admin is a highly privileged role that should be distributed carefully. They operate at a broader scope than workspace admins, who manage permissions within a single workspace, and [Metastore](/concepts/metastore.md) admins, who govern data access within a single [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Account admins and [Metastore](/concepts/metastore.md) admins are separate roles. When an account admin creates a [Metastore](/concepts/metastore.md), they become its initial [Metastore](/concepts/metastore.md) admin by default. They can then assign the [Metastore](/concepts/metastore.md) admin role to a different user, group, or service principal and relinquish it themselves. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship to other admin roles

The three roles work together:

- **Account admins** govern the account, create and link metastores, and assign admin roles.
- **Workspace admins** manage workspace membership, jobs, and workspace objects within a single workspace.
- **Metastore admins (optional)** govern data access, ownership, and top-level Unity Catalog securable objects within a single [Metastore](/concepts/metastore.md).

For more information, see [workspace admins](/concepts/workspace-admins-unity-catalog.md) and [metastore admins](/concepts/metastore-admin-role.md).

## Best practices

Because account admin is a highly privileged role, it should be distributed carefully across the organization. Databricks recommends using groups rather than individual users wherever possible when assigning admin roles. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
