---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d361abd9cbc1023bec82b0584d6b31a8895f3873cbb2bee9d56a5f23dc1d4ed
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-object-and-registration-workflow
    - Registration Workflow and Feature Object
    - FOARW
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Feature Object and Registration Workflow
description: Two-step workflow for defining features locally with the Feature class and persisting them to Unity Catalog via register_feature() or create_feature(), supporting experimentation before registration.
tags:
  - feature-engineering
  - python-api
  - databricks
timestamp: "2026-06-19T09:56:46.219Z"
---

# Feature Object and Registration Workflow

The **Feature Object and Registration Workflow** describes the two primary approaches for creating and persisting declarative feature definitions in Unity Catalog. The recommended method separates local experimentation from catalog registration, while a single-step alternative combines validation and registration into one call. ^[declarative-features-api-reference-databricks-on-aws.md]

## Two-Step Workflow (Recommended)

The two-step workflow starts by constructing a `Feature` object locally using the declarative [Feature Engineering API](/concepts/declarative-feature-engineering-api.md). You define the data source, aggregation or column selection function, entity keys, and optional time-series column. Once the feature is built and tested — for example, by creating a training set with `create_training_set()` — you persist it to Unity Catalog by calling `register_feature()` on a `FeatureEngineeringClient`. ^[declarative-features-api-reference-databricks-on-aws.md]

### Feature Constructor

The `Feature` constructor accepts these parameters: ^[declarative-features-api-reference-databricks-on-aws.md]

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | `DataSource` | Yes | Either [DeltaTableSource](/concepts/deltatablesource.md) (backed by a Delta table) or [RequestSource](/concepts/requestsource.md) (inference-time request data) |
| `function` | `AggregationFunction` or `ColumnSelection` | Yes | Time-windowed aggregation operation or a pass-through column selection |
| `entity` | `List[str]` | Conditionally | Columns that define the aggregation level (required for aggregation features) |
| `timeseries_column` | `str` | Conditionally | Timestamp column used for time-window aggregation (required for aggregation features) |
| `name` | `str` | No | Feature name; auto-generated if omitted |
| `description` | `str` | No | Feature description |

### Registering with `register_feature()`

`register_feature()` takes the locally constructed `Feature` instance and the target catalog/schema names, then persists the definition to Unity Catalog. The method expects a feature that has not already been registered. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    Feature, DeltaTableSource, AggregationFunction, Sum, RollingWindow
)
from datetime import timedelta

# Step 1: Build feature locally
feature = Feature(
    source=DeltaTableSource(
        catalog_name="main", schema_name="store", table_name="transactions"
    ),
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Sum(input="amount"), 
        RollingWindow(window_duration=timedelta(days=7))
    ),
)

# Step 2: Register in Unity Catalog
fe = FeatureEngineeringClient()
registered_feature = fe.register_feature(
    feature=feature,
    catalog_name="main",
    schema_name="store",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Single-Step Workflow with `create_feature()`

When you do not need to experiment locally before registration, `create_feature()` validates, constructs, and immediately registers a feature in a single call. It accepts the same parameters as the `Feature` constructor plus `catalog_name` and `schema_name`. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
fe = FeatureEngineeringClient()
feature = fe.create_feature(
    source=DeltaTableSource(
        catalog_name="main", schema_name="store", table_name="transactions"
    ),
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Sum(input="amount"), 
        RollingWindow(window_duration=timedelta(days=7))
    ),
    catalog_name="main",
    schema_name="store",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Auto-Generated Names

If the `name` parameter is omitted, a name is automatically generated following the pattern `{column}_{function}_{window}`. Examples: ^[declarative-features-api-reference-databricks-on-aws.md]

- `price_avg_rolling_1h` — 1-hour rolling average price
- `transaction_count_rolling_30d_1d` — 30-day transaction count with 1-day delay

## Deleting Features

Use `delete_feature()` to remove a feature from Unity Catalog by its fully qualified name (`<catalog>.<schema>.<feature_name>`). Before deletion, you must remove or update any models or [Feature Specs](/concepts/featurespec.md) that reference the feature. If the feature has been materialized, delete the materialized feature first. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
fe.delete_feature(full_name="main.store.amount_sum_rolling_7d")
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — Full API reference for feature definitions
- [DeltaTableSource](/concepts/deltatablesource.md) — Feature source from a Delta table
- [RequestSource](/concepts/requestsource.md) — Feature source for inference-time request data
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — Time-windowed aggregation operations (Sum, Avg, Count, etc.)
- [ColumnSelection](/concepts/automl-column-selection.md) — Pass-through of a single column without aggregation
- [Training Set Creation](/concepts/training-set-feature-store.md) — Using features to build training datasets with `create_training_set()`
- materialize_features() API|Materialized Features — Online serving materialization of features
- [Feature Specs](/concepts/featurespec.md) — Packaging features for model serving

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
