---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ce33b5c2df0fe6ea3a8742745b0493aff237e12a4fd80e62a8ae63502898e10
  pageDirectory: concepts
  sources:
    - view-training-results-with-mlflow-runs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-filtering-and-search
    - Search and MLflow Run Filtering
    - MRFAS
    - MLflow Run Filtering
  citations:
    - file: view-training-results-with-mlflow-runs-databricks-on-aws.md
title: MLflow Run Filtering and Search
description: The ability to search and filter MLflow runs using queries on parameters, metrics, tags, state, creation time, and datasets to locate specific experiment executions.
tags:
  - mlflow
  - experiment-tracking
  - query
timestamp: "2026-06-19T23:25:24.756Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Filtering and Search

**MLflow Run Filtering and Search** allows you to find specific [MLflow runs](/concepts/mlflow-run.md) from an experiment based on parameter values, metric values, tags, creation time, run state, and datasets used. The search functionality is available on the experiment details page and can be used to narrow down runs for comparison or analysis. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Search Query Syntax

Enter a query in the search field on the experiment details page and press **Enter** to filter the runs table. The query syntax supports comparisons on metrics, parameters, and tags. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Metrics

Use `metrics.<metric_name>` followed by a comparison operator and a numeric value. By default, the filter checks the **last logged** value of the metric. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

- `metrics.r2 > 0.3`
- `metrics.avg_areaUnderROC > 0.3`

To search based on the **minimum** or **maximum** logged value of a metric, use the `MIN()` or `MAX()` functions. These functions are only available for runs logged **after August 2024**. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

- `MIN(metrics.rmse) <= 1`
- `MAX(metrics.memUsage) > 0.9`
- `LATEST(metrics.memUsage) = 0 AND MIN(metrics.rmse) <= 1`

### Parameters

Use `params.<parameter_name>` with a string equality operator (`=`). Values must be enclosed in quotes when they contain special characters, though the source examples show plain values. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

- `params.elasticNetParam = 0.5`

### Combined Expressions

Use the `AND` operator to combine multiple conditions. Parentheses are not shown in the source, but simple conjunctions are supported. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

- `params.elasticNetParam = 0.5 AND metrics.avg_areaUnderROC > 0.3`

### Tags

Tags are key-value pairs that can be added to a run. To filter runs by tag, use the format `tags.<key>="<value>"`. The key and value must be enclosed in double quotes; if the key contains spaces, it must be enclosed in **backticks**. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

- `tags.estimator_name="RandomForestRegressor"`
- `tags.color="blue" AND tags.size=5`
- `` tags.`my custom tag` = "my value" ``

## Filtering by Run State, Time Created, and Datasets

You can also filter runs using the drop-down menus on the experiment details page: ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

- **State** – choose between **Active** (default) and **Deleted** runs.
- **Time created** – select a time range.
- **Datasets** – filter by datasets used during the run.

These filters can be combined with the text search query.

## Adding Tags for Searching

To enable tag-based filtering, you must first add tags to a run. Tags are key-value pairs that you can create and later use to search for runs. Tags can be added, edited, or deleted from the **Details** table on the run page. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

For more information on managing tags, see Add a tag to a run.

## Related Concepts

- [MLflow Runs](/concepts/mlflow-run.md) – execution of model code, recording parameters, metrics, tags, and artifacts.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – organizational unit that groups related runs.
- [MLflow Tags](/concepts/mlflow-trace-tags.md) – key-value metadata used for filtering and organization.
- MLflow Metrics – numeric values logged during training that can be filtered.
- MLflow Parameters – key-value input parameters used in a run.

## Sources

- view-training-results-with-mlflow-runs-databricks-on-aws.md

# Citations

1. [view-training-results-with-mlflow-runs-databricks-on-aws.md](/references/view-training-results-with-mlflow-runs-databricks-on-aws-c299681f.md)
