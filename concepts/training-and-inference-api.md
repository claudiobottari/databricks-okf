---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 220ed95a396df83fa67cc34663d4344617f2ae412f9dadbba82677c66ff7bfb8
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-and-inference-api
    - Inference API and Training
    - TAIA
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Training and Inference API
description: Client methods for creating point-in-time correct training sets (create_training_set), logging models with feature lineage (log_model), and performing batch inference (score_batch)
tags:
  - machine-learning
  - training
  - inference
  - databricks
timestamp: "2026-06-18T11:45:16.426Z"
---

# Training and Inference API

The **Training and Inference API** in Databricks’ Declarative Feature Engineering provides methods for creating point-in-time correct training datasets, logging models with feature metadata, and performing batch inference with automatic feature lookup. These APIs are part of the `FeatureEngineeringClient` and ensure consistency between training and inference by using the same feature definitions registered in [Unity Catalog](/concepts/unity-catalog.md). ^[declarative-features-api-reference-databricks-on-aws.md]

---

## `create_training_set()`

`FeatureEngineeringClient.create_training_set()` creates a training dataset with point-in-time correct feature computation. It takes a DataFrame of training data, a list of Feature objects, and the label column(s). Optional `exclude_columns` can be specified. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
FeatureEngineeringClient.create_training_set(
    df: DataFrame,                                # DataFrame with training data
    features: Optional[List[Feature]],            # List of Feature objects
    label: Union[str, List[str], None],           # Label column name(s)
    exclude_columns: Optional[List[str]] = None,  # Optional: columns to exclude
) -> TrainingSet
```

For detailed usage, see the documentation on training models with declarative features. ^[declarative-features-api-reference-databricks-on-aws.md]

---

## `log_model()`

`FeatureEngineeringClient.log_model()` logs a model along with feature metadata for lineage tracking and automatic feature lookup during inference. It accepts the trained model object, an artifact path, an [MLflow flavor](/concepts/mlflow-model-flavors.md) module, and the `TrainingSet` produced by `create_training_set()`. Optionally, the model can be registered in [Unity Catalog](/concepts/unity-catalog.md) via `registered_model_name`. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
FeatureEngineeringClient.log_model(
    model,                                    # Trained model object
    artifact_path: str,                       # Path to store model artifact
    flavor: ModuleType,                       # MLflow flavor module (e.g., mlflow.sklearn)
    training_set: TrainingSet,                # TrainingSet used for training
    registered_model_name: Optional[str],     # Optional: register model in Unity Catalog
)
```

The feature metadata stored with the model enables automatic lookup of feature values during inference, eliminating manual feature engineering at serving time. ^[declarative-features-api-reference-databricks-on-aws.md]

---

## `score_batch()`

`FeatureEngineeringClient.score_batch()` performs offline batch inference with automatic feature lookup. It uses the feature metadata stored with the model to compute point-in-time correct features, ensuring consistency with the training pipeline. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
FeatureEngineeringClient.score_batch(
    model_uri: str,                           # URI of logged model (e.g., "models:/catalog.schema.model/1")
    df: DataFrame,                            # DataFrame with entity keys and timestamps
) -> DataFrame
```

The input DataFrame must contain the entity and timeseries columns used during training. Features are automatically computed from the source data. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
fe = FeatureEngineeringClient()

# Batch scoring with automatic feature lookup
predictions = fe.score_batch(
    model_uri="models:/main.ecommerce.fraud_model/1",
    df=inference_df,
)
predictions.display()
```

---

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) – Overview of the declarative API approach
- [Feature objects](/concepts/featurespec.md) – Definition and registration of features
- [Unity Catalog](/concepts/unity-catalog.md) – The underlying catalog for feature storage and model registry
- MLflow model signature – Automatic inclusion of request features in serving schemas
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) – Avoiding data leakage in feature computation

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
