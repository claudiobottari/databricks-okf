---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6f61aa440dc2fee103507d3f14adf216c96ff66863e9379acb73ce1d358428b
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-access-control-vs-unity-catalog
    - FSACVUC
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store Access Control vs Unity Catalog
description: Legacy access control for feature tables in workspaces not enabled for Unity Catalog; workspaces with Unity Catalog should use UC privileges instead.
tags:
  - databricks
  - access-control
  - feature-store
  - unity-catalog
timestamp: "2026-06-19T08:49:29.289Z"
---

# Feature Store Access Control vs Unity Catalog

**Feature Store Access Control vs Unity Catalog** describes two distinct permission models for managing access to [Feature Tables](/concepts/feature-tables.md) in Databricks. The key difference is whether the workspace is enabled for [Unity Catalog](/concepts/unity-catalog.md) or uses the legacy workspace-level Feature Store.

## Overview

The access control model you use depends on your workspace configuration. Workspaces not enabled for Unity Catalog use a legacy access control model specific to the Feature Store, while workspaces enabled for Unity Catalog leverage Unity Catalog's unified privilege model. ^[access-control-legacy-databricks-on-aws.md]

## Legacy Feature Store Access Control

In workspaces without Unity Catalog, Feature Store access control provides fine-grained permissions on feature table **metadata** only. You can control a user's ability to view a feature table in the UI, edit its description, manage permissions, and delete the table — but the actual data access is governed separately. ^[access-control-legacy-databricks-on-aws.md]

### Permission Levels

Three permission levels are available for feature table metadata: ^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Abilities |
|-----------------|-----------|
| CAN VIEW METADATA | View the feature table in the UI |
| CAN EDIT METADATA | Edit the feature table description and metadata |
| CAN MANAGE | Manage permissions for other users, delete the table |

Any user can **create** a new feature table. The creator automatically receives CAN MANAGE permission on tables they create. ^[access-control-legacy-databricks-on-aws.md]

### Default Permissions

When a feature table is created: ^[access-control-legacy-databricks-on-aws.md]

- The creator has CAN MANAGE permission
- Workspace admins have CAN MANAGE permission
- Other users have NO PERMISSIONS

### Configuring Permissions

**Per-table permissions:** On the feature table page, click the arrow next to the table name and select **Permissions**. This option is only visible to users with CAN MANAGE permission on that table. ^[access-control-legacy-databricks-on-aws.md]

**Broad permissions for all tables:** Workspace administrators (or users with CAN MANAGE permission for the Feature Store) can set permission levels on all feature tables at once from the Feature Store page's **Permissions** button. These settings also apply to all future feature tables. ^[access-control-legacy-databricks-on-aws.md]

Permissions set at the Feature Store level can only be removed from that page. On individual feature table pages, you can add permissions (overriding the inherited settings) but cannot set more restrictive permissions than those inherited from the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Access Control

For workspaces enabled with Unity Catalog, access control is managed through [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) rather than the Feature Store's legacy permission model. This provides a unified governance framework that applies across all data assets, including feature tables. ^[access-control-legacy-databricks-on-aws.md]

In the Unity Catalog model, feature tables are treated like any other [catalog object](/concepts/unity-catalog-securable-objects.md) and are secured using standard Unity Catalog privileges such as SELECT, MODIFY, and MANAGE. This allows administrators to use consistent permissions across tables, views, models, and functions.

## Key Differences

| Aspect | Legacy Feature Store | Unity Catalog |
|--------|---------------------|---------------|
| **Scope** | Feature table metadata only | Full data + metadata governance |
| **Integration** | Standalone Feature Store model | Unified across all data assets |
| **Permission types** | CAN VIEW METADATA, CAN EDIT METADATA, CAN MANAGE | Standard UC privileges (SELECT, MODIFY, etc.) |
| **Inheritance** | Feature Store → table level | Catalog → schema → table level |
| **Data access** | Governed separately | Governed within the same model |

## Migration Considerations

When migrating from the legacy Feature Store to Unity Catalog, permissions set using the legacy model do not automatically transfer. Administrators need to configure [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) equivalent to the desired access levels for feature tables.

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)
- [Feature Store Overview](/concepts/feature-store.md)
- Data Governance in Databricks
- [Workspace-Level Feature Store](/concepts/workspace-feature-store-ui.md)

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
