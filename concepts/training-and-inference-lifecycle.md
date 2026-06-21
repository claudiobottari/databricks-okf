---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38c64fede36466a2d8b82bc96b071ecd5b67cf25a39cfc813f0a5783fb5b1566
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-and-inference-lifecycle
    - Inference Lifecycle and Training
    - TAIL
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Training and Inference Lifecycle
description: "End-to-end ML workflow using declarative features: create_training_set for point-in-time correct datasets, log_model for lineage tracking, and score_batch for offline batch inference with automatic feature lookup."
tags:
  - feature-engineering
  - ml-lifecycle
  - training
  - inference
timestamp: "2026-06-19T18:18:11.985Z"
---

# Training and Inference Lifecycle

The **Training and Inference Lifecycle** describes the end-to-end process of developing, deploying, and maintaining machine learning models, from initial feature engineering through model training and ultimately to production inference. This lifecycle encompasses both the **training** phase, where models learn from historical data, and the **inference** phase, where trained models make predictions on new data.

## Overview

The lifecycle begins with the creation of features from source data, followed by model training using those features, and concludes with deployment for batch or real-time inference. The [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) provides a unified framework for managing this entire lifecycle, ensuring that features computed during training are computed identically during inference to prevent [training-serving skew](/concepts/trainingserving-skew-elimination.md). ^[declarative-features-api-reference-databricks-on-aws.md]

## Training Phase

### Feature Engineering

During the training phase, features are defined and registered using the Feature constructor and `register_feature()` or `create_feature()` methods. Features can be constructed from:

- **[DeltaTableSource](/concepts/deltatablesource.md)**: Features computed from [Delta Lake](/concepts/delta-lake.md) tables with time-window aggregations
- **[RequestSource](/concepts/requestsource.md)**: Features that are passed through from the inference request payload

The recommended workflow is to construct features locally and experiment with them before registration. ^[declarative-features-api-reference-databricks-on-aws.md]

### Creating Training Sets

The `create_training_set()` method creates a training dataset with [point-in-time correct](/concepts/point-in-time-correctness.md) feature computation. This ensures that features are computed using only data available up to the timestamp of each training example, preventing data leakage from future information. ^[declarative-features-api-reference-databricks-on-aws.md]

### Model Logging

After training, models are logged using `log_model()` with feature metadata for lineage tracking. This metadata enables automatic feature lookup during inference, ensuring that the same features used during training are available at serving time. ^[declarative-features-api-reference-databricks-on-aws.md]

## Inference Phase

### Batch Inference

Batch inference is performed using `score_batch()`, which performs offline scoring with automatic feature lookup. The method uses the feature metadata stored with the model to compute features consistently with the training phase. The input DataFrame must contain the entity keys and timestamps used during training. ^[declarative-features-api-reference-databricks-on-aws.md]

### Real-Time Inference

For real-time inference, [RequestSource](/concepts/requestsource.md) features are provided in the HTTP request payload. These features are defined at serving time and are extracted from the labeled DataFrame during training. The model signature includes [RequestSource](/concepts/requestsource.md) columns as required inputs, ensuring that the serving endpoint's API schema reflects which fields callers must provide. ^[declarative-features-api-reference-databricks-on-aws.md]

## Time Window Management

The lifecycle supports three time window types for controlling lookback behavior:

- **RollingWindow**: Continuous, real-time aggregates that update as new events occur
- **TumblingWindow**: Fixed, non-overlapping windows that partition time completely
- **SlidingWindow**: Overlapping windows with configurable slide intervals

## Lifecycle Phases

The training and inference lifecycle includes several distinct phases:

1. **Data Preparation**: Source data is prepared and filtered using `filter_condition` and `transformation_sql`
2. **Feature Registration**: Features are registered in [Unity Catalog](/concepts/unity-catalog.md) for governance and discovery
3. **Model Training**: Training datasets are created with point-in-time correct feature computations
4. **Model Deployment**: Models are logged and registered for serving
5. **Inference Execution**: Batch or real-time scoring with automatic feature lookups

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — The primary API for managing the training-inference lifecycle
- [Feature Store](/concepts/feature-store.md) — Centralized repository for feature management
- [Model Serving](/concepts/model-serving.md) — Deployment infrastructure for real-time and batch inference
- Training-Serving Skew — Prevention of feature computation differences between phases
- materialize_features() API|Materialized Features — Pre-computed features for faster inference

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
