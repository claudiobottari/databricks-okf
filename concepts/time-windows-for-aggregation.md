---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1a0697abede742b024d01cfe25b420576d756e5d1332a875910c1ae29dec353
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-windows-for-aggregation
    - TWFA
    - Time Window Aggregation
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Time Windows for Aggregation
description: Three types of time windows — rolling, tumbling, and sliding — that control lookback behavior for time-series aggregations in declarative features, each with distinct semantics for overlapping, non-overlapping, and real-time windows.
tags:
  - feature-engineering
  - time-series
  - aggregation
timestamp: "2026-06-19T09:57:19.701Z"
---

# Time Windows for Aggregation

**Time Windows for Aggregation** are a core concept in declarative feature engineering that control how historical data is aggregated for use in machine learning features. They define the lookback period and behavior for time-based aggregations, ensuring consistent and accurate feature computation.

## Overview

Time windows are used with aggregation functions (such as `Sum`, `Avg`, `Count`) to specify which historical data should be included when computing features at a given point in time. They are essential for preventing data leakage and ensuring online-offline consistency in feature engineering pipelines. ^[declarative-features-api-reference-databricks-on-aws.md]

## Window Types

Declarative Feature Engineering APIs support three distinct window types:

- **[Rolling Window](/concepts/rolling-window-backtesting.md)**: Looks back from the event time, with explicit duration and optional delay.
- **Tumbling Window**: Fixed, non-overlapping windows where each data point belongs to exactly one window.
- **Sliding Window**: Overlapping windows with a configurable slide interval.

## Rolling Window

`RollingWindow`, previously named `ContinuousWindow`, is an up-to-date, real-time aggregate typically used over streaming data. In streaming pipelines, the rolling window emits a new row only when the contents of the fixed-length window change, such as when an event enters or leaves. When used in training pipelines, an accurate point-in-time calculation is performed using the fixed-length window duration immediately preceding a specific event's timestamp. ^[declarative-features-api-reference-databricks-on-aws.md]

Features at time `T` aggregate events from [`T` − duration, `T`).

### Parameters

| Parameter | Description |
|-----------|-------------|
| `window_duration` | The lookback period from the evaluation time |
| `delay` (optional) | Offset to account for data ingestion delays |

The window start and end times are based on these parameters:
- Start time: `evaluation_time - window_duration - delay` (inclusive)
- End time: `evaluation_time - delay` (exclusive)

### Examples

- `window_duration=timedelta(days=7)`: Creates a 7-day lookback window ending at the current evaluation time. For an event at 2:00 PM on Day 7, this includes all events from 2:00 PM on Day 0 up to (but not including) 2:00 PM on Day 7.
- `window_duration=timedelta(hours=1), delay=timedelta(minutes=30)`: Creates a 1-hour lookback window ending 30 minutes before the evaluation time. For an event at 3:00 PM, this includes all events from 1:30 PM up to (but not including) 2:30 PM. ^[declarative-features-api-reference-databricks-on-aws.md]

## Tumbling Window

`TumblingWindow` creates pre-determined fixed-length windows that advance by a slide interval, producing non-overlapping windows that fully partition time. As a result, each event in the source contributes to exactly one window. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). Windows start at the Unix epoch. ^[declarative-features-api-reference-databricks-on-aws.md]

### Parameters

| Parameter | Description |
|-----------|-------------|
| `window_duration` | The fixed duration of each window |

### Example

`window_duration=timedelta(days=5)`: Creates pre-determined fixed-length windows of 5 days each. Window #1 spans Day 0 to Day 4, Window #2 spans Day 5 to Day 9, Window #3 spans Day 10 to Day 14, and so on. Each event belongs to exactly one window. ^[declarative-features-api-reference-databricks-on-aws.md]

## Sliding Window

`SlidingWindow` creates pre-determined fixed-length windows that advance by a slide interval, producing overlapping windows. Each event in the source can contribute to feature aggregation for multiple windows. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). Windows start at the Unix epoch. ^[declarative-features-api-reference-databricks-on-aws.md]

### Parameters

| Parameter | Description |
|-----------|-------------|
| `window_duration` | The fixed duration of each window |
| `slide_duration` | The interval by which the window advances |

### Example

`window_duration=timedelta(days=5), slide_duration=timedelta(days=1)`: Creates overlapping 5-day windows that advance by 1 day each time. Window #1 spans Day 0 to Day 4, Window #2 spans Day 1 to Day 5, Window #3 spans Day 2 to Day 6, and so on. Because windows overlap, a single event can belong to multiple windows (up to 5 in this example). ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — The operator (e.g., `Sum`, `Avg`, `Count`) applied within a time window
- materialize_features() API|Materialized Features — How time windows are used in materialization pipelines
- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The broader framework for defining features
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) — Ensuring features are computed using only data available before the prediction time

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
