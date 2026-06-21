---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1be4c165e1197cbcfd9972666df36a8590834b076cff76526c87232dd08ebcf0
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data Profiling
description: Summary statistics and historical metrics tracking for table data distributions, ML model performance, and inference endpoints; formerly known as Lakehouse Monitoring.
tags:
  - data-quality
  - profiling
  - monitoring
  - machine-learning
timestamp: "2026-06-18T11:32:12.558Z"
---

# Data Profiling

**Data profiling** is a capability of [Data Quality Monitoring](/concepts/data-quality-monitoring.md) in Unity Catalog that provides summary statistics of the data in a table. It captures historical metrics of a table's data distribution or a model's performance, which can be used for quick summary statistics and to monitor a table while sending alerts for changes. Data profiling was formerly known as **Lakehouse Monitoring**. ^[data-quality-monitoring-databricks-on-aws.md]

## Overview

Data profiling helps you answer questions about data integrity, statistical distributions, drift, and model performance. It allows you to control the time granularity of observations and set up custom metrics. Data profiling does not modify any tables it monitors, nor does it add overhead to any jobs that populate those tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Use Cases

Data profiling helps you answer questions such as:

- What does data integrity look like, and how does it change over time? For example, what is the fraction of null or zero values in the current data, and has it increased?
- What does the statistical distribution of the data look like, and how does it change over time? For example, what is the 90th percentile of a numerical column? Or, what is the distribution of values in a categorical column, and how does it differ from yesterday?
- Is there drift between the current data and a known baseline, or between successive time windows of the data?
- What does the statistical distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?

You can also use data profiling to track the performance of GenAI apps, ML models, and [model-serving endpoints](/concepts/model-serving-endpoint.md) by monitoring [Inference Tables](/concepts/inference-tables.md) that contain model inputs and predictions. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader framework that includes data profiling and anomaly detection.
- [Anomaly Detection](/concepts/anomaly-detection.md) — A complementary capability that monitors table freshness and completeness.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform where data profiling operates.
- [Inference Tables](/concepts/inference-tables.md) — Tables containing model inputs and predictions that can be monitored with data profiling.
- [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md) — The former name of data profiling.

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
