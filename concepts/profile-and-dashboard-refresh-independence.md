---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5265b1962b31d9fc2c1ceb9dd21e5517a37ddb79e6153fc94ca32915678b3f4
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-and-dashboard-refresh-independence
    - Dashboard Refresh Independence and Profile
    - PADRI
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Profile and Dashboard Refresh Independence
description: The mechanism by which profile metric tables and the profiling dashboard are updated independently — refreshing the profile updates metric tables but not the dashboard, and vice versa.
tags:
  - databricks
  - data-profiling
  - refresh
  - dashboard
timestamp: "2026-06-19T14:42:27.733Z"
---

# Profile and Dashboard Refresh Independence

**Profile and Dashboard Refresh Independence** refers to the design principle in Databricks data profiling where the underlying metric tables and the visual dashboard are updated by separate, independent actions. A profile refresh recalculates the metrics and writes them to tables, but does not automatically update the dashboard’s displayed values. Conversely, a dashboard refresh re-runs the queries against the metric tables to show the latest data, but does not trigger new profile calculations. Understanding this independence is essential for keeping profiling visualizations in sync with the most recent data. ^[data-profiling-dashboard-databricks-on-aws.md]

## How Profile Refresh Works

When you trigger a profile—either manually through the [UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#refresh) or the [API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api#refresh), or by setting up a [scheduled run](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#schedule)—the system computes key metrics (e.g., null counts, distributions, statistics) and writes them to metric tables. This action does **not** automatically update the dashboard that was created from the profile. The dashboard remains unchanged until its data source queries are re-executed. ^[data-profiling-dashboard-databricks-on-aws.md]

## How Dashboard Refresh Works

The dashboard is an independent artifact that displays the results of queries over the metric tables. It can be viewed in the **Dashboards** sidebar or from the **Catalog** UI, and it includes user-editable parameters for date range, data slices, and model selection. To update what the dashboard shows, you click the **Refresh** button on the dashboard itself. This action runs the underlying queries against the latest data in the metric tables, but it does **not** trigger a new profile computation. ^[data-profiling-dashboard-databricks-on-aws.md]

## The Independence Explained

The key point is that the metric tables and the dashboard are updated by separate operations:

- **Profile refresh** → updates metric tables.
- **Dashboard refresh** → re-runs queries over the existing metric tables.

Modifying the dashboard (e.g., adding or editing charts) does **not** cause statistics to be recalculated. You cannot refresh the metrics from the dashboard itself; that must be done by a profile refresh. ^[data-profiling-dashboard-databricks-on-aws.md]

Therefore, to see the most current profile data on the dashboard, you must perform **two sequential actions**:

1. Trigger a profile refresh to recompute the metrics into the metric tables.
2. Then click **Refresh** on the dashboard to re-run the queries and display the updated numbers.

If you only refresh the dashboard but not the profile, the visualizations will reflect the same (possibly stale) metrics that were already in the tables. If you only refresh the profile but not the dashboard, the dashboard will still show the old values until its queries are re-executed. ^[data-profiling-dashboard-databricks-on-aws.md]

## Best Practices

- After a scheduled or manual profile run, remember to refresh the dashboard to pick up the new metrics.
- If you are automating workflows, ensure that the dashboard refresh is called after the profile refresh completes (or use a trigger that refreshes the dashboard as a downstream step).
- Use the dashboard’s parameter widgets to filter data without needing to re-profile; profile and dashboard independence means you can explore existing results without recomputing them.

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The process of computing summary statistics and quality metrics for a table.
- Unity Catalog Monitors — The monitoring infrastructure that supports data profiling and quality alerts.
- [Dashboard Customization](/concepts/dashboard-customization-and-sharing.md) — How to edit, share, and add widgets to Databricks dashboards.
- Scheduled Profile Runs — Automating profile refreshes on a time-based schedule.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
