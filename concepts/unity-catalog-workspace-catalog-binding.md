---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b71187a12f815ecd81b5d33f62a5fc34c092806cbe55b371d1f58dfddde5a713
  pageDirectory: concepts
  sources:
    - access-control-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-workspace-catalog-binding
    - UCWB
  citations:
    - file: access-control-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Workspace-Catalog Binding
description: Workspace-level restrictions that limit which workspaces can access specific catalogs, external locations, and storage credentials.
tags:
  - workspace-management
  - access-control
  - unity-catalog
timestamp: "2026-06-18T14:16:38.562Z"
---

# Unity Catalog Workspace-Catalog Binding

**Workspace-Catalog Binding** is an access control mechanism in [Unity Catalog](/concepts/unity-catalog.md) that restricts which workspaces can access specific [catalogs](/concepts/unity-catalog.md), [external locations](/concepts/external-location.md), and storage credentials. It controls the "where" of data access—limiting securable objects to particular workspaces—and is one of three complementary access control models in Unity Catalog, alongside privileges and [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md). ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Purpose

Workspace bindings allow administrators to enforce organizational boundaries by preventing users in one workspace from reading data in a catalog that belongs to another workspace. For example, a production catalog can be bound only to production workspaces, while a development catalog is bound only to development workspaces. This is separate from who can access the data (handled by privileges) or what data they can see within objects (handled by ABAC policies). ^[access-control-in-unity-catalog-databricks-on-aws.md]

## How It Fits in the Access Control Model

Unity Catalog uses three complementary models that evaluate access at different levels: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- **Workspace bindings** – control *where* users can access data, by limiting objects to specific workspaces.
- **Privileges** – control *who* can access *what*, using grants on securable objects.
- **Attribute-based policies (ABAC)** – control *what* data users can access, using governed tags and centralized policies.

These models work together. A user must first be in a workspace that is bound to a catalog, then have the necessary privileges on that catalog and its children, and finally be subject to any ABAC policies that further restrict access within objects.

## Scope

Workspace-catalog binding applies to the following securable object types: ^[access-control-in-unity-catalog-databricks-on-aws.md]

- Catalogs
- External locations
- Storage credentials

For each of these objects, an administrator can specify the set of workspaces that are allowed to see and use the object.

## Management

To manage workspace-catalog bindings, administrators use the Databricks Catalog Explorer or the REST API. The exact steps (add workspace, remove workspace) are documented in the official *Workspace-catalog binding* guide (linked in the source). ^[access-control-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that provides workspace-catalog binding
- Workspace — The Databricks environment that must be bound to a catalog
- Privileges in Unity Catalog — Grants that control who can access objects
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Tag-driven policies for fine-grained data filtering
- [External Locations](/concepts/external-location.md) — Securable objects that can also be bound to workspaces
- [Storage Credentials](/concepts/copy-into-source-credentials.md) — Cloud credentials that can be workspace-bound
- Access Control in Unity Catalog — The broader access control framework

## Sources

- access-control-in-unity-catalog-databricks-on-aws.md

# Citations

1. [access-control-in-unity-catalog-databricks-on-aws.md](/references/access-control-in-unity-catalog-databricks-on-aws-817d7ad8.md)
