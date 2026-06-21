---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4cf93ad0bceeb40d1e9aca8b9e50507d100ea3047ddcf61ab3d8faf8b841c210
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - catalog-and-schema
    - Schema and Catalog
    - CAS
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Catalog and Schema
description: Catalogs are the first-level and schemas the second-level container objects in Unity Catalog's three-level namespace, used to organize data and AI assets by organizational unit, project, or lifecycle scope.
tags:
  - unity-catalog
  - data-organization
  - namespace
timestamp: "2026-06-19T23:15:31.321Z"
---

# Catalog and Schema

In [Unity Catalog](/concepts/unity-catalog.md), **catalog** and **schema** are the first two layers of the [Three-Level Namespace](/concepts/three-level-namespace.md) that organizes data assets (`catalog.schema.table`). Together, they form the hierarchical structure that provides the foundation for access control and data organization in [Unity Catalog](/concepts/unity-catalog.md).^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Catalog

A **catalog** is the first and highest-level layer for your data assets within a [Unified Catalog Metastore|metastore](/concepts/unity-catalog-metastore.md). Catalogs are container objects that contain schemas, which in turn contain tables, views, volumes, and functions. Catalogs exist directly under the [Metastore](/concepts/metastore.md) and are typically used to organize data and AI assets by organizational units or software development lifecycle scopes, such as development, staging, and production environments.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

Catalogs form the first part of the [Three-Level Namespace](/concepts/three-level-namespace.md) (for example, `catalog.schema.table`). They are the top-level securable object for data assets in the [Unity Catalog](/concepts/unity-catalog.md) hierarchy.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Schema

A **schema** (also called a database) is the second layer of the object hierarchy for your data assets. Schemas exist within catalogs and are container objects that organize data and AI assets into categories that are more granular than catalogs. A schema may represent a single use case, project, or team sandbox. A schema contains tables, views, volumes, and functions.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

Schemas form the second part of the [Three-Level Namespace](/concepts/three-level-namespace.md) (for example, `catalog.schema.table`).^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Object Hierarchy

The [Three-Level Namespace](/concepts/three-level-namespace.md) is fundamental to how [Unity Catalog](/concepts/unity-catalog.md) organizes data assets:

- **Catalog** — the top-level layer (`catalog`)
- **Schema** — the second layer, contained within a catalog (`catalog.schema`)
- **Asset** — the third layer, such as a table or view (`catalog.schema.table`)

Both catalogs and schemas are container objects in [Unity Catalog](/concepts/unity-catalog.md), meaning they exist primarily to organize and contain other securable objects rather than to represent data themselves. Privileges granted on a catalog or schema can propagate to the objects within them, establishing the foundation for access control in Unity Catalog.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Related Concepts

- [Unified Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level securable object that contains all catalogs
- Table — A collection of structured data organized by rows and columns, contained within a schema
- View — A saved query against tables or other views, contained within a schema
- Volume — A securable object for unstructured data, contained within a schema
- Function — Reusable logic units, contained within a schema

## Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
