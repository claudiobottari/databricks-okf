---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53b7f94333b63697c81e2f3217bb88cac5c490aadbe7e3861b25e50d1771921f
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-and-inference-api-with-point-in-time-correctness
    - Inference API with Point-in-Time Correctness and Training
    - TAIAWPC
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Training and Inference API with Point-in-Time Correctness
description: API methods (create_training_set, log_model, score_batch) that ensure point-in-time correct feature computation, lineage tracking, and automatic feature lookup during batch inference.
tags:
  - training
  - inference
  - mlflow
  - point-in-time
timestamp: "2026-06-19T14:57:22.602Z"
---

# Training and Inference API with Point-in-Time Correctness

**Training and Inference API with Point-in-Time Correctness** refers to the set of methods in the Databricks Declarative Feature Engineering API that ensure feature values are computed exactly as they would have been at a given point in time, preventing data leakage and online‑offline skew. The core methods – `create_training_set`, `log_model`, and `score_batch` – work together to guarantee that the same point‑in‑time logic used during training is applied at inference time.

## Overview

Point-in-time correctness is essential for time‑series features (such as rolling aggregations) where using future data to compute past features would introduce leakage. The Declarative Feature Engineering API enforces this by:

- Recording the feature definitions (source table, entity keys, time window, aggregation function) and storing them as MLflow model metadata. ^[declarative-features-api-reference-databricks-on-aws.md]
- At training time, the `create_training_set` method computes features for each training row using only data available *before* that row’s event timestamp. ^[declarative-features-api-reference-databricks-on-aws.md]
- At inference time, the `score_batch` method reads the stored metadata and recomputes features using the same point‑in‑time logic, guaranteeing consistency. ^[declarative-features-api-reference-databricks-on-aws.md]

The API supports rolling, tumbling, and sliding windows; the point‑in‑time calculation is most commonly described for rolling windows:

> “When a rolling window feature is used in training pipelines, an accurate point‑in‑time feature calculation is performed on the source data using the fixed-length window duration immediately preceding a specific event’s timestamp. This helps prevent online‑offline skew or data leakage.” ^[declarative-features-api-reference-databricks-on-aws.md]

## Key API Functions

### `create_training_set()` ^[declarative-features-api-reference-databricks-on-aws.md]

Creates a [TrainingSet](/concepts/training-set-feature-store.md) that computes features with point‑in‑time correctness.

```python
FeatureEngineeringClient.create_training_set(
    df: DataFrame,
    features: Optional[List[Feature]],
    label: Union[str, List[str], None],
    exclude_columns: Optional[List[str]] = None
) -> TrainingSet
```

The input DataFrame must contain the entity columns and a timestamp column (defined in the `Feature` objects). The system looks back from each row’s timestamp to compute feature values, ensuring that no future data influences the training labels.

### `log_model()` ^[declarative-features-api-reference-databricks-on-aws.md]

Logs a model together with the feature metadata needed for point‑in‑time inference.

```python
FeatureEngineeringClient.log_model(
    model,
    artifact_path: str,
    flavor: ModuleType,
    training_set: TrainingSet,
    registered_model_name: Optional[str]
)
```

This stores the feature definitions (sources, entities, time windows) inside the MLflow model so that `score_batch` can later reproduce the exact same feature computation.

### `score_batch()` ^[declarative-features-api-reference-databricks-on-aws.md]

Performs offline batch inference with automatic, point‑in‑time correct feature lookup.

```python
FeatureEngineeringClient.score_batch(
    model_uri: str,
    df: DataFrame
) -> DataFrame
```

The input `df` must contain the entity and timeseries columns used during training. Features are recomputed from the source data using the same lookback windows as training, ensuring consistency.

> “Uses the feature metadata stored with the model to compute point‑in‑time correct features, ensuring consistency with training.” ^[declarative-features-api-reference-databricks-on-aws.md]

## Point‑in‑Time Correctness Mechanism

The guarantee of point‑in‑time correctness is built into the [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md)’s handling of time windows:

- **RollingWindow** – The window `[T - duration - delay, T - delay)` is evaluated for each event at time `T`. ^[declarative-features-api-reference-databricks-on-aws.md]
- **TumblingWindow** – For each event, the aggregation uses only windows that end at or before the event timestamp. ^[declarative-features-api-reference-databricks-on-aws.md]
- **SlidingWindow** – Similar to tumbling, but overlapping windows are allowed; each event’s features are computed from windows ending at or before that event’s time. ^[declarative-features-api-reference-databricks-on-aws.md]

Both `create_training_set` and `score_batch` apply the same window semantics relative to the timestamp column provided in the input DataFrame. This eliminates the common pitfall of training on “future” feature values that would not be available at inference time.

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — The broader API for defining feature sources, aggregations, and time windows.
- [Point‑in‑Time Join](/concepts/point-in-time-joins.md) — A related technique for joining historical feature data without leakage.
- Online‑Offline Skew — The discrepancy that point‑in‑time correctness aims to prevent.
- [Rolling Window](/concepts/rolling-window-backtesting.md) — The most common time window type for point‑in‑time features.
- MLflow Model Lineage — How feature metadata is persisted alongside the model.
- Batch Inference — The offline use case where `score_batch` is applied.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
