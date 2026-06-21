---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a49e47216c9f71d0eff92f90e6d380eca36b41b7884537a57034d61afa0e1e6d
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - accessing-the-data-profiling-dashboard
    - ATDPD
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Accessing the Data Profiling Dashboard
description: "Two methods to view the dashboard: via Catalog Explorer (Quality tab on the primary table) or via the Dashboards sidebar."
tags:
  - databricks
  - navigation
  - dashboard
  - unity-catalog
timestamp: "2026-06-19T09:44:15.869Z"
---

```markdown
# Accessing the Data Profiling Dashboard

The **Data Profiling Dashboard** is an automatically generated visual dashboard created whenever a profile is run in Databricks. It displays key metrics computed by the profile, organized by profile type into sections with tables and charts. The dashboard is built in your workspace and can be customized and shared like any other dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Viewing the Dashboard

You must use the same Databricks workspace where data profiling was enabled. There are two ways to open the dashboard:

- **From the Catalog Explorer UI:** In the left sidebar, click **Catalog** to open Catalog Explorer. Navigate to the primary table, click the **Quality** tab, then click **View dashboard**. ^[data-profiling-dashboard-databricks-on-aws.md]

- **From the Dashboards sidebar:** In the left sidebar, click **Dashboards**. The listing page shows dashboards you have access to, sorted in reverse chronological order by default. You can filter by name, last modified time period, or owner. ^[data-profiling-dashboard-databricks-on-aws.md]

## Refreshing the Dashboard

The metrics displayed on the dashboard are calculated by the profile run. To update the values, you must first trigger a profile refresh (using the [UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#refresh) or [API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api#refresh), or by scheduling a recurring profile run). You cannot refresh the metrics directly from the dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

The metric tables and the dashboard are updated separately. After a profile refresh, the metric tables are updated but the dashboard is not automatically refreshed. To see the new data in the dashboard, click the **Refresh** button on the dashboard itself. Conversely, clicking **Refresh** on the dashboard does not trigger a profile recalculation — it only re‑runs the queries over the existing metric tables. To bring in fresh data, you must refresh the profile first, then refresh the dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Selecting Data to Display

Use the widgets at the top of the dashboard to control which data is shown. The widgets available depend on the profile type:

- **Snapshot** analysis – specific filters appear.
- **Timeseries** analysis – different selectors appear.
- **InferenceLog** analysis – yet another set of selectors appears.

These widgets allow you to customize the date range, data slices, models, and other parameters. ^[data-profiling-dashboard-databricks-on-aws.md]

## Customization and Sharing

The dashboard is fully customizable. You can modify existing charts, add new ones, edit chart queries, and apply user‑editable parameters both at the dashboard level and per chart. For general guidance on using and customizing dashboards (including editing charts, viewing queries, and sharing), see the Dashboards documentation. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [[Data Profiling]] – The process that generates the metrics displayed on the dashboard.
- [[Unity Catalog]] – The governance system that manages data profiling monitors.
- [[Catalog Explorer]] – The UI for navigating tables and accessing the dashboard.
- Monitoring Dashboard – General concept of dashboards for data quality monitoring.

## Sources

- data-profiling-dashboard-databricks-on-aws.md
```

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
