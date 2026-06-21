---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef46afc60abc0aa86825d6a6e103703a0ddcce16ccd04f2c6585760164255c90
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-metrics-in-data-profiling
    - CMIDP
    - Custom Metrics (Data Profiling)
    - Custom Metrics with Data Profiling
    - Use custom metrics with data profiling
  citations:
    - file: use-custom-metrics-with-data-profiling-databricks-on-aws.md
title: Custom Metrics in Data Profiling
description: A feature allowing users to define custom metrics beyond the built-in summary statistics when profiling tables in Databricks.
tags:
  - data-quality
  - databricks
  - customization
timestamp: "2026-06-19T14:43:02.191Z"
---

```markdown
---
title: Custom Metrics in Data Profiling
summary: The ability to define user-specified custom metrics in addition to the default profile and drift metrics, allowing tailored monitoring beyond standard summary statistics.
sources:
  - data-profiling-databricks-on-aws.md
  - use-custom-metrics-with-data-profiling-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:31:14.308Z"
updatedAt: "2026-06-18T11:31:14.308Z"
tags:
  - data-quality
  - customization
aliases:
  - custom-metrics-in-data-profiling
  - CMIDP
confidence: 0.85
provenanceState: merged
inferredParagraphs: 2
---

# Custom Metrics in Data Profiling

**Custom metrics** extend the built-in analysis and drift statistics computed by [[Data Profiling]] in Unity Catalog. While data profiling automatically calculates summary statistics and drift measures for monitored tables, custom metrics allow you to define calculations that capture domain-specific business logic, such as weighted means, custom model quality scores, or specialized drift comparisons. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

## Why Use Custom Metrics

Standard profiling metrics cover common statistical properties like null fractions, percentiles, and distribution shifts. However, many use cases require metrics that reflect specific business rules or quality criteria. For example:

- A weighted error metric that penalizes misclassifications more heavily in critical cases
- A custom model quality score incorporating domain-specific weighting
- A drift metric tracking changes in a derived business metric across time windows

Custom metrics allow you to encode these requirements directly into the profiling pipeline, storing the results alongside automatically computed metrics in the same metric tables. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

## Types of Custom Metrics

Data profiling supports three types of custom metrics, each serving a different purpose in the analysis pipeline. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

### Aggregate Metrics

Aggregate metrics are calculated directly from columns in the primary table. They require a full scan of the table data and are stored in the profile metrics table. Use aggregate metrics when the calculation depends on raw column values, such as weighted averages or custom error functions. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

### Derived Metrics

Derived metrics are calculated from previously computed aggregate metrics and do not require access to the primary table data. Because they reference only existing metric values, they avoid recomputation over the full dataset. Derived metrics are also stored in the profile metrics table. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

### Drift Metrics

Drift metrics compare previously computed aggregate or derived metrics across two different time windows, or between the primary table and a baseline table. They are stored in the drift metrics table and are useful for tracking changes in business-specific measurements over time. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

## Defining Custom Metrics

Custom metrics are defined using the `MonitorMetric` API from the Databricks SDK. Each metric requires a Jinja template that specifies a SQL column expression. The template cannot contain joins or subqueries. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

### Metric Parameters

The `MonitorMetric` class accepts the following key parameters when defining a custom metric: ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

| Parameter | Description |
|-----------|-------------|
| `type` | The metric type: `CUSTOM_METRIC_TYPE_AGGREGATE`, `CUSTOM_METRIC_TYPE_DERIVED`, or `CUSTOM_METRIC_TYPE_DRIFT` |
| `name` | A unique name for the custom metric |
| `input_columns` | The columns the metric operates on; use `[":table"]` when the metric references multiple columns |
| `definition` | A Jinja template string defining the SQL expression |
| `output_data_type` | The JSON representation of the output StructField, including the data type |

## Examples

### Aggregate Metric: Squared Average

The following example computes the average of the square of the values in columns `f1` and `f2`. The Jinja parameter `{{input_column}}` is replaced with each applicable column name. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

```python
from databricks.sdk.service.catalog import MonitorMetric, MonitorMetricType
from pyspark.sql import types as T

