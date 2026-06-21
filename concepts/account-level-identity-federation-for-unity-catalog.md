---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6eae737993d39ded073b71838cf75bc3d33b09016ed5e1afc00df1459550920d
  pageDirectory: concepts
  sources:
    - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-level-identity-federation-for-unity-catalog
    - AIFFUC
  citations:
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
title: Account-Level Identity Federation for Unity Catalog
description: Enabling Unity Catalog shifts identity management from workspace-level to account-level interfaces, requiring SCIM provisioning connectors and automation to target account endpoints.
tags:
  - unity-catalog
  - identity-management
  - scim
  - databricks
timestamp: "2026-06-18T12:10:03.536Z"
---

# Account-Level [Identity Federation for Unity Catalog](/concepts/identity-federation-for-unity-catalog.md)

**Account-Level Identity Federation for Unity Catalog** is a mechanism that allows Databricks workspace admins to manage identities — including users, groups, and service principals — centrally using account-level interfaces rather than workspace-level tools. When a workspace is enabled for Unity Catalog, identity federation is automatically activated, enabling account admins to handle identity provisioning and user-to-workspace assignment from the account console. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## How Identity Federation Works

When you assign a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) to a workspace, the workspace becomes "enabled for Unity Catalog." As part of this process, the workspace's identity management is federated to the account level. This means that all users, groups, and service principals for that workspace must be managed through account-level tools — such as the account console, account-level SCIM provisioning, or Terraform — rather than through workspace-level SCIM endpoints. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

### Key Effects

- **Centralized identity management:** Account admins can manage all identities across multiple workspaces from a single account console. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Workspace assignment:** Account admins can assign users to workspaces directly from account-level interfaces. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **SCIM provisioning shift:** Any existing SCIM provisioning connectors or automation that were configured to use workspace-level endpoints must be updated to use account-level SCIM endpoints after enabling Unity Catalog. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Irreversible:** Once a workspace is enabled for Unity Catalog, identity management is permanently moved to the account level and cannot be reverted. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Requirements

Account-level identity federation is automatically enabled when a workspace is assigned to a Unity Catalog [Metastore](/concepts/metastore.md). Before enabling a workspace, you must have a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) configured for your Databricks account. The [Metastore](/concepts/metastore.md) acts as the top-level container for data and exposes the three-level namespace (`catalog.schema.table`) for data organization. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Implications for Workspace Admins

When account-level identity federation is active, workspace admins retain the ability to manage operations within their workspace — such as adding users and service principals, creating clusters, and delegating other workspace admins. However, they no longer manage the identity layer directly. Account admins can further restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

If a workspace was not enabled for Unity Catalog automatically (i.e., it was enabled after initial creation), workspace admins have no more access to Unity Catalog objects by default than any other user. They do retain the ability to perform workspace management tasks such as managing job ownership and viewing notebooks, which may provide indirect access to data registered in Unity Catalog. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Best Practices

- **Update automation early.** Before enabling a workspace for Unity Catalog, update any SCIM provisioning connectors and Terraform configurations to use account-level endpoints instead of workspace-level endpoints. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Review workspace admin assignments.** Understand the privileges that workspace admins will have and distribute the role carefully. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Use workspace-catalog bindings.** If you use workspaces to isolate user data access, consider binding catalogs and external locations to specific workspaces so that workspace admins and users can only access data from designated environments. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that requires account-level identity federation
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for data in Unity Catalog
- SCIM Provisioning — How to configure SCIM at the account level
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) — Limiting catalog access by workspace boundaries
- [Restrict Workspace Admins](/concepts/restrictworkspaceadmins-setting.md) — Account-level setting to limit workspace admin privileges

## Sources

- enable-a-workspace-for-unity-catalog-databricks-on-aws.md

# Citations

1. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
