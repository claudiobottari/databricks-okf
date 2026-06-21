---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03296e154efbd808cb69cf7de352b0ae7555f239bec441bacc8b123d1630c3d0
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - declarative-feature-engineering-apis
    - DFEA
    - Declarative Feature Engineering on Databricks
    - Declarative Feature APIs
    - Declarative Feature Engineering|declarative features
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Declarative Feature Engineering APIs
description: A Databricks framework for defining and computing ML features using declarative objects rather than imperative data pipelines
tags:
  - feature-engineering
  - machine-learning
  - databricks
  - mlops
timestamp: "2026-06-19T18:18:57.091Z"
---

Here is the wiki page for "Declarative Feature Engineering APIs".

---

## Declarative Feature Engineering APIs

**Declarative Feature Engineering APIs** are a set of Python interfaces in [Databricks Feature Store](/concepts/databricks-feature-store.md) that allow you to define and compute features from data sources using a declarative approach—specifying *what* features to compute rather than *how* to compute them. These APIs work with [Unity Catalog](/concepts/unity-catalog.md) to manage feature definitions as first-class objects, supporting both model training and serving workflows. ^[declarative-features-databricks-on-aws.md]

### Overview

The Declarative Feature Engineering APIs enable you to define features using a variety of data sources (Delta tables and request-time data) and computations (time-windowed aggregations, simple column selections, and more). The API provides two primary workflows: feature development and feature materialization. ^[declarative-features-databricks-on-aws.md]

- **Feature development workflow**: Use `create_feature` to define Unity Catalog feature objects, or construct `Feature` objects locally and register them later with `register_feature`. ^[declarative-features-databricks-on-aws.md]
- **Model training workflow**: Use `create_training_set` to calculate point-in-time aggregated features for machine learning. ^[declarative-features-databricks-on-aws.md]
- **Feature materialization and serving workflow**: After defining a feature, use `materialize_features` to materialize it to an offline or online store for efficient reuse and serving. ^[declarative-features-databricks-on-aws.md]

### Requirements

