---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 327281f9858e24d9bcba6ba7b1c841c0cf4bd3b5db9fdc8b94d5b77da74ca38d
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - configuring-permissions-on-individual-feature-tables
    - CPOIFT
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Configuring Permissions on Individual Feature Tables
description: Procedure to edit permissions on a single feature table via the UI, requiring CAN MANAGE to modify
tags:
  - configuration
  - permissions
  - feature-store
timestamp: "2026-06-18T14:16:41.199Z"
---

# Configuring Permissions on Individual Feature Tables

In workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md), you can use Feature Store access control to grant fine-grained permissions on feature table metadata. This allows you to control a user’s ability to view a feature table in the UI, edit its description, manage other users’ permissions on the table, and delete the table. ^[access-control-legacy-databricks-on-aws.md]

If your workspace is enabled for Unity Catalog, use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

You can assign three permission levels to feature table metadata: ^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Abilities |
|------------------|-----------|
| `CAN VIEW METADATA` | View the feature table in the UI |
| `CAN EDIT METADATA` | View and edit the description and other metadata |
| `CAN MANAGE` | Full control, including managing other users’ permissions and deleting the table |

Any user can create a new feature table. By default, when a feature table is created: ^[access-control-legacy-databricks-on-aws.md]

- The creator has `CAN MANAGE` permission.
- Workspace admins have `CAN MANAGE` permission.
- Other users have **NO PERMISSIONS**.

## Configuring Permissions on a Single Feature Table

1. On the feature table page, click the arrow to the right of the feature table name and select **Permissions**. This option is only visible if you have `CAN MANAGE` permission for that feature table.  
   ![Permissions drop-down menu](https://docs.databricks.com/aws/en/assets/images/feature-store-permissions-840e0dfb9dce73d02e7e520219a4b652.png)
2. Edit the permissions and click **Save**. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for All Feature Tables (Feature Store Level)

Workspace administrators (and users with `CAN MANAGE` permission on the Feature Store itself) can set default permission levels on **all** current and future feature tables from the Feature Store page. ^[access-control-legacy-databricks-on-aws.md]

1. On the feature store page, click **Permissions**. This button is only available for workspace administrators and users with `CAN MANAGE` on the Feature Store.  
   ![Feature Store Permissions button](https://docs.databricks.com/aws/en/assets/images/feature-store-wide-permissions-65c0edf83a192ef0b3b1adf7395003e8.png)
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level can only be removed from that page. On an individual feature table page, you can add extra permissions beyond the Feature Store‑level defaults, but you **cannot** set more restrictive permissions than those defaults. When viewing a specific feature table, permissions inherited from the Feature Store are marked as “Some permissions cannot be removed because they are inherited.” ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — Recommended governance solution for workspaces that support it.
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Alternative authorization model for Unity Catalog‑enabled workspaces.
- [Feature Store](/concepts/feature-store.md) — Central repository for feature tables and their metadata.
- Access Control Lists (ACLs) — General Databricks permissions model.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