MonitorMetric(
    type=MonitorMetricType.CUSTOM_METRIC_TYPE_AGGREGATE,
    name="squared_avg",
    input_columns=["f1", "f2"],
    definition="avg(`{{input_column}}`*`{{input_column}}`)",
    output_data_type=T.StructField("output", T.DoubleType()).json(),
)
```

### Aggregate Metric: Multi-Column Calculation

This example computes the average difference between columns `f1` and `f2`. The `[":table"]` input column indicator signals that the calculation involves multiple columns from the table. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

```python
MonitorMetric(
    type=MonitorMetricType.CUSTOM_METRIC_TYPE_AGGREGATE,
    name="avg_diff_f1_f2",
    input_columns=[":table"],
    definition="avg(f1 - f2)",
    output_data_type=T.StructField("output", T.DoubleType()).json(),
)
```

### Aggregate Metric: Weighted Model Quality

This metric computes a weighted error score for model predictions. When the `critical` column is `True`, misclassifications receive a heavier penalty. Jinja parameters `{{prediction_col}}` and `{{label_col}}` are replaced with the profile's prediction and label column names. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

```python
MonitorMetric(
    type=MonitorMetricType.CUSTOM_METRIC_TYPE_AGGREGATE,
    name="weighted_error",
    input_columns=[":table"],
    definition="""avg(CASE
      WHEN {{prediction_col}} = {{label_col}} THEN 0
      WHEN {{prediction_col}} != {{label_col}} AND critical=TRUE THEN 2
      ELSE 1 END)""",
    output_data_type=T.StructField("output", T.DoubleType()).json(),
)
```

### Derived Metric: Root Mean Square

This derived metric computes the square root of the `squared_avg` aggregate metric. Because it references an existing metric rather than raw table data, it is defined as a derived metric. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

```python
MonitorMetric(
    type=MonitorMetricType.CUSTOM_METRIC_TYPE_DERIVED,
    name="root_mean_square",
    input_columns=["f1", "f2"],
    definition="sqrt(squared_avg)",
    output_data_type=T.StructField("output", T.DoubleType()).json(),
)
```

### Drift Metric: Error Rate Delta

This drift metric tracks the change in `weighted_error` between the current time window and a comparison window (either the baseline or the previous time window). The parameters `{{current_df}}` and `{{base_df}}` reference the metric values from the two windows. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]

```python
MonitorMetric(
    type=MonitorMetricType.CUSTOM_METRIC_TYPE_DRIFT,
    name="error_rate_delta",
    input_columns=[":table"],
    definition="{{current_df}}.weighted_error - {{base_df}}.weighted_error",
    output_data_type=T.StructField("output", T.DoubleType()).json(),
)
```

## Best Practices

- **Use derived and drift metrics where possible** to minimize recomputation over the full primary table. Only aggregate metrics require scanning the primary table; derived and drift metrics can be computed from existing aggregate values. ^[use-custom-metrics-with-data-profiling-databricks-on-aws.md]
- **Choose clear, descriptive metric names** that reflect the business meaning of the calculation, making it easier to interpret results in dashboards and alerts.
- **Validate the SQL template** in your definition parameter against the target table schema before attaching it to a profile, as the template cannot contain joins or subqueries.
- **Define the output data type accurately** to ensure proper storage and downstream query compatibility.

## Related Concepts

- [[Data Profiling]] — The core profiling framework that custom metrics extend
- Data Profiling Metric Tables — Where aggregate and drift metric values are stored
- [[Data Profiling Dashboard]] — The visualization layer that can display custom metric results
- [[Profile Alerts]] — Alerting on custom metric thresholds
- MonitorMetric API — The SDK API for defining custom metrics

## Sources

- data-profiling-databricks-on-aws.md
- use-custom-metrics-with-data-profiling-databricks-on-aws.md
```

# Citations

1. [use-custom-metrics-with-data-profiling-databricks-on-aws.md](/references/use-custom-metrics-with-data-profiling-databricks-on-aws-8de965f1.md)
