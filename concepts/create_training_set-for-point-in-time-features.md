---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50f044342828b9051b39c001d5662cadf1f933d3f641339bb792f3895028b6f9
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create_training_set-for-point-in-time-features
    - CFPF
  citations:
    - file: declarative-features-databricks-on-aws.md
title: create_training_set for Point-in-Time Features
description: An API that computes point-in-time correct feature values for ML training by joining labeled data with feature definitions, ensuring no data leakage by aligning timestamps.
tags:
  - feature-engineering
  - model-training
  - databricks
timestamp: "2026-06-18T15:12:49.393Z"
---

# create_training_set for Point-in-Time Features

The **`create_training_set`** API in the Databricks Declarative Feature Engineering framework computes point-in-time aggregated features from time-series data sources. It combines a labeled training dataset with feature definitions to produce a training DataFrame where each row contains features computed as of the time of the labeled event, avoiding data leakage. ^[declarative-features-databricks-on-aws.md]

## Overview

Point-in-time feature computation ensures that when training a machine learning model, each feature value reflects only information available up to the moment of the prediction event. The `create_training_set` function performs this computation by joining a labeled DataFrame with feature definitions that reference time-series data sources, using entity columns and timeseries columns to align the temporal context. ^[declarative-features-databricks-on-aws.md]

## How It Works

When you call `create_training_set`, the system:

1. Takes a labeled DataFrame that must include entity columns (e.g., `user_id`), a timeseries column (e.g., `transaction_time`), and a label column.
2. For each feature definition, computes the aggregation over the specified time window ending at the timestamp in the labeled DataFrame's timeseries column.
3. Returns a [TrainingSet](/concepts/training-set-feature-store.md) object whose `load_df()` method can be called to materialize the combined training data.

```python
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
training_set.load_df().display()
```

^[declarative-features-databricks-on-aws.md]

## Requirements

- Names of entity columns and timeseries columns must match between the labeled training dataset and the feature definitions. ^[declarative-features-databricks-on-aws.md]
- The column name used as the `label` column in the training dataset must not exist in any of the source tables used to define the features. ^[declarative-features-databricks-on-aws.md]
- Entity columns cannot be of type `DATE` or `TIMESTAMP`. ^[declarative-features-databricks-on-aws.md]

## Working with Registered and Local Features

### Using Unregistered Local Features

You can construct `Feature` objects locally using the Feature class and pass them to `create_training_set` without first registering them in Unity Catalog. This enables rapid experimentation during feature development. ^[declarative-features-databricks-on-aws.md]

```python
avg_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Avg(input="amount"), TumblingWindow(window_duration=timedelta(days=30))),
    name="avg_transaction_30d",
)
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
```

^[declarative-features-databricks-on-aws.md]

### Using Registered Features

After registering features with register_feature or create_feature, you can retrieve them with get_feature and pass them to `create_training_set`. The [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) provides a unified API for both workflows. ^[declarative-features-databricks-on-aws.md]

## Integration with Model Training

The `TrainingSet` object returned by `create_training_set` can be used with [log_model](/concepts/loggedmodel.md) and score_batch to track feature lineage and enable consistent inference. When calling `log_model`, you pass the `training_set` so that the model artifacts include feature metadata for serving. ^[declarative-features-databricks-on-aws.md]

```python
with mlflow.start_run():
    training_df = training_set.load_df()
    # training code
    fe.log_model(
        model=model,
        artifact_path="recommendation_model",
        flavor=mlflow.sklearn,
        training_set=training_set,
        registered_model_name=f"{CATALOG_NAME}.{SCHEMA_NAME}.recommendation_model",
    )
```

^[declarative-features-databricks-on-aws.md]

## Point-in-Time Correctness

The system automatically handles point-in-time semantics by using the timeseries column from the labeled DataFrame as the reference timestamp. For each labeled row, features are computed only from data that occurred before that timestamp. This prevents leakage where future information could influence model training. Common time window types include:

- **TumblingWindow**: Non-overlapping, fixed-duration windows (e.g., 30-day blocks).
- **SlidingWindow**: Overlapping windows with a slide duration (e.g., 7-day window sliding daily).
- **RollingWindow**: Continuous windows extending backward from each timestamp.

^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) – The overall framework for defining features.
- create_feature – One-step feature definition and registration.
- register_feature – Register locally-constructed features in Unity Catalog.
- compute_features – Preview feature values without creating a training set.
- materialize_features() API|materialize_features – Persist features for offline or online serving.
- [Point-in-Time Features](/concepts/point-in-time-feature-joins.md) – The general ML concept of time-aware feature computation.
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) – The client class that provides the API.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
