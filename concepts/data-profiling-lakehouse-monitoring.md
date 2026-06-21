---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a29f496af2771add87415cfb94c6c1388ece1b04076c31e8d4412db47d7f6ab
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-lakehouse-monitoring
    - DP(M
    - Data Profiling with Databricks Lakehouse Monitoring
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 14
      end: 22
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 10
      end: 22
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 12
      end: 13
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 36
      end: 37
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 24
      end: 34
    - file: data-quality-monitoring-databricks-on-aws.md
      start: 39
      end: 40
title: Data Profiling (Lakehouse Monitoring)
description: A feature that captures historical metrics of a table's data distribution or ML model performance, providing summary statistics, drift detection, and custom metrics to track data quality over time.
tags:
  - data-profiling
  - monitoring
  - machine-learning
timestamp: "2026-06-18T15:01:48.611Z"
---

---
title: Data Profiling (Lakehouse Monitoring)
summary: Data Profiling (formerly Lakehouse Monitoring) in Unity Catalog provides summary statistics for table data and inference tables, enabling tracking of data quality, drift, and ML model performance over time.
sources:
  - data-quality-monitoring-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:04:06.735Z"
updatedAt: "2026-06-18T08:04:06.735Z"
tags:
  - data-quality
  - monitoring
  - unity-catalog
  - mlflow
aliases:
  - lakehouse-monitoring
  - data-profiling-unity-catalog
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Data Profiling (Lakehouse Monitoring)

**Data Profiling** (formerly known as **Lakehouse Monitoring**) is a feature of [Unity Catalog](/concepts/unity-catalog.md) that provides quantitative measures to help track and confirm the quality and consistency of data over time. It captures historical metrics of a table's data distribution or corresponding model's performance, which can be used for quick summary statistics and to send alerts for changes. ^[data-quality-monitoring-databricks-on-aws.md:14-22]

Data profiling is part of Databricks' broader [Data Quality Monitoring](/concepts/data-quality-monitoring.md) capabilities, which also include [Anomaly Detection](/concepts/anomaly-detection.md). Unlike anomaly detection, which monitors table freshness and completeness, data profiling focuses on the statistical properties of the data and model behavior. ^[data-quality-monitoring-databricks-on-aws.md:10-22]

## Capabilities

Data profiling provides summary statistics about the data in a table. In addition, you can use it to track the performance of [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications, machine learning models, and model-serving endpoints by monitoring [Inference Tables](/concepts/inference-tables.md) that contain model inputs and predictions. ^[data-quality-monitoring-databricks-on-aws.md:12-13]

Data profiling lets you control the time granularity of observations and set up custom metrics. ^[data-quality-monitoring-databricks-on-aws.md:36-37]

## Use Cases

Data profiling helps you answer questions such as: ^[data-quality-monitoring-databricks-on-aws.md:24-34]

- What does data integrity look like, and how does it change over time? (e.g., fraction of null or zero values)
- What does the statistical distribution of the data look like, and how does it change over time? (e.g., 90th percentile of a numerical column, distribution of categorical values)
- Is there drift between current data and a known baseline, or between successive time windows?
- What does the distribution or drift of a subset or slice of data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time? Is model version A performing better than version B?

## Important Note

Data quality monitoring **does not** modify any tables it monitors, nor does it add overhead to any jobs that populate these tables. ^[data-quality-monitoring-databricks-on-aws.md:39-40]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — Monitors table freshness and completeness
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — Overall capability that includes both anomaly detection and data profiling
- [Inference Tables](/concepts/inference-tables.md) — Tables containing model inputs and predictions that can be profiled
- ML model monitoring — Tracking model performance over time
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that provides data profiling

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md:14-22](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
2. [data-quality-monitoring-databricks-on-aws.md:10-22](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
3. [data-quality-monitoring-databricks-on-aws.md:12-13](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
4. [data-quality-monitoring-databricks-on-aws.md:36-37](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
5. [data-quality-monitoring-databricks-on-aws.md:24-34](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
6. [data-quality-monitoring-databricks-on-aws.md:39-40](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
