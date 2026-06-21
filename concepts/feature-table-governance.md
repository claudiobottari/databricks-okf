---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65accbb17b6cf09f8b2eab589f2dbfb41c94075faecfbd90808a6c95a7368bbc
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-governance
    - FTG
    - Feature Governance
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Feature Table Governance
description: Unity Catalog governs feature tables, functions, and models; models inherit permissions from the data they were trained on.
tags:
  - governance
  - unity-catalog
  - security
timestamp: "2026-06-19T10:26:48.179Z"
---

Here is the wiki page for "Feature Table Governance".

---

## Feature Table Governance

**Feature Table Governance** refers to the policies, permissions, and management controls applied to feature tables within [Unity Catalog](/concepts/unity-catalog.md). When feature engineering is enabled in Unity Catalog, all standard Unity Catalog governance capabilities — including discovery, access control, lineage tracking, and cross-workspace sharing — are automatically available for feature tables. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Governance Capabilities

### Feature Discovery

Users can browse and search for feature tables by name, feature name, comment, or tag. Search is case-insensitive and can be scoped to a specific catalog using the catalog selector in the Features UI. A tag selector is also available to filter feature tables by specific key-value tags. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Access Control

Feature tables, functions, and models are all governed by Unity Catalog's permission model. When a model is trained on feature data, it inherits permissions from the data it was trained on, ensuring that access restrictions propagate to downstream artifacts. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Lineage

When a feature table is created, the data sources used to build it are saved and accessible. For each individual feature within a table, users can trace lineage to the models, notebooks, jobs, and endpoints that consume that feature. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Cross-Workspace Access

Feature tables, functions, and models are automatically available in any workspace that has access to the catalog they reside in. This eliminates the need to duplicate or manually sync feature data across workspaces. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Enabling Feature Tables

Any Delta table in Unity Catalog that includes a primary key constraint is automatically a feature table. It will appear in the Features UI without requiring any additional registration step. For tables that do not appear, see how to [add a primary key constraint on the table](https://docs.databricks.com/aws/en/machine-learning/feature-store/uc/feature-tables-uc#use-existing-uc-table). ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Managing Feature Tables

You can explore and manage feature tables through two primary interfaces:

- **Features UI** — Access the Features UI by clicking **Features** in the sidebar. This view shows the owning catalog, online stores where the feature table has been published, the last write time from notebooks or jobs, key-value tags, and text comments describing the table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]
- **Catalog Explorer** — Click a feature table name to navigate to Catalog Explorer, which provides a full management interface for the underlying Delta table, including privileges, lineage, and tags. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Finding Features with Genie Code

You can use Genie Code to locate features or feature tables by mentioning "features" or "feature tables" in a `/findTables` query. For example, `/findTables features related to movie ratings` or `/findTables feature tables related to movie ratings`. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [What is Unity Catalog?](/concepts/unity-catalog.md) — Foundational governance platform for data and AI assets.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — Overview of the feature engineering workflow.
- [Feature Tables](/concepts/feature-tables.md) — How to create and manage feature tables.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for managing Unity Catalog objects including feature tables.
- [Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) — Tracking data and model lineage across the estate.

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
