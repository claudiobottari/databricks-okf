---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd883e7f316bda656d5e43e3d9d210b194e49ebcef25534835734437ebe20793
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managing-mlflow-runs
    - MMR
    - Training Runs
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Managing MLflow Runs
description: Capabilities to delete, compare, and tag MLflow runs from the chart view interface for experiment organization.
tags:
  - mlflow
  - experiment-tracking
  - workflow
timestamp: "2026-06-18T14:40:18.564Z"
---

# Managing MLflow Runs

**Managing MLflow Runs** refers to the set of operations for organizing, filtering, sorting, comparing, and visualizing the runs logged to an [MLflow Experiment](/concepts/mlflow-experiment.md). The MLflow UI provides a chart view that enables you to inspect and compare runs, and to create custom visualizations for understanding parameter–metric relationships. With [MLflow 3](/concepts/mlflow-3.md), these same visualization features are also available for models from the **Models** tab.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

MLflow metadata for experiments and runs is also exposed in System Tables, allowing you to use Databricks SQL and other lakehouse tooling to query and visualize experiment data programmatically.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Chart View Overview

To access the chart view, click the **Chart view** icon on the experiment details page. By default, charts display the most recent 10 runs. Hovering over a line on a chart reveals run details. You can move, resize, or enlarge a chart to full screen; a kebab menu at the upper-right of each chart provides options to edit, delete, or download it.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting Runs to Display

At the top of the runs list, a show/hide menu lets you select how many runs to display (e.g., first 10, 20, or all runs). Runs shown on the charts are marked with a visible icon and a colored dot; hidden runs appear with a grayed-out dot.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing Runs

You can manage runs by checking the box to the left of one or more runs. When at least one run is selected, buttons appear for **Delete**, **Compare**, and **Add tags** operations. For details on the compare runs page, refer to the dedicated Compare Runs documentation.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering Runs

To filter runs, use the search field to the right of the **Chart view** icon. You can filter based on parameter or metric values, or by tag. See Filter Runs for more details.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sorting Runs

The sort order of runs in the charts is controlled by the **Sort** dropdown menu. You can select a parameter or metric to sort by.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

To group runs by parameter value, select one or more parameters from the **Group by** dropdown menu. This is useful for visually separating runs by different configurations.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating New Visualizations

To add a chart, click **Add chart** and choose a chart type from the dropdown menu. One specialized type is the **Parallel Coordinates** plot, which helps you explore the effect of multiple parameters on a metric. When creating a parallel coordinates plot, select the parameters and metrics of interest; the resulting chart highlights runs (often in black) that achieve higher metric values for certain parameter combinations.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

A parallel coordinates plot is useful for understanding how different parameter settings affect model performance and for investigating relationships between parameters and metrics. For example, runs with lower values of `max_depth` might correspond to higher `auc` values.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [MLflow Runs](/concepts/mlflow-run.md)
- Compare Runs
- Filter Runs
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md)
- [MLflow 3](/concepts/mlflow-3.md)
- System Tables
- Databricks SQL

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
