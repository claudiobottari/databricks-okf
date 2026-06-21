---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d79570f5acbc27074ca8e20ed3ac1616967a6b3acc5c4c51b018ef34bc90adda
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-permission-behavior-on-feature-table-creation
    - DPBOFTC
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Default Permission Behavior on Feature Table Creation
description: "Default permissions assigned when a feature table is created: creator and workspace admins get CAN MANAGE, all others get NO PERMISSIONS"
tags:
  - defaults
  - permissions
  - feature-store
timestamp: "2026-06-18T14:17:02.039Z"
---

# Default Permission Behavior on Feature Table Creation

**Default Permission Behavior on Feature Table Creation** describes the initial access control permissions automatically assigned to a new feature table in Databricks Feature Store (for workspaces not enabled for Unity Catalog).

## Overview

When a feature table is created in a workspace that is not enabled for [Unity Catalog](/concepts/unity-catalog.md), the system automatically assigns default permissions to the feature table metadata. These defaults determine who can view, edit, manage permissions, or delete the feature table from the outset. ^[access-control-legacy-databricks-on-aws.md]

## Default Permission Assignments

By default, when a feature table is created, the following permissions are applied: ^[access-control-legacy-databricks-on-aws.md]

- **The creator** receives **CAN MANAGE** permission
- **Workspace admins** receive **CAN MANAGE** permission
- **All other users** receive **NO PERMISSIONS**

This means that only the table creator and workspace administrators can initially view the feature table in the UI, edit its metadata, manage permissions for other users, or delete the table. Every other user in the workspace has no access to the feature table at all. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Feature store access control for non-Unity Catalog workspaces supports three permission levels: ^[access-control-legacy-databricks-on-aws.md]

- **CAN VIEW METADATA** — Allows viewing the feature table in the UI and its metadata
- **CAN EDIT METADATA** — Allows editing the feature table's description and metadata
- **CAN MANAGE** — Allows managing other users' permissions on the table, editing metadata, and deleting the table

## Modifying Default Permissions

### Per-Feature Table

To change permissions on an individual feature table, the owner or a user with CAN MANAGE permission can click the arrow to the right of the feature table name and select **Permissions** from the dropdown menu. If a user does not have CAN MANAGE permission, this option is not visible. ^[access-control-legacy-databricks-on-aws.md]

### For All Feature Tables

Workspace administrators or users with CAN MANAGE permission for the Feature Store can set permission levels on **all** feature tables — both existing and future — from the Feature Store page by clicking the **Permissions** button. ^[access-control-legacy-databricks-on-aws.md]

Permissions set at the Feature Store level:
- Apply to all future feature tables created in the workspace
- Can only be removed from the Feature Store page itself
- Can be overridden at the individual feature table level to **add** permissions (but not to restrict them further) ^[access-control-legacy-databricks-on-aws.md]

When viewing an individual feature table, permissions inherited from the Feature Store level are marked with the notice: *"Some permissions cannot be removed because they are inherited."* ^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Workspaces

If your workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md), use Unity Catalog privileges instead of Feature Store access control. The default permission behavior described on this page applies only to workspaces that are not enabled for Unity Catalog. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store Access Control](/concepts/feature-store-access-control-legacy.md) — The broader permissions system for feature tables
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The modern access control approach for Unity Catalog-enabled workspaces
- [Feature Table Management](/concepts/feature-tables.md) — Creating and managing feature tables
- [CAN MANAGE Permission](/concepts/can-manage-permission.md) — The highest permission level for feature tables

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
