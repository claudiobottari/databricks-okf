---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1305256f1834f556b603b558625165bb61e0a58305f28704c34265f3f14ff16d
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - freshness-data-quality
    - F(Q
    - Freshness
    - freshness
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Freshness (data quality)
description: A data quality metric that measures how recently a table has been updated; anomaly detection builds a per-table model to predict next commit time and flags stale tables.
tags:
  - data-quality
  - monitoring
timestamp: "2026-06-19T18:08:11.876Z"
---

# Freshness (Data Quality)

**Freshness** is a data quality dimension monitored by [Anomaly Detection](/concepts/anomaly-detection.md) in [Unity Catalog](/concepts/unity-catalog.md). It measures how recently a table has been updated. Anomaly detection analyzes the history of commits to a table and builds a per‑table model to predict the time of the next commit. If a commit arrives unusually late — beyond the predicted window — the table is marked as **stale**. ^[data-quality-monitoring-databricks-on-aws.md]

Freshness is one of two core metrics that anomaly detection evaluates, alongside [Completeness (data quality)](/concepts/completeness-data-quality.md), which tracks expected row counts over the last 24 hours. Together they help data consumers and governance administrators quickly identify tables that may no longer be reliable for downstream analysis or production use. ^[data-quality-monitoring-databricks-on-aws.md]

## How Freshness Is Measured

The freshness check relies on historical commit patterns. Anomaly detection collects the commit history for each table, builds a statistical model of the intervals between successive commits, and predicts a lower and upper bound for when the next commit should occur. If no commit occurs within that predicted window, the system flags the table as stale. ^[data-quality-monitoring-databricks-on-aws.md]

Because the model is per‑table, it adapts to tables that are updated daily, hourly, or at irregular intervals. The analysis uses the commit log as its only input; no user‑supplied schedule is required. ^[data-quality-monitoring-databricks-on-aws.md]

## Relationship to Anomaly Detection

Freshness is evaluated as part of anomaly detection, a capability within [Data Quality Monitoring](/concepts/data-quality-monitoring.md). Anomaly detection monitors all tables in a schema using intelligent scanning that prioritizes important tables and skips low‑impact ones. Databricks automatically assesses data quality by analyzing historical data patterns to evaluate each table’s freshness and completeness. ^[data-quality-monitoring-databricks-on-aws.md]

Anomaly detection is designed to be a one‑click solution; after it is enabled on a schema, health indicators appear in the user interface (for details, see the [Anomaly Detection](/concepts/anomaly-detection.md) documentation). ^[data-quality-monitoring-databricks-on-aws.md]

## Additional Capabilities

In addition to anomaly detection, [Data Quality Monitoring](/concepts/data-quality-monitoring.md) also includes [Data Profiling](/concepts/data-profiling.md) (formerly known as Lakehouse Monitoring). Data profiling provides quantitative summary statistics of a table’s data distribution over time, supports custom metrics, and can track ML model inputs and predictions. Data quality monitoring **does not** modify any tables it monitors, nor does it add overhead to jobs that populate those tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — the parent capability that computes freshness scores
- [Completeness (data quality)](/concepts/completeness-data-quality.md) — the other core metric tracked alongside freshness
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — the broader framework for observing table health
- [Unity Catalog](/concepts/unity-catalog.md) — the governance solution that provides anomaly detection
- [Data Profiling](/concepts/data-profiling.md) — additional monitoring capability for summary statistics and drift

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
