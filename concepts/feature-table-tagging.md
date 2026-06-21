---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f3a93d603083f4371b61ddede32dcc66f3e1b0f5f9b4a448b21cd1afb0dc35e
  pageDirectory: concepts
  sources:
    - explore-features-and-lineage-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-tagging
    - FTT
    - Feature Table Tags
  citations:
    - file: explore-features-and-lineage-legacy-databricks-on-aws.md
title: Feature Table Tagging
description: Adding key-value tag pairs to feature tables for organization and searchability, with edit and delete capabilities.
tags:
  - feature-store
  - tagging
  - metadata
timestamp: "2026-06-19T18:45:30.200Z"
---

# Feature Table Tagging

**Feature Table Tagging** refers to the practice of attaching key-value metadata – called tags – to feature tables in the Databricks Workspace Feature Store (legacy). Tags enable teams to categorize, search for, and manage feature tables more efficiently. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Adding a Tag

Tags can be added directly from the feature table page in the Workspace Feature Store UI:

1. Open the feature table page by clicking the feature table name in the **Features** listing.
2. Click the tag icon if it is not already open to display the tags table.
3. Enter a key and an optional value in the **Name** and **Value** fields.
4. Click **Add**.

The tag is immediately associated with the feature table. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Searching with Tags

The Workspace Feature Store search box supports full or partial matching on tag keys and values. Searching for part of a key or value returns all feature tables that carry a matching tag. The search is case‑insensitive. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Editing and Deleting Tags

Existing tags can be modified or removed from the feature table page. In the tags table, use the icons in the **Actions** column to edit the key/value or delete the tag entirely. ^[explore-features-and-lineage-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Feature Store (Legacy)](/concepts/databricks-workspace-feature-store-legacy.md) — The Databricks feature store that supports tag‑based search.
- [Feature Store Access Control](/concepts/feature-store-access-control-legacy.md) — Managing permissions on feature tables.
- Feature Lineage and Freshness — Additional metadata tracked in the feature store.

## Sources

- explore-features-and-lineage-legacy-databricks-on-aws.md

# Citations

1. [explore-features-and-lineage-legacy-databricks-on-aws.md](/references/explore-features-and-lineage-legacy-databricks-on-aws-6e819774.md)
