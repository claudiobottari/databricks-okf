---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 058ca4de55e18f095babc710452bdbb0d18770aff7a1542a2db307933cfc494e
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-tracing-with-enable_feature_tracing
    - FTWE
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Feature Tracing with ENABLE_FEATURE_TRACING
description: Logging automatic feature lookup DataFrames to inference tables by setting the ENABLE_FEATURE_TRACING environment variable
tags:
  - machine-learning
  - feature-store
  - databricks
timestamp: "2026-06-18T14:43:21.045Z"
---

# Feature Tracing with ENABLE_FEATURE_TRACING

**Feature Tracing with `ENABLE_FEATURE_TRACING`** is a feature in [Databricks Model Serving](/concepts/databricks-model-serving.md) that enables logging of automatic feature lookup DataFrames to [Inference Tables](/concepts/inference-tables.md). When enabled, the system captures the feature data that was used during model inference and writes it to the endpoint's inference table for analysis, monitoring, and debugging purposes. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

To use `ENABLE_FEATURE_TRACING`, you must have:

- [Inference Tables](/concepts/inference-tables.md) enabled on the serving endpoint
- [MLflow](/concepts/mlflow.md) version 2.14.0 or above
- A model serving endpoint configured with [automatic feature lookup](/concepts/automatic-feature-lookup-for-model-serving.md) from [Feature Store](/concepts/feature-store.md)

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## How It Works

When `ENABLE_FEATURE_TRACING` is set to `true` on a model serving endpoint, the system logs the feature lookup DataFrame — the set of features retrieved from the Feature Store during inference — to the endpoint's inference table. This provides visibility into which feature values were used for each prediction request, enabling feature engineering validation, drift detection, and root cause analysis of model behavior changes. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Configuration

You set `ENABLE_FEATURE_TRACING` as an environment variable on the model serving endpoint. This can be done when creating or updating an endpoint through any of the following interfaces:

- **Serving UI:** Under **Advanced configurations**, add an environment variable with name `ENABLE_FEATURE_TRACING` and value `true`
- **REST API**
- **WorkspaceClient SDK**
- **MLflow Deployments SDK**

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Configuration via Serving UI

1. Navigate to the model serving endpoint configuration
2. Open **Advanced configurations**
3. Click **+ Add environment variables**
4. Enter `ENABLE_FEATURE_TRACING` as the environment name
5. Enter `true` as the value

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

Feature tracing is valuable for:

- **Debugging production models** — Understanding which feature values led to unexpected predictions
- **Monitoring feature drift** — Tracking changes in feature distributions over time
- **Auditing model behavior** — Maintaining a historical record of features used in each inference
- **Validating feature pipelines** — Confirming that the correct features are being served at inference time
- **Compliance and observability** — Meeting regulatory requirements for model explainability

## Related Concepts

- [Inference Tables](/concepts/inference-tables.md) — The destination where feature tracing logs are written
- [Automatic Feature Lookup](/concepts/automatic-feature-lookup-for-model-serving.md) — The mechanism that retrieves features from Feature Store during inference
- [Model Serving Environment Variables](/concepts/model-serving-environment-variables.md) — How to configure model serving behavior, including plain text and secrets-based variables
- [Feature Store](/concepts/feature-store.md) — The repository for storing and serving features
- Model Monitoring and Observability — Broader practices for tracking model performance in production

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
