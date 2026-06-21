---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aae20beb852f1ad73f8a72ebad2b09bec5b9aae55235837d649d7e3254930707
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-windows
    - TimeWindow
    - time window
    - tumbling windows
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Time Windows
description: Three types of lookback windows (Rolling, Tumbling, Sliding) that control aggregation time ranges for feature computation in Databricks Feature Engineering
tags:
  - time-series
  - feature-engineering
  - aggregation
  - databricks
timestamp: "2026-06-18T11:44:56.635Z"
---



# Time Windows

**Time Windows** are the core mechanism in [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) for defining how historical data is aggregated over time. They specify the lookback period used to compute features from time-series data, ensuring point-in-time correctness and preventing data leakage between training and inference.

## Purpose

Time windows define the temporal scope over which aggregations are computed. They determine which historical events contribute to a feature value at a given point in time. Different window types create different aggregation behaviors, affecting whether events overlap or are strictly partitioned. ^[declarative-features-api-reference-databricks-on-aws.md]

## Supported Window Types

Declarative Feature Engineering APIs support three distinct window types for time-based aggregations: rolling, tumbling, and sliding. ^[declarative-features-api-reference-databricks-on-aws.md]

### Rolling Window

Rolling windows are up-to-date, real-time aggregates that look back from the evaluation time. In streaming pipelines, they emit new rows only when the contents of the fixed-length window change (such as when an event enters or leaves). For training pipelines, they perform accurate point-in-time feature computation to prevent online-offline skew or data leakage. Features at time `T` aggregate events from [`T` − duration, `T`). ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import RollingWindow
from datetime import timedelta

# Look back 7 days from evaluation time
window = RollingWindow(window_duration=timedelta(days=7))
```

The start time is `evaluation_time - window_duration - delay` (inclusive), and the end time is `evaluation_time - delay` (exclusive). An optional `delay` parameter accounts for data ingestion latency. ^[declarative-features-api-reference-databricks-on-aws.md]

### Tumbling Window

Tumbling windows are fixed, non-overlapping time windows that fully partition time. Each event contributes to exactly one window, and windows start at the Unix epoch. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import TumblingWindow
from datetime import timedelta

# Pre-determined fixed windows of 5 days each
window = TumblingWindow(window_duration=timedelta(days=5))
```

### Sliding Window

Sliding windows are overlapping, rolling time windows that advance by a configurable slide interval. Each event can contribute to multiple windows. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import SlidingWindow
from datetime import timedelta

# Overlapping 5-day windows advancing 1 day at a time
window = SlidingWindow(
    window_duration=timedelta(days=5),
    slide_duration=timedelta(days=1)
)
```

## Visual Representation

The following illustration shows how rolling, tumbling, and sliding windows operate differently:

![Rolling, tumbling, and sliding lookback windows](https://docs.databricks.com/aws/en/assets/images/time-windows-overview-517ebf268394f277c9b3cdebca32e6a9.png)

## Usage in Feature Definitions

Time windows are specified on Feature objects using the `function` parameter, which takes an `AggregationFunction` wrapper that combines an aggregation operator (such as `Sum`, `Avg`, `ApproxCountDistinct`) with the time window. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    AggregationFunction, Feature, Sum, RollingWindow
)
from datetime import timedelta

feature = Feature(
    source=source,
    entity=["user_id"],
    timeseries_column="event_time",
    function=AggregationFunction(
        Sum(input="amount"),
        RollingWindow(window_duration=timedelta(days=7))
    ),
)
```

## Choosing the Right Window

- **Rolling windows** provide real-time, up-to-date aggregates and are best for streaming or near-real-time use cases.
- **Tumbling windows** produce non-overlapping, fixed partitions ideal for batch processing where each event belongs to exactly one window.
- **Sliding windows** create overlapping windows with a configurable slide interval, useful for capturing gradual trends or repeating patterns.

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The framework for defining features programmatically
- Feature Engineering Pipeline — How features are materialized and served
- Online-Offline Skew — Why point-in-time correctness prevents ML prediction drift
- Aggregation Function — The operator applied within a time window
- [Training and Inference API](/concepts/training-and-inference-api.md) — How `create_training_set()` and `log_model()` use time windows

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
