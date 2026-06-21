---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fdb606502b6d30a516065040364bf4aa60fc96822f623c9eb38cf92638c349fe
  pageDirectory: concepts
  sources:
    - organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - viewing-and-searching-mlflow-experiments
    - Searching MLflow Experiments and Viewing
    - VASME
  citations:
    - file: organize-training-runs-with-mlflow-experiments-databricks-on-aws.md
title: Viewing and Searching MLflow Experiments
description: Experiments are viewed from the Experiments page (sidebar under AI/ML), from the workspace for workspace experiments, or from the notebook sidebar for notebook experiments. Filter experiments by name, location, or by searching tags like tags.mlflow.note.content for descriptions.
tags:
  - mlflow
  - experiments
  - search
  - ui
timestamp: "2026-06-19T19:53:29.668Z"
---

# Viewing and Searching MLflow Experiments

**Viewing and Searching MLflow Experiments** covers the methods available in Databricks to browse, access, and filter [MLflow experiments](/concepts/mlflow-experiment.md) and their associated runs. Experiments are organizational units that group runs from model training, agent traces, and LLM evaluations. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Viewing Experiments

All experiments that a user has access to appear on the **Experiments** page, accessible from the sidebar under **AI/ML** → **Experiments**. From this page, you can click any experiment name to open its details page. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

Additional ways to reach the experiment details page:

- For a workspace experiment, navigate to it directly from the workspace menu.
- For a notebook experiment, access the experiment details page from the notebook itself via the **Experiment** icon in the notebook’s right sidebar. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

The experiment details page lists all runs associated with the experiment. You can open any run by clicking its **Run Name**. The **Source** column provides a link to the notebook version that created the run. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Searching for Experiments

On the **Experiments** page, you can filter the experiment list by typing text in the **Filter experiments** field and pressing **Enter** or clicking the magnifying glass icon. The list updates to show only those experiments whose **Name** or **Location** columns contain the search text. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

For advanced searches, you can enter a query using the syntax `` tags.`mlflow.note.content` `` to search within the **Description** column. This tag‑based search requires you to manually construct the query with an identifier and comparator; it does not automatically return all results that contain the search text. See also: Search Experiments (MLflow documentation). ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Filtering Runs Within an Experiment

Inside the experiment details page, you can also search and filter the runs table by metrics or parameter settings. This helps narrow down runs that meet specific performance or configuration criteria without leaving the experiment view. ^[organize-training-runs-with-mlflow-experiments-databricks-on-aws.md]

## Related Concepts

- Organize Training Runs with MLflow Experiments – How to create, rename, delete, and manage permissions on experiments.
- [MLflow Runs](/concepts/mlflow-run.md) – The individual execution units logged to an experiment.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The API and UI for logging parameters, metrics, and artifacts.
- [Notebook Experiments](/concepts/notebook-experiment-in-databricks.md) – Experiments automatically associated with a Databricks notebook.
- [Workspace Experiments](/concepts/mlflow-active-experiment.md) – Standalone experiments not tied to a specific notebook.

## Sources

- organize-training-runs-with-mlflow-experiments-databricks-on-aws.md

# Citations

1. [organize-training-runs-with-mlflow-experiments-databricks-on-aws.md](/references/organize-training-runs-with-mlflow-experiments-databricks-on-aws-079819a5.md)
