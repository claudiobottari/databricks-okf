---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a327e79ddfad911ce7cfd07f432315ed32f4318ff1fc5dd9984bd849877c51a0
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-feature-lifecycle-workflows
    - DFLW
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Declarative Feature Lifecycle Workflows
description: The end-to-end workflow covering feature development, model training, and feature materialization/serving with declarative APIs
tags:
  - feature-engineering
  - mlops
  - workflow
timestamp: "2026-06-19T18:18:23.171Z"
---

# Declarative Feature Lifecycle Workflows

**Declarative Feature Lifecycle Workflows** refers to the end-to-end process of defining, registering, computing, training with, materializing, and serving features using the Declarative Feature Engineering APIs on Databricks. These workflows enable data scientists and ML engineers to manage feature definitions as first-class objects in Unity Catalog, supporting reproducible model training and real-time serving. ^[declarative-features-databricks-on-aws.md]

## Overview

The Declarative Feature Engineering APIs simplify feature management by treating feature definitions as declarative objects rather than imperative transformation code. Features are defined from data sources—including [Delta Table](/concepts/delta-lake-table.md) sources and request-time data—using a variety of computations such as time-windowed aggregations, simple column selections, and more. The API supports three primary workflow categories: feature development, model training, and feature materialization and serving. ^[declarative-features-databricks-on-aws.md]

## Requirements

To use declarative feature workflows, you need:

1. A [Databricks Compute|classic compute](/concepts/databricks-connect-with-classic-compute.md) cluster running Databricks Runtime 17.0 ML or above. ^[declarative-features-databricks-on-aws.md]
2. The custom Python package installed in your notebook session: ^[declarative-features-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering>=0.15.0
dbutils.library.restartPython()
```

## Feature Development Workflow

The feature development workflow allows you to create and register feature definitions in [Unity Catalog](/concepts/unity-catalog.md). You can either define features directly and register them in one step using `create_feature`, or construct `Feature` objects locally and persist them later using `register_feature`. ^[declarative-features-databricks-on-aws.md]

Features can be defined with the following components: ^[declarative-features-databricks-on-aws.md]
- A [Delta Table](/concepts/delta-lake-table.md) source
- Entity columns (e.g., `user_id`, `customer_id`)
- Time-series columns for temporal features
- Aggregation functions such as `Sum`, `Avg`, `Count` with window configurations (`TumblingWindow`, `SlidingWindow`, `RollingWindow`)
- Simple column selections for non-aggregated features

### Example Feature Definition

```python
from databricks.feature_engineering.entities import (
    DeltaTableSource, Feature, AggregationFunction,
    Sum, Avg, TumblingWindow, SlidingWindow
)

source = DeltaTableSource(
    catalog_name="main",
    schema_name="feature_store",
    table_name="transactions"
)

avg_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"),
        TumblingWindow(window_duration=timedelta(days=30))
    ),
    name="avg_transaction_30d",
)
```

^[declarative-features-databricks-on-aws.md]

## Model Training Workflow

The training workflow uses `create_training_set` to compute point-in-time correct training datasets. This API joins labeled data with feature definitions, computing features as they existed at the time of each label observation—preventing data leakage. ^[declarative-features-databricks-on-aws.md]

Key points for training: ^[declarative-features-databricks-on-aws.md]
- Entity column names and timeseries column names must match between the labeled dataset and feature definitions.
- The label column name should not exist in any source tables used for feature definitions.
- The `log_model()` API logs the feature engineering pipeline alongside the model, enabling consistent batch inference with `score_batch()`.

### Training Example

```python
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
training_set.load_df().display()
```

^[declarative-features-databricks-on-aws.md]

## Feature Materialization and Serving Workflow

After defining features, you can materialize them to offline or online stores for efficient reuse. [Feature Materialization](/concepts/feature-materialization.md) enables fast feature retrieval during model training and real-time serving via CPU model serving endpoints. ^[declarative-features-databricks-on-aws.md]

Materialization supports two trigger types: ^[declarative-features-databricks-on-aws.md]
- **`CronSchedule`** for aggregation features—supports both offline and online store configurations.
- **`TableTrigger`** for column selection features—supports online store configuration only.

### Materialization Example

```python
fe.materialize_features(
    features=[avg_feature, sum_feature],
    offline_config=OfflineStoreConfig(
        catalog_name="main",
        schema_name="feature_store",
        table_name_prefix="customer_features",
    ),
    online_config=OnlineStoreConfig(
        catalog_name="main",
        schema_name="feature_store",
        table_name_prefix="customer_features_serving",
        online_store_name="customer_features_store",
    ),
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)
```

^[declarative-features-databricks-on-aws.md]

## Best Practices

### Feature Naming
- Use descriptive names for business-critical features.
- Follow consistent naming conventions across teams.
- Use auto-generated names during early development phases. ^[declarative-features-databricks-on-aws.md]

### Time Window Selection
Align window boundaries with business cycles (daily, weekly). Shorter windows capture recent trends but can be noisy; longer windows produce more stable distributions. Tumbling and sliding windows are more scalable than rolling windows. ^[declarative-features-databricks-on-aws.md]

### Performance Optimization
- Materialize features from the same data source in a single `materialize_features` call to minimize data scans.
- Use the same granularity for features on the same data source to enable better grouping during materialization. ^[declarative-features-databricks-on-aws.md]

### Entity Columns vs. Filter Conditions
- Use `entity` when you need different aggregation levels (e.g., customer-level vs. customer-merchant features).
- Use `filter_condition` on `DeltaTableSource` when filtering rows at the same aggregation level (e.g., high-value transactions only). ^[declarative-features-databricks-on-aws.md]

## Limitations

- Entity and timeseries column names must match between training datasets and feature definitions. ^[declarative-features-databricks-on-aws.md]
- The label column name in training data must not exist in source tables used for feature definitions. ^[declarative-features-databricks-on-aws.md]
- Only a limited list of user-defined aggregate functions (UDAFs) is supported. ^[declarative-features-databricks-on-aws.md]
- Entity columns cannot be of type `DATE` or `TIMESTAMP`. ^[declarative-features-databricks-on-aws.md]
- `RequestSource` supports only scalar data types (`INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, `SHORT`). Complex types are not supported. ^[declarative-features-databricks-on-aws.md]
- `RequestSource` does not support aggregation functions or time windows—only `ColumnSelection` functions. ^[declarative-features-databricks-on-aws.md]
- The set of entity column names, timeseries column names, and request feature column names must be globally unique across all sources in a training set or serving endpoint. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Delta Table](/concepts/delta-lake-table.md)
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md)
- [Point-in-time correctness](/concepts/point-in-time-correctness.md)
- [Feature Materialization](/concepts/feature-materialization.md)
- Online Serving
- Batch Inference

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
