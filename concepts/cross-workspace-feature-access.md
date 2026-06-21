---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a7c299d8b95361a5d42b7aebfbd7b48f734ede63ac120dbf54b148651a32d83
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-workspace-feature-access
    - CFA
    - Cross-Workspace Access
    - Cross-workspace access
    - cross-workspace access
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Cross-workspace Feature Access
description: Feature tables, functions, and models are automatically available across any workspace that has access to the Unity Catalog catalog
tags:
  - multi-workspace
  - unity-catalog
  - feature-store
  - collaboration
timestamp: "2026-06-19T18:45:45.127Z"
---

# Cross-workspace Feature Access

**Cross-workspace Feature Access** is a capability of [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) that makes feature tables, functions, and models automatically available across any workspace that has access to the catalog. This eliminates the need to manually copy or replicate feature data between workspaces.

## Overview

With Feature Engineering in Unity Catalog, all of the benefits of Unity Catalog are available for feature tables. One of these benefits is that feature tables, functions, and models are automatically available in any workspace that has access to the catalog.^[explore-features-in-unity-catalog-databricks-on-aws.md]

This cross-workspace accessibility is a core governance and discoverability feature. When you create a feature table in Databricks, the data sources used to create the feature table are saved and accessible across workspaces. For each feature in a feature table, you can also access the models, notebooks, jobs, and endpoints that use that feature across all connected workspaces.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Key Benefits

### Feature Discovery
Users can browse and search for features by feature table name, feature name, comment, or tag across any workspace with access to the containing catalog.^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Governance
Feature tables, functions, and models are all governed by Unity Catalog. When you train a model, it inherits permissions from the data it was trained on, maintaining consistent access controls across workspaces.^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Lineage
Lineage information is preserved across workspaces. For each feature in a feature table, you can access the models, notebooks, jobs, and endpoints that use the feature, regardless of which workspace created or consumes them.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Technical Details

Any [Delta table](/concepts/delta-lake-table.md) in Unity Catalog that includes a primary key constraint can be used as a feature table. Once created, these tables are automatically available in any workspace that has access to the catalog.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance layer that enables cross-workspace access
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The overall framework for managing feature tables
- [Feature Store](/concepts/feature-store.md) — The traditional concept of a centralized feature repository
- Delta Tables with Primary Keys — The table structure required for feature tables
- [Catalog Explorer](/concepts/catalog-explorer.md) — A tool for exploring and managing feature tables across workspaces

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
