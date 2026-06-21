---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 066125e6ee81ba62e57a15440b2bbe65b2f7bfe16326ae62c678496e088956eb
  pageDirectory: concepts
  sources:
    - model-serving-with-automatic-feature-lookup-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-feature-lookup-for-model-serving
    - AFLFMS
    - Automatic Feature Lookup
    - automatic feature lookup
  citations:
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
title: Automatic Feature Lookup for Model Serving
description: Databricks Model Serving can automatically look up feature values from online feature stores (Databricks or third-party) during model inference, eliminating the need for manual feature engineering in the serving pipeline.
tags:
  - machine-learning
  - model-serving
  - feature-store
timestamp: "2026-06-19T19:44:45.694Z"
---

# Automatic Feature Lookup for Model Serving

**Automatic Feature Lookup for Model Serving** is a capability in Databricks that enables model serving endpoints to automatically retrieve feature values from configured online stores during inference. When a model is deployed, the serving infrastructure automatically looks up required features from the specified online store without requiring custom lookup logic in the scoring code. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Overview

When a model is logged using `FeatureEngineeringClient.log_model` (for [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)) or `FeatureStoreClient.log_model` (for the legacy Workspace Feature Store), the model's feature dependencies are captured as part of the model metadata. When that model is deployed to a [Model Serving](/concepts/model-serving.md) endpoint, the serving infrastructure automatically looks up the required feature values from the configured online store before performing inference. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Supported Online Stores

Automatic feature lookup supports the following online stores:

- **Databricks Online Feature Store** — Databricks recommends this for real-time serving of feature values.
- **Amazon DynamoDB** — Supported from Databricks SDK v0.3.8 and above.
- **Third-party online stores** — Stores that have been published with read-only credentials.

For third-party online stores, the store must be configured with read-only credentials using Databricks Secrets. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Requirements

- The model must be logged using `FeatureEngineeringClient.log_model` (v0.3.5 and above) or `FeatureStoreClient.log_model` (for the legacy Workspace Feature Store).
- For third-party online stores, the store must be published with read-only credentials.
- The feature table can be published at any time before model deployment, including after model training. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Supported Data Types

Automatic feature lookup supports these data types:

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
- `MapType`

^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Overriding Feature Values

All features required by the model are automatically looked up from online stores for model scoring. To override feature values when scoring a model using a REST API, include the feature values as part of the API payload. The provided feature values must conform to the feature's expected data type. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Inference Table Logging

For endpoints created starting February 2025, you can configure a model serving endpoint to log the augmented DataFrame that contains the looked-up feature values and function return values. The DataFrame is saved to the [inference table](/concepts/inference-tables.md) for the served model, enabling auditing and debugging of feature lookup behavior during model serving. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Related Concepts

- [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) — The online store infrastructure for real-time feature serving.
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — Managing feature tables with Unity Catalog.
- [Model Serving](/concepts/model-serving.md) — The serving infrastructure that hosts models.
- [Feature Lookup](/concepts/feature-lookup.md) — The general mechanism for retrieving feature values.
- [Inference Tables](/concepts/inference-tables.md) — Storage for logged inference data including looked-up features.
- [Online Tables](/concepts/online-tables.md) — Row-oriented copies of Delta Tables optimized for online access.

## Sources

- model-serving-with-automatic-feature-lookup-databricks-on-aws.md

# Citations

1. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
