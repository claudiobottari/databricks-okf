---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a555bb4f76b7496bfe943f3a1e24680151306696bb7c588900124557b3aefa35
  pageDirectory: concepts
  sources:
    - flag-data-as-certified-or-deprecated-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - permissions-for-governed-tags
    - PFGT
    - Manage Permissions on Governed Tags
    - Manage permissions on governed tags
    - manage permissions on governed tags
  citations:
    - file: flag-data-as-certified-or-deprecated-databricks-on-aws.md
title: Permissions for Governed Tags
description: The ASSIGN permission on system.certification_status governed tag required to apply certification status to objects, along with APPLY TAG, USE SCHEMA, and USE CATALOG privileges on the target object.
tags:
  - data-governance
  - permissions
  - unity-catalog
timestamp: "2026-06-19T18:52:44.174Z"
---

# Permissions for Governed Tags

**Permissions for Governed Tags** control which users and service principals can assign governed tags — such as the `system.certification_status` tag — to objects within Unity Catalog. These permissions are enforced separately from object ownership and standard SQL privileges.

## Overview

Governed tags require a specific permission, `ASSIGN`, to be applied to objects. In addition, users must meet the standard tag privilege requirements on the target Unity Catalog securable object. The exact combination of permissions depends on whether the tag is a system‑governed tag (like `system.certification_status`) or a user‑defined tag. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Permissions Required for the `system.certification_status` Tag

To apply the `system.certification_status` governed tag to an object, a user or service principal must have the **`ASSIGN` permission on that tag**. This permission is managed separately from object‑level privileges. For further details on managing this permission, see the documentation on [Manage permissions on governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/manage-permissions). ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## General Tag Permissions on Unity Catalog Objects

In addition to the `ASSIGN` permission on the governed tag itself, users who want to add tags (including `system.certification_status`) to Unity Catalog securable objects must fulfill one of the following:

- **Own the object**, or
- Have **all** of the following privileges:
  - `APPLY TAG` on the object
  - `USE SCHEMA` on the object’s parent schema
  - `USE CATALOG` on the object’s parent catalog

These privileges ensure that the user has the necessary access to the object’s schema and catalog hierarchy before they can assign a tag. ^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Supported Object Types

The `system.certification_status` governed tag can be assigned to the following Unity Catalog securable objects, each subject to the permissions described above:

- Catalogs
- Schemas
- Tables
- Views
- Volumes
- Functions
- Registered models
- Dashboards
- Genie Spaces
- Databricks Apps
- Notebooks

^[flag-data-as-certified-or-deprecated-databricks-on-aws.md]

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md) – The broader framework for system‑managed tags in Unity Catalog.
- [Unity Catalog](/concepts/unity-catalog.md) – The underlying [Metastore](/concepts/metastore.md) that governs permissions and object hierarchy.
- Data Governance – Organizational policies that governed tags help enforce.
- Data Lineage and Discoverability – How certified/deprecated tags affect data discovery in the workspace.

## Sources

- flag-data-as-certified-or-deprecated-databricks-on-aws.md

# Citations

1. [flag-data-as-certified-or-deprecated-databricks-on-aws.md](/references/flag-data-as-certified-or-deprecated-databricks-on-aws-ee1b377b.md)
