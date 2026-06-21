---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92d4e3445348770876da2e14e5ee0d51b1effe51a37c9c7caa40c1dae317a815
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-default-permissions
    - FTDP
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Table Default Permissions
description: By default, the creator and workspace admins get CAN MANAGE, while other users have NO PERMISSIONS on a new feature table.
tags:
  - access-control
  - feature-store
  - defaults
timestamp: "2026-06-19T17:24:14.762Z"
---

# Feature Table Default Permissions

**Feature Table Default Permissions** define the initial access control levels automatically assigned to a [Feature Table](/concepts/feature-table.md) at the time of its creation in workspaces not enabled for [Unity Catalog](/concepts/unity-catalog.md). These defaults establish who can view, edit, manage, or delete feature table metadata.

## Default Permission Levels

When a feature table is created, three permission levels are available: **CAN VIEW METADATA**, **CAN EDIT METADATA**, and **CAN MANAGE**. The system assigns the following defaults: ^[access-control-legacy-databricks-on-aws.md]

- **The creator** receives **CAN MANAGE** permission. ^[access-control-legacy-databricks-on-aws.md]
- **Workspace admins** receive **CAN MANAGE** permission. ^[access-control-legacy-databricks-on-aws.md]
- **All other users** receive **NO PERMISSIONS** by default. ^[access-control-legacy-databricks-on-aws.md]

This means that only the table creator and workspace administrators can initially manage permissions, edit metadata, or view metadata for a newly created feature table. Regular users have no access until explicitly granted.

## Permissions Overview

| Permission Level | Abilities |
|------------------|-----------|
| CAN VIEW METADATA | View the feature table in the UI |
| CAN EDIT METADATA | Edit the description and other metadata |
| CAN MANAGE | Manage other users' permissions, delete the table |

Any user can create a new feature table, but only the creator and workspace admins have CAN MANAGE by default.

## Scope

This default permission model applies to workspaces **not** enabled for Unity Catalog. For Unity Catalog-enabled workspaces, use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

## Changing Default Permissions

Workspace administrators can configure default permissions for all feature tables in the Feature Store from the Feature Store page. Settings made at the Feature Store level apply to all **future** feature tables. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Access control (legacy)](/concepts/feature-table-access-control-legacy.md)
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md)
- [Feature Store](/concepts/feature-store.md)
- Feature Store permissions

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
