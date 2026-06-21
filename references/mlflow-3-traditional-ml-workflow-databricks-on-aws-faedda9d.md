---
title: MLflow 3 traditional ML workflow | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/mlflow3-ml-workflow
ingestedAt: "2026-06-18T08:14:08.234Z"
---

## Example notebook[​](#example-notebook "Direct link to Example notebook")

The example notebook runs a model training job, which is tracked as an MLflow Run, to produce a trained model, which is tracked as an [MLflow Logged Model](https://docs.databricks.com/aws/en/mlflow/logged-model).

#### MLflow 3 traditional ML model notebook

## Explore model parameters and performance using the MLflow UI[​](#explore-model-parameters-and-performance-using-the-mlflow-ui "Direct link to Explore model parameters and performance using the MLflow UI")

To explore the model in the MLflow UI:

1.  Click **Experiments** in the workspace sidebar.
    
2.  Find your experiment in the experiments list. You can select the **Only my experiments** checkbox or use the **Filter experiments** search box to filter the list of experiments.
    
3.  Click the name of your experiment. The **Runs** page opens. The experiment contains two MLflow runs, one used to train the model and one used to evaluate the model.
    
    ![MLflow 3 runs tab showing training and test runs.](https://docs.databricks.com/aws/en/assets/images/mlflow3-ml-runs-e434bb1d8938792ad88d2889f19d4b78.png)
    
4.  Click the **Models** tab. The `LoggedModel` (`elasticnet`) is tracked on this screen. You can see all of the parameters and metadata, as well as all of the metrics linked from the training and evaluation runs.
    
    ![MLflow 3 models tab showing trained model with metrics and parameters.](https://docs.databricks.com/aws/en/assets/images/mlflow3-ml-models-903b93c36bf0d259843274b2baac1d0d.png)
    
5.  Click the model name to display the model page, which contains information like the model's parameters and metrics, as well as details such as its source run, relevant datasets, and model versions registered in Unity Catalog.
    
    ![MLflow 3 model details page.](https://docs.databricks.com/aws/en/assets/images/mlflow3-logged-model-16894ae892e1dba1946beca467828fb8.png)
    
6.  The notebook registers the model to Unity Catalog. As a result, all model parameters and performance data are available on the model version page in Catalog Explorer. You can get to this page directly by clicking on the model version from the MLflow model page. Clicking on the model ID and source run here will bring you back to the MLflow model and run pages respectively.
    
    ![Model version page in Catalog Explorer.](https://docs.databricks.com/aws/en/assets/images/mlflow3-model-version-page-3bef0948f25abb51b63eb489ea55e01f.png)
    

## What's the difference between the **Models** tab on the MLflow experiment page and the model version page in Catalog Explorer?[​](#whats-the-difference-between-the-models-tab-on-the-mlflow-experiment-page-and-the-model-version-page-in-catalog-explorer "Direct link to whats-the-difference-between-the-models-tab-on-the-mlflow-experiment-page-and-the-model-version-page-in-catalog-explorer")

The **Models** tab of the [experiment page](https://docs.databricks.com/aws/en/mlflow/experiments) and the model version page in [Catalog Explorer](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#ui) show similar information about the model. The two views have different roles in the model development and deployment lifecycle.

*   The **Models** tab of the experiment page presents the results of logged models from an experiment on a single page. The [Charts tab](https://docs.databricks.com/aws/en/mlflow/visualize-runs) on this page provides visualizations to help you compare models and select the model versions to register to Unity Catalog for possible deployment.
*   In Catalog Explorer, the model version page provides an overview of all model performance and evaluation results. This page shows model parameters, metrics, and traces across all linked environments including different workspaces, endpoints, and experiments. This is useful for monitoring and deployment, and works especially well with [deployment jobs](https://docs.databricks.com/aws/en/mlflow/deployment-job). The evaluation task in a deployment job creates additional metrics that appear on this page. The approver for the job can then review this page to assess whether to approve the model version for deployment.

## Next steps[​](#next-steps "Direct link to Next steps")

To learn more about `LoggedModel` tracking introduced in MLflow 3, see the following article:

*   [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).

To learn more about using MLflow 3 with deep learning workflows, see the following article:

*   [MLflow 3 deep learning workflow](https://docs.databricks.com/aws/en/mlflow/mlflow3-dl-workflow).
