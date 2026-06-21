---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 16f261d15f5f60e3ecb816f1a7160225fd651f25f36bbd342555835a623cd26b
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-tracing-for-inference-tables
    - FTFIT
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Feature Tracing for Inference Tables
description: Logging automatic feature lookup DataFrames to inference tables by setting the ENABLE_FEATURE_TRACING environment variable on a model serving endpoint
tags:
  - model-serving
  - feature-store
  - inference
  - mlflow
timestamp: "2026-06-19T17:51:21.691Z"
---

---
title: Feature Tracing for Inference Tables
summary: Logging the automatic feature lookup DataFrame to inference tables using the ENABLE_FEATURE_TRACING environment variable on model serving endpoints.
sources:
  - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
kind: concept
tags:
  - databricks
  - model-serving
  - feature-store
  - inference-tables
aliases:
  - feature-tracing
  - FTFIT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Tracing for Inference Tables

**Feature tracing for inference tables** is a configuration option that logs the automatic feature lookup DataFrame from a model serving endpoint to its associated inference table. When enabled, every request’s feature lookup data is recorded alongside the request and response payloads, providing a complete audit trail of the features used during inference.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The model serving endpoint must have [Inference Tables](/concepts/inference-tables.md) enabled.
- The model must use [automatic feature lookup](/concepts/automatic-feature-lookup-for-model-serving.md) (e.g., from the Databricks Feature Store).
- MLflow version 2.14.0 or above is required on the serving environment.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Configuration

Feature tracing is activated by setting the environment variable `ENABLE_FEATURE_TRACING` to `true` on the model serving endpoint. This can be done when creating or updating the endpoint through any of the supported interfaces (Serving UI, REST API, or SDK).^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Example (Serving UI)

1. Open the endpoint’s **Advanced configurations** section.
2. Click **+ Add environment variables**.
3. Enter `ENABLE_FEATURE_TRACING` as the name and `true` as the value.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

The same environment variable can be set via the REST API or the WorkspaceClient SDK when calling the endpoint creation or update operations.

## Use cases

- **Observability**: Track which feature values were served for each prediction, making it easier to debug model behavior and reproduce results.
- **Compliance**: Maintain a historical record of the features used in production, supporting audit and governance requirements.
- **Feature drift monitoring**: Compare logged feature distributions over time to detect changes in upstream feature pipelines.

## Related concepts

- [Inference Tables](/concepts/inference-tables.md) – the storage target for logged inference data
- [Model Serving](/concepts/model-serving.md) – the serving infrastructure that hosts the model
- [Automatic Feature Lookup](/concepts/automatic-feature-lookup-for-model-serving.md) – the mechanism that retrieves features from the Feature Store at serving time
- [Feature Store](/concepts/feature-store.md) – the centralized repository for machine learning features
- [MLflow](/concepts/mlflow.md) – the ML lifecycle tool that versioned the model and enforces the version requirement

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
