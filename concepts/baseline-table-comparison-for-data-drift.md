---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 118cc1ecae02ea1ca1b8b47df3b2c6ed7248935f4876ecf0832d26236ba7314f
  pageDirectory: concepts
  sources:
    - profile-alerts-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - baseline-table-comparison-for-data-drift
    - BTCFDD
  citations:
    - file: profile-alerts-databricks-on-aws.md
title: Baseline Table Comparison for Data Drift
description: The practice of comparing current data distribution against a baseline table to detect statistical drift and trigger retraining of models.
tags:
  - databricks
  - data-quality
  - drift-detection
  - machine-learning
timestamp: "2026-06-19T19:57:52.819Z"
---

# Baseline Table Comparison for Data Drift

**Baseline Table Comparison for Data Drift** is a monitoring technique in Databricks [Data Profiling](/concepts/data-profiling.md) that compares the statistical properties of a production data profile against a static reference dataset — the baseline table — in order to detect distribution changes over time. When drift is detected against the baseline, it can trigger alerts for investigation or, in the case of [Inference Log Analysis](/concepts/inferencelog-analysis.md), signal that a machine learning model may need to be retrained. ^[profile-alerts-databricks-on-aws.md]

## How It Works

The baseline table is an optional, user-defined reference dataset that represents the expected data distribution for a monitored table. When a profile is configured to use a baseline table, the profiling system computes statistics for both the baseline and the current data, and the [Drift Metrics Table](/concepts/drift-metrics-table.md) stores statistics that quantify how the current distribution has changed relative to the baseline distribution. ^[profile-alerts-databricks-on-aws.md]

These drift metrics are stored alongside the regular profile metrics, making them directly queryable for alerting and analysis purposes. ^[profile-alerts-databricks-on-aws.md]

## Setting Up Alerts for Baseline Drift

You can create [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) based on drift metrics to be notified when data distribution changes relative to the baseline. This is particularly useful for:

- Detecting anomalous changes in data distributions that may affect downstream systems.
- Monitoring data quality over time against a known-good baseline.
- For `InferenceLog` analysis, receiving alerts that indicate a model should be retrained due to distribution shift between the baseline and current data.

To set up an alert:

1. Create a Databricks SQL Query against the drift metrics table or profile metrics table that compares current metrics to baseline metrics.
2. Create a Databricks SQL Alert for this query.
3. Configure the alert to evaluate at the desired frequency.
4. Set notification channels (email, webhook, Slack, PagerDuty, or other applications).
5. Ensure that any query parameters have default values that reflect the alert's intent, as alerts are based on default parameter values.

^[profile-alerts-databricks-on-aws.md]

## Relationship to Other Profiling Concepts

Baseline table comparison is one of several drift detection mechanisms available in Databricks data profiling. The [30-Day Lookback Window](/concepts/30-day-lookback-window.md) applies to time series and inference log profiles when no baseline is configured, providing a rolling historical comparison. When a baseline table is specified, the drift comparison is against that fixed reference rather than the rolling window. ^[profile-alerts-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The overall system for computing statistical summaries on Databricks tables.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) — Stores statistics that track distribution changes over time, including against a baseline.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) — Stores summary statistics for each column, time window, and slice.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) — A profile type where baseline drift can trigger model retraining signals.
- Time Series Analysis — A profile type for monitoring data over continuous time windows.
- [Data Slicing](/concepts/data-slicing-expressions.md) — Metrics are computed for data slices defined by slicing expressions.
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — The alerting infrastructure used to receive notifications based on query results.

## Sources

- profile-alerts-databricks-on-aws.md

# Citations

1. [profile-alerts-databricks-on-aws.md](/references/profile-alerts-databricks-on-aws-08d2e777.md)
