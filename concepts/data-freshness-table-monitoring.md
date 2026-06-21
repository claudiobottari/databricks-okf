---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b452eb23ae3243a381ced552da7f02bc3c71004d04ffc050b0b89fcddde2940
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-freshness-table-monitoring
    - DF(M
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data Freshness (Table Monitoring)
description: A monitoring metric that tracks how recently a table has been updated by analyzing commit history to predict the next commit time; tables are marked stale if a commit is unusually late.
tags:
  - monitoring
  - data-quality
  - freshness
timestamp: "2026-06-19T09:45:33.446Z"
---

# Data Freshness (Table Monitoring)

**Data Freshness** is a metric measured by [Anomaly Detection](/concepts/anomaly-detection.md) in [Unity Catalog](/concepts/unity-catalog.md) that indicates how recently a table has been updated. If a table’s last commit is unusually late relative to its historical pattern, the table is marked as stale. ^[data-quality-monitoring-databricks-on-aws.md]

## Definition

Freshness refers to the timeliness of data in a table. Anomaly detection monitors all enabled tables by analyzing the history of commits to each table and building a per-table model that predicts the expected time of the next commit. ^[data-quality-monitoring-databricks-on-aws.md]

## How It Works

1. **Historical analysis** – The system records the timestamp of every commit (write operation) on a table.
2. **Predictive model** – Based on the observed commit cadence, a model is built for each table to estimate when the next commit should occur.
3. **Staleness detection** – When the current time exceeds the predicted commit window without a new commit, the table is flagged as stale.

This process is fully automated and requires no manual threshold configuration. It is part of the broader anomaly detection capability that also monitors **completeness** (the expected number of rows written in a rolling 24-hour window). ^[data-quality-monitoring-databricks-on-aws.md]

## Why Use Freshness Monitoring

- **Confidence in data quality** – Knowing that tables are updated on schedule allows downstream consumers to trust the data.
- **Proactive alerting** – Teams can be notified when ingestion pipelines fall behind, enabling faster resolution.
- **Scalable oversight** – Databricks automatically prioritizes important tables using intelligent scanning, so low-impact tables are skipped, keeping monitoring efficient. ^[data-quality-monitoring-databricks-on-aws.md]

## Relationship to Data Quality Monitoring

Freshness monitoring is one of the two core anomaly detection features in [data quality monitoring](/concepts/data-quality-monitoring.md) (the other is completeness). Data quality monitoring also includes [Data Profiling](/concepts/data-profiling.md) for quantitative summaries and drift detection. Data quality monitoring **does not** modify any tables it monitors, nor does it add overhead to jobs that populate the tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Completeness (Table Monitoring)](/concepts/data-completeness-table-monitoring.md)
- [Data Profiling](/concepts/data-profiling.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
