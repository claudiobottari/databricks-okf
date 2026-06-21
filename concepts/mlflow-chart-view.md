---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c211f3aeb008b921c6cbc8c0b755e3f0323e420f05550998a093aa950787243b
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-chart-view
    - MCV
    - Chart View
    - Chart view
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Chart View
description: A page in the MLflow UI that shows a collection of charts comparing runs of an experiment, with capabilities to select, filter, sort, group runs and customize or create new charts.
tags:
  - mlflow
  - visualization
  - experiment-tracking
timestamp: "2026-06-19T17:47:20.566Z"
---

---
title: MLflow Chart View
summary: A visualization page in the MLflow UI that displays a collection of charts comparing the runs of an experiment, with customizable options for selecting runs, modifying charts, and creating new visualizations.
sources:
  - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:02:45.709Z"
updatedAt: "2026-06-19T14:18:59.373Z"
tags:
  - mlflow
  - visualization
  - experiment-tracking
aliases:
  - mlflow-chart-view
  - MCV
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Chart View

**MLflow Chart View** is a visualization interface within the [MLflow](/concepts/mlflow.md) UI that displays a collection of charts comparing the runs of an experiment. You can customize the page by selecting which runs to include, modifying existing charts, and creating new charts. With [MLflow 3](/concepts/mlflow-3.md), these chart features are also available for models from the **Models** tab, enabling visual comparison of logged models. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

MLflow metadata for experiments and runs is also available in [MLflow System Tables](/concepts/mlflow-system-tables.md), where you can leverage Databricks SQL and all the lakehouse tooling to visualize experiment data. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Accessing Chart View

To display the chart view page, click the **Chart view** icon on the experiment details page. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

For information about the runs list page, see [MLflow Runs](/concepts/mlflow-run.md). To display runs from multiple experiments, see [Comparing Runs Across Experiments](/concepts/comparing-runs-from-multiple-experiments.md). ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Chart Overview

By default, charts on this page show the most recent 10 runs. As you roll your cursor over the lines or data points on a chart, details for that run appear in a tooltip. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

Each chart provides controls to move, resize, or enlarge to full screen. A kebab menu at the upper-right corner lets you edit, delete, or download the chart as an image. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting Runs to Display

To control how many runs appear on the charts, click the **Show run icon** at the top of the runs list. A dropdown menu lets you show the first 10, 20, or all runs. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

Runs that are currently displayed on charts are indicated by a colored dot. Runs that are hidden appear with a grayed-out dot. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing Runs

To manage runs, check the box next to the left of one or more runs. When at least one run is selected, the following action buttons appear: ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

- **Delete** — Remove the selected runs.
- **Compare** — Open the Comparing MLflow Runs page to compare selected runs side by side.
- **Add tags** — Add or edit tags on the selected runs.

## Filtering Runs

Use the search field to the right of the **Chart view** icon to filter runs based on parameter values, metric values, or tags. For detailed filtering syntax, see [MLflow Run Filtering](/concepts/mlflow-run-filtering-and-search.md). ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sorting Runs

To change the sort order of runs shown in the charts, select the parameter to sort by from the **Sort** dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

To group runs by parameter value, select one or more parameters from the **Group by** dropdown menu. Grouping assigns different colors or visual markers to runs with different parameter values, making it easier to compare performance across configurations. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating New Visualizations

To add a chart, click **Add chart** and select the type of chart to add from the dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

A **parallel coordinates plot** is useful for understanding the effect of parameter settings on model performance and for investigating relationships between parameters and metrics. To create a parallel coordinates plot: ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

1. Click **Add chart** and select **Parallel coordinates** from the menu.
2. In the dialog, select the parameters and metrics to investigate.
3. The resulting plot displays each run as a line connecting its parameter and metric values across parallel axes.

For example, the plot can reveal that lower values for a parameter like `max_depth` result in higher values for a metric like `auc`. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit containing runs
- [MLflow Runs](/concepts/mlflow-run.md) — Individual training executions tracked by MLflow
- Comparing MLflow Runs — Side-by-side run comparison page
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — Model comparison features available with MLflow 3
- [MLflow System Tables](/concepts/mlflow-system-tables.md) — System table reference for MLflow metadata
- Databricks SQL — SQL-based analysis of experiment data

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
