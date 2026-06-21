---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c9c7446d2a8ed53145ad20e61567c8ea405dd4aa507bfd2683c0c567c701caa
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-completeness-table-monitoring
    - DC(M
    - Completeness (Table Monitoring)
    - completeness monitoring
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data Completeness (Table Monitoring)
description: A monitoring metric that tracks the expected number of rows written to a table in a 24-hour window; tables are marked incomplete if row commits fall below the predicted lower bound.
tags:
  - monitoring
  - data-quality
  - completeness
timestamp: "2026-06-19T09:46:02.353Z"
---

# Data Completeness (Table Monitoring)

**Data completeness (table monitoring)** refers to the mechanism in Databricks data quality monitoring that detects when a table receives fewer rows than expected within a rolling 24‑hour window. It is one of two core checks provided by the anomaly detection engine, the other being data freshness. ^[data-quality-monitoring-databricks-on-aws.md]

## Overview

Completeness monitoring ensures that a table’s row count stays within a predicted healthy range. The anomaly detection system analyses the historical row count of each enabled table, builds a per‑table model, and produces a forecasted range of expected rows. If the number of rows committed in the last 24 hours falls below the lower bound of that range, the table is flagged as **incomplete**. ^[data-quality-monitoring-databricks-on-aws.md]

This check is part of Databricks’ broader [Data Quality Monitoring](/concepts/data-quality-monitoring.md) capability in [Unity Catalog](/concepts/unity-catalog.md). It runs automatically for all tables in a schema once anomaly detection is enabled, using intelligent scanning that prioritises important tables and skips low‑impact ones. ^[data-quality-monitoring-databricks-on-aws.md]

## How it works

- Historical analysis: The system collects the historical commit frequency and row‑count patterns for each table. ^[data-quality-monitoring-databricks-on-aws.md]
- Model building: A per‑table statistical model predicts the expected number of rows in the next 24‑hour window and computes a plausible range. ^[data-quality-monitoring-databricks-on-aws.md]
- Alerting: When actual commits in the last 24 hours are less than the predicted lower bound, the table is marked as incomplete. This typically triggers an alert so that data owners can investigate. ^[data-quality-monitoring-databricks-on-aws.md]

Completeness and [freshness](/concepts/data-freshness-table-monitoring.md) work together: freshness tracks how recently a table was updated, while completeness checks whether enough rows were written. Both can be enabled with a single click and require no manual threshold tuning. ^[data-quality-monitoring-databricks-on-aws.md]

## Benefits

- **No overhead**: Data quality monitoring does not modify any monitored tables nor add latency to the jobs that populate them. ^[data-quality-monitoring-databricks-on-aws.md]
- **Scalable**: Intelligent scanning automatically focuses on high‑impact tables, reducing noise from tables where small variations are normal. ^[data-quality-monitoring-databricks-on-aws.md]
- **Proactive**: Teams are notified as soon as a table deviates from its expected row‑count pattern, allowing early investigation before downstream consumers are affected. ^[data-quality-monitoring-databricks-on-aws.md]

## Relationship to data profiling

[Data Profiling](/concepts/data-profiling.md) (formerly Lakehouse Monitoring) provides a different view of table quality: it captures summary statistics, null‑value ratios, distributional drift, and custom metrics at configurable time granularity. While data profiling answers “*what* does the data look like and how is it changing?”, completeness monitoring answers “*how much* data arrived and was it enough?”. Both are part of the same data quality monitoring suite and can be used together for a comprehensive view of table health. ^[data-quality-monitoring-databricks-on-aws.md]

## Related concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The engine that drives both freshness and completeness monitoring.
- [Data Freshness (Table Monitoring)](/concepts/data-freshness-table-monitoring.md) – The complementary check for timely updates.
- [Data Profiling](/concepts/data-profiling.md) – Historical statistical summaries and drift analysis.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages monitored tables.

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
