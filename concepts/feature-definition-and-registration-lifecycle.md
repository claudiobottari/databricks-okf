---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 92905d41f8cc76714488903c4b98c7305af11bbbcbaa8982973ee94dd930a57f
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-definition-and-registration-lifecycle
    - Registration Lifecycle and Feature Definition
    - FDARL
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Feature Definition and Registration Lifecycle
description: Workflow for defining Feature objects locally or via create_feature, then persisting them to Unity Catalog using register_feature for reuse in training, serving, and model governance.
tags:
  - feature-engineering
  - unity-catalog
  - mlops
timestamp: "2026-06-18T15:13:24.669Z"
---

# Feature Definition and Registration Lifecycle

The **Feature Definition and Registration Lifecycle** describes the end-to-end process of creating, registering, and managing features in [Unity Catalog](/concepts/unity-catalog.md) using the Declarative Feature Engineering APIs. This lifecycle spans from initial feature development to production deployment and materialization.

## Overview

The Declarative Feature Engineering APIs support two main workflows for defining and registering features. Developers can either define and register features in a single step using `create_feature`, or construct Feature objects locally and persist them later using `register_feature`. Both approaches enable features to be used in model training and serving workflows. ^[declarative-features-databricks-on-aws.md]

## Feature Development Workflow

### One-Step Creation with `create_feature`

The `create_feature` function defines a feature and immediately registers it in Unity Catalog. This approach requires specifying the catalog name, schema name, source data, entity columns, timeseries column, and computation function. ^[declarative-features-databricks-on-aws.md]

```python
feature = fe.create_feature(
    source=source,
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    catalog_name=CATALOG_NAME,
    schema_name=SCHEMA_NAME,
    name="latest_amount",
)
```

### Two-Step Workflow with Local Construction and Registration

Developers can first construct local Feature objects without specifying a catalog or schema, then use `register_feature` to persist them to Unity Catalog later. Locally constructed features can be used with `create_training_set` before registration. ^[declarative-features-databricks-on-aws.md]

```python
# 1. Define features locally
avg_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Avg(input="amount"), TumblingWindow(window_duration=timedelta(days=30))),
    name="avg_transaction_30d",
)

# 2. Register features in Unity Catalog
avg_feature = fe.register_feature(
    feature=avg_feature,
    catalog_name=CATALOG_NAME,
    schema_name=SCHEMA_NAME,
)
```

## Feature Component Hierarchy

Features are composed of several components:

- **Source**: A [DeltaTableSource](/concepts/deltatablesource.md) or [RequestSource](/concepts/requestsource.md) that provides the raw data
- **Entity**: Column names that define the grouping level for aggregations (e.g., `user_id`, `merchant_id`)
- **Timeseries column**: A timestamp column used for point-in-time computations
- **Function**: The computation logic, which can be:
  - [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) with time windows (tumbling, sliding, or rolling)
  - [ColumnSelection](/concepts/automl-column-selection.md) for simple column passthrough

^[declarative-features-databricks-on-aws.md]

## Training Workflow

After defining features, developers can use `create_training_set` to calculate point-in-time aggregated features for machine learning. The training set combines labeled data with feature definitions and supports the [log_model](/concepts/loggedmodel.md) function for model tracking. ^[declarative-features-databricks-on-aws.md]

```python
training_set = fe.create_training_set(
    df=labeled_df,
    features=[avg_feature, sum_feature],
    label="target",
)
```

## Materialization and Serving Workflow

After registration, features can be materialized for efficient reuse in training and serving workflows. The `materialize_features` function supports:

- **Offline stores**: For batch training datasets
- **Online stores**: For real-time model serving
- **Triggers**: CronSchedule for time-based materialization or TableTrigger for change-based materialization

^[declarative-features-databricks-on-aws.md]

```python
fe.materialize_features(
    features=[avg_feature, sum_feature],
    offline_config=OfflineStoreConfig(
        catalog_name=CATALOG_NAME,
        schema_name=SCHEMA_NAME,
        table_name_prefix="customer_features",
    ),
    online_config=online_config,
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)
```

## Feature Lifecycle Stages

1. **Definition**: Features are defined using source data, entity columns, timeseries columns, and computation functions
2. **Registration**: Features are persisted as Unity Catalog objects using `create_feature` or `register_feature`
3. **Exploration**: Features can be previewed using `compute_features` to inspect computed values
4. **Training**: Features are used in `create_training_set` for model training
5. **Materialization**: Features are materialized to offline or online stores for production use
6. **Serving**: Materialized features are used for batch inference or real-time model serving

## Requirements

- A classic compute cluster running **Databricks Runtime 17.0 ML** or above
- Installation of `databricks-feature-engineering>=0.15.0`

^[declarative-features-databricks-on-aws.md]

## Best Practices

### Feature Naming
- Use descriptive names for business-critical features
- Follow consistent naming conventions across teams
- Use auto-generated names during initial development

### Entity Columns vs. Filter Conditions
- Use different `entity` values when features need different aggregation levels (e.g., customer-level vs. customer-merchant-level)
- Use `filter_condition` on the source when filtering rows at the same aggregation level (e.g., high-value transactions only)

### Performance
- Materialize features from the same data source in a single `materialize_features` call to minimize data scans
- Use consistent granularity (e.g., all 1-hour windows) for features on the same data source

^[declarative-features-databricks-on-aws.md]

## Limitations

- Entity and timeseries column names must match between training datasets and feature definitions
- Label columns in training datasets should not exist in source tables
- Entity columns cannot be of type `DATE` or `TIMESTAMP`
- [RequestSource](/concepts/requestsource.md) supports only scalar data types and does not support aggregation functions or time windows
- Entity column names, timeseries column names, and request feature column names must be globally unique across all sources in a training set or serving endpoint

^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md)
- [Feature Store](/concepts/feature-store.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Training with Features](/concepts/training-set-feature-store.md)
- [Feature Materialization](/concepts/feature-materialization.md)
- [Online Store](/concepts/online-feature-store.md)
- [Offline Store](/concepts/offline-feature-store.md)

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
