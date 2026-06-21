---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ed307bf919727a366484b15b65c2af9f9993fdec7ae093e5bd078d42045ce54
  pageDirectory: concepts
  sources:
    - view-training-results-with-mlflow-runs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-download-and-export
    - Export and MLflow Run Download
    - MRDAE
  citations:
    - file: view-training-results-with-mlflow-runs-databricks-on-aws.md
title: MLflow Run Download and Export
description: The ability to download MLflow run data as CSV files from the UI or programmatically, and to copy runs between workspaces using the MLflow Export-Import community tool.
tags:
  - mlflow
  - experiment-tracking
  - export
timestamp: "2026-06-19T23:25:53.367Z"
---

## [MLflow Run](/concepts/mlflow-run.md) Download and Export

**MLflow Run Download and Export** refers to the methods available in [MLflow](/concepts/mlflow.md) for retrieving run data in portable formats and transferring runs between Databricks workspaces. [MLflow](/concepts/mlflow.md) provides built-in options to download run information as a CSV file and a community-driven tool for exporting and importing full runs across workspaces. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Download Runs from the UI

From the experiment details page, you can download run data in CSV format. Click the kebab menu (three vertical dots) and select **Download `<n>` runs**. [MLflow](/concepts/mlflow.md) creates and downloads a file with one row per run, up to a maximum of 100 runs. The CSV contains the following fields for each run: `Start Time, Duration, Run ID, Name, Source Type, Source Name, User, Status`, followed by columns for each parameter and metric logged during the run. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Downloading Large Numbers of Runs Programmatically

If you want to download more than 100 runs or prefer a programmatic approach, select **Download all runs** from the same kebab menu. A dialog opens showing a code snippet that you can copy or open in a notebook. After running this code in a notebook cell, select **Download all rows** from the cell output to retrieve the full set of runs. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Exporting and Importing Runs Between Workspaces

To import or export [MLflow](/concepts/mlflow.md) runs to or from your Databricks workspace, you can use the community-driven open source project [MLflow](/concepts/mlflow.md) Export-Import](https://github.com/[MLflow](/concepts/mlflow.md)/mlflow-export-import). This tool enables transferring run metadata, parameters, metrics, artifacts, and tags between different Databricks workspaces. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

### Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizing container for runs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The logging API that records run data.
- [MLflow Runs](/concepts/mlflow-run.md) – A single execution of model code.
- MLflow Artifacts – Output files associated with a run.

### Sources

- view-training-results-with-mlflow-runs-databricks-on-aws.md

# Citations

1. [view-training-results-with-mlflow-runs-databricks-on-aws.md](/references/view-training-results-with-mlflow-runs-databricks-on-aws-c299681f.md)
