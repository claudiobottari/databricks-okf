---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffeb8303f4c12046668353aa1a58a994d3f1bcb3035d3cac961bc335955f41de
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-admin-privileges-in-feature-store
    - WAPIFS
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Workspace Admin Privileges in Feature Store
description: Workspace administrators automatically have CAN MANAGE permission on all feature tables and can set permissions on the entire Feature Store
tags:
  - access-control
  - permissions
  - admin
  - databricks
timestamp: "2026-06-19T21:55:35.561Z"
---

# Workspace Admin Privileges in Feature Store

**Workspace Admin Privileges in Feature Store** refers to the elevated permissions that workspace administrators automatically receive for feature table metadata in Databricks Feature Store workspaces that are not enabled for Unity Catalog. These privileges allow administrators to manage access control across all feature tables in the workspace.

## Default Permissions

When a feature table is created in a workspace not enabled for Unity Catalog, the following default permissions are assigned:

- The creator of the feature table receives **CAN MANAGE** permission
- **Workspace admins** receive **CAN MANAGE** permission
- All other users receive **NO PERMISSIONS**

^[access-control-legacy-databricks-on-aws.md]

## CAN MANAGE Permission

The **CAN MANAGE** permission level is the highest permission level available for feature table metadata. Users with this permission can:

- View the feature table in the UI
- Edit the feature table's description
- Manage other users' permissions on the feature table
- Delete the feature table

^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for All Feature Tables

Workspace administrators can use the Feature Store UI to set permission levels on all feature tables for specific users or groups. This capability is available only to workspace administrators and users who have CAN MANAGE permission for the Feature Store itself. ^[access-control-legacy-databricks-on-aws.md]

To configure permissions for all feature tables:

1. Navigate to the Feature Store page.
2. Click the **Permissions** button (visible only to workspace administrators and users with CAN MANAGE permission for the Feature Store).
3. Edit the permissions and click **Save**.

Permissions set from the Feature Store page apply to all existing and future feature tables. These permissions can only be removed from the Feature Store page, not from individual feature table pages. ^[access-control-legacy-databricks-on-aws.md]

## Inheritance Behavior

When permissions are set from the Feature Store page, they are inherited by individual feature tables. On a specific feature table page, inherited permissions are marked with the message "Some permissions cannot be removed because they are inherited." Users can add additional permissions on individual feature table pages, but they cannot set more restrictive permissions than those inherited from the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for Individual Feature Tables

Workspace administrators with CAN MANAGE permission for a specific feature table can also configure permissions on that individual table:

1. On the feature table page, click the arrow to the right of the feature table name and select **Permissions**.
2. Edit the permissions and click **Save**.

This option is only available to users with CAN MANAGE permission for the specific feature table. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store Access Control](/concepts/feature-store-access-control-legacy.md) — Overview of permission levels for feature table metadata
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Alternative access control for workspaces enabled for Unity Catalog
- [Feature Table Metadata](/concepts/feature-table.md) — The metadata objects that workspace admins can manage
- [CAN MANAGE Permission](/concepts/can-manage-permission.md) — The highest permission level for feature tables

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
