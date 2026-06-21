---
title: Evaluation dataset reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-datasets
ingestedAt: "2026-06-18T08:14:46.327Z"
---

Evaluation datasets in MLflow define the structured test data used to evaluate your GenAI app: `inputs`, optional ground-truth `expectations`, and lineage fields such as source and tags. This page documents the dataset schema and links to the most frequently used SDK methods and classes.

For general information and examples of how to use evaluation datasets, see [Evaluate GenAI apps during development](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness).

## Evaluation dataset schema[​](#evaluation-dataset-schema "Direct link to Evaluation dataset schema")

Evaluation datasets must use the schema described in this section.

### Core fields[​](#core-fields "Direct link to Core fields")

The following fields are used in both the evaluation dataset abstraction or if you pass data directly.

#### `expectations` reserved keys[​](#expectations-reserved-keys "Direct link to expectations-reserved-keys")

`expectations` has several reserved keys that are used by built-in LLM judges: `guidelines`, `expected_facts`, and `expected_response`.

### Additional fields[​](#additional-fields "Direct link to Additional fields")

The following fields are used by the evaluation dataset abstraction to track lineage and version history.

#### Source field[​](#source-field "Direct link to source-field")

The `source` field tracks where a dataset record came from. Each record can have **only one** source type.

**Human source**: Record created manually by a person

