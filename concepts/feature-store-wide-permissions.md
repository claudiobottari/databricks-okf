---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd175a7a082a09b733a4231837524f867303d2188e013c58ac6f95d617c3b473
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-wide-permissions
    - FSP
    - Feature Store permissions
    - Effective Permissions
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store-Wide Permissions
description: Workspace administrators can set permissions for all current and future feature tables from the Feature Store UI.
tags:
  - access-control
  - feature-store
  - administration
timestamp: "2026-06-19T17:24:10.983Z"
---

# Feature Store Wide Permissions

**Feature Store wide permissions** allow workspace administrators to set access control levels on all feature tables within a legacy (non–Unity Catalog) Feature Store at once. These permissions apply to both existing and future feature tables, providing a consistent baseline for users and groups across the entire Feature Store.

## Overview

In workspaces not enabled for Unity Catalog, the Databricks Feature Store uses a fine-grained permission model with three levels: **CAN VIEW METADATA**, **CAN EDIT METADATA**, and **CAN MANAGE**. By default, the feature table creator and workspace admins have CAN MANAGE permission; other users have no permissions. To avoid setting permissions on every feature table individually, administrators and delegated users can configure wide permissions at the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]

## How Wide Permissions Work

A user with CAN MANAGE permission for the Feature Store (or a workspace administrator) can change permissions for all other users from the Feature Store UI. Permissions set at this level:

- Apply to **all existing feature tables** in the Feature Store.
- Also apply to **all future feature tables** created after the wide permission is set.
- Can only be removed or modified from the Feature Store page itself – not from individual feature table pages. ^[access-control-legacy-databricks-on-aws.md]

## Setting Wide Permissions

1. On the Feature Store page, click **Permissions**. This button is visible only to workspace administrators and users with CAN MANAGE permission for the Feature Store.
2. Edit the permissions and click **Save**.

![Drop-down menu where you select permissions](https://docs.databricks.com/aws/en/assets/images/feature-store-wide-permissions-65c0edf83a192ef0b3b1adf7395003e8.png)

## Behavior and Inheritance

When a user navigates to a specific feature table page, permissions inherited from the Feature Store level are marked with the note “Some permissions cannot be removed because they are inherited.” This indicates that the wide permission cannot be removed from the table-level settings. However, a user with CAN MANAGE permission on the table can **add** additional permissions to the table (granting more access to others), but **cannot set more restrictive permissions** than those inherited from the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]

This inheritance model ensures that wide permissions provide a minimum baseline, while allowing per-table grants to extend access as needed.

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – The legacy Feature Store for workspace-level feature tables.
- Access Control (legacy) – Detailed description of the three permission levels (CAN VIEW METADATA, CAN EDIT METADATA, CAN MANAGE).
- [Unity Catalog](/concepts/unity-catalog.md) – The modern governance solution that replaces legacy access control.
- Feature Store Permissions (individual table) – How to set permissions on a single feature table.
- [CAN MANAGE](/concepts/can-manage-permission.md) – The highest permission level in the legacy Feature Store.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
