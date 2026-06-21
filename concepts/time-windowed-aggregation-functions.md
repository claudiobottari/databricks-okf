---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0246d500d7fe6e8844ba8fbba256986438a536e9478565587cf99e45a4fa39cf
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-windowed-aggregation-functions
    - TAF
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Time-Windowed Aggregation Functions
description: Feature computation patterns using TumblingWindow, SlidingWindow, and RollingWindow for point-in-time aggregations over time-series data.
tags:
  - feature-engineering
  - time-series
  - aggregation
timestamp: "2026-06-19T14:57:47.977Z"
---

```markdown
# Time-windowed Aggregation Functions

**Time-windowed Aggregation Functions** are a core component of the [[Declarative Feature Engineering APIs]] that enable computing aggregated statistics over time-based windows from data sources. These functions allow you to define features that capture temporal patterns, trends, and behaviors by aggregating data within specified time ranges relative to each observation point.

## Overview

Time-windowed aggregation functions compute summary statistics (such as sum, average, or count) over a defined time window for each entity. They are essential for creating features that capture recent behavior, historical patterns, and trends in time-series data. These functions are defined using the `AggregationFunction` class in the Databricks Feature Engineering API. ^[declarative-features-databricks-on-aws.md]

## Supported Aggregation Functions

The Declarative Feature Engineering APIs support a limited set of user-defined aggregate functions (UDAFs) for time-windowed computations. The available functions include:

- **Sum** — Computes the total of a numeric column over the window
- **Avg** — Computes the average of a numeric column over the window
- **Count** — Counts the number of records over the window

For the complete list of supported functions, see the [[Declarative Feature Engineering API|Declarative features API reference]]. ^[declarative-features-databricks-on-aws.md]

## Window Types

Time-windowed aggregation functions support three types of windows, each suited for different use cases.

### Tumbling Windows

A **tumbling window** is a fixed-duration, non-overlapping window that resets at regular intervals. For example, a 30-day tumbling window computes aggregates for each consecutive 30-day period without overlap. ^[declarative-features-databricks-on-aws.md]

```python
from datetime import timedelta
from databricks.feature_engineering.entities import (
    AggregationFunction, Avg, TumblingWindow
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

### Sliding Windows

A **sliding window** computes aggregates over a moving window that advances by a specified slide duration. For example, a 7-day window sliding by 1 day computes daily rolling averages over the past week. Sliding windows are recommended for most use cases due to their scalability. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    AggregationFunction, Sum, SlidingWindow
)

sum_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Sum(input="amount"),
        SlidingWindow(
            window_duration=timedelta(days=7),
            slide_duration=timedelta(days=1)
        )
    ),
    # name auto-generated: "amount_sum_sliding_7d_1d"
)
```

### Rolling Windows

A **rolling window** (also called a continuous window) computes aggregates over a fixed lookback period from each point in time. Rolling windows are more computationally intensive than tumbling or sliding windows. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    AggregationFunction, Count, RollingWindow
)

recency_feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Count(input="transaction_id"),
        RollingWindow(window_duration=timedelta(days=1))
    ),
)
```

## Window Parameters

### Window Duration

The `window_duration` parameter specifies the length of the time window for aggregation. It is defined using `timedelta` objects. ^[declarative-features-databricks-on-aws.md]

### Slide Duration

The `slide_duration` parameter (available for sliding windows) specifies how often the window advances. It must be shorter than or equal to the `window_duration`. ^[declarative-features-databricks-on-aws.md]

### Delay

The `delay` parameter (available for rolling windows) shifts the window backward in time. This is useful for comparing current behavior against historical baselines or for avoiding lookahead bias. ^[declarative-features-databricks-on-aws.md]

