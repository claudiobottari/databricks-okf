---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c429c1c5f710ff1cdd0555a6fa0855c51fb988e2b53d646ecf102a6148853177
  pageDirectory: concepts
  sources:
    - model-serving-with-automatic-feature-lookup-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-table-augmented-dataframe-logging
    - ITADL
  citations:
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
title: Inference Table Augmented DataFrame Logging
description: Model serving endpoints created from February 2025 onwards can log the augmented DataFrame (containing looked-up features and function return values) to inference tables for monitoring.
tags:
  - monitoring
  - model-serving
  - inference-tables
timestamp: "2026-06-19T19:44:31.374Z"
---

# Inference Table Augmented DataFrame Logging

**Inference Table Augmented DataFrame Logging** is a feature of [Model Serving](/concepts/model-serving.md) on Databricks that allows a model serving endpoint to save the augmented DataFrame—containing looked-up feature values and function return values—to the endpoint's [inference table](/concepts/inference-tables.md). This logging is available for endpoints created starting February 2025. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## How It Works

When a model is served with automatic feature lookup enabled, the serving endpoint automatically retrieves feature values from an online store (such as a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) or a third-party online store like Amazon DynamoDB) to augment the inference request. With augmented DataFrame logging configured, the endpoint writes the complete, enriched DataFrame—including the looked-up features and any values returned by feature-computing functions—into the inference table associated with the served model. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Requirements

To use this logging feature, the model must have been logged with either `FeatureEngineeringClient.log_model` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.log_model` (for legacy Workspace Feature Store), requiring Databricks Feature Store client version 0.3.5 or above. For third-party online stores, the store must be published with read-only credentials|publish an online store with read-only credentials using Databricks secrets. The feature table may be published at any time prior to model deployment, including after model training. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Configuration

For detailed instructions on enabling this logging behavior, see Log feature lookup DataFrames to inference tables. The configuration is set on the model serving endpoint level and controls whether the augmented DataFrame is saved to the inference table for each request. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Related Concepts

- [Model Serving with Automatic Feature Lookup](/concepts/model-serving-with-automatic-feature-lookup.md) – Overview of the feature lookup mechanism.
- [Inference Tables](/concepts/inference-tables.md) – The storage target for request/response logs and augmented DataFrames.
- [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) – Recommended online store for real-time feature serving.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – Used to log models with feature metadata.
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) – Provides monitoring capabilities for inference tables.

## Sources

- model-serving-with-automatic-feature-lookup-databricks-on-aws.md

# Citations

1. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
