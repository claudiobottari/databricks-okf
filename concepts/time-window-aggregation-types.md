---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72200d3c84104d5b288ed40cd7bdc25baa89db228f3104f0722be457af811776
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-window-aggregation-types
    - TWAT
    - Time‑Window Aggregations
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Time Window Aggregation Types
description: Different window strategies (tumbling, sliding, rolling) for computing time-series aggregations with trade-offs between scalability and recency
tags:
  - feature-engineering
  - time-series
  - aggregation
timestamp: "2026-06-19T18:18:19.064Z"
---

```markdown
---
title: Time Window Aggregation Types
summary: "Three types of time windows for feature aggregation: Tumbling (fixed non-overlapping intervals), Sliding (overlapping windows with slide duration), and Rolling (continuous windows with optional delay), each with different scalability and sensitivity characteristics."
sources:
  - declarative-features-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:57:20.846Z"
updatedAt: "2026-06-19T09:57:20.846Z"
tags:
  - feature-engineering
  - time-series
  - aggregation
aliases:
  - time-window-aggregation-types
  - TWAT
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Time Window Aggregation Types

**Time Window Aggregation Types** define how time-series data is grouped and aggregated over specified time intervals in the [[Declarative Feature Engineering APIs]]. These window types control the temporal scope and behavior of feature computations, enabling the creation of features that capture trends, patterns, and historical behavior from event data.

## Overview

Time window aggregations are a core component of feature engineering for machine learning models that process sequential or time-series data. The Declarative Feature Engineering APIs support multiple window types, each with different characteristics for how they compute aggregations over time. ^[declarative-features-databricks-on-aws.md]

## Supported Window Types

### Tumbling Window

A **Tumbling Window** is a fixed-size, non-overlapping time window. Each window covers a distinct time period with no overlap between consecutive windows. This type is useful for computing aggregations over discrete time intervals such as daily, weekly, or monthly periods. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import TumblingWindow
from datetime import timedelta

# 30-day tumbling window
window = TumblingWindow(window_duration=timedelta(days=30))
```

### Sliding Window

A **Sliding Window** is a fixed-size window that moves forward in time by a specified slide duration, creating overlapping windows. This type is useful for capturing rolling trends where you want to see how metrics change over time with frequent updates. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import SlidingWindow
from datetime import timedelta

# 7-day sliding window that slides daily
window = SlidingWindow(
    window_duration=timedelta(days=7),
    slide_duration=timedelta(days=1)
)
```

### Rolling Window

A **Rolling Window** computes aggregations over a lookback period from each point in time. Unlike tumbling and sliding windows, rolling windows are computed for every data point, providing a continuous view of historical behavior. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import RollingWindow
from datetime import timedelta

# 30-day rolling window
window = RollingWindow(window_duration=timedelta(days=30))
```

## Window with Delay

The `delay` parameter shifts the window backward in time. In the source material, the delay parameter is shown with `RollingWindow` for comparing recent behavior against historical baselines or analyzing seasonal patterns. ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import RollingWindow
from datetime import timedelta

# 7-day window from 7 days ago (historical comparison)
window = RollingWindow(
    window_duration=timedelta(days=7),
    delay=timedelta(days=7)
)
```

## Best Practices

### Window Duration Selection

- **Shorter windows** capture recent trends but can be noisy. They react quickly to behavioral changes but may introduce variance that degrades model performance. ^[declarative-features-databricks-on-aws.md]
- **Longer windows** produce more stable feature distributions but might miss recent behavioral shifts. They smooth out daily fluctuations and produce consistent model inputs. ^[declarative-features-databricks-on-aws.md]
- Choose window duration based on how quickly the underlying signal changes for your use case. If model accuracy degrades when the distribution shifts, use a longer window to stabilize inputs. ^[declarative-features-databricks-on-aws.md]

### Scalability Considerations

- **Tumbling and sliding windows** are more scalable than rolling windows. Start with sliding windows for most use cases. ^[declarative-features-databricks-on-aws.md]
- Align window boundaries with business cycles (daily, weekly) for better interpretability. ^[declarative-features-databricks-on-aws.md]
- Use the same granularity (for example, all 1-hour or all 1-day slide durations) for features on the same data source to enable better grouping during materialization. ^[declarative-features-databricks-on-aws.md]

## Common Use Cases

### Customer Analytics

Time window aggregations are commonly used for RFM (Recency, Frequency, Monetary) analysis, where different window durations capture different aspects of customer behavior. ^[declarative-features-databricks-on-aws.md]

### Trend Analysis

Comparing recent windows against historical windows (using the `delay` parameter) enables trend detection and anomaly identification. ^[declarative-features-databricks-on-aws.md]

### Seasonal Patterns

Using delayed windows allows analysis of same-day-of-week or same-period patterns from previous cycles, such as comparing current behavior to behavior four weeks ago. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [[Declarative Feature Engineering APIs]] – The framework for defining and computing features
- Aggregation Functions – The mathematical operations applied within windows (Sum, Avg, Count, etc.)
- [[Feature Materialization]] – Persisting computed features for efficient reuse
- [[Point-in-Time Correctness]] – Ensuring features use only data available at prediction time
- [[Clustering columns|Entity Columns]] – The grouping keys for time window aggregations

## Sources

- declarative-features-databricks-on-aws.md
```

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
