---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9344b8d739a69ca0705e45cd390dd2fe6628ac9a40875a3861097ac9b56aefd0
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-training-set-with-point-in-time-features
    - CTSWPF
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Create Training Set with Point-in-Time Features
description: Workflow for using declaratively defined features to compute point-in-time aggregated training datasets via create_training_set, ensuring temporal consistency between feature values and labels.
tags:
  - feature-engineering
  - model-training
  - mlops
timestamp: "2026-06-19T09:57:42.147Z"
---

## Create Training Set with Point-in-Time Features

**Create Training Set with Point-in-Time Features** refers to the process of using the Databricks Declarative Feature Engineering APIs to assemble a labeled training dataset that joins feature values as they existed at a specific point in time. This technique prevents data leakage by ensuring that each training example uses only feature values computed from data available before the prediction timestamp, rather than from future data.

## Overview

The `create_training_set` function from the `FeatureEngineeringClient` takes a labeled DataFrame and a list of Feature objects (defined declaratively) and produces a training set that aligns features with the correct time context. The labeled DataFrame must contain entity columns (e.g., `user_id`), a timeseries column (e.g., `transaction_time`), and a label column (e.g., `target`). For each row, the API retrieves feature values that were computed over the appropriate lookback window ending at or before that row’s timestamp. ^[declarative-features-databricks-on-aws.md]

This approach is essential for supervised learning tasks on time‑stamped data — such as forecasting, recommendation systems, and fraud detection — where the model must learn from historical data without referencing future events.

## Requirements

- A classic compute cluster running **Databricks Runtime 17.0 ML or above**. ^[declarative-features-databricks-on-aws.md]
- The custom Python package `databricks-feature-engineering` version 0.15.0 or later, installed in the notebook: ^[declarative-features-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering>=0.15.0
dbutils.library.restartPython()
```

- Entity and timeseries column names in the labeled DataFrame **must match** the column names used in the feature definitions. ^[declarative-features-databricks-on-aws.md]
- The label column name must **not** exist in any source table used for defining features. ^[declarative-features-databricks-on-aws.md]

## How It Works

### Define Features

Features are defined using the Declarative APIs (e.g., `create_feature` or constructing `Feature` objects). Each feature specifies:

- A `source` (e.g., `DeltaTableSource`).
- One or more `entity` columns.
- A `timeseries_column` (timestamp).
- An aggregation function over a time window (e.g., `Avg`, `Sum`, `Count` with `TumblingWindow`, `SlidingWindow`, or `RollingWindow`).

A feature can be defined and registered in Unity Catalog in a single step:

```python
latest_amount = fe.create_feature(
    source=source,
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    catalog_name=CATALOG_NAME,
    schema_name=SCHEMA_NAME,
    name="latest_amount",
)
```

^[declarative-features-databricks-on-aws.md]

### Assemble the Training Set

Once features are defined (locally or registered), pass them to `create_training_set` along with the labeled DataFrame:

```python
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
```

The resulting `training_set` object can be loaded as a Spark DataFrame with `training_set.load_df()`. This DataFrame contains one row per labeled example, with feature values computed exactly as they would have been at the prediction time. ^[declarative-features-databricks-on-aws.md]

### Log Model with Training Set Metadata

After training a model, use `fe.log_model()` to record the training set definition alongside the model. This enables the same point‑in‑time feature computation during batch inference and model serving:

```python
with mlflow.start_run():
    training_df = training_set.load_df()
    # training code ...
    fe.log_model(
        model=model,
        artifact_path="recommendation_model",
        flavor=mlflow.sklearn,
        training_set=training_set,
        registered_model_name=f"{CATALOG_NAME}.{SCHEMA_NAME}.recommendation_model",
    )
```

^[declarative-features-databricks-on-aws.md]

## Limitations

- The label column name must be unique and must not collide with column names in the feature source tables. ^[declarative-features-databricks-on-aws.md]
- Entity columns cannot be of type `DATE` or `TIMESTAMP`. ^[declarative-features-databricks-on-aws.md]
- Only a limited set of user‑defined aggregate functions (UDAFs) are supported in the `create_feature` API. See Supported Functions for more information. ^[declarative-features-databricks-on-aws.md]
- The set of entity column names, timeseries column names, and request feature column names must be globally unique across all sources in a training set. ^[declarative-features-databricks-on-aws.md]

## Best Practices

- **Use declarative features for training and inference.** The same feature definitions used in `create_training_set` can be reused with `score_batch()` for consistent offline inference. ^[declarative-features-databricks-on-aws.md]
- **Materialize features for performance.** After defining features, materialize them to an offline store to avoid recomputing time‑window aggregations repeatedly during training. See materialize_features() API|Materialize Declarative Features. ^[declarative-features-databricks-on-aws.md]
- **Align window sizes with business cycles.** For example, use 7‑day windows to smooth daily fluctuations or 1‑hour windows to capture rapid behavioral changes. ^[declarative-features-databricks-on-aws.md]
- **Group materialization of features from the same data source** in a single `materialize_features` call to minimize data scans. ^[declarative-features-databricks-on-aws.md]
- **Verify point‑in‑time correctness** by inspecting the training set DataFrame — each row’s feature values should reflect only historical data relative to that row’s timestamp.

## Related Concepts

- [Declarative Features](/concepts/declarative-feature-engineering-api.md) — The overarching API for defining and computing features.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The Python client used to create training sets and materialize features.
- [Point-in-Time Features](/concepts/point-in-time-feature-joins.md) — The principle of preventing data leakage by using only past data.
- materialize_features() API|Materialize Declarative Features — Making features available for offline and online serving.
- Train Models with Declarative Features — Complete workflow from training to batch inference.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
