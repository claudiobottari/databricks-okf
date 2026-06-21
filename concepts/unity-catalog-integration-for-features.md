---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8c685a70c987578a489784afa5ad6f2ff11ac7dbd4f323f3ff494f043389c4a
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-integration-for-features
    - UCIFF
    - Unity Catalog Integration for Traces
    - unity-catalog-integration-for-feature-store
    - UCIFFS
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Unity Catalog Integration for Features
description: Feature tables and models registered in Unity Catalog enable built-in governance, point-in-time joins, and cross-workspace feature sharing and discovery.
tags:
  - unity-catalog
  - governance
  - databricks
timestamp: "2026-06-18T11:36:49.620Z"
---

# Unity Catalog Integration for Features

**Unity Catalog Integration for Features** refers to the tight coupling between [Databricks Feature Store](/concepts/databricks-feature-store.md) and [Unity Catalog](/concepts/unity-catalog.md) that provides a unified governance, lineage, and discovery layer for machine learning features across the entire ML lifecycle. When feature tables and models are registered in Unity Catalog, the integration delivers built-in governance, automatic point-in-time joins, cross-workspace feature sharing and discovery, and lineage tracking that connects training data to inference serving. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

The integration unifies the ML workflow on a single platform: data pipelines that ingest raw data and create feature tables; model training that automatically captures which features were used; and serving endpoints that provide millisecond-latency feature lookups at inference time. ^[databricks-feature-store-databricks-on-aws.md]

Because the entire pipeline — from ingestion through training to serving — runs on Databricks, the Feature Store automatically handles feature computation and lookup, eliminating training/serving skew. The feature computations used at inference are identical to those used during training. ^[databricks-feature-store-databricks-on-aws.md]

## Key Capabilities

### Governance and Lineage

When a model is trained using features from a Unity Catalog‑registered Feature Store, the model automatically records lineage metadata linking it to the feature tables it consumed. At inference time, the model looks up the latest feature values from the same source, ensuring consistency between training and serving. ^[databricks-feature-store-databricks-on-aws.md]

### Point-in-Time Joins

The Feature Store supports [Point-in-time Joins](/concepts/point-in-time-joins.md), which align feature values to the exact timestamp of each training record. This prevents look-ahead bias by joining historical feature values to the correct point in time. The integration handles this automatically when features are registered in Unity Catalog. ^[databricks-feature-store-databricks-on-aws.md]

### Cross-Workspace Feature Sharing

Teams can share feature tables across workspaces using [Delta Sharing](/concepts/delta-sharing.md) and Unity Catalog. This enables organizations to maintain a central, governed feature catalog while allowing individual workspaces to discover and consume features for model development. ^[databricks-feature-store-databricks-on-aws.md]

### Feature Serving

Model serving endpoints pick up the latest feature values automatically. The Feature Store supports both batch lookups and online serving with sub‑millisecond latency using [Model Serving](/concepts/model-serving.md) endpoints. ^[databricks-feature-store-databricks-on-aws.md]

### On-Demand Feature Computation

For real‑time applications, the Feature Store can compute features on‑demand, handling all computation in the serving layer. This means client‑side code can be simplified — all feature lookups and computations are handled by Databricks. ^[databricks-feature-store-databricks-on-aws.md]

## Requirements

The Unity Catalog integration requires that the workspace be enabled for Unity Catalog. Workspaces not enabled for Unity Catalog must use the deprecated [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md). ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

The Feature Store supports the following [PySpark data types](/concepts/supported-pyspark-data-types-for-features.md) for feature values: ^[databricks-feature-store-databricks-on-aws.md]

| Data Type | Notes |
|-----------|-------|
| `IntegerType` | Common for numerical features |
| `FloatType` | Decimal‑precision features |
| `BooleanType` | Binary flags |
| `StringType` | Text features |
| `DoubleType` | High‑precision numerics |
| `LongType` | Large integers |
| `TimestampType` | Time‑series features |
| `DateType` | Date features |
| `ShortType` | Compact integers |
| `ArrayType` | Dense vectors, tensors, embeddings |
| `BinaryType` | Supported in v0.3.5+ |
| `DecimalType` | Supported in v0.3.5+ |
| `MapType` | Sparse vectors, tensors, embeddings; supported in v0.3.5+ |
| `StructType` | Supported in v0.6.0+ |

- `ArrayType` and `MapType` features are stored as JSON when published to online stores. ^[databricks-feature-store-databricks-on-aws.md]

## Feature Engineering in Unity Catalog

The [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) API provides programmatic access to the Feature Store, including functions for creating, publishing, and managing feature tables, as well as for training and serving models using registered features. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that the Feature Store integrates with
- [Feature Store](/concepts/feature-store.md) — The central registry for ML features
- [MLflow](/concepts/mlflow.md) — The model lifecycle management framework that tracks feature lineage
- [Model Serving](/concepts/model-serving.md) — The serving layer that provides low‑latency feature lookup
- [Point-in-Time Queries](/concepts/point-in-time-feature-joins.md) — Correctly joining feature values to training records
- [Delta Sharing](/concepts/delta-sharing.md) — Cross‑workspace feature sharing
- [ABAC GRANT Policy](/concepts/abac-grant-policy.md) — Attribute‑based access control for models ([ABAC GRANT Policy](/concepts/abac-grant-policy.md))

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
