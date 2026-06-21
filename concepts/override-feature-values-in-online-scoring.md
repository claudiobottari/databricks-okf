---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e323757230a9b4cac86c007bffdc1d30f2a650dd6cf607486a6b5d4d33a2c5d3
  pageDirectory: concepts
  sources:
    - model-serving-with-automatic-feature-lookup-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - override-feature-values-in-online-scoring
    - OFVIOS
  citations:
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
title: Override Feature Values in Online Scoring
description: Users can override automatically looked-up feature values during REST API scoring by including the desired feature values in the API payload, as long as the data types match the model's expectations.
tags:
  - model-serving
  - api
  - feature-override
timestamp: "2026-06-19T19:44:22.537Z"
---

# Override Feature Values in Online Scoring

**Override Feature Values in Online Scoring** allows you to supply custom feature values at inference time when scoring a model served via [Model Serving](/concepts/model-serving.md), bypassing the automatic lookup from the [Online Feature Store](/concepts/online-feature-store.md). This is useful for testing, edge cases, or when you want to provide a feature value that differs from what the online store returns.

All features required by the model – logged with `FeatureEngineeringClient.log_model` (for Feature Engineering in Unity Catalog) or `FeatureStoreClient.log_model` (for legacy Workspace Feature Store) – are automatically looked up from online stores during scoring. To override one or more of those values, include the desired feature values as part of the REST API payload when calling the serving endpoint. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Data Type Constraints

The new feature values must conform to the feature’s data type as expected by the underlying model. If the type does not match, the scoring request may fail or produce unexpected results. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Usage Context

Override works on top of the existing automatic feature lookup mechanism. You can mix automatically looked-up features with overridden values in the same request: any feature included in the payload is used instead of the online store value; any feature omitted from the payload is automatically looked up. This is supported for both [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) and third-party online stores such as Amazon DynamoDB (v0.3.8 and above). ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

## Related Concepts

- [Automatic Feature Lookup](/concepts/automatic-feature-lookup-for-model-serving.md) – The default behavior that override replaces for specific features.
- [Model Serving](/concepts/model-serving.md) – The serving infrastructure that processes scoring requests.
- REST API – The mechanism for sending scoring requests with overridden values.
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) and [FeatureStoreClient](/concepts/feature-store.md) – The logging clients that record the feature metadata.
- [Inference Table](/concepts/inference-tables.md) – Can store the augmented DataFrame (including looked-up and overridden features) for endpoints created after February 2025.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog where feature tables can be registered.

## Sources

- model-serving-with-automatic-feature-lookup-databricks-on-aws.md

# Citations

1. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
