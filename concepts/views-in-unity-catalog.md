---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abbd8d8047b0277b193bdc619cb0ddf5c114b5037061ce1f35b35649f45b72ec
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - views-in-unity-catalog
    - VIUC
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Views in Unity Catalog
description: Views are read-only objects defined by stored SQL queries, including standard views, materialized views (pre-computed cached results with REFRESH privilege), and metric views (reusable metric definitions).
tags:
  - unity-catalog
  - views
  - sql
timestamp: "2026-06-19T23:16:24.157Z"
---

# Views in [Unity Catalog](/concepts/unity-catalog.md)

**Views** are read‑only securable objects in [Unity Catalog](/concepts/unity-catalog.md) that are defined by a stored SQL query over one or more tables or other views. They are a type of data asset that lives within a schema in the three‑level [Unity Catalog](/concepts/unity-catalog.md) namespace (`catalog.schema.view`).^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## How Views Are Defined

A view is a saved SQL query; every time a user queries a view, the system re‑executes the underlying query and returns the current result. Because views do not store data themselves, they always reflect the latest state of the underlying tables or views at query time.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Location in the Object Hierarchy

Views sit below schema|schemas in the [Unity Catalog](/concepts/unity-catalog.md) hierarchy. A schema (also called a database) is a container object that can hold tables, views, volumes, and functions. The full path to a view is expressed as `catalog.schema.view`.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Privileges and Permissions

The permission model for views follows the standard [Unity Catalog](/concepts/unity-catalog.md) pattern. To grant a principal access to a view, a user grants the `SELECT` privilege on the view itself. To create a view, the creator must have the appropriate ownership and `USE CATALOG` / `USE SCHEMA` privileges on the parent [Catalog and Schema](/concepts/catalog-and-schema.md).^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Variants of Views

[Unity Catalog](/concepts/unity-catalog.md) supports two special types of views that build on the standard view concept:

- **Materialized views** – These pre‑compute and store their query results. The stored results reflect the state of the data at the time the materialized view was last refreshed. In addition to `SELECT` and `MANAGE`, materialized views support the `REFRESH` privilege, which allows a user to trigger a manual refresh of the stored results. Users with only `SELECT` can query the stored results but cannot trigger a refresh.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]
- **Metric views** – These are read‑only objects that define a set of reusable metric definitions based on one or more tables, views, or SQL queries. Users query a metric view as they would a standard view. The metric view owner’s privileges are used to resolve the underlying data sources at query time.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

Both materialized views and metric views share the same permission model as standard views. Users need `SELECT` and the appropriate usage privileges to query them.^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Related Concepts

- [Catalog](/concepts/unity-catalog.md) – The top‑level container for data assets in [Unity Catalog](/concepts/unity-catalog.md).
- Schema – The container that holds views, tables, and other objects.
- Table – The primary structured data object that views often query.
- [Materialized View](/concepts/materialized-views-in-databricks.md) – A view variant that caches results.
- Metric View – A view variant for reusable metric definitions.
- Securable Objects – The general concept of objects on which privileges can be granted in [Unity Catalog](/concepts/unity-catalog.md).
- [Unity Catalog](/concepts/unity-catalog.md) – The full data governance and cataloging system for Databricks.

## Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
