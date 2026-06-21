---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76b4f4d0a1a3b3654210aaac09549bace78d1580aea4c6bcca4daf12c19bb306
  pageDirectory: concepts
  sources:
    - model-serving-with-automatic-feature-lookup-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - third-party-online-stores-for-feature-serving
    - TOSFFS
    - Online stores for real-time serving
    - Third-Party Online Store
    - Third-party online stores
    - third-party online store
    - third-party online stores
  citations:
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
title: Third-Party Online Stores for Feature Serving
description: Databricks supports publishing feature tables to third-party online stores like Amazon DynamoDB (v0.3.8+), which must be configured with read-only credentials using Databricks secrets.
tags:
  - feature-store
  - third-party
  - dynamodb
  - databricks
timestamp: "2026-06-19T19:44:39.233Z"
---

# Third-Party Online Stores for Feature Serving

**Third-Party Online Stores for Feature Serving** refers to the integration of external, non‑Databricks online databases as the source of feature values for automated feature lookup when serving machine learning models. Databricks [Model Serving](/concepts/model-serving.md) can automatically retrieve feature values from either a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) or a supported third‑party online store during real‑time inference. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Overview

For real‑time serving of feature values, Databricks recommends using its own [Online Feature Store](/concepts/online-feature-store.md) for best performance and integration. However, users can also publish feature tables to a third‑party online store and configure the model to look up features from that store automatically. The feature table can be published at any time before model deployment, including after model training. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Requirements

To use a third‑party online store for automatic feature lookup:

- The model must have been logged using `FeatureEngineeringClient.log_model` (for [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)) or `FeatureStoreClient.log_model` (for the legacy Workspace Feature Store). Both clients require version 0.3.5 or above. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]
- The third‑party online store must be published with read‑only credentials using Databricks Secrets. Credentials are stored as a Databricks secret scope and referenced during publishing. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Supported Third‑Party Stores

As of the source documentation, **Amazon DynamoDB** is the supported third‑party online store for automatic feature lookup (requires Feature Store client version 0.3.8 and above). ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Supported Data Types

Automatic feature lookup from third‑party online stores supports the following Spark data types:

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

## Override Feature Values in Online Model Scoring

When scoring a model via the REST API, you can override automatically looked‑up feature values by including the new values as part of the API payload. The override values must conform to the data type expected by the underlying model. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Save the Augmented DataFrame to the Inference Table

For Model Serving endpoints created starting February 2025, you can configure the endpoint to log the augmented DataFrame that contains the looked‑up feature values and any function return values. This DataFrame is saved to the [inference table](/concepts/inference-tables.md) associated with the served model. Instructions for enabling this configuration are provided in the documentation on logging feature lookup DataFrames to inference tables. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Notebook Examples

Databricks provides example notebooks that demonstrate how to publish features to a third‑party online store and serve a trained model with automatic feature lookup. Separate notebooks are available for [Unity Catalog](/concepts/unity-catalog.md) and for the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md)
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md)
- [Publishing Feature Tables to an Online Store](/concepts/publishing-feature-tables-to-online-stores.md)
- [Inference Tables](/concepts/inference-tables.md)

## Sources

- model-serving-with-automatic-feature-lookup-databricks-on-aws.md

# Citations

1. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
