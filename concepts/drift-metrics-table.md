---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0bb9173432b714df0d458f60302d8eed63d5e41a6551f03c635c60edf870e97
  pageDirectory: concepts
  sources:
    - profile-alerts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - drift-metrics-table
    - DMT
  citations:
    - file: data-profiling-metric-tables-databricks-on-aws.md
    - file: profile-alerts-databricks-on-aws.md
title: Drift Metrics Table
description: A table that stores statistics tracking changes in data distribution over time, enabling alerts on data drift.
tags:
  - databricks
  - data-quality
  - monitoring
  - drift-detection
timestamp: "2026-06-19T19:58:08.903Z"
---

# Drift Metrics Table

The **Drift Metrics Table** is a Databricks metric table created by [Data Profiling](/concepts/data-profiling.md) runs that stores statistics tracking changes in data distribution over time. It enables visualization and alerting on data drift rather than static metric values. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Location

The drift metrics table is saved to `{output_schema}.{table_name}_drift_metrics`, where `{output_schema}` is the [Catalog and Schema](/concepts/catalog-and-schema.md) specified by the `output_schema_name` parameter and `{table_name}` is the name of the table being profiled. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Drift Types

The drift metrics table supports two types of drift comparison, recorded in the `drift_type` column: ^[data-profiling-metric-tables-databricks-on-aws.md]

- **Consecutive drift** compares a time window to the immediately preceding time window. This is only calculated if a consecutive time window exists after aggregation according to the specified granularities.
- **Baseline drift** compares a time window to a baseline distribution defined by a baseline table. This is only calculated if a baseline table is provided.

## Schema

The drift metrics table includes grouping columns such as time window (start and end), granularity (for `TimeSeries` and `InferenceLog` analysis only), log type (input table or baseline table), slice key and value, model ID (for `InferenceLog` analysis only), comparison time window (start and end), drift type, and version. ^[data-profiling-metric-tables-databricks-on-aws.md]

Numeric distribution statistics include `mean`, `stddev`, `min`, `max`, quantiles (array of 1000 values), `count`, `num_nulls`, `distinct_count`, and `frequent_items`. Where applicable, the table also includes the [population stability index](/concepts/population-stability-index-psi.md) (PSI) for categorical distributions. Where a metric is not applicable to a row, the corresponding cell is null. ^[data-profiling-metric-tables-databricks-on-aws.md]

The table is only generated if a baseline table is provided, or if a consecutive time window exists after aggregation according to the specified granularities. For `TimeSeries` or `InferenceLog` profiles, the profile looks back 30 days from the time the profile is created; due to this cutoff, the first analysis might include a partial window. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Population Stability Index (PSI)

The population stability index is a standard drift metric that quantifies how different two distributions are, with a range of [0, ∞): ^[data-profiling-metric-tables-databricks-on-aws.md]

- PSI < 0.1 indicates no significant population change.
- PSI < 0.2 indicates moderate population change.
- PSI >= 0.2 indicates significant population change.

## Use Cases

The drift metrics table can be queried directly to detect data changes and can be used to create [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md). Common use cases include: ^[profile-alerts-databricks-on-aws.md]

- Getting notified when a statistic moves out of a certain range.
- Getting notified of a change in data distribution (e.g., via consecutive drift).
- Getting notified if data has drifted in comparison to the baseline table, which can trigger investigation or, for `InferenceLog` analysis, indicate that the model should be retrained.

Alerts are created by building a Databricks SQL query on the drift metrics table and then configuring a [Databricks SQL alert](/concepts/databricks-sql-alerts.md) that evaluates the query at a desired frequency and sends notifications (email, webhook, Slack, PagerDuty, etc.). If the query uses parameters, the alert is based on the default values for those parameters. ^[profile-alerts-databricks-on-aws.md]

## Related Concepts

- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Data Profiling](/concepts/data-profiling.md)
- Data Drift
- [Baseline Table](/concepts/baseline-table.md)
- [InferenceLog Analysis](/concepts/inferencelog-analysis.md)
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md)
- Databricks SQL Query
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md)

## Sources

- data-profiling-metric-tables-databricks-on-aws.md
- profile-alerts-databricks-on-aws.md

# Citations

1. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
2. [profile-alerts-databricks-on-aws.md](/references/profile-alerts-databricks-on-aws-08d2e777.md)
