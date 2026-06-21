---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1000318769cefd157e5f1ecc218ac23ffc77994e1778b3d4b0159219dfe0e870
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
    - use-custom-metrics-with-data-profiling-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - drift-metrics
  citations:
    - file: data-profiling-databricks-on-aws.md
    - file: use-custom-metrics-with-data-profiling-databricks-on-aws.md
title: Drift Metrics
description: Statistics produced by data profiling that quantify how a table's data distribution changes over time or relative to a baseline table, used to detect data and model drift.
tags:
  - data-quality
  - drift-detection
  - monitoring
timestamp: "2026-06-19T09:45:08.699Z"
---



---
title: Drift Metrics
description: Drift Metrics are a key output of data profiling on Databricks, tracking changes in data distributions over time.
sources:
  - data-profiling-databricks-on-aws.md
  - use-custom-metrics-with-data-profiling-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:31:41.933Z"
updatedAt: "2026-06-19T09:31:41.933Z"
tags:
  - data-profiling
  - drift
  - data-quality
aliases:
  - drift-metrics
  - DM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Drift Metrics

**Drift Metrics** are metrics computed by [Data Profiling](/concepts/data-profiling.md) that track changes in data distributions over time. They are stored in a dedicated drift metrics table and provide quantitative measures of stability or drift in a dataset's statistical properties.^[data-profiling-databricks-on-aws.md]

## Overview

Drift metrics are part of the output tables generated when you profile a table in [Unity Catalog](/concepts/unity-catalog.md) using [Data Profiling](/concepts/data-profiling.md). While the profile metrics table contains summary statistics about the current state of the data, the drift metrics table specifically captures how the data's distribution has changed relative to a previous state.^[data-profiling-databricks-on-aws.md]

If a [Baseline Table](/concepts/baseline-table.md) is provided when creating the profile, drift is also computed relative to the baseline values. Baseline tables represent expected data quality or statistical distributions, and drift metrics compare the primary table against this reference.^[data-profiling-databricks-on-aws.md]

## Types of Drift

Drift metrics can capture several types of change:

- **Time‑window drift:** Comparing the primary table's data across successive time windows (e.g., day over day, week over week).^[data-profiling-databricks-on-aws.md]
- **Baseline drift:** Comparing the primary table against an optional baseline table that represents expected normal data. For example, weather data might be compared against a season of "normal" temperatures.^[data-profiling-databricks-on-aws.md]
- **Custom drift metrics:** Track changes between the primary table and the baseline or previous time window using user‑defined metrics.^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

## Drift Metrics Table

The drift metrics table is a Delta table stored in a Unity Catalog schema that you specify when creating the profile. It contains statistics related to the data's drift over time. Like the profile metrics table, you can query it using Databricks SQL, visualize it in a dashboard, and set up alerts.^[data-profiling-databricks-on-aws.md]

For the full schema of the drift metrics table, see the [drift metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#drift-metrics-table).^[data-profiling-databricks-on-aws.md]

## Custom Drift Metrics

In addition to the automatically computed drift statistics, you can create custom drift metrics using the MonitorMetric API. Custom drift metrics compare previously computed aggregate or derived metrics from two different time windows, or between the primary table and the baseline table. Using derived and drift metrics where possible minimizes recomputation over the full primary table. Only aggregate metrics access data from the primary table; derived and drift metrics can be computed directly from the aggregate metric values.^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

### Example: Custom Drift Metric

The following example defines a drift metric that tracks the change in a `weighted_error` metric between the current time window and the comparison window (baseline or previous time window):^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

```python
from databricks.sdk.service.catalog import MonitorMetric, MonitorMetricType
from pyspark.sql import types as T

MonitorMetric(
    type=MonitorMetricType.CUSTOM_METRIC_TYPE_DRIFT,
    name="error_rate_delta",
    input_columns=[":table"],
    definition="{{current_df}}.weighted_error - {{base_df}}.weighted_error",
    output_data_type=T.StructField("output", T.DoubleType()).json(),
)
```

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The overall system that produces drift metrics
- Profile Metrics — The companion table to drift metrics
- [Baseline Table](/concepts/baseline-table.md) — The reference dataset used for drift comparison
- Custom Metrics — User‑defined metrics beyond the default set
- Drift — The broader concept of distribution shift in MLOps and data monitoring

## Sources

- data-profiling-databricks-on-aws.md
- use-custom-metrics-with-data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
2. [use-custom-metrics-with-data-profiling-databricks-on-aws.md](/references/use-custom-metrics-with-data-profiling-databricks-on-aws-8de965f1.md)
