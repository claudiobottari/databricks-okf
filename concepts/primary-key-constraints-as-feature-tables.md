---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb0e3c3f3218d804a3f7851492418a4bb31987edb92f941422bb6fbfbbecbcf0
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - primary-key-constraints-as-feature-tables
    - PKCAFT
    - primary key constraint
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Primary Key Constraints as Feature Tables
description: Any Delta table in Unity Catalog with a primary key constraint is automatically treated as a feature table and appears in the Features UI.
tags:
  - feature-tables
  - delta-table
  - primary-key
timestamp: "2026-06-18T12:17:57.139Z"
---

# Primary Key Constraints as Feature Tables

In [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md), any Delta table in [Unity Catalog](/concepts/unity-catalog.md) that includes a **primary key constraint** can be used as a feature table. This means you don't need to create a separate feature store table — any existing Unity Catalog table with a defined primary key is automatically recognized as a feature table and becomes available for feature engineering workflows. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Overview

Feature tables in Unity Catalog leverage the governance, discovery, and lineage capabilities of Unity Catalog, including cross-workspace access, tag-based governance, and [lineage tracking](/concepts/feature-lineage-tracking.md). Because any Delta table with a primary key qualifies, teams can use their existing data infrastructure without migrating to a specialized feature store format. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Key Benefits

- **Feature discovery.** You can browse and search for features by feature table name, feature, comment, or tag using the Features UI or Catalog Explorer.
- **Governance.** Feature tables, functions, and models are all governed by Unity Catalog. When you train a model, it inherits permissions from the data it was trained on.
- **Lineage.** For each feature in a feature table, you can access the data sources used to create the feature table, as well as the models, notebooks, jobs, and endpoints that use the feature.
- **Cross-workspace access.** Feature tables are automatically available in any workspace that has access to the catalog.

^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Using Existing Unity Catalog Tables

Any table managed by Unity Catalog that has a primary key automatically appears as a feature table in the Features UI. If you don't see a table on this page, you may need to [add a primary key constraint on the table](/concepts/primary-key-constraint-for-feature-tables.md) using ALTER TABLE or the appropriate Unity Catalog DDL commands. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

For information about managing tables in Unity Catalog — including privileges, lineage, and tags — see [What is Unity Catalog?](/concepts/unity-catalog.md). ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Exploring Feature Tables

### Features UI

To explore feature tables, navigate to the **Features** icon in the sidebar. Select a catalog with the catalog selector to view all available feature tables in that catalog, along with metadata including:

- Who owns the feature table
- Online stores where the feature table has been published
- The last time a notebook or job wrote to the feature table
- Key-value tags added to the feature table
- Text comments describing the feature table

^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Catalog Explorer

Clicking a feature table name opens it in [Catalog Explorer](/concepts/catalog-explorer.md), where you can manage permissions, view lineage, and explore table details. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Searching and Browsing

Use the search box to search for feature tables by name, feature name, comment, or tag. Search text is case-insensitive. You can also use the tag selector to filter feature tables with a specific tag, or limit results to a specific catalog using the **Catalogs** selector. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Genie Code Discovery

[Genie Code](/concepts/genie-code.md) can help you find features or feature tables. In a `/findTables` query, mention "features" or "feature tables" — for example, `/findTables features related to movie ratings` or `/findTables feature tables related to movie ratings`. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Requirements

For a table to be usable as a feature table, it must meet the following conditions:

- The table must be managed by Unity Catalog
- The table must have a **primary key constraint** defined
- The table must be accessible from the workspace (subject to Unity Catalog permissions)

^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The unified feature management platform
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance layer for tables and models
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — Table constraints that enable feature table recognition
- [Add a Primary Key Constraint](/concepts/primary-key-constraint-for-feature-tables.md) — How to define primary keys on existing tables
- [Online Stores](/concepts/online-feature-store.md) — Where feature tables can be published for low-latency serving
- Lineage Tracking — Viewing upstream sources and downstream consumers of features
- Cross-Workspace Access — Sharing feature tables across workspaces in a [Metastore](/concepts/metastore.md)

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
