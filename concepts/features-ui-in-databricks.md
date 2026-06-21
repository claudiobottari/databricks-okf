---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9515ae7cb19833433efadb78f545162072d6fc0e3902a9e97ec626cdabda922b
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - features-ui-in-databricks
    - FUID
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Features UI in Databricks
description: A dedicated user interface for browsing, searching, and managing feature tables within Unity Catalog
tags:
  - user-interface
  - feature-store
  - databricks
  - discovery
timestamp: "2026-06-19T18:45:56.098Z"
---

# Features UI in Databricks

The **Features UI** is a graphical interface in Databricks that allows users to discover, browse, and manage feature tables governed by [Unity Catalog](/concepts/unity-catalog.md). It provides a centralized view of all available feature tables along with their metadata, enabling feature discovery, governance, and lineage tracking across workspaces. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Accessing the Features UI

To open the Features UI, click **Features** in the sidebar. Use the **Catalogs** selector to choose a catalog and view all feature tables within that catalog. Any table managed by Unity Catalog that has a [primary key constraint](/concepts/primary-key-constraints-as-feature-tables.md) automatically appears as a feature table on this page. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Metadata Displayed

For each feature table, the Features UI shows the following metadata:

- Owner of the feature table
- Online stores where the feature table has been published
- Timestamp of the last write (notebook or job) to the feature table
- Key-value tags applied to the feature table
- Text comments describing the feature table

^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Searching and Browsing

The UI includes a search box to find feature tables. You can enter all or part of a feature table name, feature name, comment, or tag; search is case‑insensitive. The **Catalogs** selector limits results to a specific catalog. A tag selector is also available to filter feature tables by a specific tag. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Integration with Catalog Explorer

Clicking on a feature table name opens [Catalog Explorer](/concepts/catalog-explorer.md) for deeper management, including privilege administration, lineage inspection, and tag editing. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Finding Features with Genie Code

[Genie Code](/concepts/genie-code.md) can assist in discovering features or feature tables through natural‑language queries. For example, you can type `/findTables features related to movie ratings` or `/findTables feature tables related to movie ratings` to retrieve relevant results. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Benefits of Unity Catalog–Managed Features

Because Feature Engineering in Unity Catalog governs all feature tables, functions, and models, the Features UI inherits Unity Catalog's capabilities: cross‑workspace access, built‑in lineage tracking (data sources used to create a feature table are saved, and each feature shows the models, notebooks, jobs, and endpoints that use it), and permission inheritance from training data to models. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Feature Tables](/concepts/feature-table.md)
- [Online store](/concepts/online-feature-store.md)
- Tags in Unity Catalog
- [Primary key constraint](/concepts/primary-key-constraint-for-feature-tables.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
