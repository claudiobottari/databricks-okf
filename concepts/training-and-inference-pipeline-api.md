---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eae904d8eb10214c35749879c90f3867877594bde9ae9f338368cf4c2ba268c7
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-and-inference-pipeline-api
    - Inference Pipeline API and Training
    - TAIPA
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Training and Inference Pipeline API
description: End-to-end ML pipeline API with create_training_set() for point-in-time correct feature computation, log_model() for lineage tracking, and score_batch() for batch inference with automatic feature lookup.
tags:
  - ml-pipeline
  - inference
  - training
  - databricks
timestamp: "2026-06-19T09:57:01.013Z"
---

# Training and Inference Pipeline API

The **Training and Inference Pipeline API** provides a set of methods in the `FeatureEngineeringClient` for creating point-in-time correct training datasets, logging models with feature lineage, and performing offline batch inference with automatic feature lookup. This API ensures consistency between training and inference by using feature metadata stored with the model.^[declarative-features-api-reference-databricks-on-aws.md]

## `create_training_set()`

`FeatureEngineeringClient.create_training_set()` creates a training dataset that performs point-in-time correct feature computation. It takes a Spark DataFrame (which must contain entity keys, timestamps, and optional label columns) together with a list of [`Feature`](/concepts/declarative-feature-engineering-api.md) objects, and returns a `TrainingSet` object. The method can optionally exclude columns from the input DataFrame.^[declarative-features-api-reference-databricks-on-aws.md]

```python
FeatureEngineeringClient.create_training_set(
    df: DataFrame,                                # DataFrame with training data
    features: Optional[List[Feature]],            # List of Feature objects
    label: Union[str, List[str], None],           # Label column name(s)
    exclude_columns: Optional[List[str]] = None,  # Optional: columns to exclude
) -> TrainingSet
```

For detailed usage, see the [Train models with declarative features](https://docs.databricks.com/aws/en/machine-learning/feature-store/train-with-declarative-features) guide.^[declarative-features-api-reference-databricks-on-aws.md]

## `log_model()`

`FeatureEngineeringClient.log_model()` logs a trained model along with its feature metadata for lineage tracking. This metadata enables automatic feature lookup during inference. The method accepts a trained model object, an artifact path, an MLflow flavor module (e.g., `mlflow.sklearn`), the `TrainingSet` used during training, and an optional registered model name in Unity Catalog.^[declarative-features-api-reference-databricks-on-aws.md]

```python
FeatureEngineeringClient.log_model(
    model,                                    # Trained model object
    artifact_path: str,                       # Path to store model artifact
    flavor: ModuleType,                       # MLflow flavor module
    training_set: TrainingSet,                # TrainingSet used for training
    registered_model_name: Optional[str],     # Optional: register model in Unity Catalog
)
```

## `score_batch()`

`FeatureEngineeringClient.score_batch()` performs offline batch inference with automatic feature lookup. It uses the feature metadata stored with the model to compute point-in-time correct features, ensuring consistency with training. The input DataFrame must contain the entity keys and timestamps used during training; features are automatically computed from the source data.^[declarative-features-api-reference-databricks-on-aws.md]

```python
FeatureEngineeringClient.score_batch(
    model_uri: str,                           # URI of logged model (e.g., "models:/catalog.schema.model/1")
    df: DataFrame,                            # DataFrame with entity keys and timestamps
) -> DataFrame
```

Example usage:

```python
fe = FeatureEngineeringClient()
predictions = fe.score_batch(
    model_uri="models:/main.ecommerce.fraud_model/1",
    df=inference_df,
)
predictions.display()
```

## Relationship Between the Methods

The training–inference pipeline follows this flow:

1. **Create training set** – `create_training_set()` prepares a point-in-time correct dataset from a Spark DataFrame and a list of `Feature` objects.  
2. **Train and log model** – After training, `log_model()` stores the model together with its feature metadata, including references to the `TrainingSet`.  
3. **Score batch** – `score_batch()` uses the logged model’s metadata to automatically retrieve and compute the same features for new inference data, maintaining point-in-time correctness.

These methods together form the core of the [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) workflow, enabling reproducible and consistent feature computation across training and inference.^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The client class that provides these methods.
- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) – The underlying API for defining features (`Feature`, `DeltaTableSource`, etc.).
- [MLflow](/concepts/mlflow.md) – Used for model logging and experiment tracking.
- [Unity Catalog](/concepts/unity-catalog.md) – Where features, models, and training sets are registered.
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) – The principle that ensures features are computed using only historical data available at each prediction time.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
