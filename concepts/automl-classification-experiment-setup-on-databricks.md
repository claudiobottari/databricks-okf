---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ffbdca84173f717073f9643b6879c6b8c845eba682962c7c88c0f1beebe5b06
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-classification-experiment-setup-on-databricks
    - ACESOD
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Classification Experiment Setup on Databricks
description: GUI-based workflow to configure and launch a classification experiment using AutoML on Databricks, including dataset selection, prediction target, and compute specification.
tags:
  - databricks
  - automl
  - classification
  - experiment-setup
timestamp: "2026-06-18T14:35:55.518Z"
---

# AutoML Classification Experiment Setup on Databricks

**AutoML Classification Experiment Setup on Databricks** refers to the process of using the Databricks AutoML UI to automatically find the best classification algorithm and hyperparameter configuration for predicting a label or category from a given input dataset. This feature is available on Databricks Runtime ML clusters.

## Overview

The AutoML classification experiment automates the search for the optimal machine learning model for classification problems. Users configure the experiment through the UI by specifying a dataset, a prediction target column, evaluation metrics, and stopping conditions. AutoML then trains multiple models using various algorithms and tunes hyperparameters to find the best performing configuration. ^[classification-with-automl-databricks-on-aws.md]

## Setting Up a Classification Experiment via the UI

### Prerequisites

Before setting up an AutoML classification experiment, you need:

- A cluster running [Databricks Runtime ML](/concepts/databricks-runtime-for-machine-learning.md)
- A table or dataset to use for training

### Step-by-Step Configuration

1. In the sidebar, select **Experiments**.
2. In the **Classification** card, select **Start training**. The **Configure AutoML experiment page** displays.
3. In the **Compute** field, select a cluster running Databricks Runtime ML.
4. Under **Dataset**, select **Browse** and navigate to the table you want to use. The table schema appears after selection. ^[classification-with-automl-databricks-on-aws.md]

   - In Databricks Runtime 10.3 ML and above, you can specify which columns AutoML should use for training. You cannot remove the column selected as the prediction target or the time column used to split the data.
   - In Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed by selecting from the **Impute with** dropdown. By default, AutoML selects an imputation method based on the column type and content. ^[classification-with-automl-databricks-on-aws.md]

5. Click in the **Prediction target** field and select the column you want the model to predict from the dropdown list of columns shown in the schema.
6. The **Experiment name** field shows a default name. To change it, type a new name in the field. ^[classification-with-automl-databricks-on-aws.md]

### Additional Configuration Options

You can also:

- Use existing feature tables in [Feature Store](/concepts/feature-store.md) to augment the original input dataset.
- Specify advanced configuration parameters by opening the **Advanced Configuration (optional)** section. ^[classification-with-automl-databricks-on-aws.md]

### Advanced Configuration Parameters

- **Evaluation metric**: The primary metric used to score the runs.
- **Excluded training frameworks**: In Databricks Runtime 10.4 LTS ML and above, you can exclude training frameworks from consideration. By default, AutoML trains models using the frameworks listed under AutoML algorithms. ^[classification-with-automl-databricks-on-aws.md]
- **Stopping conditions**: Default stopping conditions vary by runtime version:
  - For forecasting experiments: stop after 120 minutes.
  - In Databricks Runtime 10.4 LTS ML and below, for classification and regression experiments: stop after 60 minutes or after completing 200 trials, whichever happens first.
  - In Databricks Runtime 11.0 ML and above: the number of trials is not used as a stopping condition.
  - In Databricks Runtime 10.4 LTS ML and above: AutoML incorporates early stopping, stopping training and tuning if the validation metric is no longer improving. ^[classification-with-automl-databricks-on-aws.md]
- **Time column**: In Databricks Runtime 10.4 LTS ML and above, you can select a `time column` to split the data for training, validation, and testing in chronological order (applies to classification and regression experiments). ^[classification-with-automl-databricks-on-aws.md]
- **Data directory**: Databricks recommends leaving this field empty. Not populating it triggers the default behavior of securely storing the dataset as an MLflow artifact. A DBFS path can be specified, but in this case, the dataset does not inherit the AutoML experiment's access permissions. ^[classification-with-automl-databricks-on-aws.md]

## Running the Experiment and Monitoring Results

To start the AutoML experiment, click **Start AutoML**. The experiment begins running, and the AutoML training page appears. From this page, you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor runs.
- Navigate to the run page for any run. ^[classification-with-automl-databricks-on-aws.md]

With Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential issues with the dataset, such as unsupported column types or high cardinality columns. To see any warnings, click the **Warnings** tab on the training page or the experiment page after the experiment completes. ^[classification-with-automl-databricks-on-aws.md]

## Viewing Results

When the experiment completes, you can:

- Register and deploy one of the models with MLflow.
- Select **View notebook for best model** to review and edit the notebook that created the best model.
- Select **View data exploration notebook** to open the data exploration notebook.
- Search, filter, and sort the runs in the runs table.
- See details for any run, including the generated notebook containing source code found in the **Artifacts** section of the run page. You can download this notebook and import it into the workspace, if downloading artifacts is enabled by your workspace administrators.
- Click in the **Models** column or the **Start Time** column to view run results, including parameters, metrics, tags, and artifacts such as the model. This page also includes code snippets for making predictions with the model. ^[classification-with-automl-databricks-on-aws.md]

To return to an AutoML experiment later, find it in the table on the [Experiments page](/concepts/mlflow-experiment.md). The results of each AutoML experiment, including the data exploration and training notebooks, are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. ^[classification-with-automl-databricks-on-aws.md]

## Registering and Deploying a Model

Register and deploy your model using the AutoML UI. When a run completes, the top row shows the best model based on the primary metric.

1. Select the link in the **Models** column for the model you want to register.
2. Select the register model button to register it to [Unity Catalog](/concepts/unity-catalog.md) or [Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends registering models to Unity Catalog for the latest features.
3. After registration, you can deploy the model to a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md). ^[classification-with-automl-databricks-on-aws.md]

### Troubleshooting: Pandas Compatibility Error

When serving a model built using AutoML with [Model Serving](/concepts/model-serving.md), you may encounter the error: `No module named 'pandas.core.indexes.numeric`. This is due to an incompatible pandas version between AutoML and the model serving endpoint environment. To resolve this error, run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py), which edits the `requirements.txt` and `conda.yaml` for your logged model to include the appropriate pandas dependency version (`pandas==1.5.3`). After modifying the script to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where your model was logged, re-register the model and try serving the new version. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML Classification API](/concepts/automl-classification-classify.md) - Programmatic setup using the classification API
- [Classification Data Preparation Settings](/concepts/automl-classification-data-preparation.md) - Details on data preparation options
- AutoML Algorithms - The list of algorithms AutoML uses for training
- [MLflow Experiments](/concepts/mlflow-experiment.md) - Organizing and tracking AutoML experiment runs
- [Feature Store Integration with AutoML](/concepts/automl-feature-store-integration.md) - Using feature tables to augment datasets

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
