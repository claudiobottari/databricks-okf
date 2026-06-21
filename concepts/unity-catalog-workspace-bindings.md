---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e0fad9cdef5cea57155f570e9d56fe2eeb82876c1f1d33dfab4e7357ea0f7e1
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-workspace-bindings
    - UCWB
    - External Location Workspace Binding
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Workspace Bindings
description: Mechanism to restrict which workspaces can access specific catalogs, external locations, and storage credentials.
tags:
  - access-control
  - unity-catalog
  - workspace-management
timestamp: "2026-06-19T17:23:47.579Z"
---

# Unity Catalog Workspace Bindings

**Unity Catalog Workspace Bindings** are a mechanism within [Unity Catalog](/concepts/unity-catalog.md) that restrict which Workspace|workspaces can access specific securable objects. By binding a catalog, external location, or storage credential to a particular set of workspaces, administrators can enforce workspace-level restrictions on data access. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Overview

Workspace bindings are one of the four complementary access control models in Unity Catalog, alongside privileges, attribute-based policies (ABAC), and table-level filtering/masking. Together these models allow fine-grained control over *who* can access *what*, *where*, and under *which conditions*. ^[access-control-in-unity-catalog-databricks-on-aws.md]

Bindings operate at the workspace level: they limit which workspaces are allowed to interact with bound objects. The objects that can be bound include:

- **Catalogs** – the top-level container for schemas and tables.
- **External locations** – paths to cloud storage that Unity Catalog can access.
- **Storage credentials** – cloud IAM roles or service principals used to authenticate to external locations. ^[access-control-in-unity-catalog-databricks-on-aws.md]

When a workspace is not bound to a given object, users in that workspace cannot see or use that object, even if they have been granted the appropriate privileges.

## Relationship with Other Access Control Models

Workspace bindings, privileges, and ABAC policies evaluate access at different levels and are designed to be used together. For example:

- **Privileges** (e.g., `SELECT`, `READ FILES`) determine *who* can act on an object.
- **ABAC policies** dynamically filter or mask data based on user attributes and tags.
- **Workspace bindings** determine *where* (which workspace) the object is visible and usable.

Because they address different dimensions of access control, applying all three is recommended for a layered security model. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Privileges](/concepts/privileges-and-ownership.md) – Grants on securable objects controlling actions like reading, writing, or creating.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Tag-driven, centralized policies for dynamic data filtering.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) – Per-table logic that hides or transforms data at query time.
- [Catalog](/concepts/unity-catalog.md) – The top-level object in the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md).
- [External location](/concepts/external-location.md) – A path in cloud storage governed by Unity Catalog.
- [Storage credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) – A cloud IAM credential used to authenticate to an external location.

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
