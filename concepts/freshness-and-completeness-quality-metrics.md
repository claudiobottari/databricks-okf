---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 666e92375a8993015b4aa280f676d31ed224ebd33cdf41d9fa419d3da4939511
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - freshness-and-completeness-quality-metrics
    - Completeness Quality Metrics and Freshness
    - FACQM
    - Freshness Completeness Checks
    - Freshness and Completeness
    - Freshness and Completeness Checks
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Freshness and Completeness Quality Metrics
description: "Two core data quality dimensions: freshness measures how recently a table was updated compared to predicted commit patterns; completeness measures whether row counts fall within expected historical ranges over 24 hours."
tags:
  - data-quality
  - metrics
  - monitoring
timestamp: "2026-06-19T22:05:54.949Z"
---

# Freshness and Completeness Quality Metrics

**Freshness and Completeness Quality Metrics** are two core dimensions that Databricks [Anomaly Detection](/concepts/anomaly-detection.md) uses to evaluate the data quality of tables in a Unity Catalog schema. Based on historical patterns, the system builds per-table models and alerts when a table deviates from its expected update schedule (freshness) or expected row count (completeness). ^[anomaly-detection-databricks-on-aws.md]

## Freshness

Freshness measures how recently a table has been updated. Data quality monitoring analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as **stale**. ^[anomaly-detection-databricks-on-aws.md]

The freshness check only considers the timing of commits; it does not examine the data content. Event freshness, which was based on event time columns and ingestion latency, was available only during a beta version and is no longer supported. ^[anomaly-detection-databricks-on-aws.md]

## Completeness

Completeness refers to the number of rows expected to be written to a table in the last 24 hours. The monitoring system analyzes the historical row count and, based on that data, predicts a range of expected rows. If the number of rows committed over the last 24 hours falls below the lower bound of this range, the table is marked as **incomplete**. ^[anomaly-detection-databricks-on-aws.md]

The determination of completeness does **not** take into account metrics such as the fraction of nulls, zero values, or NaN. ^[anomaly-detection-databricks-on-aws.md]

### Percent null for completeness

**Percent null** adds additional quality detail to the completeness evaluation. It tracks the percentage of rows written to the table in the last 24 hours that are expected to have null values for a given column. Data quality monitoring analyzes the historical trend for each column and predicts a range. If the percent null for a column over the last 24 hours exceeds the upper bound of this range, the table is also marked as incomplete. ^[anomaly-detection-databricks-on-aws.md]

## Backtesting and scanning

When anomaly detection is first enabled on a schema, the system may run a backtest scan on historical data. For schemas enabled prior to September 24, 2025, the first scan checked quality as if monitoring had been running for two weeks. After that, each table is scanned automatically at the same frequency it is updated, using intelligent scanning that prioritizes high-impact tables. ^[anomaly-detection-databricks-on-aws.md]

## Health indicators

After a scan, [health indicators](/concepts/health-indicators-databricks.md) appear in Catalog Explorer for each table. The health summary reflects the results of both freshness and completeness checks. Tables that fail either check are marked as Unhealthy in the [Data Quality Monitoring](/concepts/data-quality-monitoring.md) dashboard. ^[anomaly-detection-databricks-on-aws.md]

## Legacy customization parameters

In the legacy version of anomaly detection, users could customize the freshness and completeness evaluations by editing job task parameters. The `metric_configs` JSON string allowed configuration of thresholds, tables to scan or skip, and other overrides. These customizations are no longer supported for new customers starting July 21, 2025. ^[anomaly-detection-databricks-on-aws.md]

### Freshness-specific parameters (legacy)

- `table_latency_threshold_overrides`: Override the allowed latency for specific tables.
- `event_timestamp_col_names`: Specify columns containing event timestamps (no longer used in the current version).

### Completeness-specific parameters (legacy)

- `static_table_threshold_override`: Define a static threshold for tables that rarely change.

## Limitations

- Freshness and completeness metrics are computed only for tables, not for views or foreign tables. ^[anomaly-detection-databricks-on-aws.md]
- The completeness metric does not incorporate null fractions, zero values, or NaN counts (though percent null is evaluated separately). ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The feature that uses these metrics.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Overall framework for tracking table quality.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI where health indicators appear.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where schemas are monitored.
- Serverless Compute – Required compute for anomaly detection.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
