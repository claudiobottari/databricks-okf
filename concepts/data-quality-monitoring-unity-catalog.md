---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3fad53fd6a5143b9e8c13ed0bcae9a0eeac94366b4f204efeaf923c7786f0714
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring-unity-catalog
    - DQM(C
    - Data Quality Monitoring in Unity Catalog
    - Data Quality Monitoring with Unity Catalog
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data Quality Monitoring (Unity Catalog)
description: A Databricks capability in Unity Catalog that ensures data asset quality through anomaly detection and data profiling without modifying tables or adding job overhead.
tags:
  - data-governance
  - unity-catalog
  - data-quality
timestamp: "2026-06-18T15:01:48.060Z"
---

```markdown
---
title: Data Quality Monitoring (Unity Catalog)
summary: Databricks' capability in Unity Catalog to monitor and ensure the quality of data assets through anomaly detection and data profiling without modifying tables or adding job overhead.
sources:
  - data-quality-monitoring-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:32:01.010Z"
updatedAt: "2026-06-18T11:32:01.010Z"
tags:
  - data-quality
  - unity-catalog
  - databricks
aliases:
  - data-quality-monitoring-unity-catalog
  - DQM(UC)
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# Data Quality Monitoring (Unity Catalog)

**Data quality monitoring** in [[Unity Catalog]] helps you ensure the quality of all of your data assets by providing automated anomaly detection and data profiling capabilities. It is part of the broader governance framework that includes access control, lineage, auditing, and data discovery across your workspaces. ^[data-quality-monitoring-databricks-on-aws.md]

## Overview

Data quality monitoring includes two primary capabilities: **anomaly detection** and **data profiling** (formerly known as Lakehouse Monitoring). These features work together to provide both automated quality surveillance and deep statistical analysis of your data assets. ^[data-quality-monitoring-databricks-on-aws.md]

Data quality monitoring **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. It operates as a read-only observation layer on top of your existing data infrastructure. ^[data-quality-monitoring-databricks-on-aws.md]

## Anomaly Detection

Anomaly detection enables scalable data quality monitoring with one click. It monitors all tables in a schema using intelligent scanning that prioritizes important tables and skips low-impact ones. Databricks automatically assesses data quality by analyzing historical data patterns to evaluate each table's freshness and completeness. ^[data-quality-monitoring-databricks-on-aws.md]

### Freshness

**Freshness** refers to how recently a table has been updated. Anomaly detection analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale. ^[data-quality-monitoring-databricks-on-aws.md]

### Completeness

**Completeness** refers to the number of rows expected to be written to the table in the last 24 hours. Anomaly detection analyzes the historical row count, and based on this data, predicts a range of expected number of rows. If the number of rows committed over the last 24 hours is less than the lower bound of this range, a table is marked as incomplete. ^[data-quality-monitoring-databricks-on-aws.md]

## Data Profiling

Data profiling provides quantitative measures that help you track and confirm the quality and consistency of your data over time. Data profiling captures historical metrics of a table's data distribution or corresponding model's performance, which can be used for quick summary statistics. You can use these metrics to monitor a table and send alerts for changes. ^[data-quality-monitoring-databricks-on-aws.md]

Data profiling helps you answer questions like the following:

- What does data integrity look like, and how does it change over time? For example, what is the fraction of null or zero values in the current data, and has it increased?
- What does the statistical distribution of the data look like, and how does it change over time? For example, what is the 90th percentile of a numerical column? Or, what is the distribution of values in a categorical column, and how does it differ from yesterday?
- Is there drift between the current data and a known baseline, or between successive time windows of the data?
- What does the statistical distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?

In addition, data profiling lets you control the time granularity of observations and set up custom metrics. ^[data-quality-monitoring-databricks-on-aws.md]

### Use Cases for Data Profiling

Data profiling can also be used to track the performance of [[MLflow GenAI Evaluate API|GenAI]] apps, [[CI/CD for Machine Learning|machine learning]] models, and model-serving endpoints by monitoring inference tables that contain model inputs and predictions. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [[Unity Catalog]] — The unified governance layer that provides data quality monitoring capabilities
- [[Anomaly Detection]] — The specific capability for automated freshness and completeness monitoring
- [[Data Profiling]] — The specific capability for statistical analysis and drift detection
- [[MLflow GenAI Evaluate API|GenAI]] — Generative AI applications that can be monitored through inference table profiling
- [[CI/CD for Machine Learning|Machine Learning]] — ML models whose inputs, predictions, and performance can be tracked via data profiling
- [[Inference Tables]] — Tables containing model inputs and predictions used for monitoring

## Sources

- data-quality-monitoring-databricks-on-aws.md
```

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
