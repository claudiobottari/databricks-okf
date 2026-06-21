---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0f3ebc5ad8709134c677b37dc219ca7f07ae13a5219bf5773bed6251e315345
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-configuration-via-ui
    - AECVU
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Experiment Configuration via UI
description: Step-by-step process for setting up a classification experiment using the AutoML user interface in Databricks
tags:
  - automl
  - ui-configuration
  - classification
  - databricks
timestamp: "2026-06-19T09:12:46.173Z"
---

# AutoML Experiment Configuration via UI

**AutoML Experiment Configuration via UI** refers to the process of setting up, running, and monitoring an AutoML experiment through the graphical interface in Databricks, specifically for classification problems. This approach allows users to configure dataset selection, target prediction, compute resources, and advanced options without writing code. ^[classification-with-automl-databricks-on-aws.md]

## Setting up a classification experiment

To begin a classification experiment using the AutoML UI, navigate to **Experiments** in the sidebar and select **Start training** on the **Classification** card. The **Configure AutoML experiment page** displays, where you specify the dataset, problem type, target column, evaluation metric, and stopping conditions. ^[classification-with-automl-databricks-on-aws.md]

In the **Compute** field, select a cluster running Databricks Runtime ML. Under **Dataset**, click **Browse** to navigate to the desired table and click **Select**. The table schema appears. Starting with Databricks Runtime 10.3 ML and above, you can specify which columns AutoML should use for training, but you cannot remove the column selected as the prediction target or the time column used to split the data. Starting with Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed using the **Impute with** dropdown; by default, AutoML selects an imputation method based on the column type and content. ^[classification-with-automl-databricks-on-aws.md]

Click in the **Prediction target** field to see a drop-down of all schema columns, and select the column the model should predict. The **Experiment name** field shows a default name, which can be changed by typing a new name. ^[classification-with-automl-databricks-on-aws.md]

## Advanced configurations

Open the **Advanced Configuration (optional)** section to access additional parameters:

- **Evaluation metric** – The primary metric used to score the runs (see the [Automl API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference) for options).
- **Exclude training frameworks** – Starting with Databricks Runtime 10.4 LTS ML and above, you can exclude certain frameworks from consideration. By default, AutoML trains models using the frameworks listed under [AutoML algorithms](https://docs.databricks.com/aws/en/machine-learning/automl/#automl-algorithm).
- **Stopping conditions** – Defaults:
  - For forecasting experiments: stop after 120 minutes.
  - For classification and regression experiments in Databricks Runtime 10.4 LTS ML and below: stop after 60 minutes or after 200 trials, whichever comes first. In Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition.
  - In Databricks Runtime 10.4 LTS ML and above, AutoML incorporates early stopping; it stops training and tuning models if the validation metric is no longer improving.
- **Time column** – Starting with Databricks Runtime 10.4 LTS ML and above, you can select a time column to split the data for training, validation, and testing in chronological order (applies to classification and regression).
- **Data directory** – Databricks recommends leaving this field empty, which triggers the default behavior of securely storing the dataset as an MLflow artifact. If a DBFS path is specified, the dataset does not inherit the AutoML experiment's access permissions. ^[classification-with-automl-databricks-on-aws.md]

## Running the experiment and monitoring results

Click **Start AutoML** to begin the experiment. The AutoML training page appears with a runs table that can be refreshed. From this page you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor runs and navigate to the run page for any run.
- View warnings (starting with Databricks Runtime 10.1 ML and above) for potential dataset issues such as unsupported column types or high cardinality columns. Warnings appear on the **Warnings** tab on the training page or experiment page after completion. ^[classification-with-automl-databricks-on-aws.md]

## Viewing results

When the experiment completes, you can:

- Register and deploy one of the models with MLflow.
- Select **View notebook for best model** to review and edit the notebook that created the best model.
- Select **View data exploration notebook** to open the data exploration notebook.
- Search, filter, and sort runs in the runs table.
- See details for any run: the generated notebook containing source code for a trial run is saved in the **Artifacts** section of the run page. If artifact downloading is enabled by workspace administrators, you can download this notebook and import it into the workspace.
- To view run results, click in the **Models** column or the **Start Time** column. The run page shows parameters, metrics, tags, and artifacts (including the model), along with code snippets for making predictions. ^[classification-with-automl-databricks-on-aws.md]

To return to the experiment later, find it in the table on the [Experiments page](https://docs.databricks.com/aws/en/mlflow/experiments). The results of each AutoML experiment, including the data exploration and training notebooks, are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. ^[classification-with-automl-databricks-on-aws.md]

## Registering and deploying a model

After a run completes, the top row shows the best model based on the primary metric. To register:

1. Select the link in the **Models** column for the desired model.
2. Click the register model button to register it to Unity Catalog or the [Model Registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/). Databricks recommends registering models to Unity Catalog for the latest features.
3. After registration, you can deploy the model to a [custom model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints). ^[classification-with-automl-databricks-on-aws.md]

### Troubleshooting: No module named 'pandas.core.indexes.numeric'

When serving a model built using AutoML with Model Serving, you may encounter the error: `No module named 'pandas.core.indexes.numeric`. This is due to an incompatible `pandas` version between AutoML and the model serving endpoint environment. To resolve, run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py). The script edits the `requirements.txt` and `conda.yaml` for the logged model to include the appropriate pandas dependency version: `pandas==1.5.3`. After modifying the script with the `run_id` of the [MLflow Run](/concepts/mlflow-run.md), re-register the model to Unity Catalog or the model registry, then try serving the new version. ^[classification-with-automl-databricks-on-aws.md]

## Related concepts

- [AutoML API for classification](/concepts/automl-classification-classify.md)
- [AutoML Data Preparation Settings](/concepts/automl-data-preparation-settings.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog for Model Registration](/concepts/unity-catalog-for-model-registration.md)
- [Model Serving with Databricks](/concepts/model-serving-on-databricks.md)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
