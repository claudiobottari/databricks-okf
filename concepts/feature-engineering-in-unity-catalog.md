---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3752f5135e2132453b220345dba565d141df6e63f24ed9e48ab1584d7a9f458d
  pageDirectory: concepts
  sources:
    - explore-features-in-unity-catalog-databricks-on-aws.md
    - workspace-feature-store-deprecated-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - feature-engineering-in-unity-catalog
    - FEIUC
    - Feature Engineering (Unity Catalog)
  citations:
    - file: explore-features-in-unity-catalog-databricks-on-aws.md
    - file: workspace-feature-store-deprecated-databricks-on-aws.md
title: Feature Engineering in Unity Catalog
description: Databricks' feature store solution that integrates feature tables with Unity Catalog for governance, lineage, and discovery
tags:
  - machine-learning
  - feature-store
  - unity-catalog
  - databricks
timestamp: "2026-06-19T18:46:05.441Z"
---

# Feature Engineering in Unity Catalog

**Feature Engineering in Unity Catalog** is Databricks' managed feature store solution that enables teams to create, manage, and discover machine learning features with the full governance and lineage capabilities of [Unity Catalog](/concepts/unity-catalog.md). It replaces the deprecated Workspace Feature Store and provides a unified framework for feature management across workspaces. ^[explore-features-in-unity-catalog-databricks-on-aws.md, workspace-feature-store-deprecated-databricks-on-aws.md]

## Overview

With Feature Engineering in Unity Catalog, all benefits of Unity Catalog are available for feature tables, including discovery, governance, lineage, and cross-workspace access. Any Delta table in Unity Catalog that includes a primary key constraint can serve as a feature table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

The solution is fully integrated with model scoring and serving. When you use features from Feature Store to train a model, the model is packaged with feature metadata. When the model is used for batch scoring or online inference, it automatically retrieves features from Feature Store without requiring the caller to know about or include logic to look up or join features. ^[workspace-feature-store-deprecated-databricks-on-aws.md]

## Key Capabilities

### Feature Discovery

You can browse and search for features by feature table name, feature name, comment, or tag. Search text is case-insensitive. To limit search results to a specific catalog, use the catalog selector. You can also use the tag selector to filter feature tables with a specific tag. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

[Genie Code](https://docs.databricks.com/aws/en/genie-code/use-genie-code) can help you find features or feature tables. In your `/findTables` query, mention "features" or "feature tables" — for example, `/findTables features related to movie ratings`. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Governance

Feature tables, functions, and models are all governed by Unity Catalog. When you train a model, it inherits permissions from the data it was trained on. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Lineage

When you create a feature table in Databricks, the data sources used to create it are saved and accessible. For each feature in a feature table, you can also access the models, notebooks, jobs, and endpoints that use that feature. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Cross-Workspace Access

Feature tables, functions, and models are automatically available in any workspace that has access to the catalog. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Point-in-Time Lookups

Feature Engineering in Unity Catalog supports time series and event-based use cases that require point-in-time correctness. ^[workspace-feature-store-deprecated-databricks-on-aws.md]

## Working with Feature Tables

### Accessing the Features UI

To access the Features UI, click **Features** in the sidebar. Select a catalog with the catalog selector to view all available feature tables in that catalog, along with the following metadata: ^[explore-features-in-unity-catalog-databricks-on-aws.md]

- Who owns the feature table
- Online stores where the feature table has been published
- The last time a notebook or job wrote to the feature table
- Key-value tags added to the feature table
- Text comments describing the feature table

### Using Existing Unity Catalog Tables

Any table managed by Unity Catalog that has a primary key is automatically a feature table and appears in the Features UI. If you don't see a table on this page, you may need to add a primary key constraint to the table. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

### Exploring and Managing Feature Tables

Click a feature table name to explore and manage it in [Catalog Explorer](/concepts/catalog-explorer.md), where you can view its schema, lineage, permissions, and tags. ^[explore-features-in-unity-catalog-databricks-on-aws.md]

## Migration from Workspace Feature Store

The Workspace Feature Store is deprecated and available only for workspaces created before August 19, 2024. Databricks recommends migrating to Feature Engineering in Unity Catalog for all new and existing feature engineering workloads. ^[workspace-feature-store-deprecated-databricks-on-aws.md]

## Typical Workflow

The typical machine learning workflow using Feature Engineering in Unity Catalog follows these steps: ^[workspace-feature-store-deprecated-databricks-on-aws.md]

1. Write code to convert raw data into features and create a Spark DataFrame containing the desired features.
2. Write the DataFrame as a feature table in Unity Catalog.
3. Train a model using features from the feature store. The model stores the specifications of features used for training.
4. Register the model in [Model Registry](/concepts/mlflow-model-registry.md).
5. For batch scoring: the model automatically retrieves features from Feature Store.
6. For real-time serving: publish features to an [Online Feature Store](/concepts/online-feature-store.md) so the model reads pre-computed features at inference time.

## Supported Data Types

Databricks Feature Store supports the following PySpark data types: `IntegerType`, `FloatType`, `BooleanType`, `StringType`, `DoubleType`, `LongType`, `TimestampType`, `DateType`, `ShortType`, `ArrayType`, `BinaryType`, `DecimalType`, `MapType`, and `StructType` (with version restrictions). ^[workspace-feature-store-deprecated-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for all feature tables, models, and functions
- [Catalog Explorer](/concepts/catalog-explorer.md) — Tool for browsing and managing feature tables
- [Online Feature Store](/concepts/online-feature-store.md) — For real-time model serving with pre-computed features
- [Model Registry](/concepts/mlflow-model-registry.md) — For registering and managing trained models
- [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md) — The legacy feature store being replaced
- [Delta Tables](/concepts/delta-lake-table.md) — Underlying storage format for feature tables
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) — Time series support for event-based use cases

## Sources

- explore-features-in-unity-catalog-databricks-on-aws.md
- workspace-feature-store-deprecated-databricks-on-aws.md

# Citations

1. [explore-features-in-unity-catalog-databricks-on-aws.md](/references/explore-features-in-unity-catalog-databricks-on-aws-b44ec93d.md)
2. [workspace-feature-store-deprecated-databricks-on-aws.md](/references/workspace-feature-store-deprecated-databricks-on-aws-a64a8491.md)
