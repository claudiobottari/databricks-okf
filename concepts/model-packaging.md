---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20ae43a0b67687b4c6c55875a87e6df0bcd321a740f08f334f35ce0ea408f6fe
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-packaging
    - model-packaging-with-feature-metadata
    - MPWFM
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Model Packaging
description: The process of logging a model with feature metadata so it retains references to its features and can automatically retrieve feature values during batch or real-time inference.
tags:
  - feature-store
  - model-registry
  - mlops
timestamp: "2026-06-18T11:38:25.236Z"
---

# Model Packaging

**Model Packaging** refers to the process of bundling a machine learning model with the metadata and references necessary to automatically retrieve feature values at inference time. When a model is trained using [Databricks Feature Store](/concepts/databricks-feature-store.md) and logged with the appropriate client method, it retains references to the features it was trained on, enabling seamless feature retrieval during both batch and real-time scoring. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

When you train a machine learning model using Feature Engineering in Unity Catalog or the legacy Workspace Feature Store and log it using the client's `log_model()` method, the model retains references to the features used during training. At inference time, the model can optionally retrieve feature values automatically — the caller only needs to provide the primary key of the features used in the model (for example, `user_id`), and the model retrieves all required feature values from the appropriate feature store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

This approach solves a common problem in machine learning: ensuring that the same feature computations used during training are consistently applied during inference, eliminating discrepancies between the two environments.

## Batch Inference vs. Real-Time Inference

The method of feature retrieval depends on the inference scenario:

- **Batch inference**: Feature values are retrieved from the [offline store](/concepts/offline-feature-store.md) and joined with new data prior to scoring. The offline store contains feature tables materialized as [Delta tables](/concepts/delta-lake-table.md). ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

- **Real-time inference**: Feature values are retrieved from the [Online Feature Store](/concepts/online-feature-store.md). For real-time serving use cases, features are published to an online store, and at inference time the model serving endpoint automatically uses entity IDs in the request data to look up pre-computed features from the online store to score the ML model. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Packaging a Model

To package a model with feature metadata, use the appropriate client method based on your workspace configuration:

- Use `FeatureEngineeringClient.log_model()` for Feature Engineering in Unity Catalog. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- Use `FeatureStoreClient.log_model()` for Workspace Feature Store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

When you log the model, it stores the specifications of features used for training. When the model is later used for inference, it automatically joins features from the appropriate feature tables. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## How It Fits in the ML Workflow

Model packaging is a key step in the machine learning workflow on Databricks:

1. Write code to convert raw data into features and create a Spark DataFrame.
2. Create a [Delta table](/concepts/delta-lake-table.md) in Unity Catalog with a primary key (a [Feature Table](/concepts/feature-table.md)).
3. Train and log a model using the feature table — this is where model packaging occurs.
4. Register the model in the [Model Registry](/concepts/mlflow-model-registry.md).
5. For real-time serving, publish features to an online feature store.
6. At inference time, the model serving endpoint uses Unity Catalog to resolve lineage from the served model to the features used to train it, and tracks lineage to the online feature store for real-time access. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The centralized repository for machine learning features
- [Feature Table](/concepts/feature-table.md) — Delta tables that organize features with primary key constraints
- [FeatureLookup](/concepts/featurelookup.md) — Specifies which features to use from a feature table during training
- [Training Set](/concepts/training-set-feature-store.md) — A list of features combined with raw training data and labels
- [Online Feature Store](/concepts/online-feature-store.md) — Low-latency store for real-time feature serving
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer that tracks lineage between models and features
- [Model Serving](/concepts/model-serving.md) — Endpoints that use packaged model metadata for inference

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
