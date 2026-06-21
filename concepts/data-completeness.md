---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3fb4ab94c2dee7bf2ec7ef228277dc74c9e1ad0188d1f49be3e7a1af13f13ec
  pageDirectory: concepts
  sources:
    - data-quality-monitoring-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-completeness
    - Completeness
    - completeness
    - data-completeness-anomaly-detection
    - DC(D
    - data-completeness-table-monitoring
    - DC(M
    - Completeness (Table Monitoring)
    - completeness monitoring
  citations:
    - file: data-quality-monitoring-databricks-on-aws.md
title: Data Completeness
description: A data quality metric measuring whether the expected number of rows were written to a table in the last 24 hours, based on historical row count analysis; tables are marked incomplete if row count falls below predicted lower bound.
tags:
  - data-quality
  - completeness
  - monitoring
timestamp: "2026-06-19T14:44:14.669Z"
---

# Data Completeness

**Data Completeness** is a quality metric in [Anomaly Detection](/concepts/anomaly-detection.md) that measures whether a table has received the expected number of rows over a recent time period. It is one of the two core dimensions tracked by Databricks’ data quality monitoring, alongside [Data Freshness](/concepts/data-freshness.md). ^[data-quality-monitoring-databricks-on-aws.md]

## Definition

Completeness refers to the number of rows expected to be written to a table in the last 24 hours. Anomaly detection analyzes the historical row count of the table and, based on that history, predicts a range of expected row counts. If the actual number of rows committed over the last 24 hours falls below the lower bound of that predicted range, the table is marked as **incomplete**. ^[data-quality-monitoring-databricks-on-aws.md]

## Relation to Anomaly Detection

Anomaly detection in [Unity Catalog](/concepts/unity-catalog.md) monitors enabled tables for both freshness and completeness. Freshness tracks the timeliness of updates (when a commit is expected), while completeness tracks the volume of data (how many rows are expected). Both models are built per table using historical data patterns. Anomaly detection automatically assesses these dimensions to help users maintain confidence in their data. ^[data-quality-monitoring-databricks-on-aws.md]

## Integration with Data Profiling

[Data Profiling](/concepts/data-profiling.md) (formerly Lakehouse Monitoring) provides summary statistics of table data and can track historical metrics over time. While data profiling captures distributions and custom metrics, the completeness check is part of the anomaly detection subsystem. Data quality monitoring—including completeness—**does not** modify any tables it monitors, nor does it add overhead to jobs that populate those tables. ^[data-quality-monitoring-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The overarching capability that includes completeness and freshness checks.
- [Data Freshness](/concepts/data-freshness.md) – The companion metric that measures how recently a table was updated.
- [Data Profiling](/concepts/data-profiling.md) – Quantitative measures for tracking data distribution and consistency over time.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer in which data quality monitoring operates.

## Sources

- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
