---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21a058eec10d7319092cc0ef0c26d0b7b6f4eb1a512396545216eaecfa7eeb06
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-registration-workflows
    - FRW
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Feature Registration Workflows
description: "Two approaches for registering features in Unity Catalog: a two-step workflow (construct Feature locally, then register_feature) for experimentation, or single-step create_feature for immediate registration"
tags:
  - feature-engineering
  - workflow
  - databricks
  - unity-catalog
timestamp: "2026-06-18T11:45:20.567Z"
---

# Feature Registration Workflows

A **Feature Registration Workflow** is the process of persisting a declared feature definition—a `Feature` object constructed from a data source, function, and optional entity/ timeseries columns—into [Unity Catalog](/concepts/unity-catalog.md) so it can be reused in training pipelines and inference. The declarative API provides two registration paths: a two-step workflow that separates local construction from registration, and a single-step workflow that combines both actions. ^[declarative-features-api-reference-databricks-on-aws.md]

## Two-Step Workflow: `Feature` + `register_feature()`

The recommended approach first builds a `Feature` object locally, then explicitly persists it with `FeatureEngineeringClient.register_feature()`. This separation lets you experiment with the feature—including calling `create_training_set`—before committing it to the catalog. ^[declarative-features-api-reference-databricks-on-aws.md]

### Step 1: Construct a `Feature` object

```python
from databricks.feature_engineering.entities import (
    Feature, DeltaTableSource, AggregationFunction, Sum, RollingWindow
)
from datetime import timedelta

feature = Feature(
    source=DeltaTableSource(
        catalog_name="main", schema_name="store", table_name="transactions"
    ),
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=7))),
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

The `Feature` constructor requires a `source` ([DeltaTableSource](/concepts/deltatablesource.md) or [RequestSource](/concepts/requestsource.md)), a `function` ([AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) or [ColumnSelection](/concepts/automl-column-selection.md)), and—when using aggregation—the `entity` and `timeseries_column` parameters. The `name` and `description` are optional; if omitted, a name is auto-generated. ^[declarative-features-api-reference-databricks-on-aws.md]

### Step 2: Register in Unity Catalog

```python
fe = FeatureEngineeringClient()
registered_feature = fe.register_feature(
    feature=feature,
    catalog_name="main",
    schema_name="store",
)
```

`register_feature()` accepts a `Feature` instance (which must not already be registered) along with the target [Catalog and Schema](/concepts/catalog-and-schema.md) names, and returns the registered `Feature` object. ^[declarative-features-api-reference-databricks-on-aws.md]

## Single-Step Workflow: `create_feature()`

Use `FeatureEngineeringClient.create_feature()` when you want to validate, construct, and register the feature in a single call—bypassing the need for a local `Feature` object. This is convenient for production pipelines where the feature definition is already known. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
created_feature = fe.create_feature(
    source=DeltaTableSource(
        catalog_name="main", schema_name="store", table_name="transactions"
    ),
    function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=7))),
    catalog_name="main",
    schema_name="store",
    entity=["user_id"],
    timeseries_column="transaction_time",
)
```

`create_feature()` accepts the same parameters as the `Feature` constructor (source, function, entity, timeseries_column, name, description) plus the required [Catalog and Schema](/concepts/catalog-and-schema.md) names. It returns a valid `Feature` instance. ^[declarative-features-api-reference-databricks-on-aws.md]

> **Validation**: Both methods raise `ValueError` if any validation fails, such as missing required parameters for aggregation features. ^[declarative-features-api-reference-databricks-on-aws.md]

## Auto-Generated Names

When you omit the `name` parameter in either workflow, the system generates a name following the pattern `{column}_{function}_{window}`. For example:
- `price_avg_rolling_1h` (1-hour rolling average of the `price` column)
- `transaction_count_rolling_30d_1d` (30-day count with a 1-day delay)

Generated names are derived from the input column name, function operator, and window duration. ^[declarative-features-api-reference-databricks-on-aws.md]

## Deleting a Registered Feature

Use `FeatureEngineeringClient.delete_feature()` to remove a feature from the catalog by its fully qualified name (`catalog.schema.feature_name`).

```python
fe.delete_feature(full_name="main.store.amount_sum_rolling_7d")
```

Before deletion, you must remove or update any models or feature specs that reference the feature. If the feature has been materialized, delete the materialized feature first (see materialize_features() API|Materialized Features). ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — The parent API providing these registration methods
- Feature — The core entity object representing a feature definition
- [DeltaTableSource](/concepts/deltatablesource.md) — Source type for table-backed features
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — Wraps an aggregation operator and time window
- [ColumnSelection](/concepts/automl-column-selection.md) — Pass-through feature without aggregation
- [Time Windows](/concepts/time-windows.md) — Rolling, tumbling, and sliding window definitions
- [Training Set Creation](/concepts/training-set-feature-store.md) — Using registered features in `create_training_set`

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
