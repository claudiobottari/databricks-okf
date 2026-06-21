---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77a922d919ec7383a94127442ffb62563d3c99e5bdda3f5c9063c4b95bfbef74
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-feature-store-vs-workspace-feature-store
    - UCFSVWFS
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: Unity Catalog Feature Store vs Workspace Feature Store
description: "The two types of feature stores on Databricks: the newer Unity Catalog-based feature store and the legacy Workspace Feature Store"
tags:
  - feature-store
  - databricks
  - catalog
timestamp: "2026-06-19T22:11:13.872Z"
---

# Unity Catalog Feature Store vs Workspace Feature Store

**Unity Catalog Feature Store** and **Workspace Feature Store** are two feature store options available on Databricks. Both allow you to store, discover, and reuse features for machine learning, but they differ in scope and governance model.

## Overview

The Unity Catalog Feature Store is built on top of [Unity Catalog](/concepts/unity-catalog.md), providing a unified, governed, and cross-workspace approach to feature management. The Workspace Feature Store is the legacy feature store that operates within a single workspace. AutoML can augment its training datasets with features from either store. ^[automl-feature-store-integration-databricks-on-aws.md]

## Key Differences

| Aspect | Unity Catalog Feature Store | Workspace Feature Store |
|--------|-----------------------------|--------------------------|
| Scope | Cross-workspace, governed by Unity Catalog | Workspace-scoped, legacy |
| Governance | Integrated with Unity Catalog’s RBAC, lineage, and discovery | Workspace-level permissions |
| Recommendation | Current recommended approach | Legacy option |
| AutoML support | Supported | Supported |

## Using Feature Stores with AutoML

AutoML experiments can join additional features from feature tables in either store. The process is identical for both:

- **UI:** Click **Join features (optional)** during experiment configuration, select a feature table (from either store), and map primary keys to lookup keys in the training dataset. For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), a timestamp lookup key is also required. ^[automl-feature-store-integration-databricks-on-aws.md]

- **API:** Set the `feature_store_lookups` parameter in the AutoML run specification. The parameter accepts a list of dictionaries specifying `table_name` and `lookup_key`. ^[automl-feature-store-integration-databricks-on-aws.md]

### Requirements

- Classification and regression experiments: Databricks Runtime 11.3 LTS ML and above.
- Forecasting experiments: Databricks Runtime 12.2 LTS ML and above.

^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md)
- [Feature Store](/concepts/feature-store.md)
- AutoML
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md)

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
