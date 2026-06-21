---
title: Building MLflow evaluation datasets | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset
ingestedAt: "2026-06-18T08:14:41.620Z"
---

To systematically test and improve a GenAI application, you use an evaluation dataset. An evaluation dataset is a selected set of example inputs — either labeled (with known expected outputs) or unlabeled (without ground-truth answers). Evaluation datasets help you improve your app's performance in the following ways:

*   Improve quality by testing fixes against known problematic examples from production.
*   Prevent regressions. Create a "golden set" of examples that must always work correctly.
*   Compare app versions. Test different prompts, models, or app logic against the same data.
*   Target specific features. Build specialized datasets for safety, domain knowledge, or edge cases.
*   Validate the app across different environments as part of LLMOps.

MLflow evaluation datasets are stored in Unity Catalog, which provides built-in versioning, lineage, sharing, and governance.

## Requirements[​](#requirements "Direct link to Requirements")

*   To create an evaluation dataset, you must have `CREATE TABLE` permissions on a Unity Catalog schema.
*   An evaluation dataset is attached to an MLflow experiment. If you do not already have an experiment, see [Create an MLflow Experiment](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment#create-expt) to create one.

## Data sources for evaluation datasets[​](#data-sources-for-evaluation-datasets "Direct link to Data sources for evaluation datasets")

You can use any of the following to create an evaluation dataset:

*   Existing traces. If you have already captured traces from a GenAI application, you can use them to create an evaluation dataset based on real-world scenarios.
*   An existing dataset, or directly entered examples. This option is useful for quick prototyping or for targeted testing of specific features.
*   Synthetic data. Databricks can automatically generate a representative evaluation set from your documents, allowing you to quickly evaluate your agent with good coverage of test cases.

This page describes how to create an MLflow evaluation dataset. You can also use other types of datasets, such as Pandas DataFrames or a list of dictionaries. See [MLflow evaluation examples for GenAI](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/eval-examples) for examples.

## Create a dataset using the UI[​](#create-a-dataset-using-the-ui "Direct link to Create a dataset using the UI")

Follow these steps to use the UI to create a dataset from existing traces. For reference information, see [MLflow evaluation dataset UI](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-datasets#ui).

1.  Click **Experiments** in the sidebar to display the Experiments page.
    
2.  Click on the name of your experiment to open it.
    
    ![Open experiment](https://docs.databricks.com/aws/en/assets/images/experiments-page-ce16367da375cf850a6aaac58669ab42.png)
    
3.  In the left sidebar, click **Traces**.
    
4.  Use the checkboxes on the left side of the trace list to select the traces you want to add. To select all traces on the current page, click the checkbox next to **Trace ID** in the column header.
    
    ![Select traces](https://docs.databricks.com/aws/en/assets/images/select-traces-6574a81a57967370c4bccde8c4445e0f.gif)
    
5.  Click **Actions**. The button label shows the number of selected traces, for example **Actions (3)**.
    
    ![Actions menu](https://docs.databricks.com/aws/en/assets/images/actions-menu-eval-dataset-0166eee400c80913e174a333f0b1472c.png)
    
6.  Under **Use for evaluation**, select **Add to evaluation dataset**. The **Add traces to evaluation dataset** dialog opens.
    
7.  If no evaluation datasets exist for this experiment, or if you want to add traces to a new dataset, follow these steps to create a new evaluation dataset:
    
    1.  Click **Create new dataset**.
    2.  Select the Unity Catalog schema to hold the new dataset.
    3.  Enter a name for the dataset and click **Create Dataset**.
    4.  Click **Export** and then click **Done**.
    
    ![Add traces dialog if no evaluation datasets exist](https://docs.databricks.com/aws/en/assets/images/add-traces-dialog-none-existing-5e3febb1de1fa97e5fef1bb25bc327dc.png)
    
    If evaluation datasets already exist for the experiment, click **Export** to the right of the dataset you want to add the traces to. You can export to more than one dataset. When you've finished exporting, click **Done**.
    
    ![Add traces dialog if with existing evaluation datasets](https://docs.databricks.com/aws/en/assets/images/add-traces-eval-set-dialog-a2b335379d8c5cded02f1c4c63e7213f.png)
    

## Create a dataset using the SDK[​](#create-a-dataset-using-the-sdk "Direct link to Create a dataset using the SDK")

Follow these steps to use the SDK to create a dataset. For reference information, see [Evaluation dataset reference](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-datasets).

### Step 1. Create the dataset[​](#step-1-create-the-dataset "Direct link to Step 1. Create the dataset")

Python

    import mlflowimport mlflow.genai.datasetsimport timefrom databricks.connect import DatabricksSession# 0. If you are using a local development environment, connect to Serverless Spark which powers MLflow's evaluation dataset servicespark = DatabricksSession.builder.remote(serverless=True).getOrCreate()# 1. Create an evaluation dataset# Replace with a Unity Catalog schema where you have CREATE TABLE permissionuc_schema = "workspace.default"# This table will be created in the above UC schemaevaluation_dataset_table_name = "email_generation_eval"eval_dataset = mlflow.genai.datasets.create_dataset(    name=f"{uc_schema}.{evaluation_dataset_table_name}",)print(f"Created evaluation dataset: {uc_schema}.{evaluation_dataset_table_name}")

### Step 2: Add records to your dataset[​](#step-2-add-records-to-your-dataset "Direct link to step-2-add-records-to-your-dataset")

This section describes several options for adding records to the evaluation dataset.

*   From existing traces
*   From domain expert labels
*   Build from scratch or import existing
*   Seed using synthetic data
*   For conversation simulation

One of the most effective ways to build a relevant evaluation dataset is by curating examples directly from your application's historical interactions captured by MLflow Tracing. You can create datasets from traces using either the MLflow Monitoring UI or the SDK.

Programmatically search for traces and then add them to the dataset using `search_traces()`. Use filters to identify traces by success, failure, use in production, or other properties. See [Search traces programmatically](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk).

Python

    import mlflow# 2. Search for tracestraces = mlflow.search_traces(    filter_string="attributes.status = 'OK'",    order_by=["attributes.timestamp_ms DESC"],    tags.environment = 'production',    max_results=10)print(f"Found {len(traces)} successful traces")# 3. Add the traces to the evaluation dataseteval_dataset = eval_dataset.merge_records(traces)print(f"Added {len(traces)} records to evaluation dataset")# Preview the datasetdf = eval_dataset.to_df()print(f"\nDataset preview:")print(f"Total records: {len(df)}")print("\nSample record:")sample = df.iloc[0]print(f"Inputs: {sample['inputs']}")

#### Select traces for evaluation datasets[​](#select-traces-for-evaluation-datasets "Direct link to Select traces for evaluation datasets")

Before adding traces to your dataset, identify which traces represent important test cases for your evaluation needs. You can use both quantitative and qualitative analysis to select representative traces.

**Quantitative trace selection**

Use the MLflow UI or SDK to filter and analyze traces based on measurable characteristics:

*   **In the MLflow UI**: Filter by tags (e.g., `tag.quality_score < 0.7`), search for specific inputs/outputs, sort by latency or token usage
*   **Programmatically**: Query traces to perform advanced analysis

Python

    import mlflowimport pandas as pd# Search for traces with potential quality issuestraces_df = mlflow.search_traces(    filter_string="tag.quality_score < 0.7",    max_results=100)# Analyze patterns# For example, check if quality issues correlate with token usagecorrelation = traces_df["span.attributes.usage.total_tokens"].corr(traces_df["tag.quality_score"])print(f"Correlation between token usage and quality: {correlation}")

For complete trace query syntax and examples, see [Search traces programmatically](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk).

**Qualitative trace selection**

Review individual traces to identify patterns requiring human judgment:

*   Examine inputs that led to low-quality outputs
*   Look for patterns in how your application handled edge cases
*   Identify missing context or faulty reasoning
*   Compare high-quality vs. low-quality traces to understand differentiating factors

Once you've identified representative traces, add them to your dataset using the search and merge methods described above.

tip

Enrich your traces with expected outputs or quality indicators to enable ground truth comparison. See [collect domain expert feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/label-existing-traces) to add human labels.

## Update existing datasets[​](#update-existing-datasets "Direct link to Update existing datasets")

You can use the UI or the SDK to update an evaluation dataset.

*   Databricks UI
*   MLflow SDK

Use the UI to add records to an existing evaluation dataset.

1.  Open the dataset page in the Databricks workspace:
    
    1.  In the Databricks workspace, navigate to your experiment.
    2.  In the sidebar at left, click **Datasets**.
    3.  Click on the name of the dataset in the list.
    
    ![Datasets tab in sidebar](https://docs.databricks.com/aws/en/assets/images/datasets-tab-6e544d95c2c79d5356c306d9914b5ce4.png)
    
2.  Click **Add record**. A new row appears with generic content.
    
3.  Edit the new row directly to enter the input and expectations for the new record. Optionally, set any tags for the new record.
    
4.  Click **Save changes**.
    

## Limitations[​](#limitations "Direct link to Limitations")

*   Evaluation datasets cannot be stored in catalogs encrypted with [customer-managed keys (CMK)](https://docs.databricks.com/aws/en/security/keys/cmek-unity-catalog). Workspaces with CMK are supported as long as the dataset is stored in a non-CMK catalog.
*   Maximum of 2000 rows per evaluation dataset.
*   Maximum of 20 expectations per dataset record.

If you need any of these limitations relaxed for your use case, contact your Databricks representative.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Evaluate your app](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/evaluate-app) - Use your newly created dataset for evaluation
*   [Create custom judges](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/create-custom-judge) - Build custom LLM judges to evaluate your application outputs
*   [Align judges with feedback](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/align-judges) - Continuously improve your evaluations by aligning judges with expert feedback
*   [Query traces via SDK](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk) - Advanced programmatic trace analysis for dataset selection
