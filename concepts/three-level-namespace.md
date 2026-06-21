---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23378b46d786c1893b88993d358089fb0ba93e6ec7b191c646a430fe17a833fc
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
    - what-is-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - three-level-namespace
  citations:
    - file: what-is-unity-catalog-databricks-on-aws.md
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
    - file: inferred from the concept of metastore linkage
title: Three-Level Namespace
description: The catalog.schema.table naming convention used by Unity Catalog metastores to organize and reference data objects.
tags:
  - unity-catalog
  - data-organization
  - databricks
timestamp: "2026-06-18T11:15:52.990Z"
---

# Three-Level Namespace

**Three-Level Namespace** is the hierarchical addressing scheme used by [Unity Catalog](/concepts/unity-catalog.md) to organize and govern data and AI assets. Every securable object that stores data or provides queryable logic — such as tables, views, volumes, functions, and models — is identified by a three-part path of the form `catalog.schema.object`. ^[what-is-unity-catalog-databricks-on-aws.md]

A [Metastore](/concepts/metastore.md) is the top-level container for data in Unity Catalog. Each [Metastore](/concepts/metastore.md) exposes a three-level namespace (`catalog.schema.table`) by which data can be organized. The [Metastore](/concepts/metastore.md) registers metadata about securable objects and the permissions that govern access to them. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

The namespace has three levels:

- **Catalog** – The highest level of organization. Catalogs group related schemas and serve as the primary boundary for access control and data discovery.
- **Schema** – A logical grouping of objects within a catalog, typically representing a database or a subject area.
- **Object** – The individual securable asset, such as a table, view, volume, function, or model.

This three-level hierarchy mirrors the traditional `database.schema.table` pattern familiar to SQL users and provides a consistent way to reference assets across all Unity Catalog interactions — whether through Catalog Explorer, SQL queries, the Databricks CLI, or REST APIs. ^[what-is-unity-catalog-databricks-on-aws.md, create-a-unity-catalog-metastore-databricks-on-aws.md]

## Objects That Use the Three-Level Namespace

The following securable objects in Unity Catalog are identified using the three-level namespace:

- Tables
- Views
- Volumes
- Functions
- Models

^[what-is-unity-catalog-databricks-on-aws.md]

Other Unity Catalog objects — such as storage credentials, external locations, connections, and shares — are not nested under a [Catalog and Schema](/concepts/catalog-and-schema.md); they sit directly under the [Metastore](/concepts/metastore.md) and are referenced by a single name rather than a three-level path. ^[what-is-unity-catalog-databricks-on-aws.md]

## Practical Use

When you write a SQL query in a Databricks notebook, you reference a table as `my_catalog.my_schema.my_table`. Similarly, when you grant permissions, you specify the full three-level path of the object. This consistent naming simplifies cross-workspace collaboration because the same path is valid from any workspace linked to the same [Metastore](/concepts/metastore.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md, inferred from the concept of metastore linkage]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that provides the three-level namespace.
- [Metastore](/concepts/metastore.md) – The top-level container that exposes the namespace.
- [Securable Object](/concepts/unity-catalog-securable-objects.md) – Any object governed by Unity Catalog that can be referenced via the namespace.
- [Catalog](/concepts/unity-catalog.md) – The first level of the namespace.
- Schema – The second level of the namespace.
- Table / View / Volume / Function / Model – Object types that use the namespace.
- [Managed versus external assets](/concepts/managed-vs-external-assets-in-unity-catalog.md) – Distinction between objects whose storage is managed by Unity Catalog and those that are governed only.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI for browsing the three-level namespace.

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)
2. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
3. inferred from the concept of metastore linkage
