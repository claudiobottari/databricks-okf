---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 404152f7d09c2c0bb6b250ef9ed7c56f8d161d787287a14e82d8d4d4196630c5
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - online-store-publishing-of-features
    - OSPOF
    - Online store|Online stores
    - Publishing Selected Features
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Online Store Publishing of Features
description: Features published to online stores for real-time serving with ArrayType and MapType stored in JSON format, providing millisecond-latency serving endpoints.
tags:
  - real-time
  - serving
  - feature-store
timestamp: "2026-06-18T11:37:37.709Z"
---

# Online Store Publishing of Features

**Online Store Publishing of Features** is the process of making feature tables from [Databricks Feature Store](/concepts/databricks-feature-store.md) available for real-time inference by publishing them to an online store. This enables low-latency feature lookups for serving models in production environments.

## Overview

When features are published to an online store, they become accessible for real-time serving with millisecond latency. Databricks Feature Store handles all feature computation tasks, including on-demand computation for real-time applications. This eliminates training/serving skew by ensuring that the feature computations used at inference are identical to those used during model training, and significantly simplifies client-side code as all feature lookups and computation are handled by Databricks Feature Store. ^[databricks-feature-store-databricks-on-aws.md]

## How Online Store Publishing Works

Feature tables registered in [Unity Catalog](/concepts/unity-catalog.md) can be published to an online store. When a model is trained using features from Databricks Feature Store, the model automatically tracks lineage to the features used in training. At inference time, the model automatically looks up the latest feature values from the online store. ^[databricks-feature-store-databricks-on-aws.md]

The publishing workflow covers:

- Data pipelines that ingest raw data and create feature tables
- Training models using published features
- Batch inference using the same features
- Real-time serving through [model serving endpoints](/concepts/model-serving-endpoint.md) and [feature serving endpoints](/concepts/feature-serving-endpoint.md) with milliseconds of latency

## Benefits

Publishing features to an online store provides several key advantages:

- **Eliminates training/serving skew** — The same feature computations used during model training are used at inference time, ensuring consistency. ^[databricks-feature-store-databricks-on-aws.md]
- **Simplifies client-side code** — All feature lookups and computation are handled by Databricks Feature Store, removing the need for custom lookup logic. ^[databricks-feature-store-databricks-on-aws.md]
- **Built-in governance and lineage** — When feature tables are registered in Unity Catalog, features automatically track lineage between training data and the models that use them. ^[databricks-feature-store-databricks-on-aws.md]
- **Cross-workspace sharing** — Published features can be discovered and shared across workspaces through Unity Catalog. ^[databricks-feature-store-databricks-on-aws.md]

## Requirements

To use Databricks Feature Store and publish features to an online store, your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md). If your workspace is not enabled for Unity Catalog, you must use the deprecated Workspace Feature Store instead. ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types

Databricks Feature Store supports the following [PySpark data types](/concepts/supported-pyspark-data-types-for-features.md) for features published to online stores:

| Data Type | Notes |
|-----------|-------|
| `IntegerType` | |
| `FloatType` | |
| `BooleanType` | |
| `StringType` | |
| `DoubleType` | |
| `LongType` | |
| `TimestampType` | |
| `DateType` | |
| `ShortType` | |
| `ArrayType` | Stored in JSON format when published to online stores |
| `BinaryType` | Supported in Feature Engineering v0.3.5+ |
| `DecimalType` | Supported in Feature Engineering v0.3.5+ |
| `MapType` | Supported in Feature Engineering v0.3.5+; stored in JSON format when published to online stores |
| `StructType` | Supported in Feature Engineering v0.6.0+ |

When published to online stores, `ArrayType` and `MapType` features are stored in JSON format. ^[databricks-feature-store-databricks-on-aws.md]

## Feature Storage Considerations

- **Dense vectors, tensors, and embeddings** can be stored as `ArrayType`.
- **Sparse vectors, tensors, and embeddings** can be stored as `MapType`.
- **Text** can be stored as `StringType`. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer providing feature registration and lineage
- Feature Serving — Real-time serving of published features with low latency
- [Model Serving](/concepts/model-serving.md) — Deployment of models that consume online features
- Training/Serving Skew — The consistency problem that online store publishing solves
- [Point-in-time Joins](/concepts/point-in-time-joins.md) — Feature computation capability available with Unity Catalog
- Feature Store Overview and Glossary — Conceptual overview of Databricks Feature Store

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
