---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f1dee997478206c13e4f757c56349f46c543f4aac3c32579e917d9c486d14086
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-workspace-feature-store-legacy
    - DWFS(
    - Workspace Feature Store (Legacy)
    - Workspace Feature Store (legacy)
    - Feature Store (legacy)
    - Workspace Feature Table
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Databricks Workspace Feature Store (Legacy)
description: A legacy feature store UI in Databricks on AWS for managing, searching, and tracking feature tables used in machine learning workflows.
tags:
  - feature-store
  - machine-learning
  - databricks
timestamp: "2026-06-18T12:15:17.752Z"
---

# Databricks Workspace Feature Store (Legacy)

The **Databricks Workspace Feature Store (Legacy)** is a feature management system within Databricks that allows teams to discover, manage, govern, and track feature tables used for machine learning. It provides a centralized UI for browsing feature tables, controlling access, tracking lineage, and monitoring feature freshness. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Accessing the Feature Store UI

To access the Workspace Feature Store UI, in the sidebar under **AI/ML**, click **Features**. The page displays a table listing all available feature tables along with their features and associated metadata. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Key Capabilities

### Search and Browse Feature Tables

Use the search box to find feature tables by entering all or part of the feature table name, a feature name, a data source used for feature computation, or a tag key or value. Search text is case-insensitive. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Control Access to Feature Tables

Access control for feature tables is managed separately. See [Access Control (Legacy)](/concepts/feature-table-access-control-legacy.md) for details. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Track Feature Lineage and Freshness

The Feature Store UI provides comprehensive lineage tracking, showing both how a feature was created and where it is used. You can track: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- Raw data sources used to compute features
- Notebooks and jobs that wrote to the feature table
- Online stores where the feature table has been published
- Models trained with the feature
- Serving endpoints that access the feature
- Notebooks and jobs that read the feature

Click the name of any feature table to display its detailed page. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

#### Producers Table

The **Producers** table on the feature table page provides information about all notebooks and jobs that write to the feature table. This allows you to confirm the status of scheduled jobs and the freshness of the feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

#### Features Table

The **Features** table lists all features in the table and provides links to the models, endpoints, jobs, and notebooks that use each feature. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Add Tags to Feature Tables

Tags are key-value pairs that you can create and use to search for feature tables. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

To add a tag:
1. On the feature table page, click the tag icon to open the tags table.
2. Click in the **Name** and **Value** fields and enter the key and value for your tag.
3. Click **Add**.

To edit or delete an existing tag, use the icons in the **Actions** column. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Feature Table Metadata

The main Features page displays the following metadata for each feature table: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- Who created the feature table
- Data sources used to compute the feature table
- Online stores where the feature table has been published
- Scheduled jobs that compute the features
- The last time a notebook or job wrote to the feature table

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The broader feature management paradigm
- MLflow Models — Models that consume features from the feature store
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that can integrate with feature stores
- [Model Serving](/concepts/model-serving.md) — Serving endpoints that access published features

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
