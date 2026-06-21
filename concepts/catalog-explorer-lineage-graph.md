---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1262c898a342d5fc7e7ad67cdef5554530efb9cbe5da0393637764f37a623e91
  pageDirectory: concepts
  sources:
    - feature-governance-and-lineage-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - catalog-explorer-lineage-graph
    - CELG
  citations:
    - file: feature-governance-and-lineage-databricks-on-aws.md
title: Catalog Explorer Lineage Graph
description: Visual UI in Databricks Catalog Explorer showing lineage relationships between feature tables, models, and functions with an interactive graph view
tags:
  - ui
  - lineage
  - catalog-explorer
timestamp: "2026-06-19T18:48:14.249Z"
---

# Catalog Explorer Lineage Graph

The **Catalog Explorer Lineage Graph** is a visual, interactive graph in Databricks that shows how data assets in [Unity Catalog](/concepts/unity-catalog.md) — including [Feature Store](/concepts/feature-store.md) tables, functions, and model versions — are connected through upstream and downstream dependencies. It is accessed from the **Lineage** tab of any table, model version, or function in [Catalog Explorer](/concepts/catalog-explorer.md). ^[feature-governance-and-lineage-databricks-on-aws.md]

## Accessing the Lineage Graph

To view the lineage graph:

1. Navigate to the table, model version, or function page in Catalog Explorer.
2. Select the **Lineage** tab. The left sidebar lists Unity Catalog objects that were logged with this asset (e.g., feature tables and functions used by a model). ^[feature-governance-and-lineage-databricks-on-aws.md]
3. Click **See lineage graph**. A full-screen graph opens, displaying the relationships between the selected asset and its ancestors/descendants. ^[feature-governance-and-lineage-databricks-on-aws.md]
4. To close the graph, click the close button (×) in the upper-right corner. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Exploring the Graph

The lineage graph provides an interactive canvas. For details about navigating the graph — such as expanding nodes, filtering, or viewing details — see the [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) documentation. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Capturing Lineage Automatically

Lineage for feature tables, Python UDFs, and models is recorded automatically when you log a model using FeatureEngineeringClient.log_model. The `FeatureLookup` and `FeatureFunction` objects passed to `create_training_set` are included in the lineage, allowing you to trace which feature tables and functions contributed to a particular model version. ^[feature-governance-and-lineage-databricks-on-aws.md]

For example, if you log a model with on-demand features computed by UDFs such as `extract_user_latitude` and `haversine_distance`, those functions appear in the lineage graph for the model version. ^[feature-governance-and-lineage-databricks-on-aws.md]

## Related Concepts

- [Catalog Explorer](/concepts/catalog-explorer.md) – The main UI for browsing Unity Catalog objects.
- [Feature Store](/concepts/feature-store.md) – The system that manages feature tables and their lineage.
- [Data Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md) – General documentation on how lineage works across all Unity Catalog assets.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer for data and AI assets.
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) – The client used to log models and capture lineage.
- [Feature Lookup](/concepts/feature-lookup.md) and [Feature Function](/concepts/feature-function.md) – Objects that define which features are used during model training.

## Sources

- feature-governance-and-lineage-databricks-on-aws.md

# Citations

1. [feature-governance-and-lineage-databricks-on-aws.md](/references/feature-governance-and-lineage-databricks-on-aws-4bd9813b.md)
