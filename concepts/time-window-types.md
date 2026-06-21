---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6de8286228d4bbe0d7ec132c03111426188b78929f1dfd8b81a5cfe4ecd99095
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-window-types
    - TWT
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Time Window Types
description: "Three distinct lookback window semantics for time-series aggregations: Rolling (real-time, up-to-date), Tumbling (fixed non-overlapping partitions), and Sliding (overlapping windows with configurable slide interval)."
tags:
  - feature-engineering
  - time-windows
  - aggregation
timestamp: "2026-06-19T18:17:45.497Z"
---

# Time Window Types

**Time window types** define the lookback behavior for time‑window‑based aggregations in Databricks Declarative Feature Engineering. The declarative API supports three distinct window types: rolling, tumbling, and sliding. Each type controls how the aggregation scope is computed relative to an evaluation timestamp. ^[declarative-features-api-reference-databricks-on-aws.md]

---

## Rolling Window

A rolling window is an up‑to‑date, real‑time aggregate typically used with streaming data. In streaming pipelines, the window emits a new row only when the contents of the fixed‑length window change (for example, when an event enters or leaves). In training pipelines, an accurate point‑in‑time calculation is performed on the source data using the fixed‑length window duration immediately preceding a specific event’s timestamp. This helps prevent online‑offline skew or data leakage. Features at time `T` aggregate events from `[T − duration, T)`. ^[declarative-features-api-reference-databricks-on-aws.md]

**Note:** `RollingWindow` was previously named `ContinuousWindow`. If you are migrating from an earlier SDK version, update your imports accordingly. ^[declarative-features-api-reference-databricks-on-aws.md]

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `window_duration` | `datetime.timedelta` | The lookback length (e.g., 7 days, 1 hour). |
| `delay` | `Optional[datetime.timedelta]` | An offset applied to the evaluation time before computing the window, used to account for data ingestion delays. |

- **Start time:** `evaluation_time - window_duration - delay` (inclusive)
- **End time:** `evaluation_time - delay` (exclusive)

^[declarative-features-api-reference-databricks-on-aws.md]

### Examples

```python
from datetime import timedelta
from databricks.feature_engineering.entities import RollingWindow

# Look back 7 days from evaluation time
window = RollingWindow(window_duration=timedelta(days=7))

# Look back 7 days, offset by 1 minute to account for data ingestion delay
window = RollingWindow(
    window_duration=timedelta(days=7),
    delay=timedelta(minutes=1),
)
```

- `window_duration=timedelta(days=7)`: For an event at 2:00 PM on Day 7, includes all events from 2:00 PM on Day 0 up to (but not including) 2:00 PM on Day 7.
- `window_duration=timedelta(hours=1), delay=timedelta(minutes=30)`: For an event at 3:00 PM, includes all events from 1:30 PM up to (but not including) 2:30 PM. Useful to account for data ingestion delays.

^[declarative-features-api-reference-databricks-on-aws.md]

---

## Tumbling Window

A tumbling window is a fixed‑length, non‑overlapping window that fully partitions time. Each event in the source contributes to exactly one window. Windows start at the Unix epoch and advance by the `window_duration`. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). ^[declarative-features-api-reference-databricks-on-aws.md]

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `window_duration` | `datetime.timedelta` | The fixed length of each window (e.g., 5 days, 1 week). |

No `delay` or `slide_duration` is used; windows are contiguous and deterministic.

### Example

```python
from datetime import timedelta
from databricks.feature_engineering.entities import TumblingWindow

window = TumblingWindow(window_duration=timedelta(days=5))
```

- `window_duration=timedelta(days=5)`: Window #1 spans Day 0 to Day 4, Window #2 spans Day 5 to Day 9, etc. Each event belongs to exactly one window.

^[declarative-features-api-reference-databricks-on-aws.md]

---

## Sliding Window

A sliding window is a fixed‑length window that advances by a configurable slide interval, producing overlapping windows. Each event in the source can contribute to multiple windows. Windows start at the Unix epoch. Features at time `t` aggregate data from windows ending at or before `t` (exclusive). ^[declarative-features-api-reference-databricks-on-aws.md]

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `window_duration` | `datetime.timedelta` | The fixed length of each window (e.g., 7 days). |
| `slide_duration` | `datetime.timedelta` | The interval between the start of successive windows (e.g., 1 day). |

### Example

```python
from datetime import timedelta
from databricks.feature_engineering.entities import SlidingWindow

window = SlidingWindow(
    window_duration=timedelta(days=5),
    slide_duration=timedelta(days=1),
)
```

- `window_duration=timedelta(days=5), slide_duration=timedelta(days=1)`: Window #1 spans Day 0 to Day 4, Window #2 spans Day 1 to Day 5, Window #3 spans Day 2 to Day 6, etc. Because windows overlap, a single event can belong to up to 5 windows.

^[declarative-features-api-reference-databricks-on-aws.md]

---

## Summary of Behavior

| Window Type | Overlap | Event Membership | Typical Use Case |
|-------------|---------|------------------|------------------|
| **Rolling** | No (point‑in‑time) | Each event belongs to the window that ends at the evaluation time | Real‑time streaming, online‑offline consistency |
| **Tumbling** | No | Each event belongs to exactly one window | Batch processing, fixed time‑based aggregations |
| **Sliding** | Yes | An event may belong to multiple windows | Rolling statistics with finer granularity (e.g., daily averages over a week) |

All three window types are subclasses of `TimeWindow` and are used inside an [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) together with an operator (e.g., `Sum`, `Avg`, `Count`). ^[declarative-features-api-reference-databricks-on-aws.md]

---

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — Overview of the feature engineering API.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — How window types are combined with aggregation operators.
- [DeltaTableSource](/concepts/deltatablesource.md) — Data source used in feature definitions.
- RollingWindow / TumblingWindow / SlidingWindow — Individual entities.
- [Materialization Triggers](/concepts/materialization-triggers.md) — How materialization schedules interact with feature types.

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
