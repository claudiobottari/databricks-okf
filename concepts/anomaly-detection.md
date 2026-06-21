---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c22200fccc908daf1ed9d136fdd2b3fc272671a5537ec9f34b57b9388f47f631
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Anomaly Detection
description: One-click scalable data quality monitoring that uses intelligent scanning to prioritize important tables, analyzing historical patterns to detect freshness and completeness issues.
tags:
  - data-quality
  - anomaly-detection
  - monitoring
timestamp: "2026-06-18T11:32:01.873Z"
---

#Anomaly Detection

**Anomaly detection** is a capability of Databricks [Data Quality Monitoring](/concepts/data-quality-monitoring.md) that enables scalable, one‑click monitoring of table freshness and completeness across all tables in a Unity Catalog schema. It uses intelligent scanning that prioritizes important tables and skips low‑impact ones, automatically assessing data quality by analyzing historical data patterns. ^[data-quality-monitoring-databricks-on-aws.md]

## How Anomaly Detection Works

Anomaly detection monitors two dimensions of data quality:

### Freshness

Freshness measures how recently a table has been updated. The system analyzes the history of commits to the table and builds a per‑table model to predict the time of the next commit. If a commit is unusually late compared to this prediction, the table is marked as stale. ^[data-quality-monitoring-databricks-on-aws.md]

### Completeness

Completeness measures the number of rows expected to be written to the table in the last 24 hours. Anomaly detection analyzes the historical row count and, based on this data, predicts a range of expected number of rows. If the number of rows committed over the last 24 hours is less than the lower bound of this range, the table is marked as incomplete. ^[data-quality-monitoring-databricks-on-aws.md]

## Benefits

- **Automated monitoring**: No manual thresholds or rule definitions are required; the system learns from historical patterns.
- **Scalable**: With one click, all tables in a schema are monitored, and intelligent scanning focuses on high‑impact tables.
- **Non‑intrusive**: Anomaly detection does not modify any tables it monitors nor adds overhead to jobs that populate them. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The broader framework that includes anomaly detection and data profiling.
- [Data Profiling](/concepts/data-profiling.md) – Provides summary statistics, drift detection, and custom metrics for tables and inference tables.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer where data quality monitoring is configured.

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
