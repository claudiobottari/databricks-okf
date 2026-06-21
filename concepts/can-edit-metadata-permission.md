---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1bfd296e87c8d59c79867608dc60cbd73d190d21f6086724bd08e5813c1ca90
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - can-edit-metadata-permission
    - CEMP
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: CAN EDIT METADATA Permission
description: A permission level allowing users to view and edit a feature table's description and metadata
tags:
  - access-control
  - permissions
  - feature-store
timestamp: "2026-06-19T21:55:34.646Z"
---

# CAN EDIT METADATA Permission

The **CAN EDIT METADATA Permission** is one of three permission levels available for controlling access to [Feature Store (legacy)](/concepts/databricks-workspace-feature-store-legacy.md) feature tables on Databricks workspaces that are not enabled for [Unity Catalog](/concepts/unity-catalog.md). It grants a user the ability to modify a feature table’s metadata — for example, editing its description — without granting broader management or deletion rights. ^[access-control-legacy-databricks-on-aws.md]

## Overview

In the legacy Feature Store access control model, you can assign three permission levels to feature table metadata: [CAN VIEW METADATA](/concepts/can-view-metadata-permission.md), **CAN EDIT METADATA**, and [CAN MANAGE](/concepts/can-manage-permission.md). The official documentation includes a table that lists the specific abilities for each permission level. Any user can create a new feature table, but once created, access is restricted based on the assigned permissions. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

By default, when a feature table is created:

- The creator has **CAN MANAGE** permission.
- Workspace admins have **CAN MANAGE** permission.
- All other users have **NO PERMISSIONS**.

This means that, out of the box, only the creator and workspace admins can edit metadata or manage the table; other users must be explicitly granted CAN EDIT METADATA (or a higher level) to make changes. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions

### On a Single Feature Table

1. On the feature table page, click the arrow to the right of the table’s name and select **Permissions**.
2. Edit the permissions (e.g., add or remove CAN EDIT METADATA for a user or group) and click **Save**.

> **Note:** This option is only visible if you have CAN MANAGE permission for the feature table. ^[access-control-legacy-databricks-on-aws.md]

### On All Feature Tables (Feature Store Level)

Workspace administrators or users with CAN MANAGE permission for the entire Feature Store can set default permission levels that apply to all current and future feature tables.

1. On the Feature Store page, click **Permissions**.
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level are inherited by individual feature tables. They can only be removed from the Feature Store page, not from the individual table page. On the individual table page, you can grant additional permissions (including CAN EDIT METADATA), but you cannot set more restrictive permissions than those inherited from the store level. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store (legacy)](/concepts/databricks-workspace-feature-store-legacy.md) – The context in which this permission is used.
- [CAN VIEW METADATA](/concepts/can-view-metadata-permission.md) – The read-only permission level.
- [CAN MANAGE](/concepts/can-manage-permission.md) – The highest permission level, allowing editing, permission management, and deletion.
- [Unity Catalog](/concepts/unity-catalog.md) – The modern data governance model for workspaces; if enabled, use Unity Catalog privileges instead of these legacy permissions.
- [Workspace admins](/concepts/workspace-admins-unity-catalog.md) – Users who receive default CAN MANAGE access on all feature tables.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
