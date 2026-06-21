---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ed3bace9b760228f3d46be51b2f861e62950fe7c21fbe493f43e0e193b47694
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-definition-and-registration-workflow
    - Registration Workflow and Feature Definition
    - FDARW
    - feature-definition-and-registration-lifecycle
    - Registration Lifecycle and Feature Definition
    - FDARL
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Definition and Registration Workflow
description: Workflow for creating Feature objects locally or directly in Unity Catalog using create_feature and register_feature, which can then be used in training and serving.
tags:
  - feature-engineering
  - workflow
  - unity-catalog
timestamp: "2026-06-18T11:45:40.055Z"
---

# Feature Definition and Registration Workflow

The **Feature Definition and Registration Workflow** describes how to declare, compute, and persist features in [Unity Catalog](/concepts/unity-catalog.md) using the Declarative Feature Engineering APIs. This workflow covers two complementary paths: defining features directly in Unity Catalog with `create_feature`, or constructing them locally as `Feature` objects and registering them later with `register_feature`. ^[declarative-features-databricks-on-aws.md]

## Requirements

- A classic compute cluster running Databricks Runtime 17.0 ML or above.
- Install the custom Python package each session:

```python
%pip install databricks-feature-engineering>=0.15.0
dbutils.library.restartPython()
```

^[declarative-features-databricks-on-aws.md]

## Feature Development Paths

### One-Step Definition and Registration

Use `create_feature` to define a feature and immediately persist it to Unity Catalog. This is the simplest path when you know the target [Catalog and Schema](/concepts/catalog-and-schema.md) ahead of time.

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.feature_engineering.entities import (
    DeltaTableSource, ColumnSelection, AggregationFunction, Sum, TumblingWindow
)

fe = FeatureEngineeringClient()

latest_amount = fe.create_feature(
    source=DeltaTableSource(
        catalog_name="main", schema_name="feature_store", table_name="transactions"
    ),
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    catalog_name="main",
    schema_name="feature_store",
    name="latest_amount",
)
```

^[declarative-features-databricks-on-aws.md]

### Local Construction with Delayed Registration

Construct `Feature` objects locally without providing a Unity Catalog path. You can then use them immediately with `create_training_set` for model training, and later persist them via `register_feature`.

```python
from databricks.feature_engineering.entities import Feature, AggregationFunction, Avg, TumblingWindow

source = DeltaTableSource(
    catalog_name="main", schema_name="feature_store", table_name="transactions"
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

# Use locally before registration
training_set = fe.create_training_set(df=labeled_df, features=[avg_feature], label="target")

# Register later
avg_feature = fe.register_feature(feature=avg_feature, catalog_name="main", schema_name="feature_store")
```

^[declarative-features-databricks-on-aws.md]

## Workflow Stages

### 1. Feature Definition

With either path, you define the feature by specifying:

- **Source**: a `DeltaTableSource` (or `RequestSource` for request-time data) that describes the backing table.
- **Function**: the computation to apply — `AggregationFunction` (with time-windowed aggregations like `Sum`, `Avg`, `Count`) or `ColumnSelection`.
- **Entity columns**: the key(s) used for joins (e.g., `["user_id"]`).
- **Timeseries column**: the timestamp column for point-in-time correctness.
- **Filter condition** (optional): applied to the source table to restrict rows used in the aggregation.

^[declarative-features-databricks-on-aws.md]

### 2. Local Exploration (Optional)

Before registering, you can explore computed values with `compute_features`:

```python
feature_df = fe.compute_features(features=[avg_feature, sum_feature])
feature_df.display()
```

^[declarative-features-databricks-on-aws.md]

### 3. Registration

Registration persists the feature definition to Unity Catalog, creating a feature object that can be discovered and reused across teams.

- `create_feature` – defines and registers in one call.
- `register_feature` – persists a locally constructed `Feature` to a target [Catalog and Schema](/concepts/catalog-and-schema.md).

After registration, the feature can be referenced in training sets and serving pipelines.

^[declarative-features-databricks-on-aws.md]

### 4. Model Training

Use `create_training_set` to combine labeled data with the feature definitions and produce a point-in-time correct training DataFrame. The training set can be logged with a model via `fe.log_model()`.

```python
with mlflow.start_run():
    training_df = training_set.load_df()
    # train model
    fe.log_model(
        model=model,
        artifact_path="model",
        flavor=mlflow.sklearn,
        training_set=training_set,
        registered_model_name="main.feature_store.recommendation_model",
    )
```

^[declarative-features-databricks-on-aws.md]

### 5. Materialization (Optional)

After registration, features can be materialized to offline or online stores for efficient serving. Materialization uses `materialize_features` with a trigger (cron schedule for aggregation features, table trigger for column selection features) and store configuration.

```python
fe.materialize_features(
    features=[avg_feature, sum_feature],
    offline_config=OfflineStoreConfig(
        catalog_name="main", schema_name="feature_store", table_name_prefix="customer_features"
    ),
    online_config=OnlineStoreConfig(
        catalog_name="main", schema_name="feature_store",
        table_name_prefix="customer_features_serving",
        online_store_name="customer_features_store",
    ),
    trigger=CronSchedule(quartz_cron_expression="0 0 * * * ?", timezone_id="UTC"),
)
```

^[declarative-features-databricks-on-aws.md]

## Best Practices

- **Naming**: Use descriptive, consistent names across teams. Auto-generated names (based on function parameters) are acceptable during early development. ^[declarative-features-databricks-on-aws.md]
- **Time windows**: Align window boundaries with business cycles. Choose window durations based on signal volatility — shorter windows react quickly but may be noisy; longer windows stabilize distributions. ^[declarative-features-databricks-on-aws.md]
- **Performance**: Materialize features from the same source in a single call to minimize data scans. Use consistent granularity (e.g., all 1-hour windows) for features on the same source to enable better grouping. ^[declarative-features-databricks-on-aws.md]
- **Entity vs. filter**: Use different `entity` values when aggregation levels differ (e.g., customer-level vs. customer-merchant-level). Use `filter_condition` on the source when filtering rows that contribute to the same aggregation level. ^[declarative-features-databricks-on-aws.md]

## Limitations

- Entity and timeseries column names must match between the training dataset and feature definitions.
- The label column in the training dataset must not exist in any source table used for feature definitions.
- Only a limited set of UDAFs is supported (see [Declarative features API reference](/concepts/declarative-feature-engineering-api.md)).
- Entity columns cannot be of type `DATE` or `TIMESTAMP`.
- `RequestSource` supports only scalar data types and cannot use aggregation functions or time windows. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The Python API client used for all declarative operations.
- materialize_features() API|Materialized Features – The process of persisting computed features for serving.
- [Training Set Creation](/concepts/training-set-feature-store.md) – Point-in-time feature computation for model training.
- MLflow Model Logging – How to log a model together with its feature dependencies.
- [DeltaTableSource](/concepts/deltatablesource.md) – The primary data source type for declarative features.
- [Online Store](/concepts/online-feature-store.md) – A low-latency store for serving features in production.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
