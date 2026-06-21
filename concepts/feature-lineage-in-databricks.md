---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2cc67f18aa37ee98ab362d5ecb73afd8b03d9575c9290c43b3e718cae5921807
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-lineage-in-databricks
    - FLID
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Feature Lineage in Databricks
description: Lineage tracking for feature tables that records data sources used to create the table and links to models, notebooks, jobs, and endpoints that consume each feature.
tags:
  - lineage
  - feature-store
  - observability
timestamp: "2026-06-19T10:27:04.135Z"
---

Here is the wiki page for "Feature Lineage in Databricks", written based solely on the provided source material.

---

## Feature Lineage in Databricks

**Feature Lineage** in Databricks refers to the tracking and visualization of the relationships between feature tables and the data sources, models, notebooks, jobs, and endpoints that create or consume them. Feature lineage is a core capability of [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md).

## Overview

When you create a feature table in Databricks, the data sources used to create that feature table are automatically saved and are accessible through the lineage system. For each feature within a feature table, you can also access the models, notebooks, jobs, and endpoints that use that feature. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Benefits

Feature lineage provides the following benefits:

- **Data provenance**: Understand where feature data originates by tracing it back to its source tables or files.
- **Impact analysis**: Identify which models, notebooks, jobs, or endpoints depend on a given feature, helping assess the downstream impact of changes to that feature.
- **Governance**: Feature lineage is governed by [Unity Catalog](/concepts/unity-catalog.md), ensuring that permissions and auditability extend to feature tables and their dependencies.

## Accessing Feature Lineage

Feature lineage is accessible through the **Features UI** in Databricks. To view lineage:

1. Click the **Features** icon in the sidebar.
2. Select the desired catalog using the catalog selector to view all available feature tables in that catalog.
3. Click on a specific feature table name to explore it further in [Catalog Explorer](/concepts/catalog-explorer.md).

In Catalog Explorer, you can view the lineage for a feature table, including its upstream data sources and downstream consumers such as models, notebooks, jobs, and endpoints.

## Lineage for Features Within a Table

For each individual feature within a feature table, lineage information is available showing:

- Which models have been trained using that feature
- Which notebooks or jobs have written to that feature
- Which endpoints serve that feature

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Feature Tables](/concepts/feature-tables.md)
- [Feature Discovery](/concepts/feature-discovery-with-genie-code.md)
- [Governance in Unity Catalog](/concepts/ai-governance-unity-catalog.md)
- [Cross-workspace access](/concepts/cross-workspace-feature-access.md)

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
