---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47c985ceb4df096c9733b8f7500279db197e27326983bc8397306fc07b4dd1b9
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-governance-for-feature-tables
    - UCGFFT
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Governance for Feature Tables
description: Feature tables inherit Unity Catalog's access control, permissions, and governance policies, including model permission inheritance from training data
tags:
  - governance
  - security
  - unity-catalog
  - feature-store
timestamp: "2026-06-19T18:45:50.071Z"
---

# Unity Catalog Governance for Feature Tables

**Unity Catalog Governance for Feature Tables** refers to the set of data governance, discovery, lineage, and access-control capabilities that [Unity Catalog](/concepts/unity-catalog.md) provides for feature tables in Databricks. When you use [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md), feature tables, functions, and models are all governed by the same Unity Catalog policies, making it possible to manage them consistently across workspaces. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Key Governance Capabilities

### Feature Discovery
Users can browse and search for feature tables by table name, feature name, comment, or tag. The search is case-insensitive and supports partial text matching. In addition, a tag selector allows filtering feature tables by specific key-value tags. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Governance and Permissions
All feature tables, functions, and models in Unity Catalog are subject to the same governance rules. When a [model training](/concepts/databricks-model-training.md) job uses a feature table, the model inherits permissions from the data it was trained on. This ensures that access controls propagate automatically from source data to downstream assets. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Lineage
Lineage is automatically captured for feature tables. The data sources used to create a feature table are saved and are accessible from the table's metadata. For each individual feature, you can also view which models, notebooks, jobs, and endpoints have used that feature. This provides full traceability from raw data to production predictions. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Cross-Workspace Access
Feature tables, functions, and models are automatically available in any workspace that has access to the catalog where they are stored. This eliminates the need to manually copy or register assets across workspaces. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Using Any Delta Table as a Feature Table

Any [Delta table](/concepts/delta-lake-table.md) in Unity Catalog that includes a [primary key constraint](/concepts/primary-key-constraints-as-feature-tables.md) can be used as a feature table. This means existing Delta tables with proper primary keys are automatically recognized as feature tables and appear in the Features UI. For tables that do not yet have a primary key, see the documentation on adding a primary key constraint to a table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Exploring Feature Tables

### Features UI
The **Features** UI (accessible via the sidebar icon) provides a centralized view of all feature tables in a selected catalog. For each feature table, the UI displays:
- Owner
- Online stores where the table has been published
- Last write time (by a notebook or job)
- Key-value tags
- Text comments

![Feature store page](https://docs.databricks.com/aws/en/assets/images/feature-store-ui-uc-47543a1b45cc58e1c664e0caee10716f.png)

^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Catalog Explorer
Clicking a feature table name in the Features UI opens the table in [Catalog Explorer](/concepts/catalog-explorer.md), where you can explore and manage the table's full metadata, permissions, and lineage. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Search and Browse
The search box at the top of the Features UI allows searching across feature table names, feature names, comments, and tags. The catalog selector lets you scope the search to a specific catalog. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Genie Code
You can also use [Genie Code](/concepts/genie-code.md) to find features and feature tables. In a `/findTables` query, mention "features" or "feature tables" — for example, `/findTables features related to movie ratings` or `/findTables feature tables related to movie ratings`. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The underlying governance platform for data and AI assets.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – The feature store built on Unity Catalog.
- [Primary Key Constraint](/concepts/primary-key-constraint-for-feature-tables.md) – Required for a Delta table to be treated as a feature table.
- [Delta Table](/concepts/delta-lake-table.md) – The storage format for feature tables.
- [Catalog Explorer](/concepts/catalog-explorer.md) – Tool for detailed metadata and permission management.
- [Genie Code](/concepts/genie-code.md) – AI-powered assistant for finding assets.
- [Model Training](/concepts/databricks-model-training.md) – Workflows that inherit permissions from feature tables.

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
