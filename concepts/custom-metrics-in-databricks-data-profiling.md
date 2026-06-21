---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2880248258ff0efaa7bdca1ef4861cf067d58a0bb1071aacd28d57f2de75b65d
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-metrics-in-databricks-data-profiling
    - CMIDDP
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Custom Metrics in Databricks Data Profiling
description: User-defined SQL-based metrics (Aggregate, Derived, or Drift) that appear alongside built-in metrics in profiling output tables for specialized data quality analysis.
tags:
  - data-quality
  - custom-metrics
  - sql
timestamp: "2026-06-18T14:47:50.517Z"
---

# Custom Metrics in Databricks Data Profiling

**Custom Metrics** in Databricks Data Profiling allow users to define user-defined calculations that extend the built-in profiling metrics. These metrics are computed during each profiling run and appear alongside standard metrics in the resulting metric tables, enabling teams to capture domain-specific statistics that are not covered by the default profiling output. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Overview

When configuring a data profile — whether through the Databricks UI or the API — users can add custom metrics to capture additional analytical dimensions. Custom metrics are evaluated for each profiling run and are stored in the same metric tables as the built-in metrics, making them queryable through notebooks, SQL query explorer, and Catalog Explorer. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Configuration

Custom metrics are configured in the **Advanced options** section of the **Data Quality Monitoring** dialog. To add a custom metric, click **Add custom metric** and provide the following parameters: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

- **Name**: A unique identifier for the custom metric.
- **Type**: The category of the metric (see below).
- **Input columns**: The columns to which the metric calculation is applied.
- **Output type**: The Spark data type of the metric's result.
- **Definition**: SQL code that defines the custom metric calculation.

## Custom Metric Types

### Aggregate

Aggregate custom metrics compute a single summary value across a set of input columns. They are computed per window or slice of data and can be used to calculate statistics such as sums, means, or any user-defined aggregation. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Derived

Derived custom metrics compute new values based on existing metrics or columns. These allow users to define ratios, transformations, or composite calculations that depend on other profiling outputs. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

### Drift

Drift custom metrics measure changes in data distributions or statistics over time or between a baseline and the current dataset. These are particularly useful for monitoring [data drift](/concepts/data-drift-detection.md) in production pipelines and [Inference profiles](/concepts/inference-profile.md). ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Definition Syntax

Custom metric definitions are written in SQL. The definition accepts the input columns selected and must return a value matching the specified output type. For example, a custom aggregate metric to calculate the null percentage of a column might be defined as: ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

```sql
SUM(CASE WHEN col IS NULL THEN 1 ELSE 0 END) / COUNT(*) * 100
```

## Integration with Slicing Expressions

Custom metrics work in conjunction with [Metric Slicing Expressions](/concepts/metric-slicing-expressions.md). When slicing expressions are defined, custom metrics are computed for each slice independently, allowing users to track custom calculations across different subsets of data. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Accessing Custom Metric Results

After a profiling run completes, custom metrics are stored in the profile's metric tables, which are [Unity Catalog](/concepts/unity-catalog.md) tables. Users can query these tables directly using SQL or view them in Catalog Explorer, and they can be incorporated into dashboards and alerts. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Best Practices

- Use descriptive names that clearly indicate the metric's purpose.
- Ensure the SQL definition is compatible with the selected output Spark data type.
- Test custom metric definitions on sample data before adding them to production profiles.
- Consider the computation cost of complex custom metrics, particularly for large tables or frequent refresh schedules.

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The overall profiling framework
- [Metric Slicing Expressions](/concepts/metric-slicing-expressions.md) – Subsetting data for per-segment profiling
- [Profile Types (TimeSeries, Inference)](/concepts/databricks-profile-types-snapshot-timeseries-inferencelog.md) – Contexts where custom metrics are computed
- Monitor Metric Tables – Where custom metric results are stored
- Data Drift – A common use case for Drift-type custom metrics

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
