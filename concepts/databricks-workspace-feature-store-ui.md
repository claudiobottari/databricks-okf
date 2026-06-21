---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5610117dfa071d53381f163510ee2690a19cd8153e6974572117657982b291a8
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-workspace-feature-store-ui
    - DWFSU
    - Databricks Workspace Feature Store
    - Databricks Workspace
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Databricks Workspace Feature Store UI
description: A user interface within Databricks on AWS for managing, searching, and governing feature tables used in machine learning workflows.
tags:
  - databricks
  - feature-store
  - user-interface
timestamp: "2026-06-19T10:26:30.390Z"
---

# Databricks Workspace Feature Store UI

The **Databricks Workspace Feature Store UI** is a graphical interface for managing and exploring feature tables in the legacy Databricks Workspace Feature Store. It provides capabilities for searching, browsing, tracking lineage and freshness, controlling access, and managing tags on feature tables. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Accessing the UI

To open the Workspace Feature Store UI, in the Databricks sidebar, under **AI/ML**, click **Features**. The main page displays a table listing all available feature tables along with their features and the following metadata: ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

- Who created the feature table.
- Data sources used to compute the feature table.
- Online stores where the feature table has been published.
- Scheduled jobs that compute the features in the feature table.
- The last time a notebook or job wrote to the feature table.

![Feature store page](https://docs.databricks.com/aws/en/assets/images/feature-store-ui-14cd6020583d17242ddb0c0275b86222.png) ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Search and Browse for Feature Tables

Use the search box to find feature tables. You can enter all or part of the name of a feature table, a feature name, a data source used for feature computation, or a tag key or value. Search text is **case-insensitive**. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

![Feature search example](https://docs.databricks.com/aws/en/assets/images/feature-search-example-9b520100ccba30d2b3a935273adf8521.png) ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Control Access to Feature Tables

Access control for feature tables is configured separately. See [Access control (legacy)](/concepts/feature-table-access-control-legacy.md) for details. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Track Feature Lineage and Freshness

Click the name of any feature table to open its dedicated page. On that page you can track both how each feature was created and where it is used — specifically the raw data sources, notebooks, and jobs that computed the features, the online stores where the feature is published, the models trained with it, the serving endpoints that access it, and the notebooks and jobs that read it. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Producers Table

The **Producers** table lists all notebooks and jobs that write to this feature table, allowing you to confirm the status of scheduled jobs and the freshness of the feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

![producers table](https://docs.databricks.com/aws/en/assets/images/producers-table-72cf0e89e441f1d0637c6a1b13689051.png) ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Features Table

The **Features** table lists every feature in the table and provides links to the models, endpoints, jobs, and notebooks that use that feature. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

![features table](https://docs.databricks.com/aws/en/assets/images/features-table-0f392167d9e5fde732562848b356a3fb.png) ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

To return to the main feature list, click **Features** near the top of the page. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Add, Edit, and Delete Tags

Tags are key-value pairs that you can create and later use in searches. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Adding a Tag

1. On the feature table page, click the Tag icon (shown in the UI) to open the tags table.  
2. Click in the **Name** and **Value** fields and enter the key and value.  
3. Click **Add**. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

![tag table](https://docs.databricks.com/aws/en/assets/images/tags-open-2b92892f2d6833c4fac51ed029b0ae39.png)  
![add tag](https://docs.databricks.com/aws/en/assets/images/tag-add-e7a0a94c7df96101259d3f82deb415fc.png) ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

### Editing or Deleting a Tag

Use the icons in the **Actions** column of the tags table to edit or delete an existing tag. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

![tag actions](https://docs.databricks.com/aws/en/assets/images/tag-edit-or-delete-2a374d59a14e35d810bf70d2e1369a79.png) ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – The underlying system for storing and serving features.  
- [Feature Table](/concepts/feature-table.md) – A collection of features stored as a Delta table.  
- Lineage Tracking – The ability to trace how features are produced and consumed.  
- [Tags](/concepts/tag-based-access-gating.md) – Key-value metadata used for discovery and organization.  
- [Access control (legacy)](/concepts/feature-table-access-control-legacy.md) – Permission settings for feature tables.

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
