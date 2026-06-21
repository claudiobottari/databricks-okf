---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e597dede5d4ad577ba91e8b913d3e50a2fba45e28bdf32d3d889472e04d609f
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-and-inference-api-methods
    - Inference API Methods and Training
    - TAIAM
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Training and Inference API Methods
description: "Core methods for ML lifecycle: create_training_set (point-in-time correct feature computation), log_model (model logging with feature lineage), and score_batch (offline batch inference with automatic feature lookup)."
tags:
  - mlops
  - training
  - inference
  - feature-engineering
timestamp: "2026-06-18T15:12:09.178Z"
---

## Training and Inference API Methods

The **Training and Inference API Methods** in Databricks Feature Engineering provide a programmatic interface for creating training datasets with point-in-time correctness, logging models with feature metadata, and performing batch inference with automatic feature lookup. These methods are exposed through the `FeatureEngineeringClient` class and are part of the [Declarative Features](/concepts/declarative-feature-engineering-api.md) system. ^[declarative-features-api-reference-databricks-on-aws.md]

### `create_training_set()`

Creates a training dataset with point-in-time correct feature computation. This method takes a DataFrame containing training data and a list of `Feature` objects, then computes the features at the appropriate historical snapshots to prevent data leakage.

```python
FeatureEngineeringClient.create_training_set(
    df: DataFrame,                                # DataFrame with training data
    features: Optional[List[Feature]],            # List of Feature objects
    label: Union[str, List[str], None],           # Label column name(s)
    exclude_columns: Optional[List[str]] = None,  # Optional: columns to exclude
) -> TrainingSet
```

For detailed usage, see [Train models with declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-with-declarative-features). ^[declarative-features-api-reference-databricks-on-aws.md]

### `log_model()`

Logs a model with feature metadata for lineage tracking and automatic feature lookup during inference. The metadata stored with the model allows the serving system to later look up the same features that were used during training.

```python
FeatureEngineeringClient.log_model(
    model,                                    # Trained model object
    artifact_path: str,                       # Path to store model artifact
    flavor: ModuleType,                       # MLflow flavor module (e.g., mlflow.sklearn)
    training_set: TrainingSet,                # TrainingSet used for training
    registered_model_name: Optional[str],     # Optional: register model in Unity Catalog
)
```

For detailed usage, see [Train models with declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-with-declarative-features). ^[declarative-features-api-reference-databricks-on-aws.md]

### `score_batch()`

Performs offline batch inference with automatic feature lookup. Uses the feature metadata stored with the model to compute point-in-time correct features, ensuring consistency between training and inference. The input DataFrame must contain the entity and timestamp columns that were used during training.

```python
FeatureEngineeringClient.score_batch(
    model_uri: str,                           # URI of logged model (e.g., "models:/catalog.schema.model/1")
    df: DataFrame,                            # DataFrame with entity keys and timestamps
) -> DataFrame
```

```python
fe = FeatureEngineeringClient()
# Batch scoring with automatic feature lookup
predictions = fe.score_batch(
    model_uri="models:/main.ecommerce.fraud_model/1",
    df=inference_df,
)
predictions.display()
```

Features are automatically computed from the source data. The method accepts a model URI referencing a model registered in Unity Catalog. ^[declarative-features-api-reference-databricks-on-aws.md]

### Related Concepts

- [Declarative Features](/concepts/declarative-feature-engineering-api.md) – The system for defining and registering features.
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) – The client class through which these methods are called.
- MLflow Model Logging – The underlying mechanism used by `log_model()`.
- Point-in-Time Correct Feature Computation – The principle that prevents data leakage during training and inference.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog system where model metadata and features are stored.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
