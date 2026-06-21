---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b65ba7bc33aa0daad117ea023d289db62cd54e0cea805d40f5665c869ec5db5
  pageDirectory: concepts
  sources:
    - serve-declarative-features-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-feature-serving-limitation
    - DFSL
  citations:
    - file: serve-declarative-features-databricks-on-aws.md
title: Declarative Feature Serving Limitation
description: Feature Serving endpoints are not supported for Declarative Feature Engineering; models must be deployed via model serving endpoints using models logged through Unity Catalog.
tags:
  - limitation
  - feature-store
  - model-serving
timestamp: "2026-06-19T23:02:55.368Z"
---

# Declarative Feature Serving Limitation

**Declarative Feature Serving Limitation** refers to the restriction that [Feature Serving endpoints](/concepts/feature-serving-endpoint.md) cannot be used to serve features defined through [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) on Databricks. Instead, features must be served by deploying a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using a model logged through [Unity Catalog](/concepts/unity-catalog.md). ^[serve-declarative-features-databricks-on-aws.md]

## Details

The limitation is explicitly stated: Feature Serving endpoints are not supported for Declarative Feature Engineering. To serve features online, you must deploy a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) using a model that has been logged through [Unity Catalog](/concepts/unity-catalog.md). ^[serve-declarative-features-databricks-on-aws.md]

Models trained using features from Databricks automatically track lineage to the features they were trained on. When these models are deployed as [Model Serving](/concepts/model-serving.md) endpoints, they use [Unity Catalog](/concepts/unity-catalog.md) to look up features from online stores. ^[serve-declarative-features-databricks-on-aws.md]

## Workaround

To serve declarative features online, follow this workflow:

1. Train a model using the declarative features. The training process automatically logs feature lineage to [MLflow](/concepts/mlflow.md) and registers the model in [Unity Catalog](/concepts/unity-catalog.md).
2. Create a [Model Serving Endpoint](/concepts/model-serving-endpoint.md) that serves the registered model. The source documentation provides example code to create such an endpoint using the Databricks SDK.
3. Query the endpoint with `dataframe_records`. If the model was trained with `RequestSource` features, the request payload must include all `RequestSource` columns, as they are part of the [MLflow](/concepts/mlflow.md) model signature.

^[serve-declarative-features-databricks-on-aws.md]

## Related Concepts

- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) – The endpoint type that is not supported for declarative features.
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) – The feature engineering approach subject to this limitation.
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md) – The required endpoint type for serving features online.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog that [Model Serving](/concepts/model-serving.md) endpoints use to look up features.
- [RequestSource Features](/concepts/requestsource-features.md) – Features passed directly in the query payload, which must be included in the request if the model uses them.
- [Feature lineage](/concepts/feature-lineage-tracking.md) – Automatic tracking of feature-to-model relationships during training.

## Sources

- serve-declarative-features-databricks-on-aws.md

# Citations

1. [serve-declarative-features-databricks-on-aws.md](/references/serve-declarative-features-databricks-on-aws-86fbe897.md)
