---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12038abbf8579b91d1b085260f842be09a5a205f9e7e65da77ac4e8220f973a7
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - on-demand-feature-computation-for-real-time-inference
    - OFCFRI
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
title: On-Demand Feature Computation for Real-Time Inference
description: Databricks Feature Store supports on-demand computation of features for real-time applications, handling all feature computation tasks to simplify client-side code.
tags:
  - real-time
  - feature-engineering
  - inference
  - databricks
timestamp: "2026-06-19T14:49:47.986Z"
---

# On-Demand Feature Computation for Real-Time Inference

**On-Demand Feature Computation for Real-Time Inference** is a capability of [Databricks Feature Store](/concepts/databricks-feature-store.md) that computes feature values dynamically at inference time, rather than pre-computing and storing all possible feature values in advance. This approach is particularly useful for real-time applications where features depend on current context, user input, or rapidly changing data that cannot be pre-computed. ^[databricks-feature-store-databricks-on-aws.md]

## Overview

When using features from Databricks Feature Store to train models, the model automatically tracks lineage to the features that were used during training. At inference time, the model automatically looks up the latest feature values. For features that require computation based on real-time inputs, Databricks Feature Store provides on-demand computation, handling all the underlying feature computation tasks. ^[databricks-feature-store-databricks-on-aws.md]

This approach eliminates training/serving skew, ensuring that the feature computations used at inference are identical to those used during model training. It also significantly simplifies client-side code, as all feature lookups and computation are handled entirely by the Databricks Feature Store rather than requiring custom logic in the application layer. ^[databricks-feature-store-databricks-on-aws.md]

## Key Benefits

### Elimination of Training/Serving Skew

Because the same feature computation logic is used during both training and inference, on-demand computation guarantees consistency between the two phases. This is a fundamental advantage over manually implemented feature engineering pipelines, where discrepancies can easily arise. ^[databricks-feature-store-databricks-on-aws.md]

### Simplified Client Code

Client applications do not need to implement any feature computation logic. All feature lookups and computations are handled transparently by Databricks Feature Store, reducing the complexity and maintenance burden of inference-serving code. ^[databricks-feature-store-databricks-on-aws.md]

### Real-Time Feature Computation

For real-time inference scenarios, features that depend on request-specific data can be computed on the fly. This is essential for use cases where pre-computing all possible feature values is impractical or impossible. ^[databricks-feature-store-databricks-on-aws.md]

## How It Works

The on-demand computation workflow integrates with the broader [Databricks Feature Store](/concepts/databricks-feature-store.md) ecosystem:

1. **Training**: Features are defined and computed using Databricks, and models are trained using those features. Lineage between the model and its features is automatically tracked.
2. **Serving**: When the model is deployed and receives an inference request, Databricks Feature Store automatically computes the required features based on the incoming request data, using the same computation logic as during training.
3. **Lineage**: The relationship between the model, its features, and the feature computation logic is maintained throughout the lifecycle. ^[databricks-feature-store-databricks-on-aws.md]

This capability is part of the end-to-end ML workflow supported by Databricks, where data pipelines ingest raw data, create feature tables, train models, and serve features with millisecond-latency endpoints. ^[databricks-feature-store-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The central registry for features used in AI and ML models
- Training/Serving Skew — The inconsistency between feature computation during training and inference, which on-demand computation prevents
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating and selecting features for machine learning models
- Real-Time Inference — Machine learning model serving that returns predictions with low latency
- [Model Serving](/concepts/model-serving.md) — The infrastructure and processes for deploying models to production
- [Feature Lineage](/concepts/feature-lineage-tracking.md) — Tracking the relationship between features and the models that use them
- Batch Inference — Offline inference over large datasets

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
