---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdc89090d33d47b3f2b9232b02771af22104e223e71d88fc45f394a537fac571
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - can-view-metadata-permission
    - CVMP
    - CAN VIEW METADATA
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: CAN VIEW METADATA Permission
description: A permission level allowing users to view a feature table in the UI and see its metadata
tags:
  - access-control
  - permissions
  - feature-store
timestamp: "2026-06-19T21:55:18.359Z"
---

# CAN VIEW METADATA Permission

**CAN VIEW METADATA** is one of three permission levels available in the [Feature Store (legacy)](/concepts/databricks-workspace-feature-store-legacy.md) on Databricks for controlling access to feature table metadata. It is used in workspaces that are not enabled for [Unity Catalog](/concepts/unity-catalog.md). This permission grants a user the ability to see a feature table in the Databricks UI and view its metadata, but does not allow editing the description, managing permissions for other users, or deleting the table. ^[access-control-legacy-databricks-on-aws.md]

## Granting and Inheritance

By default, when a feature table is created, the creator and workspace administrators receive **CAN MANAGE** permission, while all other users have **NO PERMISSIONS**. Workspace administrators or users with CAN MANAGE permission can assign the CAN VIEW METADATA level to specific users or groups either on the individual feature table page or globally on the Feature Store page. Permissions set globally on the Feature Store page apply to all current and future feature tables and cannot be overridden with a more restrictive setting on individual tables. ^[access-control-legacy-databricks-on-aws.md]

## Comparison with Other Permission Levels

| Permission | Abilities |
|------------|-----------|
| CAN VIEW METADATA | View the feature table and its metadata in the UI |
| CAN EDIT METADATA | View and edit the feature table’s description |
| CAN MANAGE | View, edit, manage permissions for other users, and delete the feature table |

^[access-control-legacy-databricks-on-aws.md]

These permissions only control access to metadata; they do not control read or write access to the underlying data in the feature table. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store (legacy)](/concepts/databricks-workspace-feature-store-legacy.md)  
- [CAN EDIT METADATA Permission](/concepts/can-edit-metadata-permission.md)  
- [CAN MANAGE Permission](/concepts/can-manage-permission.md)  
- [Unity Catalog](/concepts/unity-catalog.md) (recommended for newer workspaces)  
- [Access control for feature tables](/concepts/unity-catalog-access-control-for-feature-tables.md)  

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
