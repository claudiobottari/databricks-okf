---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac22a9358071cbc21b0968405aa3461d96284ffe0b5f2ca0e2539ded53d5e369
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-data-profiling-dashboard
    - DDPD
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Databricks Data Profiling Dashboard
description: An automatically generated, customizable dashboard in Databricks that visualizes profiling metric and drift results.
tags:
  - databricks
  - visualization
  - monitoring
timestamp: "2026-06-19T18:07:12.381Z"
---

# Databricks Data Profiling Dashboard

**Databricks Data Profiling Dashboard** is an automatically generated visualization tool that presents the results of [data profiling](data-profiling-databricks-on-aws.md) on a table. For each profile created, Databricks automatically creates a dashboard to help you visualize and present the profile results. The dashboard is fully customizable.^[data-profiling-databricks-on-aws.md]

## Overview

The data profiling dashboard is one of the three main outputs created when you profile a table, alongside two metric tables: the [profile metrics table](data-profiling-metric-tables-databricks-on-aws.md) and the [drift metrics table](data-profiling-metric-tables-databricks-on-aws.md).^[data-profiling-databricks-on-aws.md]

The dashboard provides a visual interface for monitoring key metrics over time, enabling you to track data quality trends and model performance for [inference tables](data-profiling-databricks-on-aws.md).

## Relationship to Metric Tables

Metric values are computed for the entire table, and for the time windows and data subsets (or "slices") that you specify when you create the profile. For inference analysis, metrics are computed for each model ID. The dashboard presents these metrics in a visual format, while the underlying metric tables are Delta tables stored in a Unity Catalog schema that you specify. You can view these tables using the Databricks UI, query them using Databricks SQL, and create dashboards and alerts based on them.^[data-profiling-databricks-on-aws.md]

## Customization

The dashboard is fully customizable, allowing you to tailor the visualizations to your specific monitoring needs. See the [Dashboards](https://docs.databricks.com/aws/en/dashboards/) documentation for more details on customization capabilities.^[data-profiling-databricks-on-aws.md]

## Use Cases

The data profiling dashboard helps you answer questions such as:

- What does data integrity look like, and how does it change over time?
- What does the statistical distribution of the data look like?
- Is there drift between the current data and a known baseline?
- How are ML model inputs and predictions shifting over time?
- How is model performance trending over time?^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) - The process of computing summary statistics for a table
- [Profile Metrics Table](/concepts/profile-metrics-table.md) - Stores summary statistics for each column, time window, and slice
- [Drift Metrics Table](/concepts/drift-metrics-table.md) - Stores statistics related to data drift over time
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) - Profiling of model-serving endpoints and inference tables
- Time Series Analysis - Continuous monitoring over time windows
- Snapshot Analysis - Point-in-time profiling

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
