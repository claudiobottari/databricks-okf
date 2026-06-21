---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d9baed1749fc3f3fac93954c4b5634459133d903832b69083f269debad4f1f1
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-data-quality-monitoring
    - UCDQM
    - Unity Catalog Quality Monitoring
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Unity Catalog Data Quality Monitoring
description: A capability in Unity Catalog that helps ensure the quality of data assets through anomaly detection and data profiling, without modifying tables or adding job overhead.
tags:
  - data-governance
  - unity-catalog
  - data-quality
timestamp: "2026-06-19T09:46:06.431Z"
---

Here is the wiki page for "Unity Catalog Data Quality Monitoring".

---

## Unity Catalog Data Quality Monitoring

**Unity Catalog Data Quality Monitoring** is a set of built-in capabilities within [Unity Catalog](/concepts/unity-catalog.md) that helps organizations assess and maintain the quality of their data assets. It provides automated anomaly detection for table freshness and completeness, as well as detailed data profiling to track statistical distributions and trends over time. ^[data-quality-monitoring-databricks-on-aws.md]

### Why Use Data Quality Monitoring?

To draw useful insights from data, users must have confidence in its quality. Data quality monitoring provides this confidence by offering two primary features: **anomaly detection** and **data profiling**. These features run entirely as a monitoring layer and do not modify any tables they monitor, nor do they add overhead to the jobs that populate those tables. ^[data-quality-monitoring-databricks-on-aws.md]

### Anomaly Detection

Anomaly detection enables scalable, one-click data quality monitoring. It monitors all tables in a schema using intelligent scanning that prioritizes important tables and skips low-impact ones. Databricks automatically assesses data quality by analyzing historical data patterns to evaluate each table's **freshness** and **completeness**. ^[data-quality-monitoring-databricks-on-aws.md]

- **Freshness** refers to how recently a table has been updated. Anomaly detection analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale. ^[data-quality-monitoring-databricks-on-aws.md]

- **Completeness** refers to the number of rows expected to be written to the table in the last 24 hours. Anomaly detection analyzes the historical row count and, based on this data, predicts a range of expected rows. If the number of rows committed over the last 24 hours is less than the lower bound of this range, the table is marked as incomplete. ^[data-quality-monitoring-databricks-on-aws.md]

### Data Profiling

Data profiling provides quantitative measures that help users track and confirm the quality and consistency of their data over time. It captures historical metrics of a table's data distribution or a corresponding model's performance, which can be used for quick summary statistics and to send alerts for changes. ^[data-quality-monitoring-databricks-on-aws.md]

Data profiling helps answer questions like the following: ^[data-quality-monitoring-databricks-on-aws.md]

- What does data integrity look like, and how does it change over time? (e.g., fraction of null or zero values)
- What does the statistical distribution of the data look like, and how does it change over time? (e.g., 90th percentile of a numerical column)
- Is there drift between the current data and a known baseline, or between successive time windows?
- What does the distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?

Data profiling also allows users to control the time granularity of observations and set up custom metrics. It can be used to track the performance of [GenAI](/concepts/mlflow-genai-evaluate-api.md) apps, machine learning models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions. ^[data-quality-monitoring-databricks-on-aws.md]

### Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Lakehouse Monitoring (former name)](/concepts/lakehouse-monitoring.md)
- [GenAI App Performance Monitoring](/concepts/performance-monitoring-with-mlflow-traces.md)
- MLflow Model Performance Monitoring

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
