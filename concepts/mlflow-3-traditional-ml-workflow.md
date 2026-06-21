---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef002d9a9a889d8cb31fb7cabd7d8a971421baf0ff5ff046f71de9e2d7d8bc00
  pageDirectory: concepts
  sources:
    - mlflow-3-traditional-ml-workflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-traditional-ml-workflow
    - M3TMW
  citations:
    - file: mlflow-3-traditional-ml-workflow-databricks-on-aws.md
title: MLflow 3 traditional ML workflow
description: A Databricks notebook-based workflow demonstrating model training as an MLflow Run, producing a Logged Model, and exploring results via the MLflow UI and Unity Catalog.
tags:
  - mlflow
  - workflow
  - databricks
timestamp: "2026-06-19T19:37:47.601Z"
---

# MLflow 3 traditional ML workflow

**MLflow 3 traditional ML workflow** describes the process of training, tracking, evaluating, and registering a machine learning model using [MLflow 3](/concepts/mlflow-3.md). The workflow is demonstrated in an example notebook that runs a model training job, tracked as an [MLflow Run](/concepts/mlflow-run.md), and produces a trained model, tracked as an [MLflow Logged Model](/concepts/mlflow-logged-model.md). ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Example notebook[​](#example-notebook "Direct link to Example notebook")

The example notebook runs a model training job, which is tracked as an [MLflow Run](/concepts/mlflow-run.md), to produce a trained model, which is tracked as an MLflow Logged Model. ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Explore model parameters and performance using the MLflow UI[​](#explore-model-parameters-and-performance-using-the-mlflow-ui "Direct link to Explore model parameters and performance using the MLflow UI")

To explore the model in the MLflow UI:

1. Click **Experiments** in the workspace sidebar.
2. Find your experiment in the experiments list. You can select the **Only my experiments** checkbox or use the **Filter experiments** search box to filter the list.
3. Click the name of your experiment. The **Runs** page opens. The experiment contains two MLflow runs, one used to train the model and one used to evaluate the model.
4. Click the **Models** tab. The `LoggedModel` (`elasticnet`) is tracked on this screen. You can see all of the parameters and metadata, as well as all of the metrics linked from the training and evaluation runs.
5. Click the model name to display the model page, which contains information like the model's parameters and metrics, as well as details such as its source run, relevant datasets, and model versions registered in [Unity Catalog](/concepts/unity-catalog.md).
6. The notebook registers the model to Unity Catalog. All model parameters and performance data are available on the model version page in [Catalog Explorer](/concepts/catalog-explorer.md). You can get to this page directly by clicking on the model version from the MLflow model page. Clicking on the model ID and source run here will bring you back to the MLflow model and run pages respectively.

^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Difference between the Models tab and the model version page in Catalog Explorer[​](#difference-between-the-models-tab-and-the-model-version-page-in-catalog-explorer "Direct link to Difference between the Models tab and the model version page in Catalog Explorer")

The **Models** tab of the [MLflow Experiments|experiment page](/concepts/mlflow-experiment.md) and the model version page in Catalog Explorer show similar information about the model but serve different roles in the model development and deployment lifecycle.

- The **Models** tab of the experiment page presents the results of logged models from an experiment on a single page. The **Charts** tab provides visualizations to help you compare models and select the model versions to register to Unity Catalog for possible deployment.
- In Catalog Explorer, the model version page provides an overview of all model performance and evaluation results. This page shows model parameters, metrics, and traces across all linked environments including different workspaces, endpoints, and experiments. This is useful for monitoring and deployment, and works especially well with [deployment jobs](/concepts/mlflow-deployment-jobs.md). The evaluation task in a deployment job creates additional metrics that appear on this page. The approver for the job can then review this page to assess whether to approve the model version for deployment.

^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Next steps[​](#next-steps "Direct link to Next steps")

To learn more about `LoggedModel` tracking introduced in MLflow 3, see the article on [Track and compare models using MLflow Logged Models](/concepts/mlflow-loggedmodel.md). To learn more about using MLflow 3 with deep learning workflows, see the article on [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md). ^[mlflow-3-traditional-ml-workflow-databricks-on-aws.md]

## Related concepts

- [MLflow Run](/concepts/mlflow-run.md)
- [MLflow Logged Model](/concepts/mlflow-logged-model.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Deployment jobs](/concepts/mlflow-deployment-jobs.md)
- [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md)

## Sources

- mlflow-3-traditional-ml-workflow-databricks-on-aws.md

# Citations

1. [mlflow-3-traditional-ml-workflow-databricks-on-aws.md](/references/mlflow-3-traditional-ml-workflow-databricks-on-aws-faedda9d.md)
