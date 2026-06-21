---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9880f1ead6c3e089ed003b113e14f1853a03a7919498b8da2f76eedf423c4c6d
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lakehouse-monitoring
    - LakehouseMonitoring tag
    - Databricks Lakehouse Monitoring
    - lakehouse-monitoring-legacy-name
    - LM(N
    - Lakehouse Monitoring (former name)
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Lakehouse Monitoring
description: The former name for Data Profiling in Databricks Unity Catalog; now superseded by the data profiling capability within data quality monitoring.
tags:
  - legacy
  - data-quality
  - monitoring
  - databricks
timestamp: "2026-06-19T14:44:32.817Z"
---

```yaml
---
title: Lakehouse Monitoring
summary: The former name for Databricks' data profiling capability, now part of Data Quality Monitoring in Unity Catalog. Provides summary statistics, drift tracking, and anomaly detection for tables and inference logs.
sources:
  - data-quality-monitoring-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:04:06.735Z"
updatedAt: "2026-06-18T08:04:06.735Z"
tags:
  - databricks
  - data-quality
  - monitoring
  - lakehouse
  - unity-catalog
aliases:
  - data-profiling
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Lakehouse Monitoring

**Lakehouse Monitoring** is the former name for what is now called **data profiling** within Databricks’ Data Quality Monitoring feature in [[Unity Catalog]]. It provides automated, one‑click observability over the quality of data assets by capturing summary statistics, tracking drift, and detecting anomalies. ^[data-quality-monitoring-databricks-on-aws.md]

## Overview

Data quality monitoring in Unity Catalog offers two complementary capabilities: anomaly detection and data profiling. Data profiling was originally branded as Lakehouse Monitoring. The rename reflects its broader scope—profiling is no longer limited to monitoring but also supports tracking the performance of GenAI applications, machine learning models, and model‑serving endpoints via inference tables. ^[data-quality-monitoring-databricks-on-aws.md]

Lakehouse Monitoring (data profiling) captures historical metrics of a table’s data distribution or a model’s performance. These metrics can be used for quick summary statistics, trend analysis, and alerting on changes. ^[data-quality-monitoring-databricks-on-aws.md]

## Capabilities

Lakehouse Monitoring (as data profiling) helps answer questions such as:

- What is the fraction of null or zero values, and has it increased?
- What is the statistical distribution of the data (e.g., 90th percentile of a numerical column, value distribution of a categorical column)?
- Is there drift between current data and a known baseline, or between successive time windows?
- What is the statistical distribution of a specific subset or slice of the data?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending, and is version A performing better than version B?

Additionally, it allows control over the time granularity of observations and supports the creation of custom metrics. ^[data-quality-monitoring-databricks-on-aws.md]

## Key Features

- **Does not modify data**: Lakehouse Monitoring never alters the tables it monitors and does not add overhead to jobs that populate those tables. ^[data-quality-monitoring-databricks-on-aws.md]
- **Anomaly detection**: Built-in monitoring for table freshness and completeness using historical patterns. ^[data-quality-monitoring-databricks-on-aws.md]
- **Drift monitoring**: Tracks shifts in data distribution over time, with optional baseline comparison. ^[data-quality-monitoring-databricks-on-aws.md]
- **Custom metrics**: Users can define additional metrics beyond the defaults. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [[Data Quality Monitoring]] – The parent feature that includes anomaly detection and data profiling.
- [[Anomaly Detection]] – Monitors freshness and completeness of tables.
- [[Data Profiling]] – The current name for what was Lakehouse Monitoring.
- [[Unity Catalog]] – The [[metastore|Metastore]] that provides governance and monitoring capabilities.
- [[InferenceLog Analysis|Inference Log Analysis]] – Profiling applied to model inference logs.
- [[Drift Metrics Table]] – Stores statistics that track distribution changes over time.

## Sources

- data-quality-monitoring-databricks-on-aws.md
```

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
