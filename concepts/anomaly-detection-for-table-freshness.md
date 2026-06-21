---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65aaa712d5f29836999c84bc0f8075e61e35d3b6ca39362f777e53b5d4949095
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-for-table-freshness
    - ADFTF
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Anomaly Detection for Table Freshness
description: An intelligent scanning feature that predicts the expected time of the next table commit using historical patterns and marks a table as stale if a commit is unusually late.
tags:
  - anomaly-detection
  - freshness
  - data-monitoring
timestamp: "2026-06-18T15:01:41.849Z"
---

# Anomaly Detection for Table Freshness

**Anomaly Detection for Table Freshness** is a capability within [Data Quality Monitoring](/concepts/data-quality-monitoring.md) that automatically detects when a Unity Catalog table has not been updated as expected. It monitors enabled tables for freshness by analyzing the history of commits and building a per-table predictive model to forecast the next commit time. If a commit is unusually late, the table is flagged as stale. ^[data-quality-monitoring-databricks-on-aws.md]

## How It Works

Anomaly detection for freshness does not require manual threshold configuration. Instead, it analyzes the commit history of each monitored table and constructs a statistical model that predicts when the next commit should occur. This model accounts for the table's historical update pattern. When a table fails to receive a commit within the expected time window, it is marked as stale. ^[data-quality-monitoring-databricks-on-aws.md]

This approach is part of Databricks’ broader anomaly detection framework, which also monitors **completeness** (number of rows written in the last 24 hours). Freshness and completeness together provide a basic quality check for all enabled tables in a schema. ^[data-quality-monitoring-databricks-on-aws.md]

## Use Cases

- **Pipeline health monitoring**: Detect when a downstream table is not refreshed on schedule, allowing operators to investigate upstream failures.
- **SLA enforcement**: Automatically flag tables that violate freshness service-level agreements.
- **Data quality dashboards**: Surface stale tables in monitoring views without manual inspection.

## Relationship to Other Features

| Feature | Scope |
|---------|-------|
| Freshness anomaly | Time since last commit |
| Completeness anomaly | Row count in last 24 hours |
| Data profiling | Historical summary statistics and drift analysis |

[Data Profiling](/concepts/data-profiling.md) provides complementary quantitative measures (e.g., null fraction, distribution shifts) but does not replace the commit-history-based anomaly detection for freshness. ^[data-quality-monitoring-databricks-on-aws.md]

## Important Notes

Data quality monitoring **does not modify** any tables it monitors, nor does it add overhead to jobs that populate the tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Data Profiling](/concepts/data-profiling.md) (formerly Lakehouse Monitoring)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Anomaly Detection for Table Completeness](/concepts/anomaly-detection-for-table-completeness.md)
- [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md)

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
