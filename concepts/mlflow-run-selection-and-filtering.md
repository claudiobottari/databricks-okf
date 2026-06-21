---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d633e5845c14c989f4ec281ef0d0cbb9e206b6da7aa48dfccb63a5cce7f77fa
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-selection-and-filtering
    - Filtering and MLflow Run Selection
    - MRSAF
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Run Selection and Filtering
description: Mechanisms in the MLflow UI to select, show/hide, filter, sort, and group runs for comparative analysis in charts, including search by parameter/metric values or tags.
tags:
  - mlflow
  - experiment-tracking
  - user-interface
timestamp: "2026-06-18T11:03:01.786Z"
---

---
title: [MLflow Run](/concepts/mlflow-run.md) Selection and Filtering
summary: How to select, filter, sort, and group MLflow runs in the MLflow UI to focus on specific experiments or models.
sources:
  - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - mlflow
  - runs
  - filtering
  - visualization
aliases:
  - mlflow-run-selection-and-filtering
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# [MLflow Run](/concepts/mlflow-run.md) Selection and Filtering

**MLflow Run Selection and Filtering** refers to the set of UI controls and search capabilities in the MLflow experiment and model tracking pages that allow you to choose, filter, sort, and group training runs or logged models for comparison and visualization. These features are available on the **Chart view** page of an experiment and, with [MLflow 3](/concepts/mlflow-3.md), also on the **Models** tab for registered models. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting Runs to Display

By default, charts on the Chart view page show the most recent 10 runs. You can change the number of runs shown by clicking the show/hide run icon at the top of the runs list and selecting **First 10**, **First 20**, or **All**. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

Runs that are displayed on charts appear with a colored dot; hidden runs show a grayed-out dot. You can also manually toggle individual runs on or off by clicking the dot next to the run name. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering Runs

Use the search field (located to the right of the Chart view icon) to filter runs based on parameter values, metric values, or tags. The filtering syntax supports simple key-value comparisons. This allows you to narrow the displayed runs to only those matching criteria such as `params.alpha > 0.1` or `metrics.accuracy > 0.9`. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

See Filter Runs for detailed syntax and examples.

## Sorting Runs

To change the sort order of runs shown in the charts, select a parameter or metric from the **Sort** dropdown menu. Runs are then reordered based on the chosen value. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

To group runs by a common parameter value, select one or more parameters from the **Group by** dropdown menu. This can help identify how different parameter settings affect model performance. For example, grouping by `max_depth` will display separate chart lines for each distinct depth value. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing Runs

After selecting runs (by checking the box next to the run name), you can perform bulk actions: **Delete**, **Compare**, or **Add tags**. The button bar appears once at least one run is selected. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

- **Delete**: Removes the selected runs from the experiment.
- **Compare**: Opens the Compare Runs page to juxtapose parameters, metrics, and artifacts side-by-side.
- **Add tags**: Applies custom metadata tags to the selected runs for later filtering or organization.

## Runs from Multiple Experiments

You can also display runs from multiple experiments. For details, see [Compare Runs from Multiple Experiments](/concepts/comparing-runs-from-multiple-experiments.md). ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Availability for Models

With MLflow 3, the run selection, filtering, sorting, and grouping features are also available for models on the **Models** tab. This allows you to compare different logged models in the same way as experiment runs. See [Track and Compare Models Using MLflow Logged Models](/concepts/mlflow-loggedmodel.md) for more information. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Runs](/concepts/mlflow-run.md) — Core object representing a single execution of model training code
- [MLflow Experiment](/concepts/mlflow-experiment.md) — Logical grouping of runs
- [MLflow Logged Model](/concepts/mlflow-logged-model.md) — Model saved during a run
- [Chart View](/concepts/mlflow-chart-view.md) — Visualization page showing runs on graphs
- Compare Runs — Side-by-side comparison of selected runs
- Filter Runs — Syntax for run filtering queries
- [MLflow 3](/concepts/mlflow-3.md) — Version of MLflow that extends chart features to models
- System Tables (MLflow) — Where run metadata is available for SQL queries

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
