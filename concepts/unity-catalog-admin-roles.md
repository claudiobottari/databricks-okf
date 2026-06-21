---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 782ac412bbb163ffb6e65ed4d9c1d5905197f374192706cce2d91c4211d244ce
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
    - unity-catalog-setup-guide-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-admin-roles
    - UCAR
    - Unity Catalog admin
    - Admin roles
  citations:
    - file: unity-catalog-setup-guide-databricks-on-aws.md
title: Unity Catalog Admin Roles
description: Account admin, workspace admin, and metastore admin roles with distinct scopes of administrative privilege in Unity Catalog.
tags:
  - unity-catalog
  - admin-roles
  - permissions
timestamp: "2026-06-19T21:55:12.434Z"
---

# Unity Catalog Admin Roles

**Unity Catalog Admin Roles** are the three built-in administrative roles that govern access and management within a Unity Catalog environment: [Account Admin](/concepts/account-admin-unity-catalog.md), [Workspace Admin](/concepts/workspace-admin-unity-catalog.md), and [Metastore Admin](/concepts/metastore-admin-role.md). Unity Catalog has three main admin roles, each with a different scope and responsibilities. ^[unity-catalog-setup-guide-databricks-on-aws.md]

## Account Admin

The **account admin** is the highest-level administrative role, scoped to the entire Databricks account. Account admins can perform tasks that affect all workspaces in the account, including: ^[unity-catalog-setup-guide-databricks-on-aws.md]

- Confirming that a workspace is enabled for Unity Catalog via the account console. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Creating a [Metastore](/concepts/metastore.md) if one does not already exist. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Attaching a workspace to a Unity Catalog [Metastore](/concepts/metastore.md). ^[unity-catalog-setup-guide-databricks-on-aws.md]

This role is required for initial Unity Catalog setup steps when the workspace lacks compute resources or is not yet attached to a [Metastore](/concepts/metastore.md). ^[unity-catalog-setup-guide-databricks-on-aws.md]

## Workspace Admin

The **workspace admin** handles most day-to-day administrative tasks within a single workspace. Responsibilities include: ^[unity-catalog-setup-guide-databricks-on-aws.md]

- Adding and removing users. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Organizing users into groups. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Assigning admin roles to other users. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Managing service principals. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Creating and managing compute resources (clusters, SQL warehouses). ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Configuring workspace settings. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Granting access to data via privileges. ^[unity-catalog-setup-guide-databricks-on-aws.md]

Databricks recommends being selective about who receives this role, as workspace admins have broad access to workspace resources and settings. This role is typically appropriate for members of a central data platform or IT team responsible for maintaining the workspace. ^[unity-catalog-setup-guide-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) Admin

The **metastore admin** is an optional administrative role scoped to the [Metastore](/concepts/metastore.md). Assign this role when specialized governance tasks are needed, such as: ^[unity-catalog-setup-guide-databricks-on-aws.md]

- Delegating catalog creation to non-workspace admins. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Managing the init script and JAR allowlist. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Receiving shared data through [OpenSharing](/concepts/opensharing.md). ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Transferring object ownership when a team member leaves. ^[unity-catalog-setup-guide-databricks-on-aws.md]

This role is often assigned to a dedicated data governance team or a small group of senior platform engineers. ^[unity-catalog-setup-guide-databricks-on-aws.md]

## Role Comparison

| Role | Scope | Typical Use |
|------|-------|-------------|
| **Account Admin** | Entire account | Enable Unity Catalog, create/attach metastores |
| **Workspace Admin** | Single workspace | Day-to-day user and compute management, granting access |
| **Metastore Admin** | [Metastore](/concepts/metastore.md) | Catalog creation delegation, allowlist, ownership transfer |

## Best Practices

- Use groups rather than individual users when granting privileges; this reduces administrative overhead as the team grows. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Assign the workspace admin role to members of a central platform or IT team; be selective to limit broad access. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- Assign the [Metastore](/concepts/metastore.md) admin role only when specific governance tasks such as catalog creation delegation or allowlist management are needed. ^[unity-catalog-setup-guide-databricks-on-aws.md]
- For most workspaces, the workspace admin role is the only administrator role required; [Metastore](/concepts/metastore.md) admin is optional. ^[unity-catalog-setup-guide-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that provides these admin roles
- [Metastore](/concepts/metastore.md) — The top-level container managed by [Metastore](/concepts/metastore.md) admins
- [Privileges](/concepts/privileges-and-ownership.md) — The fine-grained permissions model in Unity Catalog
- Workspace — The environment where workspace admins operate
- Allowlist — Managed by [Metastore](/concepts/metastore.md) admins for init scripts and JARs
- [OpenSharing](/concepts/opensharing.md) — Used to receive shared data, requiring [Metastore](/concepts/metastore.md) admin privileges

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md
- unity-catalog-setup-guide-databricks-on-aws.md

# Citations

1. [unity-catalog-setup-guide-databricks-on-aws.md](/references/unity-catalog-setup-guide-databricks-on-aws-962f6ec3.md)
