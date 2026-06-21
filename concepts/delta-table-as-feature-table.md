---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 974aaf69759dbabc9c69bdbe2c7e717298222c7ba3203b38a61d3da73f54d228
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-as-feature-table
    - DTAFT
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Delta Table as Feature Table
description: Any Delta table in Unity Catalog with a primary key constraint can be used as a feature table for machine learning.
tags:
  - delta-table
  - feature-store
  - unity-catalog
timestamp: "2026-06-19T10:27:32.080Z"
---

# Delta Table as Feature Table

**Delta Table as Feature Table** refers to the ability to use any Delta table in [Unity Catalog](/concepts/unity-catalog.md) that includes a [primary key constraint](/concepts/primary-key-constraints-as-feature-tables.md) as a feature table for [Feature Engineering](/concepts/featureengineeringclient-api.md) and [Machine Learning](/concepts/cicd-for-machine-learning.md) workflows. This eliminates the need to create separate feature-specific tables, streamlining the feature management lifecycle.

## Overview

With [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md), any Delta table that is managed by Unity Catalog and has a primary key constraint is automatically treated as a feature table. This integration brings all Unity Catalog benefits to feature management, including governance, discovery, lineage, and cross-workspace access.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Requirements

To use a Delta table as a feature table, the table must:

- Be managed by [Unity Catalog](/concepts/unity-catalog.md).
- Include a [primary key constraint](/concepts/primary-key-constraints-as-feature-tables.md).

If a table does not appear in the Features UI, it likely lacks a primary key constraint. For instructions on adding a primary key constraint, see Add a primary key constraint on a table.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Benefits

Using Delta tables as feature tables provides the following capabilities through Unity Catalog:

- **Feature discovery**: Browse and search for features by feature table name, feature name, comment, or tag.^[explore-features-in-unity-catalog-databricks-on-aws.md]
- **Governance**: Feature tables, functions, and models are all governed by Unity Catalog. When a model is trained, it inherits permissions from the data it was trained on.^[explore-features-in-unity-catalog-databricks-on-aws.md]
- **Lineage**: Data sources used to create a feature table are saved and accessible. For each feature, models, notebooks, jobs, and endpoints that use that feature are tracked.^[explore-features-in-unity-catalog-databricks-on-aws.md]
- **Cross-workspace access**: Feature tables, functions, and models are automatically available in any workspace that has access to the catalog.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Exploring Feature Tables

The Features UI provides a centralized view of all feature tables. To access it, click **Features** in the sidebar. From there, you can:

- Use the catalog selector to view feature tables in a specific catalog.
- View metadata including owner, online stores where published, last write time, tags, and comments.^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Search and Browse

Use the search box to search for feature tables by name, feature name, comment, or tag. Searches are case-insensitive. You can also use the tag selector to filter tables with a specific tag.^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Catalog Explorer

Clicking a feature table name opens the table in [Catalog Explorer](/concepts/catalog-explorer.md), where you can explore and manage the table in detail.^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Using Genie Code

[Genie Code](/concepts/genie-code.md) can help find features or feature tables. In a `/findTables` query, mention "features" or "feature tables." For example: `/findTables features related to movie ratings` or `/findTables feature tables related to movie ratings`.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Automatic Registration

Any Delta table managed by Unity Catalog that has a primary key is automatically a feature table and appears on the Features UI page. No additional registration steps are required.^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Feature Tables](/concepts/feature-table.md)
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Genie Code](/concepts/genie-code.md)
- [Feature Store](/concepts/feature-store.md)
- Model Lineage

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
