---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8260882d457a02d3020cff7846c71896d72749e5472834ec9c168e567522ade
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-engineering-with-unity-catalog
    - FEWUC
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Feature Engineering with Unity Catalog
description: Integration of Databricks Feature Store with Unity Catalog to provide built-in governance, lineage, point-in-time joins, and cross-workspace feature sharing.
tags:
  - unity-catalog
  - feature-store
  - governance
timestamp: "2026-06-18T15:06:24.703Z"
---

--- SOURCE: databricks-feature-store-databricks-on-aws.md ---

---
title: Feature Engineering with Unity Catalog
summary: How to use Unity Catalog as the central governance layer for feature engineering, enabling feature discovery, sharing, and serving across workspaces.
sources:
  - databricks-feature-store-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:10:03.236Z"
updatedAt: "2026-06-18T08:10:03.236Z"
tags:
  - feature-engineering
  - unity-catalog
  - feature-store
  - mlflow
aliases:
  - feature-engineering-with-unity-catalog
  - FEWUC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Engineering with Unity Catalog

**Feature Engineering with Unity Catalog** is the practice of managing, storing, and governing machine learning features using the Unity Catalog governance framework. When you register feature tables and models in Unity Catalog, you get built-in governance, lineage tracking, point-in-time joins, and cross-workspace feature sharing and discovery. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

With Databricks, the entire model training workflow takes place on a single platform. This includes:

- Data pipelines that ingest raw data, create feature tables, train models, and perform batch inference. ^[databricks-feature-store-databricks-on-aws.md]
- Model and feature serving endpoints that are available with a single click and provide low latency. ^[databricks-feature-store-databricks-on-aws.md]
- Data and model monitoring. ^[databricks-feature-store-databricks-on-aws.md]

When you use features from Databricks Feature Store to train models, the model automatically tracks lineage to the features that were used in training. At inference time, the model automatically looks up the latest feature values. Databricks Feature Store also provides on-demand computation of features for real-time applications, handling all feature computation tasks. This eliminates training/serving skew, ensuring that the feature computations used at inference are the same as those used during model training. It also significantly simplifies the client-side code, as all feature lookups and computation are handled by Databricks Feature Store. ^[databricks-feature-store-databricks-on-aws.md]

## Requirements

To use Databricks Feature Store, your workspace must be enabled for Unity Catalog. If your workspace is not enabled for Unity Catalog, see [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md). ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

Databricks Feature Store and legacy Workspace Feature Store support the following PySpark data types:

- `IntegerType`
- `FloatType`
- `BooleanType`
- `StringType`
- `DoubleType`
- `LongType`
- `TimestampType`
- `DateType`
- `ShortType`
- `ArrayType`
- `BinaryType` [1]
- `DecimalType` [1]
- `MapType` [1]
- `StructType` [2]

[1] `BinaryType`, `DecimalType`, and `MapType` are supported in all versions of Feature Engineering in Unity Catalog and in Workspace Feature Store v0.3.5 or above. ^[databricks-feature-store-databricks-on-aws.md]

[2] `StructType` is supported in Feature Engineering v0.6.0 or above. ^[databricks-feature-store-databricks-on-aws.md]

The data types listed above support feature types that are common in machine learning applications. For example:

- You can store dense vectors, tensors, and embeddings as `ArrayType`. ^[databricks-feature-store-databricks-on-aws.md]
- You can store sparse vectors, tensors, and embeddings as `MapType`. ^[databricks-feature-store-databricks-on-aws.md]
- You can store text as `StringType`. ^[databricks-feature-store-databricks-on-aws.md]

When published to online stores, `ArrayType` and `MapType` features are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## Feature Governance and Lineage

The Feature Store UI displays metadata on feature data types. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) – The central registry for features
- Feature Serving – Online and offline feature serving
- [Feature Lineage](/concepts/feature-lineage-tracking.md) – Automatic tracking of features used in training
- [Point-in-time Joins](/concepts/point-in-time-joins.md) – Temporal consistency for feature lookups
- Training/Serving Skew – Preventing feature computation drift

## More Information

For more information on best practices, download [The Comprehensive Guide to Feature Stores](https://www.databricks.com/p/ebook/the-comprehensive-guide-to-feature-stores). ^[databricks-feature-store-databricks-on-aws.md]

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
