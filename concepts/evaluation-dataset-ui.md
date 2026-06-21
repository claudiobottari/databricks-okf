---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac9f7dd01a00c57df7deaffdd54d1c2b867ef489f7326ae984bf50b85690042d
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-ui
    - EDU
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: Evaluation Dataset UI
description: A visual interface in MLflow experiments for managing evaluation datasets and records without writing code, including create, edit, delete, tagging, and trace viewing.
tags:
  - mlflow
  - ui
  - dataset-management
timestamp: "2026-06-19T18:42:59.605Z"
---

# Evaluation Dataset UI

The **Evaluation Dataset UI** is a visual interface within the MLflow experiment page that allows you to manage evaluation datasets and their records without writing code. It provides a split-pane layout for browsing, creating, editing, and deleting datasets and individual records. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Accessing the UI

1. In the sidebar, click **Experiments** and open your experiment.
2. Click the **Datasets** tab. The left pane lists all evaluation datasets for the experiment, sorted by last updated time by default. A search bar filters datasets by name.
3. Click a dataset name to view its records in the right pane. You may need to scroll horizontally to view all columns.
4. To enlarge the right pane, hover over the pane separator and click the left-pointing arrow; click again to return to the default view.
5. To select which columns are displayed, click the **Columns** button and toggle checkboxes. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Creating an Evaluation Dataset

1. On the **Datasets** tab, click **Create dataset**.
2. In the dialog, click **Select schema** to choose a Unity Catalog schema where you have `CREATE TABLE` permissions.
3. Enter a table name for the dataset. A preview of the full dataset name (`catalog.schema.table_name`) appears.
4. Click **Create Dataset**. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Adding Dataset Records

To add existing traces to an evaluation dataset, see the documentation on [Create a dataset using the UI](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset#create-a-dataset-using-the-ui). ^[evaluation-dataset-reference-databricks-on-aws.md]

## Editing Dataset Records

- Select a dataset in the left pane to view its records.
- Edit the **Inputs** and **Expectations** fields directly in the table. These fields accept JSON and validate input as you type.
- To add a new row, click **Add record**. A new row with default values appears at the top.
- To save all pending edits, click **Save changes** at the upper right. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Deleting Records or Datasets

- **Delete records**: Use the checkboxes to select one or more records, then click **Delete (N)**.
- **Delete a dataset**: Click **Show details** to open the details pane, then click **Delete dataset** at the bottom of the pane. You can also delete a dataset from the kebab menu in the dataset list. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Viewing Dataset Details

Click **Show details** at the upper right to open a pane containing the dataset name, ID, creation time, last update, source, and a link to view the dataset in Unity Catalog. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Adding and Deleting Tags

In the **Tags** column, click a tag to edit it, or click **Add tags** to add a new tag. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Viewing Source Trace

In the **Source** column, click a trace to open an interactive window showing the full trace and assessments. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Running an Evaluation Using the Dataset

1. Click **Run an evaluation** to open a dialog with a Python code template that loads the dataset and runs `mlflow.genai.evaluate()` with a default set of scorers.
2. Click the copy icon to copy the snippet to your clipboard. ^[evaluation-dataset-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational unit for MLflow runs and evaluations.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The programmatic abstraction and schema for test data.
- GenAI app evaluation – The broader workflow for evaluating generative AI applications.
- MLflow SDK reference – Programmatic API for dataset creation and management.

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