Python

    {    "source": {        "human": {            "user_name": "jane.doe@company.com"  # user who created the record        }    }}

**Document source**: Record synthesized from a document

Python

    {    "source": {        "document": {            "doc_uri": "s3://bucket/docs/product-manual.pdf",  # URI or path to the source document            "content": "The first 500 chars of the document..."  # Optional, excerpt or full content from the document        }    }}

**Trace source**: Record created from a production trace

Python

    {    "source": {        "trace": {            "trace_id": "tr-abc123def456". # unique identifier of the source trace        }    }}

## MLflow evaluation dataset UI[​](#-mlflow-evaluation-dataset-ui "Direct link to -mlflow-evaluation-dataset-ui")

The **Datasets** tab in the MLflow experiment page provides a visual interface for managing your evaluation datasets and their records. The page uses a split-pane layout: the left pane lists all evaluation datasets associated with the experiment, and the right pane shows the records for the selected dataset. You can search, sort, create, edit, and delete datasets and records directly from the UI without writing any code.

![Evaluation datasets tab](https://docs.databricks.com/aws/en/assets/images/evaluation-datasets-tab-446703d3481c808f3b76c4446bf996b0.png)

From the right pane, you can edit record inputs and expectations inline, add tags to individual records, view the source trace for records created from production traces, and get a ready-to-use Python code snippet for running an evaluation against the dataset.

### Evaluation dataset UI overview[​](#evaluation-dataset-ui-overview "Direct link to Evaluation dataset UI overview")

1.  In the sidebar, click **Experiments** and open your experiment.
    
2.  Click the **Datasets** tab. The left pane shows all evaluation datasets for this experiment. By default, datasets are sorted by last updated time. Use the search bar to filter by dataset name.
    
3.  Click a dataset name to view its records in the right pane. You might need to scroll right and left to view all columns.
    
4.  To enlarge the right pane, hover over the pane separator and click the left-pointing arrow. Click the arrow again to return to the default view.
    
    ![Hover over the pane separator to enlarge the right pane.](https://docs.databricks.com/aws/en/assets/images/enlarge-pane-1e7327e8162fe5ac35334c103b6128f8.gif)
    
5.  To select the columns that appear, click the **Columns** button. Select or deselect the checkboxes. When you're done, click anywhere off the drop-down menu.
    
    ![Select columns for display.](https://docs.databricks.com/aws/en/assets/images/select-columns-58289032071a02a55d40316a47f01864.gif)
    

### Create an evaluation dataset[​](#create-an-evaluation-dataset "Direct link to Create an evaluation dataset")

1.  On the **Datasets** tab, click **Create dataset**.
    
    ![Create dataset button](https://docs.databricks.com/aws/en/assets/images/create-dataset-e886a654f0f20834933a35941afb6f28.png)
    
2.  In the dialog, click **Select schema** to choose a Unity Catalog schema where you have `CREATE TABLE` permissions.
    
3.  Enter a table name for the dataset. A preview of the full dataset name (`catalog.schema.table_name`) appears below the input.
    
4.  Click **Create Dataset**.
    

### Add dataset records[​](#add-dataset-records "Direct link to Add dataset records")

To add existing traces to an evaluation dataset, see [Create a dataset using the UI](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset#create-a-dataset-using-the-ui).

### Edit dataset records[​](#edit-dataset-records "Direct link to Edit dataset records")

The video shows the following steps:

1.  Select a dataset in the left pane to view its records.
2.  You can edit the **Inputs** and **Expectations** fields directly in the table. These fields accept JSON and validate your input as you type.
3.  To add a new row, click **Add record**. A new row with default values appears at the top of the table.
4.  To save all pending edits, click **Save changes** at the upper right.

![How to edit dataset records.](https://docs.databricks.com/aws/en/assets/images/edit-dataset-records-5171ae9bad56f1640429c207eed1119b.gif)

### Delete records or datasets[​](#delete-records-or-datasets "Direct link to Delete records or datasets")

*   To delete records, use the checkboxes to select one or more records, then click **Delete (N)**.

![Delete record.](https://docs.databricks.com/aws/en/assets/images/delete-record-f226d5db1c97f052888cd2b1a8cd8381.png)

*   To delete a dataset, click **Show details** to open the details pane, then click **Delete dataset** at the bottom of the pane. You can also delete a dataset from the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) in the dataset list.

![Evaluation dataset show details pane.](https://docs.databricks.com/aws/en/assets/images/show-details-pane-d249e32d89aa5846c97edc9143b5f0a9.png)

### View dataset details[​](#view-dataset-details "Direct link to View dataset details")

To view metadata for the dataset, click **Show details** at the upper right. A pane opens, including the dataset name, ID, creation time, last update, source, and a link to view the dataset in Unity Catalog.

### Add and delete tags[​](#add-and-delete-tags "Direct link to Add and delete tags")

In the **Tags** column, click a tag to edit it, or click **Add tags** to add a new tag.

![Edit tags in the UI.](https://docs.databricks.com/aws/en/assets/images/edit-tags-5fa987ea1381d03dac34a729979f7f14.gif)

### View source trace[​](#view-source-trace "Direct link to View source trace")

In the **Source** column, click the trace to open an interactive window showing the full trace and assessments.

![View the source trace in the UI.](https://assets.docs.databricks.com/_static/images/mlflow3-genai/source-trace.gif)

### Run an evaluation using the dataset[​](#run-an-evaluation-using-the-dataset "Direct link to Run an evaluation using the dataset")

To open a dialog with a Python code template that loads the dataset and runs `mlflow.genai.evaluate()` with a default set of scorers:

1.  Click **Run an evaluation**.
    
    ![Run evaluation button.](https://docs.databricks.com/aws/en/assets/images/run-evaluation-button-d5ed93c9e14b8858fa8abf74dd5319bd.png)
    
2.  Click the copy icon, shown in the following image, to copy the snippet to your clipboard.
    
    ![Copy code snippet.](https://docs.databricks.com/aws/en/assets/images/copy-run-eval-code-0d6ca59546fbbda989208eb230164979.png)
    

## MLflow evaluation dataset SDK reference[​](#mlflow-evaluation-dataset-sdk-reference "Direct link to MLflow evaluation dataset SDK reference")

The evaluation datasets SDK provides programmatic access to create, manage, and use datasets for GenAI app evaluation. For details, see the API reference: [`mlflow.genai.datasets`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#module-mlflow.genai.datasets). Some of the most frequently used methods and classes are the following:

*   [`mlflow.genai.datasets.create_dataset`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.datasets.create_dataset)
*   [`mlflow.genai.datasets.get_dataset`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.datasets.get_dataset)
*   [`mlflow.genai.datasets.delete_dataset`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.datasets.delete_dataset)
*   [`EvaluationDataset`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.datasets.EvaluationDataset). This class provides methods to interact with and modify evaluation datasets.
