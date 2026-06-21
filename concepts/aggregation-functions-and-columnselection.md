---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 100631e9e726de2ed3a3c3285e3b583ae56b7dcf6f9aa27ef062b910561a2a6b
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aggregation-functions-and-columnselection
    - ColumnSelection and Aggregation Functions
    - AFAC
    - aggregation-functions-and-column-selection
    - Column Selection and Aggregation Functions
    - AFACS
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Aggregation Functions and ColumnSelection
description: "Two function types for feature computation: AggregationFunction (wrapping operators like Sum, Avg, Count with time windows) for time-series aggregations, and ColumnSelection for pass-through features without aggregation."
tags:
  - feature-engineering
  - aggregation
  - python-api
timestamp: "2026-06-19T09:56:50.821Z"
---

# Aggregation Functions and ColumnSelection

**Aggregation Functions** and **ColumnSelection** are the two primary function types used in the [Databricks Feature Store](/concepts/databricks-feature-store.md) declarative feature engineering API to define how features are computed from source data. They determine whether a feature performs time-windowed aggregation over historical data or simply passes through a raw value.

## Overview

The `Feature` constructor and `create_feature()` method accept a `function` parameter that must be either an `AggregationFunction` or a `ColumnSelection`. This choice defines the fundamental behavior of the feature. ^[declarative-features-api-reference-databricks-on-aws.md]

## Aggregation Functions

**Aggregation functions** compute features by applying a mathematical operation (such as sum, average, or count) over a specified time window. They are always wrapped in an `AggregationFunction` object together with a TimeWindow definition that controls the lookback period.

### Structure

An aggregation function bundles three components:
- The **operator** (e.g., `Sum`, `Avg`, `Count`, `ApproxCountDistinct`) that specifies the aggregation to perform
- The **input column** (named via the `input` parameter) that identifies which source column to aggregate
- A **time window** (RollingWindow, TumblingWindow, or SlidingWindow) that defines the lookback behavior

```python
# Example: 7-day rolling sum of transaction amounts
AggregationFunction(
    Sum(input="amount"),              # Operator and input column
    RollingWindow(window_duration=timedelta(days=7))  # Time window
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

### Supported Operators

The API supports the following aggregation operators:

| Operator | Description |
|----------|-------------|
| `Sum` | Sum of values over the window |
| `Avg` | Average of values over the window |
| `Count` | Count of occurrences |
| `ApproxCountDistinct` | Approximate distinct count (with configurable `relativeSD`) |
| `Min` | Minimum value |
| `Max` | Maximum value |
| `Stddev` | Standard deviation |
| `Variance` | Variance |
| `First` | First value in the window |
| `Last` | Last value in the window |

^[declarative-features-api-reference-databricks-on-aws.md]

### Requirements

Aggregation functions require additional parameters on the `Feature` definition:
- `entity`: List of column names that define the aggregation level (similar to `GROUP BY` in SQL). Required for all aggregation features.
- `timeseries_column`: The timestamp column used for time window computation. Must be of type `TimestampType` or `DateType`.

^[declarative-features-api-reference-databricks-on-aws.md]

## ColumnSelection (Pass-Through)

**`ColumnSelection`** selects a single column from the source without applying any aggregation. It is a pass-through operation that returns the raw value from the source table. ^[declarative-features-api-reference-databricks-on-aws.md]

### Behavior by Source Type

The behavior of `ColumnSelection` depends on the underlying DataSource:

- **`DeltaTableSource`**: Returns the latest value per entity key via a point-in-time join, using the most recent record for each entity without applying a lookback window.
- **`RequestSource`**: Passes through the value provided directly at inference time (or extracted from the labeled DataFrame at training time). No lookup is performed against a materialized table.

^[declarative-features-api-reference-databricks-on-aws.md]

### Syntax

`ColumnSelection` is passed directly to the `function` parameter — not wrapped inside an `AggregationFunction`:

```python
from databricks.feature_engineering.entities import ColumnSelection

# Pass-through from a Delta table (latest value per entity)
latest_amount = Feature(
    source=delta_source,
    function=ColumnSelection("amount"),  # No AggregationFunction wrapper
    entity=["user_id"],
    timeseries_column="transaction_time",
    name="latest_transaction_amount",
)

# Pass-through from a request payload
session_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),  # Direct pass-through
    name="session_duration",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

### No Entity or Time-Series Columns

`ColumnSelection` features do not require `entity` or `timeseries_column` parameters when backed by a `RequestSource`. They are required when backed by a `DeltaTableSource` because the system needs to know the entity key for the point-in-time join. ^[declarative-features-api-reference-databricks-on-aws.md]

## When to Use Each

- **Use `AggregationFunction`** when the feature should aggregate historical data over a time window — for example, "total spending in the last 7 days" or "average transaction amount over 30 days."
- **Use `ColumnSelection`** when the feature should return a raw value from the source — for example, the latest transaction amount, a user's session duration, or a flag provided at inference time.

Both types can be combined in a single model. The same [DeltaTableSource](/concepts/deltatablesource.md) can be shared across features with different entity configurations, and aggregation and column selection features can coexist in the same training set. ^[declarative-features-api-reference-databricks-on-aws.md]

## Materialization Considerations

Because aggregation and column selection features require different [Materialization Triggers](/concepts/materialization-triggers.md) (CronSchedule for aggregation features and TableTrigger for column selection features), they cannot be mixed in a single `materialize_features` call. To materialize features of both types, issue separate calls for each group. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — The wrapper that binds operators to time windows
- TimeWindow — Rolling, tumbling, and sliding lookback configurations
- [DeltaTableSource](/concepts/deltatablesource.md) — Primary data source for feature computation
- [RequestSource](/concepts/requestsource.md) — Data source for inference-time features
- [Feature Constructor and registration](/concepts/feature-construction-and-registration-workflows.md) — The `Feature()` API and `register_feature()`

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
