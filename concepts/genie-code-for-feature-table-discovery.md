---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03be5499e2ebd9061fad1f6b30cc94a61bbf9226ff68ef2bd40b7e70b4f61741
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - genie-code-for-feature-table-discovery
    - GCFFTD
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Genie Code for Feature Table Discovery
description: Using the Genie Code assistant's /findTables command with 'features' or 'feature tables' queries to locate relevant feature tables.
tags:
  - genie-code
  - feature-discovery
  - natural-language-query
timestamp: "2026-06-18T12:16:00.498Z"
---

# Genie Code for Feature Table Discovery

**Genie Code for Feature Table Discovery** is a natural-language query interface that helps you find [Feature Tables](/concepts/feature-table.md) or individual features within [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) by using the `/findTables` command. You mention “features” or “feature tables” in your query, and Genie Code returns matching results. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Overview

[Genie Code](/concepts/genie-code.md) is an AI‑powered assistant integrated into Databricks that interprets plain‑language requests and performs actions such as searching for data assets. When used for feature table discovery, Genie Code searches across Unity Catalog–managed feature tables and returns tables that match the described topic or criteria. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## How to Use

In your `/findTables` query, include the word “features” or “feature tables” along with a description of the subject you are interested in. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Examples

| Query | Purpose |
|-------|---------|
| `/findTables features related to movie ratings` | Finds feature tables that contain information about movie ratings. |
| `/findTables feature tables related to movie ratings` | Same as above, using the phrase “feature tables”. |

The search is case‑insensitive and can match on feature table name, feature name, comments, or tags. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The platform that provides feature discovery, governance, and lineage.
- [Feature Tables](/concepts/feature-table.md) — Any Delta table in Unity Catalog that has a primary key constraint and is automatically available as a feature table.
- [Unity Catalog](/concepts/unity-catalog.md) — The underlying data governance layer that stores feature table metadata.
- /findTables command — The Genie Code command used for searching tables and assets.

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
