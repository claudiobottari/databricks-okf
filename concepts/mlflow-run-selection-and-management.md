---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2bb9f669031df5cf805ddd296be26023aa93d256b6a3e7d9ef49442e11164747
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-selection-and-management
    - Management and MLflow Run Selection
    - MRSAM
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Run Selection and Management
description: The ability to select, show/hide, delete, compare, and add/remove tags for individual runs within the MLflow experiment tracking UI.
tags:
  - mlflow
  - experiment-tracking
  - workflow
timestamp: "2026-06-19T14:18:55.799Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Selection and Management

**MLflow Run Selection and Management** refers to the set of tools and workflows available in the MLflow UI for choosing, organizing, filtering, and visualizing experiment runs. These features help users compare model performance, identify optimal hyperparameters, and manage the lifecycle of their machine learning experiments.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Overview

The MLflow chart view page displays a collection of charts comparing the runs of an experiment. Users can customize this page by selecting which runs to include, modifying existing charts, and creating new visualizations. All of these features are also available for models from the **Models** tab when using MLflow 3.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md] Additionally, MLflow metadata for experiments and runs is accessible in system tables, where Databricks SQL and the full lakehouse tooling can be used to further analyze experiment data.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

To display the chart view page, click the **Chart view** icon on the experiment details page. For information about the runs list page, see [View training results with MLflow runs](/concepts/filtering-and-sorting-mlflow-runs.md). To display runs from multiple experiments, see [Compare runs from multiple experiments](/concepts/comparing-runs-from-multiple-experiments.md).^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting Runs to Display

By default, charts show the most recent 10 runs. Users can adjust this count by clicking the show runs icon at the top of the runs list and selecting **first 10**, **first 20**, or **all runs**. Individual runs can be toggled on or off using the show/hide icons (colored dot for visible, grayed-out dot for hidden) next to each run in the list.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing Runs

To perform bulk actions, check the box to the left of one or more runs. Once runs are selected, buttons for **Delete**, **Compare**, and **Add tags** become available. Deleting removes runs from the experiment; Compare opens the run comparison page; Add tags allows adding or editing custom tags on the selected runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering Runs

Use the search field located to the right of the **Chart view** icon to filter runs based on parameter values, metric values, or tags. The filtering syntax follows MLflow’s search conventions and allows narrowing down the set of runs displayed in the charts.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md] For detailed filter options, see Filter runs in MLflow.

## Sorting Runs

To change the order in which runs appear on the charts, select a parameter from the **Sort** dropdown menu. Runs are then sorted by the chosen parameter (e.g., ascending or descending values of a metric).^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

Runs can be grouped by one or more parameter values using the **Group by** dropdown menu. This creates separate chart series for each group, making it easier to compare runs with different configurations side by side.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating New Visualizations

Users can add custom charts to the chart view by clicking **Add chart** and selecting a chart type from the dropdown menu. Available chart types include line charts, scatter plots, bar charts, and parallel coordinates plots.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

A parallel coordinates plot helps understand the effect of parameter settings on model performance and investigate relationships between parameters and metrics. To create one, select **Parallel coordinates** from the Add chart menu, then choose the parameters and metrics to include. The resulting plot highlights correlations; for example, in the sample plot, lower values for `max_depth` result in higher values for the metric `auc`.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Customizing Charts

Each chart includes a kebab menu (upper-right corner) with options to **Edit**, **Delete**, or **Download** the chart as an image. Charts can be moved or resized on the page, and can be enlarged to full screen. When hovering over lines or points in a chart, details for that run appear.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md)
- [MLflow runs](/concepts/mlflow-run.md)
- Compare runs
- [Logged Models](/concepts/logged-models.md)
- [MLflow System Tables](/concepts/mlflow-system-tables.md)

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
