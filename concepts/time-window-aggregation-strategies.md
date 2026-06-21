---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea4bee9b1d13f32968c089811b3effedcfcfd4b5dcd752b04eac9f9e132789fe
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-window-aggregation-strategies
    - TWAS
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Time Window Aggregation Strategies
description: Best practices and trade-offs for choosing window types (tumbling, sliding, rolling) and durations in feature engineering, balancing noise versus stability.
tags:
  - feature-engineering
  - time-series
  - best-practices
timestamp: "2026-06-18T11:45:53.367Z"
---

# Time Window Aggregation Strategies

**Time Window Aggregation Strategies** define how feature engineering systems compute aggregate statistics over temporal data by grouping records within specified time boundaries. These strategies are fundamental to [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) and enable the creation of features that capture behavioral patterns, trends, and seasonality from time-series data.

## Overview

Time window aggregations compute summary statistics—such as sums, averages, or counts—over data points that fall within a defined temporal window. The choice of window strategy affects both the statistical properties of the resulting features and the computational scalability of the materialization pipeline. ^[declarative-features-databricks-on-aws.md]

## Window Types

### Tumbling Windows

A **tumbling window** is a fixed-duration, non-overlapping time interval. Each data point belongs to exactly one window, and windows advance by the full window duration. Tumbling windows are appropriate for calendar-aligned aggregations such as monthly totals or daily counts. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import TumblingWindow, Avg
from datetime import timedelta

avg_feature_30d = AggregationFunction(
    Avg(input="amount"),
    TumblingWindow(window_duration=timedelta(days=30))
)
```

### Sliding Windows

A **sliding window** is a fixed-duration interval that advances by a smaller **slide duration**, creating overlapping windows. Each data point can appear in multiple consecutive windows. Sliding windows are useful for capturing rolling trends where the window endpoint moves forward incrementally. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import SlidingWindow, Sum
from datetime import timedelta

sum_feature_7d = AggregationFunction(
    Sum(input="amount"),
    SlidingWindow(
        window_duration=timedelta(days=7),
        slide_duration=timedelta(days=1)
    )
)
```

### Rolling Windows

A **rolling (continuous) window** recomputes the aggregation for every new data point using a fixed lookback period. Unlike tumbling and sliding windows, rolling windows do not align to predefined boundaries—they are evaluated on a per-row basis. Rolling windows are less scalable than tumbling or sliding windows and are best suited for use cases where the signal changes rapidly and fresh aggregations are needed for every prediction. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import RollingWindow, Count
from datetime import timedelta

count_feature_1d = AggregationFunction(
    Count(input="transaction_id"),
    RollingWindow(window_duration=timedelta(days=1))
)
```

### Delayed Windows

A **delayed window** shifts the window boundary by a fixed **delay** duration, allowing comparisons between current and historical behavior. Delayed windows are used for trend analysis and seasonal pattern detection—for example, comparing this week's average to the same week four weeks ago. ^[declarative-features-databricks-on-aws.md]

```python
historical_avg = fe.create_feature(
    source=transactions,
    entity=["user_id"],
    timeseries_column="transaction_time",
    function=AggregationFunction(
        Avg(input="amount"),
        RollingWindow(
            window_duration=timedelta(days=7),
            delay=timedelta(days=7)
        )
    ),
    catalog_name="main",
    schema_name="ecommerce",
)
```

## Choosing Window Durations

### Business Cycle Alignment

Align window boundaries with business cycles (daily, weekly, monthly) to produce features that are interpretable and match reporting rhythms. ^[declarative-features-databricks-on-aws.md]

### Stability vs. Reactivity

| Duration | Characteristic | Use Case |
|----------|---------------|----------|
| Short (e.g., 1 hour) | Reacts quickly to behavioral changes but can be noisy. | High-frequency trading or real-time fraud detection. |
| Long (e.g., 7 days) | Smooths out daily fluctuations, producing stable model inputs. | Credit risk assessment or customer lifetime value modeling. |

If model accuracy degrades when the distribution shifts unexpectedly, use a longer window to stabilize inputs. ^[declarative-features-databricks-on-aws.md]

### Scalability Trade-offs

Tumbling and sliding windows are more scalable than rolling windows. Start with sliding windows for most use cases, as they balance freshness with computational efficiency. ^[declarative-features-databricks-on-aws.md]

## Performance Considerations

### Materialization Grouping

Materialize features from the same data source in a single `materialize_features` call to minimize data scans. Use the same granularity (for example, all 1-hour or all 1-day slide durations) for features on the same data source to enable better grouping during materialization. ^[declarative-features-databricks-on-aws.md]

### Granularity Consistency

When multiple features share the same source table but have different window durations, materialization performance degrades. Maintain consistent window durations across features to allow the system to batch computations efficiently. ^[declarative-features-databricks-on-aws.md]

## Entity Columns vs. Filter Conditions

Use `entity` when you need different aggregation levels (one row per entity vs. multiple rows per entity). Use `filter_condition` on the source when you need to filter which rows contribute to the same aggregation level (e.g., high-value transactions only, still aggregated per customer). ^[declarative-features-databricks-on-aws.md]

## Best Practices

- **Start with sliding windows** for most use cases before introducing tumbling or rolling windows. ^[declarative-features-databricks-on-aws.md]
- **Use descriptive names** for business-critical features and follow consistent naming conventions across teams. ^[declarative-features-databricks-on-aws.md]
- **Align window durations with the business cycle** (daily, weekly, monthly) to make features interpretable. ^[declarative-features-databricks-on-aws.md]
- **Use delayed windows** for trend analysis and seasonal pattern detection. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The API framework that defines window-based features
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) — Ensuring features do not leak future information
- [Feature Materialization](/concepts/feature-materialization.md) — The process of computing and storing windowed features
- [Time-Series Feature Store](/concepts/time-series-feature-table.md) — The Unity Catalog-based storage for declarative features
- Aggregation Functions — The set of supported UDAFs (sum, avg, count, etc.) for windowed computations

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
