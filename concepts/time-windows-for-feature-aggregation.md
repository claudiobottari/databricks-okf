---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13b15dd90f2b13dd0e97ec9e923b990f07c869c582ac4553afbeee0a95463204
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-windows-for-feature-aggregation
    - TWFFA
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Time Windows for Feature Aggregation
description: Three types of time windows (Rolling, Tumbling, Sliding) that control lookback behavior for time-window-based aggregations in declarative feature engineering.
tags:
  - time-windows
  - feature-engineering
  - aggregation
timestamp: "2026-06-19T14:56:45.801Z"
---

# Time Windows for Feature Aggregation

**Time Windows for Feature Aggregation** define the lookback behaviour for computing aggregated features over time-series data in the Declarative Feature Engineering API. Three window types are supported: **rolling**, **tumbling**, and **sliding**. Each controls how rows in the source table are grouped relative to an evaluation timestamp, ensuring point-in-time correctness and preventing data leakage during training and inference. ^[declarative-features-api-reference-databricks-on-aws.md]

## Rolling Window

A **rolling window** (previously called `ContinuousWindow`) creates a fixed-length lookback that always ends at the current evaluation time. In streaming pipelines it emits a row only when the window contents change. For offline training it calculates the exact aggregate over the period immediately preceding the event timestamp. The aggregate includes events from `[evaluation_time - window_duration - delay, evaluation_time - delay)` (start inclusive, end exclusive). ^[declarative-features-api-reference-databricks-on-aws.md]

```python
class RollingWindow(TimeWindow):
    window_duration: datetime.timedelta
    delay: Optional[datetime.timedelta] = None
```

Example use:

```python
from databricks.feature_engineering.entities import RollingWindow
from datetime import timedelta

# 7-day lookback window, no delay
window = RollingWindow(window_duration=timedelta(days=7))

# 1-hour lookback, offset by 30 minutes to account for ingestion delay
window = RollingWindow(
    window_duration=timedelta(hours=1),
    delay=timedelta(minutes=30)
)
```

## Tumbling Window

A **tumbling window** partitions time into fixed-length, non-overlapping segments. Each source event belongs to exactly one window. The aggregate at time `t` uses only the windows that end at or before `t` (exclusive). Windows are anchored to the Unix epoch (1 January 1970). ^[declarative-features-api-reference-databricks-on-aws.md]

```python
class TumblingWindow(TimeWindow):
    window_duration: datetime.timedelta
```

Example:

```python
window = TumblingWindow(window_duration=timedelta(days=5))
# Windows: [Day0–Day4], [Day5–Day9], [Day10–Day14], ...
```

## Sliding Window

A **sliding window** produces overlapping fixed-length windows that advance by a configurable slide interval. A single event may contribute to multiple windows. The aggregate at time `t` uses windows ending at or before `t` (exclusive). Like tumbling windows, sliding windows are anchored to the Unix epoch. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
class SlidingWindow(TimeWindow):
    window_duration: datetime.timedelta
    slide_duration: datetime.timedelta
```

Example:

```python
window = SlidingWindow(
    window_duration=timedelta(days=5),
    slide_duration=timedelta(days=1)
)
# Windows: [Day0–Day4], [Day1–Day5], [Day2–Day6], ...
```

## Choosing a Window Type

- **Rolling windows** are best for real-time, up-to-date aggregates where the window should always end at the current evaluation time (e.g., last 7 days from "now").
- **Tumbling windows** produce deterministic, non-overlapping groups suitable for fixed-period reporting (e.g., weekly aggregates).
- **Sliding windows** are used when overlapping windows are needed to capture gradual changes (e.g., a 7‑day moving average recomputed daily).

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) – The higher-level API that consumes time windows.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – Wraps a window together with an operator like `Sum` or `Avg`.
- [RollingWindow (declarative features)](/concepts/rolling-window-backtesting.md)
- TumblingWindow (declarative features)
- [SlidingWindow (declarative features)](/concepts/declarative-feature-engineering-api.md)
- [Point-in-time correctness](/concepts/point-in-time-correctness.md) – Why time windows prevent data leakage.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
