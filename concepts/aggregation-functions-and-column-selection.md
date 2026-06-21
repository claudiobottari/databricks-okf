---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a197b670e6b7b3e26b01c0843bd1d3c49f5be68ba93fcc1730033180943813c3
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aggregation-functions-and-column-selection
    - Column Selection and Aggregation Functions
    - AFACS
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Aggregation Functions and Column Selection
description: Features can be computed via aggregation functions (Sum, Avg, Count, ApproxCountDistinct, etc.) wrapped in AggregationFunction with a time window, or pass-through via ColumnSelection for direct value lookup.
tags:
  - feature-engineering
  - aggregation
  - api
timestamp: "2026-06-19T18:17:37.432Z"
---

# Aggregation Functions and Column Selection

**Aggregation Functions and Column Selection** are the two fundamental types of feature functions used in Databricks' Declarative Feature Engineering API. They define how raw data from a source table is transformed into features for machine learning models.

## Overview

When defining features using the `Feature` constructor or `create_feature()` method, the `function` parameter accepts either an `AggregationFunction` or a `ColumnSelection`. These represent two distinct approaches to feature computation: aggregating data over time windows, or passing through raw column values directly. ^[declarative-features-api-reference-databricks-on-aws.md]

## Aggregation Functions

Aggregation functions compute summary statistics over groups of rows within a specified time window. They are wrapped in an `AggregationFunction` together with a [time window](/concepts/time-windows.md) definition. Each aggregation function takes an `input` parameter specifying the source column to aggregate. ^[declarative-features-api-reference-databricks-on-aws.md]

### Supported Aggregation Operators

The API supports the following aggregation operators:

- **Sum** — Computes the sum of values in the input column over the window
- **Avg** — Computes the average of values in the input column over the window
- **Count** — Counts the number of rows in the input column over the window
- **ApproxCountDistinct** — Computes an approximate count of distinct values, with a configurable `relativeSD` parameter for precision control

Each operator is used inside an `AggregationFunction` along with a time window type such as `RollingWindow`, `TumblingWindow`, or `SlidingWindow`. ^[declarative-features-api-reference-databricks-on-aws.md]

### Example: Aggregation Features

```python
from databricks.feature_engineering.entities import (
    AggregationFunction, Feature, Sum, Avg, ApproxCountDistinct,
    RollingWindow,
)
from datetime import timedelta

window = RollingWindow(window_duration=timedelta(days=7))

sum_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="event_time",
    function=AggregationFunction(Sum(input="amount"), window),
)

avg_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="event_time",
    function=AggregationFunction(Avg(input="amount"), window),
)

distinct_count = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="event_time",
    function=AggregationFunction(
        ApproxCountDistinct(input="product_id", relativeSD=0.01), window
    ),
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

### Requirements for Aggregation Features

Aggregation features require two additional parameters on the `Feature` definition:

- **`entity`**: A list of column names that define the aggregation level (equivalent to `GROUP BY` in SQL). For example, `["user_id"]` aggregates per user.
- **`timeseries_column`**: The timestamp column used for time window aggregation. This column must be of type `TimestampType` or `DateType`.

These parameters are required for aggregation features but not for `ColumnSelection`. ^[declarative-features-api-reference-databricks-on-aws.md]

## Column Selection (Pass-Through)

`ColumnSelection` selects a single column from a source without applying any aggregation. It is wrapped directly in the `function` parameter (not inside `AggregationFunction`). The return type is inferred from the source schema. ^[declarative-features-api-reference-databricks-on-aws.md]

### Behavior by Source Type

`ColumnSelection` behaves differently depending on the data source:

- **`DeltaTableSource`**: Returns the latest value per entity key via a point-in-time join. No lookback window aggregation is applied.
- **`RequestSource`**: Passes through the value provided at inference time (or extracted from the labeled DataFrame at training time).

^[declarative-features-api-reference-databricks-on-aws.md]

### Example: Column Selection Features

```python
from databricks.feature_engineering.entities import (
    ColumnSelection, DeltaTableSource, Feature, FieldDefinition,
    RequestSource, ScalarDataType,
)

delta_source = DeltaTableSource(
    catalog_name="main", schema_name="feature_store", table_name="transactions",
)

request_source = RequestSource(
    schema=[
        FieldDefinition(name="session_duration", data_type=ScalarDataType.DOUBLE),
    ]
)

# ColumnSelection from a Delta table
latest_amount = Feature(
    source=delta_source,
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    name="latest_transaction_amount",
)

# ColumnSelection from a RequestSource
session_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),
    name="session_duration",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Key Differences

| Aspect | AggregationFunction | ColumnSelection |
|--------|-------------------|-----------------|
| Purpose | Computes summary statistics over time windows | Passes through raw column values |
| Time window | Required (Rolling, Tumbling, or Sliding) | Not applicable |
| Entity columns | Required | Optional (for DeltaTableSource) |
| Timeseries column | Required | Optional (for DeltaTableSource) |
| Use with RequestSource | Not supported | Supported |
| Materialization trigger | CronSchedule | TableTrigger |

^[declarative-features-api-reference-databricks-on-aws.md]

## Auto-Generated Names

When the `name` parameter is omitted, a name is automatically generated. For aggregation features, generated names follow the pattern `{column}_{function}_{window}`. For example, `price_avg_rolling_1h` or `transaction_count_rolling_30d_1d`. For `ColumnSelection`, the name defaults to the column name. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — The overall API for defining and registering features
- [Time Windows](/concepts/time-windows.md) — Rolling, tumbling, and sliding window types for aggregation
- [DeltaTableSource](/concepts/deltatablesource.md) — Data source for features backed by Delta tables
- [RequestSource](/concepts/requestsource.md) — Data source for features provided at inference time
- Feature Constructor — The `Feature` class and its parameters
- [Materialization Triggers](/concepts/materialization-triggers.md) — Controls for when feature pipelines run

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
