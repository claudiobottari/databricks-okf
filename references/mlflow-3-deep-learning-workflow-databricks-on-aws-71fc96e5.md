---
title: MLflow 3 deep learning workflow | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/mlflow3-dl-workflow
ingestedAt: "2026-06-18T08:14:05.020Z"
---

## Example notebook[​](#example-notebook "Direct link to Example notebook")

The example notebook runs a single deep learning model training job with PyTorch, which is tracked as an MLflow run. It logs a checkpoint model after every 10 epochs. Each checkpoint is tracked as an MLflow LoggedModel. Using MLflow's UI or search API, you can inspect the checkpoint models and rank them by accuracy.

The notebook installs the `scikit-learn` and `torch` libraries.

#### MLflow 3 deep learning model with checkpoints notebook

## Use the UI to explore model performance and register a model[​](#use-the-ui-to-explore-model-performance-and-register-a-model "Direct link to Use the UI to explore model performance and register a model")

After running the notebook, you can view the saved checkpoint models in the MLflow experiments UI. A link to the experiment appears in the notebook cell output, or follow these steps:

1.  Click **Experiments** in the workspace sidebar.
    
2.  Find your experiment in the experiments list. You can select the **Only my experiments** checkbox or use the **Filter experiments** search box to filter the list of experiments.
    
3.  Click the name of your experiment. The **Runs** page opens. The experiment contains one MLflow run.
    
    ![MLflow 3 runs tab showing a deep learning training run.](https://docs.databricks.com/aws/en/assets/images/mlflow3-dl-runs-93444632391a5bffda7fbc8b547ae8bc.png)
    
4.  Click the **Models** tab. The individual checkpoint models are tracked on this screen. For each checkpoint, you can see the model's accuracy, along with all of its parameters and metadata.
    
    ![MLflow 3 models tab for a deep learning run shows all saved checkpoint models.](https://docs.databricks.com/aws/en/assets/images/mlflow3-dl-models-3a27c6fb4062e7f7c436ba2664b9cdb9.png)
    

In the example notebook, you registered the best performing model to Unity Catalog. You can also register a model from the UI. To do so, follow these steps:

1.  From the **Models** tab, click the name of the model to register.
    
2.  From the model details page, in the upper-right corner, click **Register model**.
    
    tip
    
    It can take a few minutes for a model to appear in the UI after registering it. Do not press the **Register model** more than once, otherwise you will register duplicate models.
    
    ![Register model button on model details page.](https://docs.databricks.com/aws/en/assets/images/mlflow3-register-model-c22c9c102a318810ebae87e2a6cd2128.png)
    
3.  Select **Unity Catalog** and either select an existing model name from the drop-down menu or type in a new name.
    
    ![Register model dialog.](https://docs.databricks.com/aws/en/assets/images/register-model-dialog-cb24a802d0694204b112682ac8d01fab.png)
    
4.  Click **Register**.
    

## Use the API to rank checkpoint models[​](#use-the-api-to-rank-checkpoint-models "Direct link to Use the API to rank checkpoint models")

The following code shows how to rank the checkpoint models by accuracy. For more details on searching logged models using the API, see [Search and filter Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model#search-and-filter-logged-models).

Python

    ranked_checkpoints = mlflow.search_logged_models(  output_format="list",  order_by=[{"field_name": "metrics.accuracy", "ascending": False}])best_checkpoint: mlflow.entities.LoggedModel = ranked_checkpoints[0]print(best_checkpoint.metrics[0])<Metric:  dataset_digest='9951783d',  dataset_name='train',  key='accuracy',  model_id='m-bba8fa52b6a6499281c43ef17fcdac84',  run_id='394928abe6fc4787aaf4e666ac89dc8a',  step=90,  timestamp=1730828771880,  value=0.9553571428571429>worst_checkpoint: mlflow.entities.LoggedModel = ranked_checkpoints[-1]print(worst_checkpoint.metrics[0])<Metric:  dataset_digest='9951783d',  dataset_name='train',  key='accuracy',  model_id='m-88885bc26de7492f908069cfe15a1499',  run_id='394928abe6fc4787aaf4e666ac89dc8a',  step=0,  timestamp=1730828730040,  value=0.35714285714285715

## What's the difference between the **Models** tab on the MLflow experiment page and the model version page in Catalog Explorer?[​](#whats-the-difference-between-the-models-tab-on-the-mlflow-experiment-page-and-the-model-version-page-in-catalog-explorer "Direct link to whats-the-difference-between-the-models-tab-on-the-mlflow-experiment-page-and-the-model-version-page-in-catalog-explorer")

The **Models** tab of the [experiment page](https://docs.databricks.com/aws/en/mlflow/experiments) and the model version page in [Catalog Explorer](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#ui) show similar information about the model. The two views have different roles in the model development and deployment lifecycle.

*   The **Models** tab of the experiment page presents the results of logged models from an experiment on a single page. The [Charts tab](https://docs.databricks.com/aws/en/mlflow/visualize-runs) on this page provides visualizations to help you compare models and select the model versions to register to Unity Catalog for possible deployment.
*   In Catalog Explorer, the model version page provides an overview of all model performance and evaluation results. This page shows model parameters, metrics, and traces across all linked environments including different workspaces, endpoints, and experiments. This is useful for monitoring and deployment, and works especially well with [deployment jobs](https://docs.databricks.com/aws/en/mlflow/deployment-job). The evaluation task in a deployment job creates additional metrics that appear on this page. The approver for the job can then review this page to assess whether to approve the model version for deployment.

## Next steps[​](#next-steps "Direct link to Next steps")

To learn more about `LoggedModel` tracking introduced in MLflow 3, see the following article:

*   [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).

To learn more about using MLflow 3 with traditional ML workflows, see the following article:

*   [MLflow 3 traditional ML workflow](https://docs.databricks.com/aws/en/mlflow/mlflow3-ml-workflow).
