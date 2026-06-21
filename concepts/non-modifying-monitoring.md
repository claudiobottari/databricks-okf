---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2ad5b06141f009d8ebe26aae452bb2015b43c873eb5d997dbc72d35029eb6d1
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non-modifying-monitoring
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Non-modifying Monitoring
description: Design principle stating that data quality monitoring does not modify any tables it monitors nor adds overhead to jobs that populate those tables.
tags:
  - data-quality
  - architecture
  - design-principle
timestamp: "2026-06-18T11:32:30.998Z"
---

# Non-modifying Monitoring

**Non-modifying Monitoring** refers to data quality monitoring capabilities in [Unity Catalog](/concepts/unity-catalog.md) that observe and assess data assets without altering the underlying tables or adding performance overhead to the jobs that populate them.^[data-quality-monitoring-databricks-on-aws.md]

## Overview

Non-modifying monitoring provides observability into data quality without changing the data itself. It includes two primary capabilities: [Anomaly Detection](/concepts/anomaly-detection.md) and [Data Profiling](/concepts/data-profiling.md). Neither capability modifies the tables it monitors, nor does it add overhead to any jobs that populate those tables.^[data-quality-monitoring-databricks-on-aws.md]

### Why use anomaly detection?

Anomaly detection monitors enabled tables for **freshness** and **completeness**, providing confidence in data quality without requiring modifications to the data pipeline.^[data-quality-monitoring-databricks-on-aws.md]

**Freshness** refers to how recently a table has been updated. Anomaly detection analyzes the history of commits to a table and builds a per-table model to predict the time of the next commit. If a commit is unusually late, the table is marked as stale.^[data-quality-monitoring-databricks-on-aws.md]

**Completeness** refers to the number of rows expected to be written to the table in the last 24 hours. Anomaly detection analyzes the historical row count, and based on this data, predicts a range of expected number of rows. If the number of rows committed over the last 24 hours is less than the lower bound of this range, a table is marked as incomplete.^[data-quality-monitoring-databricks-on-aws.md]

### Why use data profiling?

Data profiling provides quantitative measures that help track and confirm the quality and consistency of data over time. It captures historical metrics of a table's data distribution or corresponding model's performance, which can be used for quick summary statistics. You can use these metrics to monitor a table and send alerts for changes.^[data-quality-monitoring-databricks-on-aws.md]

Data profiling helps answer questions like:
- What does data integrity look like, and how does it change over time?
- What is the statistical distribution of the data, and how does it change over time?
- Is there drift between the current data and a known baseline, or between successive time windows?
- What does the statistical distribution or drift of a subset or slice of the data look like?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time?

Data profiling also lets you control the time granularity of observations and set up custom metrics.^[data-quality-monitoring-databricks-on-aws.md]

## Design Principles

Non-modifying monitoring operates on two key principles:

1. **No data alteration**: The monitoring system does not modify any tables it observes. All analysis is performed on existing data without changing its content or structure.
2. **No pipeline overhead**: The monitoring does not add overhead to jobs that populate monitored tables. It operates independently of the data ingestion and transformation processes.^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — Scalable data quality monitoring with one click
- [Data Profiling](/concepts/data-profiling.md) — Summary statistics and historical metrics for data quality
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer providing these capabilities
- [Data quality](/concepts/data-quality-monitoring.md) — The broader discipline of ensuring data meets quality standards

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
