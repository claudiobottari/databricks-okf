---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b3b6858984cc59990d2ffa21f7d96feeb249b2317f37c3f18a0046240952e3e
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-freshness
    - data-freshness-anomaly-detection
    - DF(D
    - data-freshness-table-monitoring
    - DF(M
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data Freshness
description: A data quality metric measuring how recently a table has been updated, determined by analyzing commit history to predict next commit timing; tables are marked stale if commits are unusually late.
tags:
  - data-quality
  - freshness
  - monitoring
timestamp: "2026-06-19T14:44:09.088Z"
---

# Data Freshness

**Data Freshness** is a data quality metric that measures how recently a table has been updated. It is a key component of automated data quality monitoring, helping organizations detect when data becomes stale and may no longer be reliable for analysis or decision-making.

## Overview

Data freshness refers to the timeliness of data updates within a table. Monitoring freshness enables scalable data quality assessment by analyzing historical commit patterns to determine whether a table has been updated as expected. When a table's updates are unusually late, it is marked as stale, indicating a potential data quality issue. ^[data-quality-monitoring-databricks-on-aws.md]

## How Freshness Is Measured

Freshness is determined through anomaly detection that analyzes the history of commits to a table. The system builds a per-table model that predicts the expected time of the next commit based on historical patterns. If a commit does not occur within the expected timeframe, the table is flagged as stale. ^[data-quality-monitoring-databricks-on-aws.md]

This approach is adaptive — each table receives its own model based on its unique update patterns, rather than applying a fixed threshold across all tables. This allows the system to accommodate tables with different update frequencies, from real-time streaming tables to daily batch updates.

## Relationship to Completeness

Data freshness is one of two primary data quality dimensions monitored by anomaly detection systems, alongside [Data Completeness](/concepts/data-completeness.md). While freshness tracks whether updates occur on time, completeness tracks whether the expected number of rows are written during each update. Together, these metrics provide a comprehensive view of data pipeline health. ^[data-quality-monitoring-databricks-on-aws.md]

## Importance

Monitoring data freshness helps organizations maintain confidence in their data assets. Stale data can lead to incorrect analyses, outdated reports, and poor decision-making. Automated freshness monitoring reduces the need for manual checks and enables rapid detection of pipeline failures or delays. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Data Completeness](/concepts/data-completeness.md) — The other primary dimension of data quality monitoring, measuring whether expected row counts are met.
- [Anomaly Detection](/concepts/anomaly-detection.md) — The broader capability that includes freshness and completeness monitoring.
- [Data Profiling](/concepts/data-profiling.md) — A complementary approach that provides summary statistics and tracks distribution changes over time.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The overall framework for ensuring data asset quality.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where data quality monitoring is configured.

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
