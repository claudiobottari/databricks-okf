---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd19f1c669abf658be694440268adf197599e2367a5764ba61a57d23cde9d38d
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - configuring-permissions-on-an-individual-feature-table
    - CPOAIFT
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Configuring Permissions on an Individual Feature Table
description: How to set or override permissions for a specific feature table via its Permissions dropdown.
tags:
  - access-control
  - feature-store
  - configuration
timestamp: "2026-06-19T17:24:12.901Z"
---

# Configuring Permissions on an Individual Feature Table

In workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md), you can use the [Feature Store](/concepts/feature-store.md) (legacy) access control system to grant fine‑grained permissions on feature table metadata. This allows you to control a user’s ability to view a feature table in the UI, edit its description, manage other users’ permissions, and delete the table. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Three permission levels can be assigned to feature table metadata:

| Permission Level | Capabilities |
|------------------|--------------|
| **CAN VIEW METADATA** | View the feature table in the UI and its metadata. |
| **CAN EDIT METADATA** | Edit the feature table’s description and other metadata. |
| **CAN MANAGE** | Manage permissions for other users, edit metadata, and delete the feature table. |

Any user can create a new feature table. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

When a feature table is first created:

*   The creator automatically receives **CAN MANAGE** permission.
*   Workspace administrators automatically receive **CAN MANAGE** permission.
*   All other users have **NO PERMISSIONS**.

^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions on an Individual Table

To change permissions for a specific feature table:

1.  On the feature table’s page, click the arrow to the right of the feature table name and select **Permissions**.
2.  Edit the permissions as desired and click **Save**.

Only users who already have **CAN MANAGE** permission on that feature table will see the **Permissions** option in the drop‑down menu. ^[access-control-legacy-databricks-on-aws.md]

## Inheritance from Feature Store–Wide Permissions

Workspace administrators (or users with **CAN MANAGE** on the entire Feature Store) can set a default permission level that applies to **all** feature tables (including future tables) from the Feature Store overview page.

When you navigate to an individual feature table, permissions inherited from the Feature Store level are marked as “Some permissions cannot be removed because they are inherited.” On the individual table page you can **add** permissions on top of the inherited ones, but you cannot set more restrictive permissions than those inherited from the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]

## Important Notes

*   Permissions set from the Feature Store page apply to all existing and future feature tables.
*   To remove a permission that was set at the Feature Store level, you must do so from the Feature Store page—it cannot be removed from an individual table’s permissions dialog.
*   If your workspace is enabled for Unity Catalog, use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead of this legacy access control system.

## Related Concepts

*   [Feature Store](/concepts/feature-store.md)
*   [Access Control (Legacy)](/concepts/feature-table-access-control-legacy.md)
*   [Unity Catalog](/concepts/unity-catalog.md) — The recommended data governance model for modern Databricks workspaces.
*   [Feature Table Metadata](/concepts/feature-table.md)
*   [CAN MANAGE Permission](/concepts/can-manage-permission.md)

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
