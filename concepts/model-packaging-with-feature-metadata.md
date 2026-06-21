---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69c1f2f2682e61d6f6a150248947ec36e73349b6d7b84c1ca2a035e1785cfad9
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - train-models-with-feature-tables-databricks-on-aws.md
  confidence: 0.94
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-packaging-with-feature-metadata
    - MPWFM
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: train-models-with-feature-tables-databricks-on-aws.md
title: Model Packaging with Feature Metadata
description: The process of logging a model with references to its feature tables so it can automatically retrieve feature values during batch or real-time inference.
tags:
  - feature-store
  - model-registry
  - mlops
timestamp: "2026-06-19T18:12:43.863Z"
---

```yaml
---
title: Model Packaging with Feature Metadata
summary: The process of logging a model using FeatureEngineeringClient.log_model so it retains references to feature tables, enabling automatic feature retrieval during both batch and real-time inference.
sources:
  - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  - train-models-with-feature-tables-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:07:14.299Z"
updatedAt: "2026-06-19T14:49:55.697Z"
tags:
  - model-serving
  - mlops
  - databricks
  - inference
aliases:
  - model-packaging-with-feature-metadata
  - MPWFM
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Model Packaging with Feature Metadata

**Model Packaging with Feature Metadata** is the process of bundling a trained machine learning model with references to the [[Databricks Feature Store]] features used during training. When a model is logged using the `log_model` method of the `FeatureEngineeringClient` (for Feature Engineering in Unity Catalog) or the `FeatureStoreClient` (for Workspace Feature Store), the model retains the specifications of the features, enabling automatic feature retrieval at inference time without requiring the caller to supply the feature values directly. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## How It Works

During training, you create a [[Training Set (Feature Store)|TrainingSet]] that defines which features to use and how to join them via [[FeatureLookup]] objects. When you log the model with `log_model`, the model stores the metadata of those feature lookups. At inference, the caller provides only the primary key(s) (for example, `user_id`), and the model automatically retrieves the required feature values from the appropriate feature tables. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md, train-models-with-feature-tables-databricks-on-aws.md]

The model must be trained using the DataFrame returned by `TrainingSet.load_df`. If you modify this DataFrame before training, the modifications are not applied at inference, which can decrease model performance. ^[train-models-with-feature-tables-databricks-on-aws.md]

## Logging a Model with Feature Metadata

To package a model with feature metadata, use the `log_model` method of the Feature Store client corresponding to your workspace configuration:

- For workspaces enabled for Unity Catalog: `FeatureEngineeringClient.log_model`
- For legacy Workspace Feature Store: `FeatureStoreClient.log_model`

^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md, train-models-with-feature-tables-databricks-on-aws.md]

The model type must have a corresponding `python_flavor` in MLflow. Supported frameworks include:

- scikit-learn
- keras
- PyTorch
- SparkML
- LightGBM
- XGBoost
- TensorFlow Keras (using `mlflow.keras`)
- Custom MLflow pyfunc models

^[train-models-with-feature-tables-databricks-on-aws.md]

After logging, you can view the model's lineage in Catalog Explorer. Tables and functions that were used to create the model are automatically tracked and displayed. ^[train-models-with-feature-tables-databricks-on-aws.md]

## Inference Behavior

The source of feature values depends on the inference context:

- **Batch inference:** Feature values are retrieved from the offline store and joined with new data prior to scoring. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]
- **Real-time inference:** Feature values are retrieved from the online store. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

When serving models with [[Model Serving]], the endpoint automatically uses the entity IDs in the request data to look up pre-computed features from the [[Online Feature Store]]. The endpoint uses Unity Catalog to resolve lineage from the served model to the features used to train the model. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

Feature store models are also compatible with the [[Custom MLflow PyFunc Model|MLflow pyfunc interface]], so you can use MLflow to perform batch inference with feature tables. However, models that use [[time series feature tables]] are not supported with `mlflow.pyfunc.predict`; use `score_batch` instead. ^[train-models-with-feature-tables-databricks-on-aws.md]

## Using Custom Feature Values at Inference

By default, a model packaged with feature metadata looks up features from feature tables at inference. To override a feature with a custom value, include a column with the same name in the DataFrame passed to `score_batch`. The API uses the provided custom values for those columns and looks up only the remaining features from the Feature Store. ^[train-models-with-feature-tables-databricks-on-aws.md]

## Combining Feature Store and External Data

You can train a model using a combination of Feature Store features and data that resides outside Feature Store. To do so, include the extra data as columns in the DataFrame passed to `create_training_set` without excluding them. At inference, the DataFrame used in `score_batch` must include those same external data columns. ^[train-models-with-feature-tables-databricks-on-aws.md]

## Constraints

- A model can use at most 50 feature tables and 100 functions for training. ^[train-models-with-feature-tables-databricks-on-aws.md]
- Batch inference with MLflow (`mlflow.pyfunc.predict`) requires MLflow version 2.11 or above and does not support time series feature tables. For those, use `score_batch`. ^[train-models-with-feature-tables-databricks-on-aws.md]

## Handling Missing Feature Values

When a non-existent lookup key is passed to the model for prediction, the feature value can be `None` or `NaN` depending on the environment:
- For offline applications using `score_batch`, the returned value for a missing feature is `NaN`. ^[train-models-with-feature-tables-databricks-on-aws.md]
- For online applications using Model Serving, the returned value might be `None` if none of the lookup keys exist, or `NaN` if only a subset are missing. ^[train-models-with-feature-tables-databricks-on-aws.md]

## Related Concepts

- [[Databricks Feature Store]] — Centralized repository for reusable features.
- [[FeatureLookup]] — Specifies which features to use and how to join them.
- [[FeatureSpec]] — A Unity Catalog entity that defines a reusable set of features and functions for serving.
- [[Training Set (Feature Store)|TrainingSet]] — Combines feature lookups with raw training data and labels.
- [[Online Feature Store]] — Low-latency store for real-time inference.
- [[Feature Engineering in Unity Catalog]] — The modern approach to feature management.
- [[Workspace Feature Store UI|Workspace Feature Store]] — The legacy feature store for workspaces not enabled for Unity Catalog.
- [[Model Serving]] — Deploys models that automatically look up features from online stores.
- [[Custom MLflow PyFunc Model|MLflow pyfunc interface]] — Standard MLflow interface for batch inference with feature tables.
- [[Feature Governance and Lineage]] — Automatic tracking of tables and functions used in model creation.

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- train-models-with-feature-tables-databricks-on-aws.md
```

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [train-models-with-feature-tables-databricks-on-aws.md](/references/train-models-with-feature-tables-databricks-on-aws-a4118a38.md)
