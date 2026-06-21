---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf045c0319d4d4702b4bdd8c381a00aaf41a09821f0837faa24f304234065684
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-discovery-in-unity-catalog
    - FDIUC
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Feature Discovery in Unity Catalog
description: The ability to browse and search for feature tables by name, feature, comment, or tag within Unity Catalog.
tags:
  - feature-store
  - discovery
  - search
timestamp: "2026-06-19T10:27:20.523Z"
---

# Feature Discovery in Unity Catalog

**Feature Discovery in Unity Catalog** refers to the capability to browse, search, and find features across all feature tables managed by [Unity Catalog](/concepts/unity-catalog.md). This functionality is part of [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md), which extends Unity Catalog's governance, lineage, and cross-workspace access capabilities to feature tables. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Overview

Feature discovery allows users to browse and search for features by feature table name, feature name, comment, or tag. This capability works across all feature tables within a catalog, making it easier to find relevant features for machine learning projects. Any Delta table in Unity Catalog that includes a primary key constraint is automatically recognized as a feature table and appears in search results. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

> **Note:** Any table managed by Unity Catalog that has a primary key is automatically a feature table and appears on the Features page. If a table does not appear, check how to add a primary key constraint to the table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Searching for Feature Tables

### Using the Features UI

To access the Features UI, click **Features** in the sidebar. The page displays all available feature tables in the selected catalog, along with the following metadata: ^[explore-features-in-unity-catalog-databricks-on-aws.md]

- Who owns the feature table
- Online stores where the feature table has been published
- The last time a notebook or job wrote to the feature table
- Key-value tags added to the feature table
- Text comments describing the feature table

### Search Capabilities

Use the search box to search for feature tables. To limit the search to a specific catalog, use the **Catalogs** selector. You can enter all or part of: ^[explore-features-in-unity-catalog-databricks-on-aws.md]

- A feature table name
- A feature name
- A comment
- A tag of the feature table

Search text is case-insensitive. You can also use the tag selector to filter feature tables with a specific tag. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Finding Features Using Genie Code

[Genie Code](/concepts/genie-code.md) can help you find features or feature tables. In your `/findTables` query, mention "features" or "feature tables". For example: ^[explore-features-in-unity-catalog-databricks-on-aws.md]

- `/findTables features related to movie ratings`
- `/findTables feature tables related to movie ratings`

## Exploring and Managing Feature Tables with Catalog Explorer

Click a feature table name to explore and manage it in [Catalog Explorer](/concepts/catalog-explorer.md). This provides access to detailed metadata, lineage information, and privileges for the feature table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Capabilities

Feature discovery is one of several benefits provided by Feature Engineering in Unity Catalog, which also includes: ^[explore-features-in-unity-catalog-databricks-on-aws.md]

- **Governance.** Feature tables, functions, and models are all governed by Unity Catalog. When you train a model, it inherits permissions from the data it was trained on.
- **Lineage.** When you create a feature table in Databricks, the data sources used to create the feature table are saved and accessible. For each feature in a feature table, you can also access the models, notebooks, jobs, and endpoints that use that feature.
- **Cross-workspace access.** Feature tables, functions, and models are automatically available in any workspace that has access to the catalog.

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The broader framework for managing features within Unity Catalog
- [Feature Tables](/concepts/feature-table.md) — The underlying data structure for storing features
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — Required for a Delta table to be recognized as a feature table
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI tool for browsing and managing Unity Catalog objects
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying governance and metadata platform
- [Genie Code](/concepts/genie-code.md) — AI assistant capable of finding features and feature tables

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
