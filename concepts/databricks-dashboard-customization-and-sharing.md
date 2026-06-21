---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb3cf293de84924154fd94a7e57ad6b2e933e7b0babb4e69e99cc145916bdc64
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-dashboard-customization-and-sharing
    - Sharing and Databricks Dashboard Customization
    - DDCAS
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Databricks Dashboard Customization and Sharing
description: User-editable parameters for the entire dashboard and individual charts, allowing customization of date range, data slices, models, and modifications to charts.
tags:
  - databricks
  - dashboard
  - customization
  - collaboration
timestamp: "2026-06-19T09:44:21.351Z"
---

# Databricks Dashboard Customization and Sharing

**Databricks Dashboard Customization and Sharing** describes the ability to modify, personalize, and share the dashboard that is automatically created when a [Data Profiling](/concepts/data-profiling.md) run completes. This dashboard is a standard Databricks dashboard, offering the same editing, parameterization, and sharing features as any user-created dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Customization

The profiling dashboard includes user-editable parameters that apply to the entire dashboard or to individual charts. You can change the date range, filter data slices, switch models, or adjust other chart-specific controls. You can also modify the existing charts, add new charts, and view the underlying queries that generate the visualizations. ^[data-profiling-dashboard-databricks-on-aws.md]

Customizing the dashboard does **not** trigger a recalculation of the underlying profile metrics. To update the data shown after a profile refresh, you must click the **Refresh** button on the dashboard separately. ^[data-profiling-dashboard-databricks-on-aws.md]

## Sharing

The dashboard is shareable like any standard Databricks dashboard. You can grant access to other users or groups through the dashboard's sharing settings. For general sharing and collaboration features, see the Dashboards documentation. ^[data-profiling-dashboard-databricks-on-aws.md]

## Accessing the Dashboard

You can locate the dashboard from two places:

- **Catalog Explorer**: Navigate to the primary table, open the **Quality** tab, and click **View dashboard**.
- **Dashboards sidebar**: Click the Dashboard icon in the left sidebar. The dashboard listing shows your accessible dashboards sorted by last modified; you can filter by name, owner, or time period.

## Refresh Behavior

- The dashboard displays metrics that have been calculated by the profile. You **cannot** refresh the metrics from within the dashboard itself — you must initiate a profile refresh using the UI or API (or set up a scheduled run). ^[data-profiling-dashboard-databricks-on-aws.md]
- Profile refresh updates the metric tables, but the dashboard is **not** automatically updated. After a profile refresh, you must click **Refresh** on the dashboard to re-run the queries against the updated metric tables and show the new values. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md)
- [Unity Catalog Data Quality Monitoring](/concepts/unity-catalog-data-quality-monitoring.md)
- Dashboards
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
