---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 508e363d34b2ee7780aa3b981178e835c89c3c9a07ab09c47c51acab625d29cf
  pageDirectory: concepts
  sources:
    - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-level-identity-management-for-unity-catalog
    - AIMFUC
    - Account‑level Identity Management
  citations:
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
title: Account-Level Identity Management for Unity Catalog
description: The shift from workspace-level to account-level management of users, groups, and service principals when Unity Catalog is enabled, requiring updates to SCIM and automation.
tags:
  - unity-catalog
  - identity-management
  - scim
  - databricks
timestamp: "2026-06-19T18:39:28.679Z"
---

```markdown
# Account-Level Identity Management for Unity Catalog

**Account-Level Identity Management for Unity Catalog** refers to the practice of managing users, groups, and service principals for workspaces enabled with Unity Catalog using account-level interfaces rather than workspace-level interfaces. This centralization enables consistent identity federation, simplified administration, and unified access control across multiple workspaces within a Databricks account.

## Overview

When you enable a workspace for Unity Catalog, identity management shifts from workspace-level administration to account-level administration. This means that account admins manage users, groups, and service principals centrally through the account console and other account-level interfaces, rather than separately within each workspace. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

The key implications of account-level identity management include:

- **Identity federation**: Workspace admins can manage identities centrally using the account console, including assigning users to workspaces. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Consistent data access**: Users across different workspaces in the same account can potentially access the same data, and data stewards can manage that access centrally across workspaces. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Audited data access**: Data access is audited automatically. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## SCIM Provisioning Considerations

When you enable a workspace for Unity Catalog, any automation configured to manage users, groups, and service principals—such as SCIM provisioning connectors and Terraform automation—must be updated to refer to account-level endpoints instead of workspace-level endpoints. See Account-level and workspace-level SCIM provisioning for more details. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Impact on Workspace Admin Privileges

Workspace admins retain the ability to manage operations for their workspace, including adding users and service principals, creating clusters, and delegating other users to be workspace admins. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

However, the default Unity Catalog privileges for workspace admins depend on how the workspace was enabled:

- **Automatic enablement**: Workspace admins have additional privileges by default, including the ability to create most Unity Catalog object types and grant access to the objects they create. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- **Manual enablement**: Workspace admins have no more access to Unity Catalog objects by default than any other user, but they retain the ability to perform workspace management tasks such as managing job ownership and viewing notebooks, which may give indirect access to data registered in Unity Catalog. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. See [[RestrictWorkspaceAdmins Setting|Restrict workspace admins]] for more details. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Workspace-Catalog Binding

If you use workspaces to isolate user data access, you can use workspace-catalog bindings. These bindings enable you to limit catalog access by workspace boundaries. For example, you can ensure that workspace admins and users can only access production data in `prod_catalog` from a production workspace environment, `prod_workspace`. The default is to share the catalog with all workspaces attached to the current [[metastore|Metastore]]. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

Similarly, you can bind access to external locations such that they are accessible only from specified workspaces. See [[Workspace-catalog binding]] and [[External location|Assign an external location to specific workspaces]]. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Permanent Change

Enabling a workspace for Unity Catalog **cannot be reversed**. Once you enable the workspace, you will manage users, groups, and service principals for this workspace using account-level interfaces. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [[Unity Catalog metastore]] — The top-level container for data in Unity Catalog, which exposes a three-level namespace (`catalog.schema.table`).
- [[Cross-Workspace Feature Sharing|Multi-workspace data sharing]] — How a single [[metastore|Metastore]] can be shared across multiple workspaces.
- [[Workspace-catalog binding]] — Restricting catalog access to specific workspaces.
- [[Account-Level Identity Provisioning for Unity Catalog|Account-level SCIM provisioning]] — Managing identities at the account level using SCIM.
- Admin privileges in Unity Catalog — Detailed breakdown of workspace admin permissions.
- [[RestrictWorkspaceAdmins Setting|Restrict workspace admins]] — Account-level setting to limit workspace admin capabilities.

## Sources

- enable-a-workspace-for-unity-catalog-databricks-on-aws.md
```

# Citations

1. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
