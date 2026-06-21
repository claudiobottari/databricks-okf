---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 619c41caa466f6d560c6fc23c031157f7f815b9654618486d16343ab3a2dbeaa
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - filtering-and-sorting-mlflow-runs
    - Sorting MLflow Runs and Filtering
    - FASMR
    - Filtering MLflow Runs
    - View training results with MLflow runs
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Filtering and Sorting MLflow Runs
description: Ability to filter runs by parameter, metric, or tag values, and sort runs by selected parameters to control which runs appear on charts.
tags:
  - mlflow
  - experiment-tracking
  - user-interface
timestamp: "2026-06-18T14:40:03.725Z"
---

# Filtering and Sorting MLflow Runs

**Filtering and Sorting MLflow Runs** refers to the tools available in the [MLflow](/concepts/mlflow.md) UI that allow you to narrow down the set of runs displayed on the [Chart View](/mlflow/visualize-runs) and control the order in which they appear. These features help you focus on specific experiments, parameters, metrics, or tags, and make it easier to compare runs visually.

## Filtering Runs

The **Filter runs** field is located to the right of the **Chart view** icon on the experiment details page. You can use it to filter runs based on parameter values, metric values, or tags. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

The search syntax follows the same patterns used in the MLflow Runs List page. For example, you can enter `params.learning_rate > 0.001` or `metrics.accuracy > 0.9` to show only runs that meet those criteria. For a complete reference, see the Filter Runs documentation.

## Sorting Runs

To change the sort order of the runs shown in the charts, use the **Sort** dropdown menu. Selecting a parameter from this menu reorders the runs by that parameter’s value. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

The dropdown lists all available parameters (e.g., `start_time`, `duration`, or any logged hyperparameter). The sort order applies to the runs list and affects how they appear in all charts on the page.

## Grouping Runs (Related Feature)

Although not strictly part of filtering or sorting, the **Group by** dropdown menu lets you group runs by one or more parameter values. This can be used together with filtering to organize runs into clusters for easier comparison. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Runs](/concepts/mlflow-run.md) – The fundamental unit of tracking in MLflow.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The container for runs.
- [Chart View](/concepts/mlflow-chart-view.md) – The visualization page where filtering, sorting, and grouping are applied.
- Comparing MLflow Runs – How to use the filtered and sorted runs for side‑by‑side comparison.
- Add Charts in Chart View – Creating custom charts once runs are filtered and sorted.

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
