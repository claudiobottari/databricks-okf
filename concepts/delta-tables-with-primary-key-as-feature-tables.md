---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bfb361460abcecdf52b4574ce2670f59b78bfb8fef240d8fe51dfd6cebb9763
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-tables-with-primary-key-as-feature-tables
    - DTWPKAFT
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Delta Tables with Primary Key as Feature Tables
description: Any Delta table in Unity Catalog with a primary key constraint can serve as a feature table
tags:
  - delta-table
  - feature-store
  - unity-catalog
  - data-modeling
timestamp: "2026-06-19T18:46:00.731Z"
---

# Delta Tables with Primary Key as Feature Tables

In [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md), any Delta table stored in Unity Catalog that has a primary key constraint defined behaves as a **feature table**. This means you can use existing Delta tables as a source of features for machine learning models without needing to copy or replicate the data into a separate feature store. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## How It Works

When a Delta table is created in Unity Catalog and a primary key constraint is added to it, the table is automatically registered as a feature table. All the governance, lineage, and discovery capabilities of Unity Catalog apply to these tables. The Feature Engineering system does not require a separate feature store schema; the Delta table itself becomes the feature table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

If a Delta table with a primary key does not appear in the Features UI, you can add a primary key constraint to the table to make it available as a feature table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Benefits

Using Delta tables with primary keys as feature tables provides the following advantages inherited from Unity Catalog:

- **Feature discovery** — You can browse and search for features by feature table name, feature name, comment, or tag. ^[explore-features-in-unity-catalog-databricks-on-aws.md]
- **Governance** — Feature tables, functions, and models are all governed by Unity Catalog. When a model is trained using a feature table, it inherits the permissions from the data it was trained on. ^[explore-features-in-unity-catalog-databricks-on-aws.md]
- **Lineage** — Data sources used to create the feature table are saved and accessible. For each feature, you can also view the models, notebooks, jobs, and endpoints that use that feature. ^[explore-features-in-unity-catalog-databricks-on-aws.md]
- **Cross-workspace access** — Feature tables, functions, and models are automatically available in any workspace that has access to the catalog. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Exploring and Managing Feature Tables

You can explore and manage feature tables using the **Features UI**. To access it, click **Features** in the sidebar. The catalog selector allows you to choose a catalog and view all available feature tables along with metadata such as owner, online stores where the table has been published, the last time a notebook or job wrote to the table, key-value tags, and text comments. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

You can also use [Catalog Explorer](/concepts/catalog-explorer.md) by clicking the feature table name to manage the table, including privileges, lineage, and tags. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Search and Browse

Use the search box to find feature tables. You can search by all or part of the name of the feature table, a feature, a comment, or a tag. The search is case-insensitive. You can also filter feature tables by specific tags using the tag selector. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Using Genie Code

[Genie Code](/concepts/genie-code.md) can help find features or feature tables. In a `/findTables` query, mention “features” or “feature tables”. For example, `/findTables features related to movie ratings` or `/findTables feature tables related to movie ratings`. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Primary Key Constraint](/concepts/primary-key-constraint-for-feature-tables.md)
- [Delta Table](/concepts/delta-lake-table.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Genie Code](/concepts/genie-code.md)
- Machine Learning Model Training

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
