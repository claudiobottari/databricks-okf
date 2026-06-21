---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f9772afe0fd8c327d56ac1d2aaeb7a7e5c385efeb876898f0146853ce909c2b
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - data-profiling-databricks
    - DP(
  citations:
    - file: data-profiling-databricks-on-aws.md
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data Profiling (Databricks)
description: A feature in Databricks that computes summary statistics for tables over time, enabling data quality monitoring, drift detection, and ML model performance tracking.
tags:
  - data-quality
  - databricks
  - monitoring
timestamp: "2026-06-19T18:06:51.114Z"
---

```yaml
---
title: Data Profiling (Databricks)
summary: A Databricks feature that computes summary statistics for tables over time, tracking data quality, distribution changes, drift, and ML model performance via profile metrics and dashboards.
sources:
  - data-profiling-databricks-on-aws.md
  - data-quality-monitoring-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:31:11.355Z"
updatedAt: "2026-06-19T14:42:44.423Z"
tags:
  - data-quality
  - databricks
  - monitoring
  - unity-catalog
aliases:
  - data-profiling-databricks
  - DP(
confidence: 0.95
provenanceState: merged
inferredParagraphs: 1
---

# Data Profiling (Databricks)

**Data profiling** in Databricks provides summary statistics for tables in Unity Catalog, computing profiling metrics over time so you can easily view historical trends. It is useful for in-depth monitoring of key metrics for selected tables, and can also be used to track the performance of machine learning models and model-serving endpoints by profiling inference tables that contain model inputs and predictions. ^[data-profiling-databricks-on-aws.md] Data profiling was formerly known as Lakehouse Monitoring. ^[data-quality-monitoring-databricks-on-aws.md]

## Why Use Data Profiling?

Quantitative metrics help you track and confirm the quality and consistency of your data over time. When changes in your table's data distribution or a corresponding model's performance are detected, the tables created by data profiling can capture and alert you to the change and help you identify the cause. ^[data-profiling-databricks-on-aws.md]

Data profiling helps answer questions such as:

- What does data integrity look like, and how does it change over time? For example, what is the fraction of null or zero values in the current data, and has it increased?
- What does the statistical distribution of the data look like, and how does it change over time? For example, what is the 90th percentile of a numerical column, or the distribution of values in a categorical column?
- Is there drift between the current data and a known baseline, or between successive time windows of the data?
- What does the statistical distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?

Additionally, data profiling lets you control the time granularity of observations and set up custom metrics. ^[data-profiling-databricks-on-aws.md, data-quality-monitoring-databricks-on-aws.md]

## Requirements

- Your workspace must be enabled for Unity Catalog and you must have access to Databricks SQL.
- To enable data profiling, you must have the following privileges:
  - `USE CATALOG` on the catalog and `USE SCHEMA` on the schema containing the table.
  - `SELECT` on the table.
  - `MANAGE` on the catalog, schema, or table.

Data profiling uses serverless compute for jobs but does not require that your account be enabled for serverless compute. ^[data-profiling-databricks-on-aws.md]

## How Data Profiling Works

To profile a table, you create a profile attached to that table. To profile the performance of a machine learning model, you attach the profile to an inference table that holds the model's inputs and corresponding predictions. Data profiling provides three types of analysis: **time series**, **inference**, and **snapshot**. ^[data-profiling-databricks-on-aws.md]

### Primary Table and Baseline Table

In addition to the table to be profiled (the "primary table"), you can optionally specify a **baseline table** to use as a reference for measuring drift. The baseline table should contain a dataset that reflects the expected quality of the input data — in terms of statistical distributions, individual column distributions, missing values, and other characteristics — and the baseline table should match the schema of the profiled table. ^[data-profiling-databricks-on-aws.md]

For profiles using a **snapshot profile**, the baseline table should contain a snapshot where the distribution represents an acceptable quality standard. For **time series profiles**, the baseline should represent time windows with acceptable data distributions. For **inference profiles**, a good baseline choice is the data used to train or validate the model being profiled. ^[data-profiling-databricks-on-aws.md]

### Metric Tables and Dashboard

Profiling creates two metric tables and a dashboard. Metric values are computed for the entire table, and for the time windows and data subsets ("slices") that you specify when creating the profile. For inference analysis, metrics are computed for each model ID. ^[data-profiling-databricks-on-aws.md]

- The **profile metric table** contains summary statistics (see [profile metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#profile-metrics-table)).
- The **drift metrics table** contains statistics related to the data's drift over time (see [drift metrics table schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-output#drift-metrics-table)).

Both metric tables are [[Delta Lake Table|Delta Tables]] stored in a Unity Catalog schema that you specify. You can view these tables using the Databricks UI, query them using Databricks SQL, and create dashboards and alerts based on them. For each profile, Databricks automatically creates a customizable dashboard. ^[data-profiling-databricks-on-aws.md]

## Types of Profiles

### Snapshot Profile

The snapshot analysis type computes metrics once against the entire primary table. The maximum table size for a snapshot profile is 4TB. For larger tables, use time series profiles instead. ^[data-profiling-databricks-on-aws.md]

### Time Series Profile

The time series analysis type computes metrics over time windows, enabling historical trend analysis. It only computes metrics over the last 30 days. ^[data-profiling-databricks-on-aws.md]

### Inference Profile

The inference analysis type profiles inference tables containing model inputs and predictions, enabling tracking of ML model performance and drift over time. ^[data-profiling-databricks-on-aws.md]

## Limitations

- Only Delta tables are supported for profiling. The table must be a managed table, external table, view, materialized view, or streaming table.
- Profiles created over materialized views do not support incremental processing.
- Not all regions are supported. See the column **Data profiling** in the table [AI and machine learning features availability](https://docs.databricks.com/aws/en/resources/feature-region-support#ai-aws).
- Profiles created using time series or inference analysis modes only compute metrics over the last 30 days.
- The maximum table size for a snapshot profile is 4TB. For larger tables, use time series profiles instead.

^[data-profiling-databricks-on-aws.md]

## Relationship to Anomaly Detection

Data profiling is one of two capabilities within Databricks' broader [[Data Quality Monitoring]] framework. The other capability is **anomaly detection**, which provides scalable, one-click monitoring of all tables in a schema by analyzing freshness and completeness. While anomaly detection is designed for broad, automated scanning, data profiling is intended for in-depth, manual analysis of specific tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Getting Started

- Create a Profile Using the UI
- Create a Profile Using the API
- Data Profiling Metric Tables
- [[Data Profiling Dashboard]]
- [[Profile Alerts]]
- [[Custom Metrics in Data Profiling|Custom Metrics with Data Profiling]]
- [[Production ML Monitoring with Inference Tables|Monitoring Served Models with Inference Tables]]
- [[Fairness and Bias Monitoring for Classification Models|Monitoring Fairness and Bias for Classification Models]]
- Data Profiling API Reference

## Related Concepts

- [[Unity Catalog]] — The governance layer that enables data profiling
- [[Data Quality Monitoring]] — Broader framework that includes profiling and anomaly detection
- [[Anomaly Detection (Databricks)]] — The complementary monitoring capability for freshness and completeness
- MLflow Models — Models whose performance can be tracked via inference profiles
- [[Delta Lake Table|Delta Tables]] — The table format required for profiling
- Databricks SQL — Used to query metric tables and create alerts

## Sources

- data-profiling-databricks-on-aws.md
- data-quality-monitoring-databricks-on-aws.md
```

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
2. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
