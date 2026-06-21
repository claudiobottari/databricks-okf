---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5f3c99522be0df419d8c30ab4218a224d153962109348c3d995d9b16e48f273
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-filtering-and-sorting
    - Sorting and MLflow Run Filtering
    - MRFAS
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Run Filtering and Sorting
description: Filtering MLflow runs based on parameter values, metric values, or tags, and sorting runs by selected parameters to control what appears in chart views.
tags:
  - mlflow
  - experiment-tracking
  - workflow
timestamp: "2026-06-19T14:19:01.601Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Filtering and Sorting

**MLflow Run Filtering and Sorting** refers to the tools available in the MLflow UI for narrowing down which runs are displayed in the chart view and controlling their ordering. These features help practitioners focus on the most relevant experimental results and identify relationships between parameters and metrics.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering Runs

Use the search field located to the right of the **Chart view** icon to filter runs based on parameter values, metric values, or tags. The filter syntax follows the same rules as the runs list page; see the [MLflow runs](/concepts/mlflow-run.md) documentation for detailed filtering syntax.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sorting Runs

To change the sort order of runs shown in the charts, select a parameter from the **Sort** dropdown menu. Runs are then ordered by the chosen parameter in ascending or descending order depending on the default sort direction.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

Runs can be grouped by one or more parameter values using the **Group by** dropdown menu. When multiple parameters are selected, runs are grouped hierarchically. This grouping is particularly useful in [parallel coordinates charts](/concepts/parallel-coordinates-chart-in-mlflow.md) for identifying how parameter combinations affect metric outcomes.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational container for runs.
- Compare MLflow runs — Side-by-side comparison of selected runs.
- [MLflow Chart View](/concepts/mlflow-chart-view.md) — The visualization page where filtering, sorting, and grouping are applied.
- [Parallel Coordinates Chart](/concepts/parallel-coordinates-chart-in-mlflow.md) — A chart type that benefits from grouping to reveal parameter-metric relationships.

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
