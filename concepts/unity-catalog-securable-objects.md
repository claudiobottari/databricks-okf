---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c653fcf2247ea6e8a477c932f4c39199acbd39433aae4b80c15f4b31ed267b3
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - unity-catalog-securable-objects
    - UCSO
    - Unity Catalog securable objects reference
    - Securable Object
    - Securable object
    - Unity Catalog objects
    - catalog object
    - securable object
    - securable objects
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Securable Objects
description: The object hierarchy in Unity Catalog including catalogs, schemas, tables, external locations, and storage credentials that can have privileges assigned
tags:
  - unity-catalog
  - objects
  - hierarchy
  - data-governance
timestamp: "2026-06-19T08:48:40.974Z"
---

# Unity Catalog Securable Objects

**Unity Catalog Securable Objects** are the fundamental entities within the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md) that can have permissions granted on them. These objects form the backbone of the access control model in Databricks, determining who can access what data and resources.

## Overview

Unity Catalog organizes data assets into a hierarchical structure of securable objects. Each object in this hierarchy can have privileges granted to users, groups, and service principals. The access control model is built on several complementary mechanisms that work together to enforce secure, fine-grained access across your data environment. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Access Control Models

Unity Catalog uses the following complementary models to control access to securable objects:

- **Privileges and ownership** control *who* can access *what*, using grants on securable objects.
- **Attribute-based policies (ABAC)** control *what* data users can access, using governed tags and centralized policies.
- **Table-level filtering and masking** control *what* data users can see within tables using table-specific filters and views.
- **Workspace-level restrictions** control *where* users can access data, by limiting objects to specific workspaces.

^[access-control-in-unity-catalog-databricks-on-aws.md]

## Object Hierarchy

Securable objects in Unity Catalog follow a hierarchical structure. Privileges granted on a parent object are inherited by its child objects, simplifying access management. The hierarchy includes:

- **Metastore** — The top-level container for all metadata and data assets.
- **Catalog** — A logical container for schemas and data assets.
- **Schema** — A logical grouping of tables, views, functions, and models.
- **Tables, Views, and Volumes** — The actual data objects.
- **Functions and Models** — Compute and AI/ML objects.
- **External Locations and Storage Credentials** — Objects that govern access to external cloud storage.

## Privileges and Permissions

Privileges are the permissions that can be granted on securable objects. Each privilege grants specific capabilities, such as reading data, modifying objects, or managing permissions. Key privileges include:

- `SELECT` — Read data from a table or view.
- `MODIFY` — Insert, update, or delete data.
- `CREATE` — Create child objects within a parent.
- `USAGE` — Use a schema or catalog.
- `OWNERSHIP` — Full control over the object.

Privileges can be granted using SQL commands or through the Catalog Explorer UI. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## When to Use Each Access Control Mechanism

Databricks recommends using [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) to centralize and scale access control based on governed tags. Use [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) only when you need per-table logic or haven't adopted ABAC yet. ^[access-control-in-unity-catalog-databricks-on-aws.md]

Workspace bindings, privileges, and ABAC policies all evaluate access at different levels, and they are designed to be used together. ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Managing Access

Access to securable objects can be managed through several mechanisms:

- **Manage privileges** — Grant, revoke, and inspect privileges on Unity Catalog objects using Catalog Explorer and SQL.
- **Access requests** — Configure destinations for access requests on Unity Catalog securable objects, including email, Slack, Teams, and webhooks.
- **Workspace-catalog binding** — Restrict which workspaces can access specific catalogs, external locations, and storage credentials.

^[access-control-in-unity-catalog-databricks-on-aws.md]

## Fine-Grained Data Access

For more granular control, Unity Catalog provides:

- **Attribute-based access control (ABAC)** — Define centralized, tag-driven policies that dynamically filter and mask data across your catalog.
- **Row filters and column masks** — Apply per-table row and column filters using UDFs to control what data users see at query time.

^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md)
- Privileges Reference
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md)
- Admin Roles in Unity Catalog
- [Governed Tags](/concepts/governed-tags.md)

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
