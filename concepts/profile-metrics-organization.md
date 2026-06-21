---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e6acd313208524eea66689996150e27e7f9012e3f67d8fbf1de0b7339b4c944
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-metrics-organization
    - PMO
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Profile Metrics Organization
description: Metrics computed by a profile run are organized into sections on the dashboard, with lists of metrics and statistics shown in tables and charts on the left side.
tags:
  - databricks
  - data-profiling
  - metrics
  - visualization
timestamp: "2026-06-18T11:30:15.338Z"
---

# Profile Metrics Organization

**Profile Metrics Organization** describes how the [Data Profiling](/concepts/data-profiling.md) dashboard structurally groups and displays the metrics computed by a profile run. The dashboard automatically organizes key metrics into labeled sections, adapts its default visualizations to the profile type, and provides user-editable parameters for filtering and customizing the displayed data. ^[data-profiling-dashboard-databricks-on-aws.md]

## Dashboard Sections

When a profile runs, the dashboard presents metrics in clearly separated sections. The exact sections and charts shown depend on the profile type — **Snapshot**, **Timeseries**, or **InferenceLog** — because each type computes a different set of statistics. ^[data-profiling-dashboard-databricks-on-aws.md]

The left side of the dashboard displays a list of all metrics and statistics included in the tables and charts, giving users a quick overview of what data is available. ^[data-profiling-dashboard-databricks-on-aws.md]

## Customization

The dashboard supports two levels of user-editable parameters:

- **Dashboard-wide parameters** – Control global settings such as date range, data slices, and model selection.
- **Per-chart parameters** – Allow modifying individual chart configurations, including changing the chart type, adding new charts, or editing existing ones.

These parameters make the dashboard fully customizable and shareable like any other dashboard in Databricks. ^[data-profiling-dashboard-databricks-on-aws.md]

## Viewing the Dashboard

To view the profile metrics dashboard, use the Databricks workspace from which data profiling was enabled:

1. In the left sidebar, click **Catalog** to open the Catalog Explorer. Navigate to the primary table, select the **Quality** tab, and click **View dashboard**.
2. Alternatively, click **Dashboards** in the sidebar and search for the dashboard by name or filter by owner or last modified time. By default, dashboards are sorted in reverse chronological order.

^[data-profiling-dashboard-databricks-on-aws.md]

## Refreshing Dashboard Data

The dashboard displays metrics that have already been calculated by a profile run. To refresh the values shown, you must first trigger a profile refresh (via the UI or API, or by setting a schedule), then click the **Refresh** button on the dashboard. The dashboard’s refresh runs queries over the metric tables; it does not recalculate the profile metrics themselves. Similarly, refreshing the profile does not automatically update the dashboard — both steps are required. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The feature that generates the metrics displayed in the dashboard
- Dashboard — General documentation for customizing and sharing Databricks dashboards
- [Catalog Explorer](/concepts/catalog-explorer.md) — The UI for navigating Unity Catalog and accessing profile details
- Profile Types — Snapshot, Timeseries, and InferenceLog analyses that affect dashboard content
- Create Monitor — How to enable data profiling and schedule profile runs

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
