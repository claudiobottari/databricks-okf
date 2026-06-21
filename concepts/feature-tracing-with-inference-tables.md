---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d040bd42e80c9f26a9dd3a1144b7fb6246f069be0bdf545392a35f5ec87b5957
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-tracing-with-inference-tables
    - FTWIT
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Feature Tracing with Inference Tables
description: Logging automatic feature lookup DataFrames to inference tables by setting ENABLE_FEATURE_TRACING environment variable to true, requiring MLflow 2.14.0 or above.
tags:
  - feature-store
  - inference
  - mlflow
  - model-serving
timestamp: "2026-06-19T14:24:34.283Z"
---

# Feature Tracing with Inference Tables

**Feature Tracing with Inference Tables** is a capability that enables logging [automatic feature lookup](/concepts/automatic-feature-lookup-for-model-serving.md) data frames to inference tables for [model serving endpoints](/concepts/model-serving-endpoint.md). When enabled, feature lookup operations are recorded alongside inference requests, providing observability into the feature values used during model serving.

## Overview

Feature tracing allows you to capture and log the feature DataFrames that are automatically looked up when a model serving endpoint processes requests. This provides a record of which feature values were used for each inference, enabling debugging, auditability, and analysis of feature behavior in production. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

Feature tracing with inference tables requires:

- **Inference tables enabled** on the model serving endpoint
- **MLflow 2.14.0 or above**
- **Feature store tables** configured with [Automatic Feature Lookup for Model Serving](/concepts/automatic-feature-lookup-for-model-serving.md)

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Enabling Feature Tracing

Feature tracing is enabled by setting the `ENABLE_FEATURE_TRACING` environment variable to `true` on the model serving endpoint. This can be configured through:

- The Serving UI
- The REST API
- The WorkspaceClient SDK
- The MLflow Deployments SDK

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Configuration via Serving UI

1. Navigate to the model serving endpoint configuration.
2. In **Advanced configurations**, click **+ Add environment variables**.
3. Enter `ENABLE_FEATURE_TRACING` as the environment variable name.
4. Enter `true` as the value.

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## How It Works

When feature tracing is enabled, each time the model serving endpoint performs an automatic feature lookup for an inference request, the feature lookup DataFrame is logged to the endpoint's inference table. This allows you to later query and analyze which feature values were served alongside each prediction. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

- **Audit and compliance**: Verify which feature values were used for specific predictions.
- **Debugging**: Investigate unexpected model behavior by examining the feature values at inference time.
- **Monitoring**: Track feature distribution shifts in production without additional instrumentation.
- **Root cause analysis**: Identify whether stale or incorrect feature values contributed to poor model performance.

## Related Concepts

- [Inference Tables](/concepts/inference-tables.md) — The storage destination where feature trace data is logged.
- [Automatic Feature Lookup for Model Serving](/concepts/automatic-feature-lookup-for-model-serving.md) — The mechanism that retrieves feature values during inference.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure where feature tracing is configured.
- Environment Variables for Model Serving — How environment variables like `ENABLE_FEATURE_TRACING` control serving behavior.
- [Feature Store](/concepts/feature-store.md) — The centralized repository for feature definitions and storage.

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
