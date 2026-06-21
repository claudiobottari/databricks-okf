---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 723fe42dc9a7004c725be08b4933435fe94945eb0d32ff197326eecf2bacf57b
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - three-level-namespace-catalogschematable
    - TN(
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Three-level namespace (catalog.schema.table)
description: The hierarchical naming convention in Unity Catalog that organizes data objects as catalog.schema.table, providing a structured way to manage and query data.
tags:
  - unity-catalog
  - data-organization
  - naming
timestamp: "2026-06-19T17:57:05.757Z"
---

# Three-Level Namespace (catalog.schema.table)

**Three-Level Namespace** refers to the hierarchical data organization model used by [Unity Catalog](/concepts/unity-catalog.md) in Databricks, where data objects are addressed using the format `catalog.schema.table`. This structure provides a logical way to organize, discover, and govern data assets within a [Metastore](/concepts/metastore.md).

## Overview

A three-level namespace (`catalog.schema.table`) is a fundamental concept in Unity Catalog that enables data to be organized in a hierarchical structure. Each [Metastore](/concepts/metastore.md) exposes this three-level namespace, allowing users to navigate and reference data objects consistently across workspaces. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Hierarchy Levels

### Catalog

The catalog is the top-level container in the three-level namespace. It serves as the primary organizational unit within a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) and can contain multiple schemas. Catalogs can also override the managed storage location defined at the [Metastore](/concepts/metastore.md) level. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### Schema

The schema (also referred to as a database) is the second level of the namespace hierarchy. Schemas exist within catalogs and serve as containers for tables, views, volumes, and other securable objects. Like catalogs, schemas can override the managed storage location. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### Table

The table is the third and lowest level of the namespace hierarchy. Tables are the actual data objects that users query and manipulate. They are organized within schemas and are referenced using the full three-level path. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Purpose and Benefits

The three-level namespace provides several benefits for data organization and governance:

- **Logical Organization**: Data can be organized hierarchically, making it easier to discover and understand relationships between data assets.
- **Multi-Tenancy**: Multiple teams or projects can share a [Metastore](/concepts/metastore.md) while maintaining clear separation through different catalogs or schemas.
- **Cross-Workspace Access**: Workspaces linked to the same [Metastore](/concepts/metastore.md) have a consistent view of the three-level namespace, enabling data sharing across teams.
- **Fine-Grained Governance**: Permissions can be applied at the catalog, schema, or table level, providing granular access control.

## Example

A typical three-level namespace reference looks like:

```sql
sales_europe.transactions.daily_sales
```

Where:
- `sales_europe` is the catalog
- `transactions` is the schema
- `daily_sales` is the table

## Relationship to Metastores

Each [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) registers metadata about securable objects (tables, volumes, external locations, shares) and the permissions that govern access to them. The three-level namespace is the mechanism by which this metadata is organized and referenced. Users must be on a workspace attached to a [Metastore](/concepts/metastore.md) to work with Unity Catalog and use the three-level namespace. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Storage Location Overrides

While the [Metastore](/concepts/metastore.md) defines a root managed storage location, the three-level namespace allows for overrides at different levels:
- **Metastore-level**: Default storage for all managed tables and volumes
- **Catalog-level**: Override storage for all schemas and tables within a catalog
- **Schema-level**: Override storage for all tables within a schema

This flexibility allows organizations to control where data is physically stored while maintaining a logical namespace. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container that exposes the three-level namespace
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that implements three-level namespacing
- [Managed storage location](/concepts/managed-storage-location.md) — Physical storage associated with namespace objects
- [Catalog](/concepts/unity-catalog.md) — First level of the namespace hierarchy
- Schema — Second level of the namespace hierarchy
- Table — Third level of the namespace hierarchy

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
