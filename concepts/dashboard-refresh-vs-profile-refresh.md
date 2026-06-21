---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12f70422e47be642bbb8ad115c79f7c280b10fc2bef34744af21a8690966f5a2
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dashboard-refresh-vs-profile-refresh
    - DRVPR
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Dashboard Refresh vs Profile Refresh
description: A key architectural distinction in Databricks data profiling where the profile recalculation and the dashboard query are separate operations that must each be triggered independently.
tags:
  - databricks
  - data-profiling
  - dashboards
  - architecture
timestamp: "2026-06-19T18:06:27.255Z"
---

# Dashboard Refresh vs Profile Refresh

**Dashboard Refresh vs Profile Refresh** refers to the distinction between updating the visualizations on a data profiling dashboard and recalculating the underlying metric tables that feed those visualizations. On Databricks these two actions are performed by separate mechanisms and serve different purposes. ^[data-profiling-dashboard-databricks-on-aws.md]

## Overview

When a [Data Profiling](/concepts/data-profiling.md) run completes, it creates a dashboard that displays key computed metrics. The dashboard is separate from the [Profile Metrics Table](/concepts/profile-metrics-table.md) and [Drift Metrics Table](/concepts/drift-metrics-table.md) that store the raw statistics. Because the metrics are computed once during the profile run and then queried later, refreshing the dashboard and refreshing the profile have different effects. ^[data-profiling-dashboard-databricks-on-aws.md]

## Profile Refresh

A profile refresh recalculates all metrics by scanning the source data again. You can initiate a profile refresh through the [UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#refresh), the [API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api#refresh), or by setting up a scheduled run. A profile refresh updates the underlying metric tables, but it does **not** automatically update the dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Dashboard Refresh

Clicking the **Refresh** button on the dashboard **does not** trigger a profile recalculation. Instead, it re-runs the queries against the metric tables to fetch the latest computed values and regenerate the visualizations. The dashboard displays the metrics that were calculated by the most recent profile run. If no new profile refresh has occurred since the last dashboard refresh, the same data appears again. ^[data-profiling-dashboard-databricks-on-aws.md]

You cannot refresh the underlying metrics from the dashboard itself. Modifying charts or dashboard parameters also does not trigger metric recalculation. ^[data-profiling-dashboard-databricks-on-aws.md]

## Workflow Summary

To get updated data on the dashboard:

1. **Trigger a profile refresh** (using UI, API, or schedule) to recalculate metrics and update the metric tables.
2. **Refresh the dashboard** by clicking the dashboard’s **Refresh** button to re-query the metric tables and display the new values.

The metric tables and the dashboard are updated separately, and both steps are required for the dashboard to reflect fresh data. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) – The dashboard automatically created from a profile run.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for columns, time windows, and slices.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics tracking distribution changes over time.
- [Scheduling Profile Refreshes](/concepts/profile-refresh-and-scheduling.md) – Setting up automated profile runs via UI or API.
- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
