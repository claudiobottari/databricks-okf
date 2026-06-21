---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b188c33c955f025478f72e4babcbadca58a12b41ac81ec2b2076833f70fe6b5f
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-search
    - FTS
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Table Search
description: A case-insensitive search capability in the Databricks Feature Store UI allowing users to find feature tables by name, feature name, data source, or tag key-value pairs.
tags:
  - feature-store
  - search
  - discovery
timestamp: "2026-06-19T10:26:37.284Z"
---

# Feature Table Search

**Feature Table Search** refers to the ability to discover and locate [Feature Tables](/concepts/feature-tables.md) in the Databricks Workspace Feature Store by searching on feature table name, feature name, data source, or tag. This functionality is accessible through the **Features** UI in the Databricks workspace sidebar.

## Overview

The Workspace Feature Store provides a search interface that allows users to browse and find feature tables across the workspace. Search is case-insensitive and can match partial strings. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

Users can search for feature tables by entering all or part of any of the following:

- Feature table name
- Feature name
- Data source used for feature computation
- Tag key or value

^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Using the Search Box

To search for feature tables, navigate to the **Features** page in the Databricks sidebar (under **AI/ML**). The search box accepts free-form text input, and the results update dynamically as you type.

Search text is case-insensitive, so capitalization does not affect the results. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Searchable Metadata

The feature table listing displays the following metadata for each table, all of which is searchable:

- Feature table name
- Features contained in the table
- Creator of the feature table
- Data sources used to compute the feature table
- Online stores where the feature table has been published
- Scheduled jobs that compute the features
- Last write time (notebook or job)
- Tags (key-value pairs)

^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Tag-Based Search

Tags are key-value pairs that users can add to feature tables. Once a tag is added to a feature table, its key or value becomes searchable through the feature store search box. This makes tags a useful mechanism for organizing and discovering feature tables by custom categories. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

To add a tag to a feature table:

1. Open the feature table page.
2. Click the tag icon to expand the tags table.
3. Enter the key and value for the tag.
4. Click **Add**.
^[explore-features-and-lineage-legacy-databricks-on-aws.md]

Existing tags can be edited or deleted using the icons in the **Actions** column of the tags table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Benefits

Feature Table Search enables practitioners to:

- Quickly locate relevant feature tables without navigating through multiple folders or knowing exact table names.
- Discover features related to specific data sources or domains.
- Find feature tables by custom classification tags, enabling organization-specific taxonomies.
- Access lineage information such as data sources, models, and online stores connected to a feature table.

## Related Concepts

- [Feature Tables](/concepts/feature-tables.md) — The fundamental unit of organization in the Feature Store
- [Workspace Feature Store UI](/concepts/workspace-feature-store-ui.md) — The interface for browsing and managing feature tables
- [Feature Lineage](/concepts/feature-lineage-tracking.md) — Tracking how features were created and where they are used
- Feature Freshness — Monitoring the timeliness of feature data
- [Tags on Feature Tables](/concepts/feature-tables.md) — Custom metadata for organizing and searching feature tables

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
