---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9b50ba4346fa0ec60898633638645e672cc837ce1457088ab3870edefe1cfedd
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - point-in-time-correct-training-sets
    - PCTS
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Point-in-Time Correct Training Sets
description: The mechanism by which create_training_set computes point-in-time aggregated features, ensuring temporal consistency between labels and features
tags:
  - feature-engineering
  - training
  - time-series
timestamp: "2026-06-19T18:18:32.631Z"
---

# Point-in-Time Correct Training Sets

A **point-in-time correct training set** is a dataset used for machine learning where each row’s feature values are computed using only information that was available *before* the observation’s label timestamp. This prevents data leakage and ensures the model is trained on a realistic snapshot of the past.

## Overview

In the [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) framework on Databricks, point-in-time correctness is achieved through the `create_training_set` API. This function joins a labeled dataset (containing entity identifiers and timestamps) with one or more feature definitions, and computes aggregated feature values for each row using only data that falls *before* the row’s timestamp. The resulting training set can then be used for model training and logging. ^[declarative-features-databricks-on-aws.md]

## How It Works

To create a point-in-time correct training set, you provide:

- A **labeled DataFrame** (`df`) that includes entity columns (e.g., `user_id`), a timeseries column (e.g., `transaction_time`), and a label column (e.g., `target`).
- One or more **Feature objects** that define the aggregations (e.g., average spend over the last 30 days) and their time-window behavior (tumbling, sliding, or rolling windows).
- The **label column name** so the system can exclude it from the feature calculations.

The API then performs a point-in-time join: for each labeled row, it looks back from the row’s timestamp and computes the requested aggregations over the specified time windows, using only data that existed up to that moment. ^[declarative-features-databricks-on-aws.md]

## Requirements

- The entity columns and the timeseries column in the **labeled dataset must exactly match** the entity and timeseries columns defined in the Feature objects. Mismatched names will cause errors. ^[declarative-features-databricks-on-aws.md]
- The column name used as the `label` in the training dataset **must not exist** in any of the source tables that define the Features. ^[declarative-features-databricks-on-aws.md]
- All entity column names, timeseries column names, and request feature column names must be **globally unique** across all sources involved in the training set. ^[declarative-features-databricks-on-aws.md]

## Usage Example

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Define features with time windows
avg_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Avg(input="amount"),
                                 TumblingWindow(window_duration=timedelta(days=30))),
    name="avg_transaction_30d",
)

# Create point-in-time correct training set
training_set = fe.create_training_set(
    df=labeled_df,          # must contain user_id, transaction_time, target
    features=[avg_feature],
    label="target",
)

# Load the DataFrame for training
training_df = training_set.load_df()
```

After training, the training set can be logged with the model using `fe.log_model()`. ^[declarative-features-databricks-on-aws.md]

## Benefits

- **No future data leakage:** Features reflect only historical information, preserving the temporal order of events.
- **Correct aggregations:** Sliding, tumbling, and rolling windows are computed relative to each label’s timestamp, not a global cutoff.
- **Scalability:** The API handles large‑scale point‑in‑time joins efficiently, leveraging Delta Lake and Spark.

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) – The framework for defining and computing features.
- [Feature Materialization](/concepts/feature-materialization.md) – Storing computed features in offline/online stores for reuse.
- [Time‑Window Aggregations](/concepts/time-window-aggregation-types.md) – Tumbling, sliding, and rolling windows supported by the API.
- Training with Declarative Features – Full workflow for model training and batch inference.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
