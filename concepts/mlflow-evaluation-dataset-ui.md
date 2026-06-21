---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a0d51dd52c556150b386504e068816b21ff76eb079d6cd10c2c51a58a93f30d
  pageDirectory: concepts
  sources:
    - evaluation-dataset-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-dataset-ui
    - MEDU
  citations:
    - file: evaluation-dataset-reference-databricks-on-aws.md
title: MLflow Evaluation Dataset UI
description: A visual interface in the MLflow experiment Datasets tab for creating, editing, searching, and managing evaluation datasets and their records without writing code.
tags:
  - mlflow
  - ui
  - dataset-management
timestamp: "2026-06-19T10:24:39.908Z"
---

# MLflow Evaluation Dataset UI

The **MLflow Evaluation Dataset UI** provides a visual interface within the MLflow experiment page for managing evaluation datasets and their records. Datasets define the structured test data — `inputs`, optional ground-truth `expectations`, and lineage fields such as `source` and `tags` — used to evaluate a [GenAI](/concepts/mlflow-genai-evaluate-api.md) application. The interface allows you to create, edit, delete, and search datasets and records without writing code.^[evaluation-dataset-reference-databricks-on-aws.md]

## Overview

The UI uses a split-pane layout. The left pane lists all evaluation datasets associated with the experiment, sorted by last updated time by default. A search bar filters datasets by name. Clicking a dataset name displays its records in the right pane. You can enlarge the right pane by hovering over the pane separator and clicking the left-pointing arrow; clicking the arrow again returns to the default view.^[evaluation-dataset-reference-databricks-on-aws.md]

To access the interface, navigate to an experiment in the sidebar (click **Experiments**), then click the **Datasets** tab.^[evaluation-dataset-reference-databricks-on-aws.md]

## Create an Evaluation Dataset

1. On the **Datasets** tab, click **Create dataset**.
2. In the dialog, click **Select schema** to choose a [Unity Catalog](/concepts/unity-catalog.md) schema where you have `CREATE TABLE` permissions.
3. Enter a table name. A preview of the full dataset name (`catalog.schema.table_name`) appears.
4. Click **Create Dataset**.^[evaluation-dataset-reference-databricks-on-aws.md]

## Add Dataset Records

To add existing production traces to an evaluation dataset, see [Create a dataset using the UI](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset#create-a-dataset-using-the-ui) in the Databricks documentation.^[evaluation-dataset-reference-databricks-on-aws.md]

## Edit Dataset Records

From the right pane, you can edit **Inputs** and **Expectations** fields directly in the table. These fields accept JSON and validate input as you type. To add a new row, click **Add record**. A new row with default values appears at the top of the table. To save all pending edits, click **Save changes** at the upper right.^[evaluation-dataset-reference-databricks-on-aws.md]

## Delete Records or Datasets

- **To delete records**, select one or more records using checkboxes, then click **Delete (N)**.
- **To delete a dataset**, click **Show details** to open the details pane, then click **Delete dataset** at the bottom. You can also delete a dataset from the kebab menu in the dataset list.^[evaluation-dataset-reference-databricks-on-aws.md]

## View Dataset Details

Click **Show details** at the upper right to open a pane showing metadata: dataset name, ID, creation time, last update, source, and a link to view the dataset in Unity Catalog.^[evaluation-dataset-reference-databricks-on-aws.md]

## Add and Delete Tags

In the **Tags** column, click a tag to edit it, or click **Add tags** to add a new tag. Tags can be used to organize or filter records.^[evaluation-dataset-reference-databricks-on-aws.md]

## View Source Trace

If a record was created from a production trace, clicking the trace in the **Source** column opens an interactive window showing the full trace and assessments.^[evaluation-dataset-reference-databricks-on-aws.md]

## Run an Evaluation Using the Dataset

1. Click **Run an evaluation**.
2. A dialog opens with a Python code template that loads the dataset and runs `mlflow.genai.evaluate()` with a default set of scorers ([LLM Judges](/concepts/llm-judges.md)).
3. Click the copy icon to copy the snippet to your clipboard.^[evaluation-dataset-reference-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md) — The structured data used for GenAI app evaluation
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The MLflow module for generative AI evaluation
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer where datasets are stored
- [LLM Judges](/concepts/llm-judges.md) — The automated scorers used in evaluation

## Sources

- evaluation-dataset-reference-databricks-on-aws.md

# Citations

1. [evaluation-dataset-reference-databricks-on-aws.md](/references/evaluation-dataset-reference-databricks-on-aws-b8093309.md)
