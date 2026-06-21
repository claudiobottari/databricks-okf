---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e40256b3f9606959cd7eecb69998c1d1821c23d62a05636d0ad0fb669ef0e9cb
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-discovery-with-genie-code
    - FDWGC
    - Feature Discovery
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Feature Discovery with Genie Code
description: Using Databricks' Genie Code assistant to find features and feature tables via natural language /findTables queries
tags:
  - genie-code
  - feature-discovery
  - natural-language
  - databricks
timestamp: "2026-06-19T18:45:54.171Z"
---

# Feature Discovery with Genie Code

**Feature Discovery with Genie Code** refers to the capability to use [Genie Code](/concepts/genie-code.md) to search for and identify [Feature Tables](/concepts/feature-tables.md) and individual features within [Unity Catalog](/concepts/unity-catalog.md) using natural language queries. This approach streamlines the process of finding relevant features for [machine learning](/concepts/cicd-for-machine-learning.md) workflows without requiring manual navigation of the catalog.

## Overview

Feature Engineering in Unity Catalog provides a centralized repository for all feature tables, with benefits including feature discovery, governance, lineage, and cross-workspace access. Users can browse and search for features by feature table name, feature name, comment, or tag using the standard Features UI. Genie Code extends this search capability by allowing users to find features and feature tables through conversational natural language queries. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Using Genie Code for Feature Discovery

To discover features using Genie Code, users can include references to "features" or "feature tables" in their `/findTables` queries. The system interprets these natural language requests and returns relevant matches from Unity Catalog. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Example Queries

```
/findTables features related to movie ratings
/findTables feature tables related to movie ratings
```

These queries would return feature tables in Unity Catalog that contain features relevant to movie ratings, along with their associated metadata. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Benefits

Genie Code enables faster, more intuitive discovery of features compared to manual browsing through the catalog. This is particularly valuable when working with large catalogs containing many feature tables, or when the exact name of a feature or feature table is not known but a description of the desired data is available.

## Related Concepts

- [Genie Code](/concepts/genie-code.md) — The AI-powered code generation and discovery tool on Databricks
- [Feature Tables](/concepts/feature-tables.md) — Delta tables in Unity Catalog with primary key constraints that serve as feature sources
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for Databricks assets
- [Feature Store](/concepts/feature-store.md) — The system for managing and serving features for ML
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for browsing and managing Unity Catalog assets
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating and managing features for ML

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
