---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9ba9faa574026ca6292b30ee5cdbfa2e5e9e6514066101b1d321174940a78db
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-filtering-sorting-and-grouping
    - Grouping and MLflow Run Filtering, Sorting
    - MRFSAG
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow Run Filtering, Sorting and Grouping
description: Capabilities in the MLflow UI to filter runs by parameter/metric values or tags, sort runs by parameters, and group runs by parameter values for comparative analysis.
tags:
  - mlflow
  - visualization
  - experiment-tracking
timestamp: "2026-06-19T17:47:23.959Z"
---

---
title: [MLflow Run](/concepts/mlflow-run.md) Filtering, Sorting and Grouping
summary: How to filter, sort, and group runs in the MLflow UI to focus on specific experiments and compare performance across different parameter sets.
sources:
  - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:43:57.264Z"
updatedAt: "2026-06-19T14:43:57.264Z"
tags:
  - MLflow
  - experiment tracking
  - visualization
  - filtering
aliases:
  - mlflow-run-filtering-sorting-and-grouping
  - MFSG
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# [MLflow Run](/concepts/mlflow-run.md) Filtering, Sorting and Grouping

**MLflow Run Filtering, Sorting and Grouping** refers to the tools available in the [MLflow UI](/concepts/mlflow.md) that let you narrow down the set of runs displayed in charts and tables, reorder them by a chosen metric or parameter, and aggregate them by common parameter values. These features help you compare runs efficiently and identify the best-performing configurations.

## Filter runs

Use the search field located to the right of the **Chart view** icon on the experiment details page to filter runs based on parameter values, metric values, or tags. The filter syntax follows the same rules as the runs list page; for details, see the Filter runs documentation. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sort runs

To change the order in which runs appear in the charts, select a parameter from the **Sort** dropdown menu. The runs are then sorted by that parameter in ascending or descending order depending on the selection. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Group runs

To group runs by parameter value, select one or more parameters from the **Group by** dropdown menu. Each unique combination of the selected parameter values produces a separate group, and the charts differentiate groups by colour and line style. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting runs to display

By default, charts show the most recent 10 runs. To change how many runs are shown, click the show‑run icon at the top of the runs list and choose **First 10**, **First 20**, or **All**. Runs that are currently displayed are marked with a coloured dot; hidden runs have a grayed‑out dot. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related concepts

- Compare MLflow runs and models using graphs and charts – The chart view page where filtering, sorting, and grouping are performed.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational unit containing the runs.
- [MLflow runs](/concepts/mlflow-run.md) – Individual training or evaluation executions.
- Filter runs – A dedicated page describing filter syntax and operators.
- Compare runs – The page for side‑by‑side comparison of selected runs.

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
