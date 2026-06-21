---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afa61eae50270d4d386a84358ac8e46ecc9ece311a4ea1571fd96b631484ed40
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - online-feature-serving
    - OFS
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: Online Feature Serving
description: Real-time feature computation and lookup with millisecond latency, including on-demand computation, available via single-click endpoints in Databricks.
tags:
  - real-time
  - inference
  - serving
timestamp: "2026-06-18T15:06:26.083Z"
---

# Online Feature Serving

**Online Feature Serving** refers to the process of making feature values available for real-time inference in machine learning applications. When a model is deployed for online predictions, it needs to access the latest feature values with low latency, typically in milliseconds. Databricks Feature Store provides built-in mechanisms to serve features for online use cases, handling all feature computation and lookup tasks automatically. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

Online Feature Serving is a critical component of production ML systems where models must generate predictions in real time, such as recommendation engines, fraud detection, and personalization systems. Unlike batch inference, where features can be computed ahead of time, online serving requires features to be retrieved or computed on demand with minimal latency. ^[databricks-feature-store-databricks-on-aws.md]

Databricks Feature Store provides online serving capabilities that eliminate training/serving skew by ensuring that the feature computations used at inference time are identical to those used during model training. This significantly simplifies client-side code, as all feature lookups and computation are handled by the Feature Store. ^[databricks-feature-store-databricks-on-aws.md]

## How It Works

When you use features from Databricks Feature Store to train a model, the model automatically tracks lineage to the features that were used in training. At inference time, the model automatically looks up the latest feature values from the online store. ^[databricks-feature-store-databricks-on-aws.md]

The serving process involves:

1. **Feature Registration**: Features are defined and registered in the Feature Store, typically stored in [Unity Catalog](/concepts/unity-catalog.md) for governance and lineage tracking.
2. **Model Training**: During training, the model records which features it used, creating a lineage connection.
3. **Online Publication**: Feature tables are published to an online store (such as a key-value database) for low-latency access.
4. **Real-Time Lookup**: When a prediction request arrives, the serving infrastructure retrieves the relevant feature values from the online store and passes them to the model.

## Key Benefits

### Elimination of Training/Serving Skew

One of the primary advantages of using Databricks Feature Store for online serving is the elimination of training/serving skew. The system ensures that the feature computations used at inference are exactly the same as those used during model training, preventing discrepancies that can degrade model performance in production. ^[databricks-feature-store-databricks-on-aws.md]

### Simplified Client-Side Code

Because all feature lookups and computation are handled by Databricks Feature Store, client applications do not need to implement complex feature engineering logic. The serving infrastructure abstracts away the complexity of feature retrieval. ^[databricks-feature-store-databricks-on-aws.md]

### On-Demand Feature Computation

For real-time applications, Databricks Feature Store provides on-demand computation of features. This means that features can be computed dynamically at inference time rather than being pre-computed and stored, which is useful for features that depend on real-time context. ^[databricks-feature-store-databricks-on-aws.md]

### Low Latency

Model and feature serving endpoints are available with a single click and provide milliseconds of latency, making them suitable for real-time applications. ^[databricks-feature-store-databricks-on-aws.md]

## Supported Data Types for Online Serving

When features are published to online stores, complex data types are stored in JSON format. The Feature Store supports the following data types for online serving:

- `ArrayType` — stored as JSON (useful for dense vectors, tensors, and embeddings)
- `MapType` — stored as JSON (useful for sparse vectors, tensors, and embeddings)
- `StringType` — stored as text
- `IntegerType`, `FloatType`, `BooleanType`, `DoubleType`, `LongType`, `TimestampType`, `DateType`, `ShortType` — stored natively
- `BinaryType`, `DecimalType` — supported in Feature Engineering v0.3.5 or above
- `StructType` — supported in Feature Engineering v0.6.0 or above

^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The central registry for features used in ML models
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The modern approach to feature management
- [Model Serving](/concepts/model-serving.md) — Deploying models for real-time inference
- Training/Serving Skew — The problem that online feature serving helps prevent
- [Feature Lineage](/concepts/feature-lineage-tracking.md) — Tracking which features were used in model training
- Batch Inference — The alternative to online serving for non-real-time use cases

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
