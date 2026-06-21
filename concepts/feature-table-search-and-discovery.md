---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4cd867925dd11b57df1fb40acd33e24b18a8e5ef08ca06e13b68d10de737cf03
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-search-and-discovery
    - Discovery and Feature Table Search
    - FTSAD
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Table Search and Discovery
description: Capability to search feature tables by name, feature name, data source, or tag with case-insensitive matching.
tags:
  - feature-store
  - search
  - discovery
timestamp: "2026-06-19T18:45:24.874Z"
---

# Feature Table Search and Discovery

**Feature Table Search and Discovery** refers to the capabilities provided by the Databricks Workspace Feature Store UI for finding, browsing, and understanding feature tables and their metadata. The UI enables data scientists and machine learning engineers to locate feature tables by name, feature, data source, or tag; track lineage and freshness; and manage access control. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Accessing the Feature Store UI

To access the Workspace Feature Store UI, in the sidebar under **AI/ML**, click **Features**. A table lists all available feature tables, along with the features in each table and the following metadata: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- Who created the feature table.
- Data sources used to compute the feature table.
- Online stores where the feature table has been published.
- Scheduled jobs that compute the features.
- The last time a notebook or job wrote to the feature table.

## Searching and Browsing

The search box allows users to locate feature tables by entering all or part of: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- The name of a feature table.
- A feature name.
- A data source used for feature computation.
- All or part of the key or value of a tag.

Search text is case-insensitive. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Tracking Feature Lineage and Freshness

Clicking the name of any feature table opens a detailed feature table page that provides lineage and freshness information. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Producers Table

The **Producers** table lists all notebooks and jobs that write to the feature table, allowing users to confirm the status of scheduled jobs and the freshness of the feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Features Table

The **Features** table lists all features in the table and provides links to the models, endpoints, jobs, and notebooks that use each feature. This enables end-to-end traceability from raw data sources through computation to consumption. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Adding Tags to Feature Tables

Tags are key-value pairs that can be created and used to improve searchability. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### How to Add a Tag

1. On the feature table page, click the **Tag** icon to open the tags table.
2. Click in the **Name** and **Value** fields and enter the key and value for your tag.
3. Click **Add**.

### Editing or Deleting a Tag

To edit or delete an existing tag, use the icons in the **Actions** column on the tags table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Access Control

The UI also supports controlling access to feature tables. See the documentation on [Access control (legacy)](/concepts/feature-table-access-control-legacy.md) for details. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The overall system for registering, storing, and serving features
- [Feature Lineage](/concepts/feature-lineage-tracking.md) — Tracking the data sources, notebooks, and jobs that compute features
- Feature Freshness — Monitoring when feature values were last updated
- [Tags](/concepts/tag-based-access-gating.md) — Key-value metadata used for organizing and discovering feature tables
- [Online Store](/concepts/online-feature-store.md) — Where feature tables are published for low-latency serving

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
