---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3532c2d94c013045ebad41fab2178a3f949f6a51d293b5a98b11bcc9a01e9808
  pageDirectory: concepts
  sources:
    - model-serving-with-automatic-feature-lookup-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featureengineeringclientlog_model-featurestoreclientlog_model
    - F/F
  citations:
    - file: model-serving-with-automatic-feature-lookup-databricks-on-aws.md
title: FeatureEngineeringClient.log_model / FeatureStoreClient.log_model
description: Models must be logged using FeatureEngineeringClient.log_model (Unity Catalog) or FeatureStoreClient.log_model (legacy) at v0.3.5+ to enable automatic feature lookup at serving time.
tags:
  - machine-learning
  - feature-store
  - model-logging
timestamp: "2026-06-19T19:44:24.777Z"
---

Here is the wiki page for `FeatureEngineeringClient.log_model` / `FeatureStoreClient.log_model`.

---

## `FeatureEngineeringClient.log_model` / `FeatureStoreClient.log_model`

**`FeatureEngineeringClient.log_model`** and **`FeatureStoreClient.log_model`** are methods used to log machine learning models to the [MLflow](/concepts/mlflow.md) model registry while capturing the feature dependencies required for automatic feature lookup during model serving. These methods ensure that the model's feature metadata is stored alongside the model artifact, enabling Databricks [Model Serving](/concepts/model-serving.md) to automatically retrieve feature values from an online store at inference time. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

### Overview

When a model is logged with `FeatureEngineeringClient.log_model` (for [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)) or `FeatureStoreClient.log_model` (for the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md)), the system records which feature tables and columns the model uses. This metadata is essential for automatic feature lookup, where feature values are fetched from a [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md) or a [third-party online store](/concepts/third-party-online-stores-for-feature-serving.md) (such as Amazon DynamoDB) during online scoring. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

### Requirements

- The model must be logged using `FeatureEngineeringClient.log_model` or `FeatureStoreClient.log_model` with the corresponding client library version **v0.3.5 and above**. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]
- For third-party online stores, the store must be [published with read-only credentials](https://docs.databricks.com/aws/en/machine-learning/feature-store/fs-authentication). ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]
- The feature table can be published to the online store at any time — before or after model training — as long as it is published prior to model deployment. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

### Automatic Feature Lookup

After a model is logged with either method, Databricks Model Serving automatically looks up all required feature values from the configured online store during scoring. The feature lookup is supported for the following data types:

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

### Overriding Feature Values

When scoring a model using the REST API, you can override feature values by including them in the API payload. The new values must conform to the data type expected by the underlying model for that feature. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

### Logging Feature Lookup DataFrames

For model serving endpoints created starting February 2025, you can configure the endpoint to log the augmented DataFrame that contains the looked-up feature values. This DataFrame is saved to the [inference table](/concepts/inference-tables.md) for the served model, enabling detailed monitoring of feature usage. ^[model-serving-with-automatic-feature-lookup-databricks-on-aws.md]

### Related Concepts

- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md)
- [Databricks Online Feature Store](/concepts/databricks-online-feature-store.md)
- [Third-party online stores](/concepts/third-party-online-stores-for-feature-serving.md)
- [Model Serving](/concepts/model-serving.md)
- [Inference Tables](/concepts/inference-tables.md)
- [Feature Store](/concepts/feature-store.md)
- [MLflow](/concepts/mlflow.md)

### Sources

- model-serving-with-automatic-feature-lookup-databricks-on-aws.md

# Citations

1. [model-serving-with-automatic-feature-lookup-databricks-on-aws.md](/references/model-serving-with-automatic-feature-lookup-databricks-on-aws-7e249d4a.md)
