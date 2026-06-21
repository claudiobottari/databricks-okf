---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 65037f18c0ac9bc74a25370c70252b6556ade56012a08ffc6186b85834eea847
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-databricks
    - DQM(
    - Data Quality Monitoring on Databricks
    - data-quality-monitoring-unity-catalog
    - DQM(C
    - Data Quality Monitoring in Unity Catalog
    - Data Quality Monitoring with Unity Catalog
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data quality monitoring (Databricks)
description: A Unity Catalog feature that ensures the quality of data assets through anomaly detection and data profiling capabilities.
tags:
  - data-governance
  - unity-catalog
  - databricks
timestamp: "2026-06-19T18:07:37.040Z"
---

# Data quality monitoring (Databricks)

**Data quality monitoring** on Databricks helps ensure the quality of all data assets in [Unity Catalog](/concepts/unity-catalog.md). It provides two complementary capabilities: **anomaly detection** for automated freshness and completeness checks, and **data profiling** for detailed statistical analysis and drift tracking. ^[data-quality-monitoring-databricks-on-aws.md]

Data quality monitoring does **not** modify any tables it monitors, nor does it add overhead to any jobs that populate those tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Anomaly detection

Anomaly detection enables scalable, one-click data quality monitoring. It monitors all tables in a schema using intelligent scanning that prioritizes important tables and skips low-impact ones. Databricks automatically assesses data quality by analyzing historical data patterns to evaluate each table's freshness and completeness. ^[data-quality-monitoring-databricks-on-aws.md]

**Freshness** refers to how recently a table has been updated. Anomaly detection analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale. ^[data-quality-monitoring-databricks-on-aws.md]

**Completeness** refers to the number of rows expected to be written to a table in the last 24 hours. Anomaly detection analyzes the historical row count and predicts a range of expected rows. If the number of rows committed over the last 24 hours falls below the lower bound of this range, the table is marked as incomplete. ^[data-quality-monitoring-databricks-on-aws.md]

## Data profiling

Data profiling (formerly known as Lakehouse Monitoring) provides quantitative measures to track and confirm data quality and consistency over time. It captures historical metrics of a table's data distribution or a corresponding model's performance, which can be used for quick summary statistics. These metrics can be used to monitor a table and send alerts for changes. ^[data-quality-monitoring-databricks-on-aws.md]

Data profiling helps answer questions such as:

- What does data integrity look like, and how does it change over time? (e.g., fraction of null or zero values)
- What does the statistical distribution look like, and how does it change over time? (e.g., 90th percentile of a numerical column, distribution of categorical values)
- Is there drift between current data and a known baseline, or between successive time windows?
- What does the statistical distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?

Data profiling also allows control over the time granularity of observations and supports custom metrics. ^[data-quality-monitoring-databricks-on-aws.md]

You can also use data profiling to track the performance of GenAI apps, machine learning models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions. ^[data-quality-monitoring-databricks-on-aws.md]

## Related concepts

- [Anomaly Detection (Databricks)](/concepts/anomaly-detection-databricks.md)
- [Data Profiling (Databricks)](/concepts/data-profiling-databricks.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Data Slicing](/concepts/data-slicing-expressions.md)
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- [Inference Log Analysis](/concepts/inferencelog-analysis.md)
- Time Series Analysis
- Snapshot Analysis

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