```python
# Compare recent vs. historical behavior
recent_avg = fe.create_feature(
    catalog_name="main", schema_name="ecommerce",
    source=transactions, entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"),
        RollingWindow(window_duration=timedelta(days=7))
    ),
)

historical_avg = fe.create_feature(
    catalog_name="main", schema_name="ecommerce",
    source=transactions, entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"),
        RollingWindow(
            window_duration=timedelta(days=7),
            delay=timedelta(days=7)
        )
    ),
)
```

## Best Practices

### Window Selection

- **Align window boundaries with business cycles** — Use daily, weekly, or monthly windows that match your business reporting periods. ^[declarative-features-databricks-on-aws.md]
- **Shorter windows** capture recent trends but can be noisy. **Longer windows** produce more stable feature distributions but might miss recent behavioral shifts. Choose based on how quickly the underlying signal changes for your use case. ^[declarative-features-databricks-on-aws.md]
- **Tumbling and sliding windows** are more scalable than rolling (continuous) windows. Start with sliding windows for most use cases. ^[declarative-features-databricks-on-aws.md]

### Performance

- Use the same granularity (for example, all 1-hour or all 1-day slide durations) for features on the same data source to enable better grouping during materialization. ^[declarative-features-databricks-on-aws.md]

## Common Patterns

### Customer Analytics (RFM)

Time-windowed aggregation functions are commonly used for Recency, Frequency, Monetary (RFM) analysis: ^[declarative-features-databricks-on-aws.md]

```python
features = [
    # Recency: Number of transactions in the last day
    fe.create_feature(
        catalog_name="main", schema_name="ecommerce",
        source=transactions, entity=["user_id"],
        timeseries_column="transaction_time",
        function=AggregationFunction(
            Count(input="transaction_id"),
            RollingWindow(window_duration=timedelta(days=1))
        )
    ),
    # Frequency: transaction count over the last 90 days
    fe.create_feature(
        catalog_name="main", schema_name="ecommerce",
        source=transactions, entity=["user_id"],
        timeseries_column="transaction_time",
        function=AggregationFunction(
            Count(input="transaction_id"),
            RollingWindow(window_duration=timedelta(days=90))
        )
    ),
    # Monetary: total spend in the last month
    fe.create_feature(
        catalog_name="main", schema_name="ecommerce",
        source=transactions, entity=["user_id"],
        timeseries_column="transaction_time",
        function=AggregationFunction(
            Sum(input="amount"),
            RollingWindow(window_duration=timedelta(days=30))
        )
    ),
]
```

### Trend Analysis

Compare recent behavior against historical baselines using the `delay` parameter: ^[declarative-features-databricks-on-aws.md]

```python
recent_avg = fe.create_feature(
    catalog_name="main", schema_name="ecommerce",
    source=transactions, entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"),
        RollingWindow(window_duration=timedelta(days=7))
    ),
)

historical_avg = fe.create_feature(
    catalog_name="main", schema_name="ecommerce",
    source=transactions, entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"),
        RollingWindow(
            window_duration=timedelta(days=7),
            delay=timedelta(days=7)
        )
    ),
)
```

### Seasonal Patterns

Capture seasonal effects by using the `delay` parameter to look back to the same period in a previous cycle: ^[declarative-features-databricks-on-aws.md]

```python
# Same day of week, 4 weeks ago
weekly_pattern = fe.create_feature(
    catalog_name="main", schema_name="ecommerce",
    source=transactions, entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"),
        RollingWindow(
            window_duration=timedelta(days=1),
            delay=timedelta(weeks=4)
        )
    ),
)
```

## Limitations

- Time-windowed aggregation functions are not supported with `RequestSource` data sources. Only `ColumnSelection` functions can be used with request-time data. ^[declarative-features-databricks-on-aws.md]
- Only a limited list of UDAFs is supported in the `create_feature` API. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering APIs](/concepts/declarative-feature-engineering-apis.md) — The framework for defining and computing features
- [Feature Materialization](/concepts/feature-materialization.md) — Materializing time-windowed features for serving
- [DeltaTableSource](/concepts/deltatablesource.md) — The data source for time-windowed aggregations
-

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
