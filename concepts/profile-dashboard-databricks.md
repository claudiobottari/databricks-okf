---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e84c3229f52bc46b1eaa365122e91aa34be7ec582c1b116181dc5349afb24612
  pageDirectory: concepts
  sources:
    - data-profiling-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-dashboard-databricks
    - PD(
    - Profile Dashboard
  citations:
    - file: data-profiling-databricks-on-aws.md
title: Profile Dashboard (Databricks)
description: An automatically generated, fully customizable dashboard in Databricks that visualizes data profiling results from profile and drift metric tables.
tags:
  - data-quality
  - databricks
  - visualization
  - dashboards
timestamp: "2026-06-19T14:43:00.839Z"
---

# Profile Dashboard (Databricks)

**Profile Dashboard (Databricks)** is an automatically generated, fully customizable visualization tool that displays the results of [Data Profiling](/concepts/data-profiling.md) for a table or inference table in Unity Catalog. It is part of the Databricks data quality monitoring system and provides an at-a-glance view of summary statistics, drift metrics, and historical trends for the profiled data.

## Overview

When a profile is created on a table or an inference table (for ML model performance monitoring), Databricks automatically generates a dashboard to help users visualize and present the profiling results. The dashboard is created in the same workspace and is fully customizable using the built-in dashboard editor. ^[data-profiling-databricks-on-aws.md]

The profile dashboard draws its data from two [Data profiling metric tables|metric tables](/concepts/databricks-data-profiling-metric-tables.md):
- **Profile metrics table** – contains summary statistics such as null fractions, percentile values, distribution summaries, and custom metrics.
- **Drift metrics table** – contains statistics related to data drift over time, including comparison against a baseline table if one is provided.

These metric tables are Delta tables stored in a Unity Catalog schema specified by the user. The dashboard queries these tables to render charts and visualizations. ^[data-profiling-databricks-on-aws.md]

## Purpose and Use Cases

The profile dashboard helps data engineers, data scientists, and ML practitioners answer questions such as:

- What is the fraction of null or zero values in a column, and how has it changed over time?
- What are the 90th percentile or other distribution statistics for numerical columns?
- How has the distribution of categorical values shifted compared to yesterday or against a baseline?
- For ML inference tables, how are model inputs and predictions shifting over time, and how does model version A compare to version B? ^[data-profiling-databricks-on-aws.md]

By surfacing these metrics in a visual dashboard, teams can quickly detect data quality regressions, drift, or model performance degradation and drill into the root cause.

## How It Works

The dashboard is created as part of the profile creation process. Users can create a profile via the Databricks UI, the API, or programmatically. The profile can be one of three analysis types:

- **Time series** – metrics computed over rolling time windows (covers the last 30 days for time series or inference profiles).
- **Snapshot** – a single-point analysis of the entire table (maximum table size 4 TB).
- **Inference** – metrics computed per model ID for inference tables.

Once the profile is set up, profiling metrics are computed on a schedule (serverless compute is used) and written to the metric tables. The dashboard automatically refreshes to reflect the latest data. ^[data-profiling-databricks-on-aws.md]

## Customization

The dashboard is fully customizable. Users can modify charts, add new visualizations, adjust time ranges, or filter by data slices and granularities. Custom metrics can also be defined and added to both the metric tables and the dashboard. ^[data-profiling-databricks-on-aws.md]

To customize the dashboard:
1. Open the dashboard from the profile’s UI page.
2. Use the dashboard editor to add, remove, or modify visualizations.
3. Save and publish changes.

## Limitations

- The dashboard only supports [Delta tables](/concepts/delta-lake-table.md) (managed tables, external tables, views, materialized views, or streaming tables).
- Profiles on materialized views do not support incremental processing.
- Time series and inference profiles compute metrics only over the last 30 days (adjustable by contacting Databricks account team).
- Snapshot profiles have a maximum table size of 4 TB.
- Not all regions support data profiling; see Databricks’ regional feature availability documentation. ^[data-profiling-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – the core feature that generates the metrics backing the dashboard.
- [Data profiling metric tables](/concepts/profile-metrics-table.md) – the schema and contents of the profile and drift metrics tables.
- [Profile Alerts](/concepts/profile-alerts.md) – set up alerting on threshold violations using the metric tables.
- Custom metrics – extend profiling with user-defined calculations.
- [Unity Catalog](/concepts/unity-catalog.md) – required [Catalog and Schema](/concepts/catalog-and-schema.md) for storing metric tables.
- Dashboards (Databricks) – general documentation for creating and editing dashboards.
- [Inference Tables](/concepts/inference-tables.md) – used for monitoring ML model serving performance via profiling.

## Sources

- data-profiling-databricks-on-aws.md

# Citations

1. [data-profiling-databricks-on-aws.md](/references/data-profiling-databricks-on-aws-79ffc4c7.md)
