---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55c45e2505d570c6f22a2c47b6e51f08b14c6d4d043260c6e0c9aebcb47bd53e
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-workspace-access-for-feature-tables
    - CAFFT
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Cross-Workspace Access for Feature Tables
description: Feature tables, functions, and models are automatically available across any workspace that has access to the Unity Catalog.
tags:
  - multi-workspace
  - unity-catalog
  - feature-store
timestamp: "2026-06-19T10:27:18.142Z"
---

# Cross-Workspace Access for Feature Tables

**Cross-workspace access** is a capability of [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) that makes feature tables, along with functions and models, automatically discoverable and usable in any Databricks workspace that has access to the catalog where they reside. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## How It Works

Feature tables in Unity Catalog are governed by the same [Catalog and Schema](/concepts/catalog-and-schema.md) model as other Unity Catalog assets. When a workspace is granted access to a catalog, the feature tables, functions, and models defined in that catalog are automatically available in that workspace. No manual replication, export, or import of feature tables is required between workspaces. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

This cross-workspace capability is one of several benefits that Feature Engineering in Unity Catalog provides, alongside:

*   **Feature discovery** – Browsing and searching by feature table name, feature, comment, or tag.
*   **Governance** – Feature tables, functions, and models inherit Unity Catalog permissions; models are governed by the data they were trained on.
*   **Lineage** – Data sources used to create a feature table are saved, and for each feature you can access the models, notebooks, jobs, and endpoints that use it.

Cross-workspace access is a direct consequence of Unity Catalog's architecture: assets are stored in a central [Metastore](/concepts/metastore.md) and are visible to any workspace that is attached to that [Metastore](/concepts/metastore.md) and has the necessary catalog-level permissions. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Requirements

- The target workspace must have **access to the catalog** that contains the feature tables. Access is typically granted through the [Metastore](/concepts/metastore.md) assignment or catalog-level permissions.
- The feature table must be a Delta table in Unity Catalog with a primary key constraint, which is the general requirement for any table to be treated as a feature table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Example Workflow

A team develops features in a catalog named `sales_features` assigned to the `production` workspace. A second workspace, `analytics`, needs to use those features for model training. Because `analytics` has been granted access to the `sales_features` catalog, users can browse and query the same feature tables directly—without copying or moving data between workspaces.

## Benefits

- **Eliminates data silos** – Feature tables are not locked to a single workspace, enabling collaboration across teams.
- **Reduces duplication** – The same feature tables serve multiple workspaces, avoiding redundant storage and computation.
- **Simplifies governance** – Access control is managed centrally through Unity Catalog permissions rather than per-workspace configurations.
- **Enables consistency** – All workspaces use the same authoritative feature definitions, reducing discrepancies in model training and inference.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The central governance layer that enables cross-workspace access
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – The overall framework for managing features
- [Feature Tables](/concepts/feature-table.md) – Delta tables in Unity Catalog with primary key constraints that are used as feature sources
- [Catalog Access Control](/concepts/unity-catalog-access-control-models.md) – Permissions that determine which workspaces can see catalogs and their assets
- [Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – Tracking the origin and usage of feature tables

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
