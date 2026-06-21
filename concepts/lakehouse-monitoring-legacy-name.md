---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e7b992e0db81b180ade51ffa4d3ac1d0f01a9cfbd4dff9e2b2f4775c8019388
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakehouse-monitoring-legacy-name
    - LM(N
    - Lakehouse Monitoring (former name)
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Lakehouse Monitoring (Legacy Name)
description: The former name of the Data Profiling feature in Databricks Unity Catalog; used for tracking summary statistics and historical metrics of data tables.
tags:
  - legacy
  - data-profiling
  - databricks
timestamp: "2026-06-18T15:01:48.013Z"
---

# Lakehouse Monitoring (Legacy Name)

**Lakehouse Monitoring** was the original name for what is now called **data profiling** within Databricks' Data Quality Monitoring product. The name was changed when Databricks expanded the monitoring capabilities to include anomaly detection, making "Lakehouse Monitoring" a legacy term that refers specifically to the data profiling functionality. ^[data-quality-monitoring-databricks-on-aws.md]

## Relationship to Data Quality Monitoring

Data Quality Monitoring in Unity Catalog includes two main capabilities:

- **Anomaly detection** — Monitors tables for freshness and completeness using intelligent scanning that prioritizes important tables and skips low-impact ones. Databricks automatically assesses data quality by analyzing historical data patterns. ^[data-quality-monitoring-databricks-on-aws.md]
- **Data profiling** — Provides summary statistics of the data in a table. This was the feature formerly known as Lakehouse Monitoring. ^[data-quality-monitoring-databricks-on-aws.md]

Data profiling can also be used to track the performance of GenAI apps, machine learning models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions. ^[data-quality-monitoring-databricks-on-aws.md]

## Data Profiling Capabilities

Data profiling (formerly Lakehouse Monitoring) provides quantitative measures that help track and confirm data quality and consistency over time. It captures historical metrics of a table's data distribution or corresponding model's performance, which can be used for quick summary statistics. ^[data-quality-monitoring-databricks-on-aws.md]

### Questions Data Profiling Answers

Data profiling helps answer questions such as: ^[data-quality-monitoring-databricks-on-aws.md]

- What does data integrity look like, and how does it change over time? For example, what is the fraction of null or zero values in the current data, and has it increased?
- What does the statistical distribution of the data look like, and how does it change over time? For example, what is the 90th percentile of a numerical column, or what is the distribution of values in a categorical column?
- Is there drift between the current data and a known baseline, or between successive time windows of the data?
- What does the statistical distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?

### Additional Features

Data profiling also allows you to control the time granularity of observations and set up custom metrics. ^[data-quality-monitoring-databricks-on-aws.md]

## Important Note

Data quality monitoring — including both data profiling (formerly Lakehouse Monitoring) and anomaly detection — **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The parent product that encompasses both data profiling and anomaly detection
- [Anomaly Detection](/concepts/anomaly-detection.md) — Monitors tables for freshness and completeness
- [Data Profiling](/concepts/data-profiling.md) — The current name for the former Lakehouse Monitoring functionality
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where data quality monitoring operates
- [Inference Tables](/concepts/inference-tables.md) — Tables containing model inputs and predictions that can be monitored for performance tracking

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
