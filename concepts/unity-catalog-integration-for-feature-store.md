---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5548c8e8f8629c4224f220e5a4aff7d43ce2a9480ffaf6d1605b388db543c451
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-integration-for-feature-store
    - UCIFFS
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Unity Catalog Integration for Feature Store
description: Built-in governance, cross-workspace sharing, and discovery of feature tables and models through Unity Catalog.
tags:
  - databricks
  - unity-catalog
  - governance
timestamp: "2026-06-19T18:12:05.999Z"
---

# Unity Catalog Integration for Feature Store

**Unity Catalog Integration for Feature Store** refers to the tight coupling between Databricks Feature Store and Unity Catalog. When feature tables and models are registered in Unity Catalog, the Feature Store automatically provides built-in governance, lineage, point-in-time joins, and cross-workspace feature sharing and discovery. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

Databricks Feature Store is a central registry for the features used in AI and ML models. With Unity Catalog integration, the entire model training workflow – from data pipelines that ingest raw data and create feature tables, to model training, batch inference, and model/feature serving endpoints – takes place on a single platform. ^[databricks-feature-store-databricks-on-aws.md]

The integration is the foundation of the modern Feature Store in Databricks. Workspaces that are not enabled for Unity Catalog must use the deprecated [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). ^[databricks-feature-store-databricks-on-aws.md]

## Key Benefits

- **Governance and Lineage:** When features are used to train a model, the model automatically tracks lineage to the features used during training. This lineage is stored in Unity Catalog, enabling auditability and reproducibility. ^[databricks-feature-store-databricks-on-aws.md]
- **Point-in-time Joins:** The Feature Store can perform point-in-time lookups to ensure that training data uses the feature values that were current at the time of the target observation. ^[databricks-feature-store-databricks-on-aws.md]
- **Cross-workspace Feature Sharing and Discovery:** Unity Catalog allows feature tables to be shared across workspaces, enabling reuse and collaboration on features across teams. ^[databricks-feature-store-databricks-on-aws.md]
- **Elimination of Training/Serving Skew:** At inference time, the model automatically looks up the latest feature values using the same computation logic that was used during training. Databricks Feature Store handles all feature computation tasks, eliminating the risk of mismatch between training and serving. ^[databricks-feature-store-databricks-on-aws.md]
- **Simplified Client Code:** All feature lookups and on-demand computation are handled by the Feature Store, significantly simplifying the code that a client application must write. ^[databricks-feature-store-databricks-on-aws.md]

## Requirements

To use Databricks Feature Store with Unity Catalog integration, the workspace must be enabled for Unity Catalog. If the workspace is not enabled, only the deprecated Workspace Feature Store is available. ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

The Feature Store supports a wide range of [PySpark data types](/concepts/supported-pyspark-data-types-for-features.md), including `IntegerType`, `FloatType`, `BooleanType`, `StringType`, `DoubleType`, `LongType`, `TimestampType`, `DateType`, `ShortType`, `ArrayType`, `BinaryType`, `DecimalType`, `MapType`, and `StructType`. These types support common ML feature representations such as dense vectors (as `ArrayType`), sparse vectors (as `MapType`), embeddings, and text. When published to online stores, `ArrayType` and `MapType` are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – The overall concept and central registry for ML features.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance and metadata layer that underpins the integration.
- [Point-in-time Joins](/concepts/point-in-time-joins.md) – A technique to avoid data leakage by joining features at the correct timestamp.
- [Feature Lineage](/concepts/feature-lineage-tracking.md) – Automatic tracking of feature-to-model associations.
- [Model Serving](/concepts/model-serving.md) – Serving endpoints that use the Feature Store for real-time inference.
- Batch Inference – Offline scoring using feature tables from Unity Catalog.
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) – The deprecated alternative for workspaces without Unity Catalog.
- Training/Serving Skew – The problem that Unity Catalog integration helps eliminate.

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
