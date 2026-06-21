---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ceefe7a606f7bfcc5ef689fba810f6eab0b4b270f3bf6d87a52b19149088042
  pageDirectory: concepts
  sources:
    - databricks-feature-store-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trainingserving-skew-elimination
    - TSE
    - Training-serving skew
    - training-serving skew
  citations:
    - file: databricks-feature-store-databricks-on-aws.md
    - file: |-
        databricks-feature-store-databricks-on-aws.md>

        This approach guarantees that the feature computations used at inference are the same as those used during model training
    - file: eliminating training/serving skew. ^[databricks-feature-store-databricks-on-aws.md
    - file: |-
        databricks-feature-store-databricks-on-aws.md>

        ## Related Concepts

        - [[Databricks Feature Store
title: Training/Serving Skew Elimination
description: Automatic alignment of feature computations between model training and inference to prevent performance degradation caused by inconsistent feature engineering.
tags:
  - machine-learning
  - mlops
  - feature-engineering
timestamp: "2026-06-19T18:12:04.484Z"
---

# Training/Serving Skew Elimination

**Training/Serving Skew Elimination** is a capability of [Databricks Feature Store](/concepts/databricks-feature-store.md) that automatically ensures feature computations used during model inference are identical to those used during model training. This eliminates a common source of silent model degradation in production machine learning systems. ^[databricks-feature-store-databricks-on-aws.md]

## The Problem

Training/serving skew, also known as training/serving mismatch, occurs when the feature computation logic differs between training and inference environments. In traditional ML workflows, feature engineering code must be duplicated across training pipelines and serving infrastructure. This creates risk: bug fixes, updates, or environmental differences can cause the two code paths to diverge over time, producing different feature values for the same input data. Such divergence can silently degrade model performance in production without triggering error signals. ^[databricks-feature-store-databricks-on-aws.md]

## How Databricks Feature Store Eliminates Skew

The [Databricks Feature Store](/concepts/databricks-feature-store.md) provides automatic mechanisms to prevent training/serving skew:

1. **Lineage Tracking**: When you use features from Databricks Feature Store to train a model, the model automatically tracks lineage to the features that were used during training. ^[databricks-feature-store-databricks-on-aws.md]

2. **Automatic Feature Lookup**: At inference time, the model automatically looks up the latest feature values using the same computation logic that was applied during training. ^[databricks-feature-store-databricks-on-aws.md]

3. **On-Demand Computation**: Databricks Feature Store provides on-demand computation of features for real-time applications, handling all feature computation tasks. ^[databricks-feature-store-databricks-on-aws.md>

This approach guarantees that the feature computations used at inference are the same as those used during model training, eliminating training/serving skew. ^[databricks-feature-store-databricks-on-aws.md]

## Benefits

- **Simplified Client-Side Code**: All feature lookups and computation are handled by Databricks Feature Store, eliminating the need for duplicated feature engineering logic in serving code. ^[databricks-feature-store-databricks-on-aws.md]
- **Single Platform Workflow**: The entire model training workflow takes place on a single platform, including data pipelines that ingest raw data, create feature tables, train models, and perform batch inference. ^[databricks-feature-store-databricks-on-aws.md]
- **Low-Latency Serving**: Model and feature serving endpoints are available with a single click and provide milliseconds of latency. ^[databricks-feature-store-databricks-on-aws.md]
- **Consistent Feature Definitions**: Any updates to feature definitions automatically apply to both training and serving workflows, preventing hidden inconsistencies. ^[databricks-feature-store-databricks-on-aws.md]

## Requirements

To use Databricks Feature Store for training/serving skew elimination, your workspace must be enabled for [Unity Catalog](/concepts/unity-catalog.md). The feature store registers feature tables and models in Unity Catalog, providing built-in governance, lineage, point-in-time joins, and cross-workspace feature sharing and discovery. ^[databricks-feature-store-databricks-on-aws.md]

## Implementation

When using features from Databricks Feature Store to train models, the training workflow automatically records feature metadata. At inference time, whether for batch or real-time serving, the system uses this metadata to retrieve or compute features using the identical logic from training. This ensures consistency without requiring manual code synchronization. ^[databricks-feature-store-databricks-on-aws.md>

## Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — The central registry for features that provides built-in training/serving consistency
- [Feature Lineage](/concepts/feature-lineage-tracking.md) — How models track which features were used during training
- [Point-in-time Joins](/concepts/point-in-time-joins.md) — A feature store capability that ensures correct historical feature lookup
- [Model Serving](/concepts/model-serving.md) — The inference infrastructure that benefits from skew elimination
- [Online Store](/concepts/online-feature-store.md) — The serving infrastructure for real-time feature lookup
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The process of creating features from raw data
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enables cross-workspace feature sharing
- Feature Store Overview and Glossary — Foundational concepts for understanding feature stores

## Sources

- databricks-feature-store-databricks-on-aws.md

# Citations

1. [databricks-feature-store-databricks-on-aws.md](/references/databricks-feature-store-databricks-on-aws-b97fcf6e.md)
2. databricks-feature-store-databricks-on-aws.md>

This approach guarantees that the feature computations used at inference are the same as those used during model training
3. eliminating training/serving skew. ^[databricks-feature-store-databricks-on-aws.md
4. databricks-feature-store-databricks-on-aws.md>

## Related Concepts

- [[Databricks Feature Store
