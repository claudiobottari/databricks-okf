---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b4cd0f0299f0be6e4dbbf2b1a286440d18092e85e6284c406fab4e6c2c86c7c
  pageDirectory: concepts
  sources:
    - upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-level-identity-provisioning-for-unity-catalog
    - AIPFUC
    - Account-Level SCIM Provisioning
    - Account-level SCIM provisioning
  citations:
    - file: upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md
title: Account-Level Identity Provisioning for Unity Catalog
description: The requirement to provision users, groups, and service principals at the Databricks account level rather than workspace level for Unity Catalog compatibility.
tags:
  - databricks
  - unity-catalog
  - identity
  - scim
timestamp: "2026-06-19T23:17:50.367Z"
---

# Account-Level Identity Provisioning for [Unity Catalog](/concepts/unity-catalog.md)

**Account-Level Identity Provisioning for Unity Catalog** is the process of synchronizing users, groups, and service principals from an identity provider (IdP) directly to a Databricks account rather than to individual workspaces. This is a prerequisite for upgrading to [Unity Catalog](/concepts/unity-catalog.md), which requires account-level identities for centralized governance and access control.

## Overview

[Unity Catalog](/concepts/unity-catalog.md) references account-level identities. Before attaching a [Metastore](/concepts/metastore.md) to a workspace, organizations must migrate from workspace-level identity provisioning to account-level provisioning. This shift enables [Unity Catalog](/concepts/unity-catalog.md) to apply consistent access controls across all workspaces within an account. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Prerequisites

To perform account-level identity provisioning, you must be a Databricks account admin. For most setup steps, account admin permissions are required unless otherwise specified in task-specific documentation. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Migration Steps

### Turn Off Workspace-Level Provisioning

If you are using SCIM to provision users, groups, and service principals from your IdP to your workspace, you must turn it off. Instead, set up provisioning directly to your Databricks account. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Update Automation

Update any automation that manages identities — such as SCIM provisioning connectors and Terraform automation — so that they reference account endpoints instead of workspace endpoints. For detailed guidance, see the documentation on Account-level and workspace-level SCIM provisioning. ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

### Convert Workspace-Local Groups to Account-Level Groups

After account-level identities are in place, convert any workspace-local groups to account-level groups. This ensures that group membership and permissions are centralized and available to [Unity Catalog](/concepts/unity-catalog.md). ^[upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md]

## Benefits for [Unity Catalog](/concepts/unity-catalog.md)

Account-level identity provisioning is essential for [Unity Catalog](/concepts/unity-catalog.md) because it enables:

- **Centralized governance**: All identity management flows through the account, providing a single source of truth for users, groups, and service principals.
- **Consistent permissions**: [Unity Catalog](/concepts/unity-catalog.md) can apply the same access controls across all workspaces attached to the same [Metastore](/concepts/metastore.md).
- **Simplified administration**: Administrators manage identities in one place rather than per-workspace.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that requires account-level identities.
- SCIM provisioning — The protocol used to synchronize identities from an IdP to Databricks.
- [Metastore](/concepts/metastore.md) — The container for [Unity Catalog](/concepts/unity-catalog.md) metadata, attached to workspaces.
- Workspace-local groups — Groups that exist only within a single workspace and must be migrated to account-level groups.
- [Upgrade a workspace to Unity Catalog](/concepts/workspace-catalog-unity-catalog.md) — The broader process that includes identity provisioning as a first step.

## Sources

- upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md

# Citations

1. [upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws.md](/references/upgrade-a-databricks-workspace-to-unity-catalog-databricks-on-aws-30141815.md)
