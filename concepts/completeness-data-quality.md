---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 585f844608ca03ad6c71932fd72a40abd7808e068bca64234c011ac43387e0e8
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - completeness-data-quality
    - C(Q
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Completeness (data quality)
description: A data quality metric tracking expected row count over 24 hours; anomaly detection predicts a range and flags tables falling below the lower bound as incomplete.
tags:
  - data-quality
  - monitoring
timestamp: "2026-06-19T18:07:42.962Z"
---

# Completeness (Data Quality)

**Completeness** is a data quality dimension tracked by Databricks' anomaly detection feature in [Data Quality Monitoring](/concepts/data-quality-monitoring.md). It measures whether a table has received the expected number of new rows within a recent 24‑hour window. If the actual row count falls below the predicted lower bound, the table is flagged as incomplete. ^[data-quality-monitoring-databricks-on-aws.md]

## How Completeness is Measured

Anomaly detection analyzes the historical row-count pattern for each enabled table and builds a predictive model of the expected number of rows. The model outputs a range (a lower and upper bound) for the number of rows that should be committed every 24 hours. Completeness is assessed by comparing the actual row count over the last 24 hours against that range. ^[data-quality-monitoring-databricks-on-aws.md]

- **Complete**: The actual row count is within or above the predicted range.
- **Incomplete**: The actual row count is below the lower bound of the predicted range.

The table is marked as incomplete only when the 24-hour row count is less than the lower bound. Commits that are late or missing entirely affect the [Freshness (data quality)](/concepts/freshness-data-quality.md) dimension rather than completeness. ^[data-quality-monitoring-databricks-on-aws.md]

## Relationship to Anomaly Detection

Completeness is one of two built-in quality signals in anomaly detection, alongside freshness. Anomaly detection automatically enables both signals on every monitored table without manual configuration for each table. Monitoring is enabled at the **schema** level — turning on anomaly detection for a schema applies completeness and freshness checks to all tables in that schema. ^[data-quality-monitoring-databricks-on-aws.md]

The service uses intelligent scanning to automate table scan frequencies. Intelligent scanning prioritizes high-impact tables as determined by popularity and downstream usage, and reduces frequency for less critical tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Use Cases

- **Data pipeline monitoring**: Detect if a nightly batch job fails to deliver the expected number of records.
- **Incremental ingestion**: Validate that streaming or incremental loads are not losing data.
- **SLA enforcement**: Alert downstream consumers when a table's row count drops below a historically reliable threshold.

## Limitations

- The basic completeness check considers only row counts; it does not detect missing values within columns or structural changes (these are addressed by [Data Profiling](/concepts/data-profiling.md) and custom metrics). ^[data-quality-monitoring-databricks-on-aws.md]
- The 24-hour window is fixed by the anomaly detection system.
- Anomaly detection does not support views or foreign tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The overarching framework for tracking data asset quality.
- [Anomaly Detection](/concepts/anomaly-detection.md) — The feature that monitors freshness and completeness.
- [Freshness (data quality)](/concepts/freshness-data-quality.md) — The other anomaly detection signal, tracking the timeliness of commits.
- [Data Profiling](/concepts/data-profiling.md) — Provides summary statistics, distribution analysis, and custom metrics beyond row counts.

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
