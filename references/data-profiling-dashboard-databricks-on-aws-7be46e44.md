---
title: Data profiling dashboard | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-dashboard
ingestedAt: "2026-06-18T08:04:23.276Z"
---

This page describes the dashboard that is automatically created when a profile is run. For an introduction to data profiling, see [Data profiling](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/).

When a profile runs, it creates a dashboard that displays key metrics computed by the profile. The visualizations included in the default dashboard configuration depend on the profile type, and the different metrics are organized into sections. The left side of the dashboard shows lists of the metrics and statistics included in the tables and charts.

The dashboard has user-editable parameters for both the entire dashboard and for each chart, allowing you to customize the date range, data slices, models, and so on. You can also modify the charts shown or add new ones.

The dashboard is created in the user's account and is customizable and shareable like any dashboard. For general information about using and customizing dashboards, including adding new charts, editing charts, viewing queries, and so on, see [Dashboards](https://docs.databricks.com/aws/en/dashboards/).

## View the dashboard[​](#view-the-dashboard "Direct link to View the dashboard")

To view the data profiling dashboard, you must use the Databricks workspace from which data profiling was enabled. Do one of the following to view the dashboard:

*   In the left sidebar, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** to open the Catalog Explorer UI.
    
    In the catalog directory, navigate to the primary table. On the **Quality** tab, click **View dashboard**.
    
    ![Access dashboard from Catalog UI.](https://docs.databricks.com/aws/en/assets/images/dashboard-in-catalog-20190888cd8183a3f7595ababeb3b02b.png)
    
*   In the left sidebar, click ![Dashboard icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xIDEuNzVDMSAxLjMzNTc5IDEuMzM1NzkgMSAxLjc1IDFIMTQuMjVDMTQuNjY0MiAxIDE1IDEuMzM1NzkgMTUgMS43NVYxNC4yNUMxNSAxNC42NjQyIDE0LjY2NDIgMTUgMTQuMjUgMTVIMS43NUMxLjMzNTc5IDE1IDEgMTQuNjY0MiAxIDE0LjI1VjEuNzVaTTIuNSAxMC41VjEzLjVINy4yNVYxMC41SDIuNVpNMi41IDlINy4yNVYyLjVIMi41VjlaTTguNzUgMi41VjUuNUgxMy41VjIuNUg4Ljc1Wk04Ljc1IDEzLjVWN0gxMy41VjEzLjVIOC43NVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) **Dashboards**.
    
    By default, the dashboard listing page shows dashboards that you have access to sorted in reverse chronological order. To filter the list by name, type any part of the name into the search box. You can also filter by last modified within a time period, or by owner.
    
    ![Access dashboard from Dashboards on sidebar.](https://docs.databricks.com/aws/en/assets/images/dashboard-list-267c17cf62ba6d46c9c46c9ccf6d6564.png)
    

## Refresh the dashboard[​](#refresh-the-dashboard "Direct link to Refresh the dashboard")

The dashboard displays metrics that have been calculated by the profile. To refresh the values shown on the dashboard, you must trigger a profile refresh using [the UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#refresh) or [the API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api#refresh), or set up a scheduled run ([UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#schedule), [API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api#schedule)). You can't refresh the metrics from the dashboard. When you modify the dashboard, statistics aren't recalculated.

The metric tables and the dashboard generated by a profile are updated separately. When you trigger a profile refresh, the metric tables are updated, but the dashboard is not automatically updated. To update the data shown on the dashboard, click the **Refresh** button on the dashboard.

Similarly, when you click **Refresh** on the dashboard, it doesn't trigger profile calculations. Instead, it runs the queries over the metric tables that the dashboard uses to generate visualizations. To update the data in the tables used to create the visualizations that appear on the dashboard, you must refresh the profile and then refresh the dashboard.

## Select data to display[​](#select-data-to-display "Direct link to Select data to display")

Use the widgets at the top of the dashboard to control what data is included. The screenshot shows the filters for `Snapshot` analysis. For `Timeseries` and `InferenceLog` analysis, different selectors appear.

![Selectors on profile dashboard](https://docs.databricks.com/aws/en/assets/images/monitor-dashboard-selectors-0394efc531e52c1e65513c5355460bc7.png)
