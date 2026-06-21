---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 890c845aa9b341c55477a98433d7149e7b125d3ca703653989873b33bbbbdc08
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - freshness-data-quality-metric
    - F(QM
    - Freshness Metric
    - Freshness Metrics
    - quality metrics
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Freshness (data quality metric)
description: A metric measuring how recently a table has been updated, using historical commit analysis to predict expected next commit time and flagging tables as stale if commits are unusually late.
tags:
  - data-quality
  - monitoring
  - freshness
timestamp: "2026-06-19T17:32:53.538Z"
---

# Freshness (Data Quality Metric)

**Freshness** is a data quality metric used by [Anomaly Detection](/concepts/anomaly-detection.md) in Unity Catalog to measure how recently a table has been updated. It is one of the two core quality dimensions that anomaly detection evaluates, alongside [Completeness (data quality metric)](/concepts/completeness-data-quality-metric.md). ^[anomaly-detection-databricks-on-aws.md]

## How Freshness Is Measured

Freshness assesses the timeliness of data updates by analyzing the history of commits to a table. Anomaly detection builds a per-table statistical model that predicts the expected time of the next commit based on historical patterns. If a commit is unusually late—meaning the actual update time falls outside the model's predicted window—the table is marked as **stale**. ^[anomaly-detection-databricks-on-aws.md]

The measurement relies solely on commit history; it does not consider event-time columns or ingestion latency. Event-based freshness, which used event time columns, was available only in the older beta version of anomaly detection and is not supported in the current version. ^[anomaly-detection-databricks-on-aws.md]

## Relationship to Anomaly Detection

Freshness is a key part of the anomaly detection framework that Databricks runs as a background job on schemas where anomaly detection is enabled. The job monitors all tables in the schema and surfaces freshness health indicators in Catalog Explorer. Users with `SELECT` or `BROWSE` permissions can see the health status—**Healthy**, **Unhealthy**, or **Stale**—for each table. For details on the health indicator statuses, see [Health Indicators (Data Quality)](/concepts/health-indicators-databricks.md). ^[anomaly-detection-databricks-on-aws.md]

## Staleness Detection

A table is considered **stale** when its most recent commit has not occurred within the time window predicted by the historical model. The model is recalculated periodically as new commits arrive. Databricks uses intelligent scanning to prioritize high-impact tables (determined by popularity and downstream usage) and reduces scan frequency for less critical tables. Tables can also be manually excluded from monitoring using the Create Monitor or Update Monitor API with the `excluded_table_full_names` parameter. ^[anomaly-detection-databricks-on-aws.md]

## Viewing Freshness Results

Freshness results are visible in several places:

- **Catalog Explorer**: Health indicators appear on table and schema overview pages, showing a summary of table freshness.
- **Data Quality Monitoring UI**: After enabling anomaly detection, clicking **View results** opens a dashboard that lists unhealthy tables, along with root‑cause analysis where available. Recently resolved incidents (tables that recovered automatically) are displayed separately.
- **Table Quality Details**: Clicking on a table's health indicator opens detailed trend graphs showing predicted versus observed commit times over the last week.

For a metastore-wide view, account admins can import a pre-built Lakeview dashboard template that aggregates freshness and completeness results across all schemas. ^[anomaly-detection-databricks-on-aws.md]

## Configuring Freshness Thresholds (Legacy)

In the legacy anomaly detection system, users could customize freshness thresholds via job task parameters (e.g., `metric_configs` containing `FreshnessConfig`). Parameters included `table_latency_threshold_overrides`, `table_threshold_overrides`, and `static_table_threshold_override`. These configuration options are not available for new customers as of July 21, 2025. The current version automatically determines thresholds based on historical analysis. ^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Freshness detection does not apply to views or foreign tables.
- The metric considers only commit timing, not the content or schema of the update.
- Event-timestamp-based freshness is not supported in the current version.

^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The feature that evaluates freshness and completeness across a schema.
- [Completeness (data quality metric)](/concepts/completeness-data-quality-metric.md) — The companion metric measuring row counts and null percentages.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader system for tracking table health in Unity Catalog.
- [Health Indicators (Data Quality)](/concepts/health-indicators-databricks.md) — Visual statuses shown in Catalog Explorer.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance platform where anomaly detection runs.
- System Tables — Storage location for anomaly detection results.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
