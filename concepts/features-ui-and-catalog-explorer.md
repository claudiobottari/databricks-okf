---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c01c93176e093ba4579bb1ae60b25c06fab45359cd661acd1ebf36b2e19dfe0
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - features-ui-and-catalog-explorer
    - Catalog Explorer and Features UI
    - FUACE
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
title: Features UI and Catalog Explorer
description: User interfaces for exploring and managing feature tables, including metadata like ownership, online stores, last write time, tags, and comments.
tags:
  - user-interface
  - catalog-explorer
  - feature-tables
timestamp: "2026-06-18T12:16:04.582Z"
---

---
title: "Features UI and Catalog Explorer"
---

The **Features UI** is the primary Databricks interface for browsing, searching, and managing feature tables in Unity Catalog. It is accessible from the sidebar and works in conjunction with **Catalog Explorer**, which provides detailed views of individual feature tables. Together, they give you the full set of unity-catalog capabilities for feature tables: discovery, governance, lineage, and cross-workspace access. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## What is the Features UI?

Any Delta table in Unity Catalog that includes a primary-key constraint is automatically a feature table. The Features UI surfaces every such table in a catalog, along with ownership, online-store publication status, last-write timestamps, key-value tags, and comments. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Accessing the Features UI

1. In your Databricks workspace, click the **Features** icon in the sidebar.
2. Use the **catalog selector** to choose a catalog. All feature tables in that catalog appear in the list, along with the following metadata:
   - **Who owns the feature table**
   - **Online stores** where the feature table has been published
   - **The last time** a notebook or job wrote to the feature table
   - **Key–value tags** added to the feature table
   - **Text comments** describing the feature table

![Feature store page showing the feature-table list with catalog selector, ownership, and tag columns – commentary removed, alt text retained.](explore-features-in-unity-catalog-databricks-on-aws.md)

## Searching and browsing

Use the search box to find feature tables. You can enter all or part of a feature-table name, a feature name, a comment, or a tag. Search is case-insensitive. To limit the search to a specific catalog, use the **Catalogs** selector. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

![Feature search example showing a search for 'customer_rewards' and matching results in the feature-table list.](explore-features-in-unity-catalog-databricks-on-aws.md)

You can also use the **tag selector** to filter feature tables by a specific tag. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Exploring a feature table with Catalog Explorer

Click any feature-table name in the list to open its full detail page in **Catalog Explorer**. There you can see:

- The data sources that were used to create the feature table
- For each feature, the models, notebooks, jobs, and endpoints that use that feature
- The primary-key constraint that makes the table a valid feature table
- Privileges, lineage, and cross-workspace access settings

## Governance and lineage

Every action in the Features UI is subject to [Unity Catalog](/concepts/unity-catalog.md) governance. Permissions on a feature table are inherited from the parent [Catalog and Schema](/concepts/catalog-and-schema.md). When you train a model on a feature table, the model inherits permissions from the data it was trained on. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

Lineage is recorded automatically: for each feature in a feature table, you can see which models, notebooks, jobs, and endpoints use that feature. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Cross-workspace access

Feature tables, functions, and models are automatically available in any workspace that has access to the catalog. No additional configuration is required. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Using Genie Code to find features

You can use [Genie Code](/concepts/genie-code.md) to discover features or feature tables. In a `/findTables` query, mention "features" or "feature tables". For example:

- `/findTables features related to movie ratings`
- `/findTables feature tables related to movie ratings`

## Related concepts

- [Feature Store](/concepts/feature-store.md) – The conceptual layer that the Features UI manages
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer for all feature tables
- [Catalog Explorer](/concepts/catalog-explorer.md) – The detailed view for individual feature tables
- [Primary key constraints](/concepts/primary-key-constraints-for-feature-tables.md) – What makes a Delta table a valid feature table
- [Online store](/concepts/online-feature-store.md) – Where feature tables can be published for low-latency serving

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
