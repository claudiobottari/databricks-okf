---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3bdc08929f1e4eb68898614cbb56c9380c80a40b6665a5c1ada7f6210b736809
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-for-feature-search
    - GCFFS
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Genie Code for Feature Search
description: A natural-language query feature in Databricks that allows users to find feature tables using `/findTables` commands mentioning 'features' or 'feature tables'.
tags:
  - genie-code
  - search
  - natural-language
timestamp: "2026-06-19T10:27:28.559Z"
---

# Genie Code for Feature Search

**Genie Code for Feature Search** refers to the use of the [Genie Code](/concepts/genie-code.md) natural language interface to discover and locate features and feature tables within [Unity Catalog](/concepts/unity-catalog.md) in Databricks. By issuing `/findTables` queries that mention "features" or "feature tables," users can search across catalogs for relevant feature data without needing to know exact table names or locations. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Overview

Feature Engineering in Unity Catalog provides several ways to discover features, including browsing by catalog, searching by name or tag, and using Catalog Explorer. Genie Code adds a conversational interface that allows users to find features and feature tables through natural language queries. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

All Delta tables in Unity Catalog that have a primary key constraint are automatically treated as feature tables, making them discoverable through Genie Code queries. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Usage

To find features or feature tables using Genie Code, use the `/findTables` command and mention "features" or "feature tables" in your query. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Example Queries

- `/findTables features related to movie ratings`
- `/findTables feature tables related to movie ratings`

Genie Code interprets the natural language request and searches across available catalogs in Unity Catalog for matching feature tables. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Benefits

Genie Code for Feature Search provides several advantages over manual browsing:

- **Natural language discovery**: Users can describe what they need in plain language rather than constructing complex search queries.
- **Cross-catalog search**: Queries can find features across multiple catalogs without manually switching between them.
- **Simplified access**: Reduces the need to know exact table names, feature names, or catalog structures.

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The underlying feature management system
- [Feature Discovery](/concepts/feature-discovery-with-genie-code.md) — Other methods for finding features, including browsing and search
- [Genie Code](/concepts/genie-code.md) — The natural language interface used for queries
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer for features
- [Primary Key Constraints](/concepts/primary-key-constraints-for-feature-tables.md) — Requirement for feature tables to be discoverable

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
