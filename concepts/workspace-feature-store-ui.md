---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9a076822c9deedaed3ab66491d15b61b95df7fba8fcfb66eeac159d1ed24970
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-feature-store-ui
    - WFSU
    - Workspace Feature Store
    - Workspace-Level Feature Store
    - workspace-level Feature Store
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Workspace Feature Store UI
description: Databricks UI for managing, searching, and governing feature tables with lineage tracking and access control.
tags:
  - feature-store
  - databricks
  - user-interface
  - machine-learning
timestamp: "2026-06-19T18:45:44.960Z"
---

Here is the wiki page for "Workspace Feature Store UI", drawn solely from the provided source material.

---

## Workspace Feature Store UI

The **Workspace Feature Store UI** is a browser-based interface in Databricks that allows users to browse, search, manage, and track feature tables and their metadata. It is accessed from the Databricks sidebar under **AI/ML** by clicking **Features**. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Main Feature Table View

The main page displays a table of all available feature tables. For each table, the UI shows the features it contains and the following metadata:

- Who created the feature table.
- Data source|Data sources used to compute the feature table.
- [Online store|Online stores](/concepts/online-store-publishing-of-features.md) where the feature table has been published.
- Scheduled jobs that compute the features in the feature table.
- The last time a notebook or job wrote to the feature table.

^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Searching and Browsing

A search box at the top of the page enables searching for feature tables. Users can enter all or part of a feature table name, a feature name, a data source name, or a tag key or value. Search text is case-insensitive. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Feature Table Details and Lineage

Clicking on the name of any feature table opens a dedicated feature table page. This page provides detailed lineage tracking and status information for that table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

#### Producers

The **Producers** table on the feature table page lists all notebooks and jobs that write to that feature table. This allows users to confirm the status of scheduled jobs and check the freshness of the feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Features

The **Features** table lists all features within the selected table and provides links to the models, endpoints, jobs, and notebooks that use each feature. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Tags

Tags are key-value pairs that can be added to feature tables and used for searching.

- **Adding a tag:** On the feature table page, click the tag icon to open the tags table. Enter the key and value, then click **Add**. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]
- **Editing or deleting a tag:** Use the icons in the **Actions** column of the tags table to edit or delete existing tags. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Access Control

The UI supports controlling access to feature tables. More information is available in the dedicated documentation on [Access control (legacy)](/concepts/feature-table-access-control-legacy.md). ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Navigation

To return to the main features UI page from a feature table page, click **Features** near the top of the page. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Feature Table](/concepts/feature-table.md)
- [Data source](/concepts/deltatablesource.md)
- [Online store](/concepts/online-feature-store.md)
- [Access control (legacy)](/concepts/feature-table-access-control-legacy.md)

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
