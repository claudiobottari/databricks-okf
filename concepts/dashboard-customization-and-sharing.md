---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b29f5cb180a61765c537e84ce6cd095b63b92b3e397d98de1638d31e469ce4b
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dashboard-customization-and-sharing
    - sharing and Dashboard customization
    - DCAS
    - Dashboard Customization
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Dashboard customization and sharing
description: The ability to edit, add new charts, modify parameters, and share the data profiling dashboard like any other Databricks dashboard.
tags:
  - databricks
  - dashboard
  - customization
  - sharing
timestamp: "2026-06-18T15:00:31.839Z"
---

# Dashboard Customization and Sharing

The **dashboard customization and sharing** feature in Databricks allows users to tailor the automatically generated data profiling dashboard to their specific needs and share it with others. The dashboard is created in the user's account when a profile runs and is fully customizable and shareable like any other Databricks dashboard.^[data-profiling-dashboard-databricks-on-aws.md]

## Customization

The data profiling dashboard includes user-editable parameters for both the entire dashboard and for each individual chart. These parameters allow you to control the date range, data slices, models, and other aspects of the displayed metrics. You can also modify the charts shown or add new ones.^[data-profiling-dashboard-databricks-on-aws.md]

For general guidance on using and customizing dashboards—including adding new charts, editing existing charts, viewing underlying queries, and applying filters—refer to the Dashboards documentation.^[data-profiling-dashboard-databricks-on-aws.md]

## Sharing

The data profiling dashboard can be shared with other users in the same way as any other Databricks dashboard. This enables collaboration on data quality monitoring and allows teams to view and interact with the same profiling metrics.^[data-profiling-dashboard-databricks-on-aws.md]

## Viewing the Dashboard

To view a data profiling dashboard, use the Databricks workspace from which data profiling was enabled. You can access it through either the Catalog Explorer or the Dashboards sidebar:^[data-profiling-dashboard-databricks-on-aws.md]

- In the left sidebar, click **Catalog** to open Catalog Explorer, navigate to the primary table, select the **Quality** tab, and click **View dashboard**.
- In the left sidebar, click **Dashboards**, then filter or search for the desired dashboard by name, owner, or last modified time.

By default, the dashboard listing page shows dashboards you have access to sorted in reverse chronological order.^[data-profiling-dashboard-databricks-on-aws.md]

## Refreshing the Dashboard

The dashboard displays metrics calculated by a profile. To update the values shown, you must first trigger a profile refresh (via the UI or API, or by setting up a scheduled run). After the profile has recalculated its metrics, click the **Refresh** button on the dashboard to run the underlying queries and display the latest data. Refreshing the dashboard does not trigger profile calculations; it only updates the visualizations based on the current metric tables.^[data-profiling-dashboard-databricks-on-aws.md]

## Selecting Data to Display

Use the widgets at the top of the dashboard to control what data is included. The available selectors depend on the profile type (e.g., `Snapshot`, `Timeseries`, `InferenceLog`). For a `Snapshot` analysis, filters such as snapshot date or version may appear; for time-based profile types, date range and granularity selectors are provided.^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The process that generates the dashboard metrics.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The broader framework for monitoring table health.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for navigating tables and accessing the dashboard.
- Dashboards – General documentation for dashboard features.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
