---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f7a22020c1e939af9ddfb6146930761ad969115fcdd2413f1448dfc6bc2c023f
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aggregationfunction-and-columnselection
    - ColumnSelection and AggregationFunction
    - AAC
    - AggregationFunction
    - aggregation functions
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: AggregationFunction and ColumnSelection
description: "Two types of function wrappers for feature computation: AggregationFunction for window-based aggregation (Sum, Avg, Count, ApproxCountDistinct) and ColumnSelection for pass-through features"
tags:
  - feature-engineering
  - aggregation
  - api
  - databricks
timestamp: "2026-06-18T11:44:56.960Z"
---

---
title: AggregationFunction and ColumnSelection
summary: Two core function types in Declarative Feature Engineering that define how features are computed from data sources: AggregationFunction for time-windowed aggregations and ColumnSelection for pass-through column values.
sources:
  - declarative-features-api-reference-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T09:00:00.000Z"
updatedAt: "2026-06-18T09:00:00.000Z"
tags:
  - feature-engineering
  - api-reference
  - databricks
aliases:
  - aggregation-function-and-column-selection
  - AFACS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AggregationFunction and ColumnSelection

**AggregationFunction** and **ColumnSelection** are the two types of functions used in the Feature constructor of Databricks Declarative Feature Engineering to define how a feature is computed from a DataSource. `AggregationFunction` bundles an aggregation operator (e.g., `Sum`, `Avg`) together with a time window to produce rolling, tumbling, or sliding aggregations. `ColumnSelection` simply selects a single column from the source without applying any aggregation, acting as a pass-through. ^[declarative-features-api-reference-databricks-on-aws.md]

Both types are passed to the `function` parameter of `Feature(..., function=...)` or `FeatureEngineeringClient.create_feature(function=...)`. ^[declarative-features-api-reference-databricks-on-aws.md]

## AggregationFunction

`AggregationFunction` is used for features that require time-windowed aggregation over historical data. It is constructed with an operator and a time window object. The available operators include `Sum`, `Avg`, `Count`, `ApproxCountDistinct`, and others. Each operator takes an `input` parameter naming the source column to aggregate. ^[declarative-features-api-reference-databricks-on-aws.md]

The time window types are `RollingWindow`, `TumblingWindow`, and `SlidingWindow`, defined in the `datetime.timedelta` module. For example, a 7‑day rolling sum is created with:

```python
from databricks.feature_engineering.entities import AggregationFunction, Sum, RollingWindow
from datetime import timedelta

feature = Feature(
    source=delta_source,
    entity=["user_id"],
    timeseries_column="event_time",
    function=AggregationFunction(Sum(input="amount"), RollingWindow(window_duration=timedelta(days=7)))
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

When an aggregation feature is created, the `entity` and `timeseries_column` parameters are required on the `Feature` definition. Entities define the grouping key (like `GROUP BY`), and the timeseries column provides the timestamp for window boundaries. ^[declarative-features-api-reference-databricks-on-aws.md]

## ColumnSelection

`ColumnSelection` selects a single column from a data source without any aggregation. It is used for pass-through features, where the latest value is taken (for [DeltaTableSource](/concepts/deltatablesource.md)) or the request payload value is passed through (for [RequestSource](/concepts/requestsource.md)). It does not require a time window. ^[declarative-features-api-reference-databricks-on-aws.md]

Example from a Delta table:

```python
from databricks.feature_engineering.entities import ColumnSelection, Feature, DeltaTableSource

latest_amount = Feature(
    source=DeltaTableSource(catalog_name="main", schema_name="store", table_name="transactions"),
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    name="latest_transaction_amount",
)
```

Example from a RequestSource (pass-through at inference time):

```python
from databricks.feature_engineering.entities import ColumnSelection, RequestSource, Feature, FieldDefinition, ScalarDataType

request_source = RequestSource(
    schema=[FieldDefinition(name="session_duration", data_type=ScalarDataType.DOUBLE)]
)

session_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),
    name="session_duration",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Key Differences

| Aspect | AggregationFunction | ColumnSelection |
|--------|---------------------|-----------------|
| Purpose | Time‑windowed aggregations (sum, count, avg, etc.) | Direct column selection (pass‑through) |
| Time window | Required (via `RollingWindow`, `TumblingWindow`, `SlidingWindow`) | Not used |
| Entity & timeseries_column | Required | Required only when used with a Delta table (to define latest value per entity) |
| Use with RequestSource | Not supported | Supported |
| Typical output | Aggregated value over a lookback period | Single column value from source or request |

^[declarative-features-api-reference-databricks-on-aws.md]

## Auto‑Generated Names

When the feature `name` is omitted, an auto‑generated name is produced. For `AggregationFunction` features, the pattern is `{column}_{function}_{window}`, e.g., `price_avg_rolling_1h`. For `ColumnSelection`, the column name is used directly unless overridden. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- Feature — The main entity that uses these functions
- [DeltaTableSource](/concepts/deltatablesource.md) — Source for table‑backed features
- [RequestSource](/concepts/requestsource.md) — Source for inference‑time pass‑through features
- RollingWindow, TumblingWindow, SlidingWindow — Time window types for aggregation
- [Materialization Triggers](/concepts/materialization-triggers.md) — How materialization pipelines are scheduled for each function type
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The broader API framework

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