- A classic compute cluster running Databricks Runtime 17.0 ML or above. ^[declarative-features-databricks-on-aws.md]
- You must install the custom Python package each time you run a notebook: ^[declarative-features-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering>=0.15.0
dbutils.library.restartPython()
```

### Core Components

#### Feature Object

A `Feature` object represents a single feature definition. It includes a data source, entity columns, a timeseries column, and an aggregation function. Features can be defined locally and then registered to Unity Catalog. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    Feature, DeltaTableSource, AggregationFunction, 
    Sum, Avg, TumblingWindow, SlidingWindow
)
from datetime import timedelta

avg_feature = Feature(
    source=DeltaTableSource(
        catalog_name="main",
        schema_name="feature_store",
        table_name="transactions",
    ),
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"), 
        TumblingWindow(window_duration=timedelta(days=30))
    ),
    name="avg_transaction_30d",
)
```

#### Data Sources

Features can be defined from multiple data source types:

- **[DeltaTableSource](/concepts/deltatablesource.md)**: Specifies a Delta table as the data source, identified by catalog, schema, and table name. ^[declarative-features-databricks-on-aws.md]
- **[RequestSource](/concepts/requestsource.md)**: Supports only scalar data types (`INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, `SHORT`). Complex types (arrays, maps, structs) are not supported. ^[declarative-features-databricks-on-aws.md]

#### Aggregation Functions

The API supports a limited list of user-defined aggregation functions (UDAFs), including `Sum`, `Avg`, `Count`, `Min`, `Max`, `Stddev`, and `Variance`. ^[declarative-features-databricks-on-aws.md]

#### Time Windows

- **TumblingWindow**: Non-overlapping windows aligned to fixed time boundaries. ^[declarative-features-databricks-on-aws.md]
- **SlidingWindow**: Overlapping windows that slide forward at regular intervals. ^[declarative-features-databricks-on-aws.md]
- **RollingWindow**: Continuous windows that update with each new data point. ^[declarative-features-databricks-on-aws.md]

### Feature Registration

#### Using `register_feature`

Features defined locally can be registered to Unity Catalog: ^[declarative-features-databricks-on-aws.md]

```python
fe = FeatureEngineeringClient()
avg_feature = fe.register_feature(
    feature=avg_feature,
    catalog_name="main",
    schema_name="feature_store",
)
```

#### Using `create_feature`

For a one-step define-and-register workflow: ^[declarative-features-databricks-on-aws.md]

```python
latest_amount = fe.create_feature(
    source=DeltaTableSource(
        catalog_name="main",
        schema_name="feature_store",
        table_name="transactions",
    ),
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    catalog_name="main",
    schema_name="feature_store",
    name="latest_amount",
)
```

### Training Set Creation

Use `create_training_set` to prepare point-in-time aggregated training data: ^[declarative-features-databricks-on-aws.md]

```python
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
training_set.load_df().display()
```

### Feature Materialization

Features can be materialized to offline or online stores for efficient reuse: ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    OfflineStoreConfig, OnlineStoreConfig,
    CronSchedule, MaterializedFeaturePipelineScheduleState
)

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

### Best Practices

#### Feature Naming

- Use descriptive names for business-critical features. ^[declarative-features-databricks-on-aws.md]
- Follow consistent naming conventions across teams. ^[declarative-features-databricks-on-aws.md]
- Use auto-generated names as you begin developing features. ^[declarative-features-databricks-on-aws.md]

#### Time Windows

- Align window boundaries with business cycles (daily, weekly). ^[declarative-features-databricks-on-aws.md]
- Shorter windows capture recent trends but can be noisy; longer windows produce more stable distributions but might miss recent shifts. ^[declarative-features-databricks-on-aws.md]
- Tumbling and sliding windows are more scalable than rolling windows. Start with sliding windows for most use cases. ^[declarative-features-databricks-on-aws.md]

#### Performance

- Materialize features from the same data source in a single `materialize_features` call to minimize data scans. ^[declarative-features-databricks-on-aws.md]
- Use the same granularity (e.g., all 1-hour or all 1-day slide durations) for features on the same data source to enable better grouping during materialization. ^[declarative-features-databricks-on-aws.md]

#### Entity Columns vs. Filter Conditions

- Use `entity` when you need different aggregation levels (e.g., customer-level vs. customer-merchant features). ^[declarative-features-databricks-on-aws.md]
- Use `filter_condition` on `DeltaTableSource` when you need to filter rows at the same aggregation level (e.g., only high-value transactions). ^[declarative-features-databricks-on-aws.md]
- Rule of thumb: if your change would result in a different number of rows per entity value, use different `entity` values; if you're just filtering which rows contribute to the same aggregation, use `filter_condition`. ^[declarative-features-databricks-on-aws.md]

### Limitations

- Names of entity and timeseries columns must match between the training dataset and the feature definitions when using `create_training_set`. ^[declarative-features-databricks-on-aws.md]
- The column name used as the `label` column in the training dataset should not exist in the source tables used for defining features. ^[declarative-features-databricks-on-aws.md]
- Entity columns cannot be of type `DATE` or `TIMESTAMP`. ^[declarative-features-databricks-on-aws.md]
- `RequestSource` does not support aggregation functions or time windows—only `ColumnSelection` functions can be used. ^[declarative-features-databricks-on-aws.md]
- The set of entity column names, timeseries column names, and request feature column names must be globally unique across all sources in a training set or serving endpoint. ^[declarative-features-databricks-on-aws.md]

### Related Concepts

- [Databricks Feature Store](/concepts/databricks-feature-store.md) — Centralized repository for managing ML features
- [Unity Catalog](/concepts/unity-catalog.md) — Governance and cataloging for data and AI assets
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Broader discipline of feature creation and selection
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) — Ensuring features use only data available at prediction time
- [Model Serving](/concepts/model-serving.md) — Deploying models with online feature lookups

### Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
