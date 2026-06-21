---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f823f167d52595923e3abc4df72a908feee60171951594fc84d7791e40df9258
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-automl-for-classification
    - DAFC
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: Databricks AutoML for Classification
description: How to use Databricks AutoML to automatically find the best classification algorithm and hyperparameter configuration
tags:
  - machine-learning
  - automl
  - classification
  - databricks
timestamp: "2026-06-19T09:13:37.663Z"
---

# Databricks AutoML for Classification

**Databricks AutoML for Classification** automates the process of finding the best classification algorithm and hyperparameter configuration for predicting the label or category of a given input. It is a core feature of the Databricks platform designed to accelerate machine learning workflows by automatically training, evaluating, and ranking candidate models. ^[classification-with-automl-databricks-on-aws.md]

## Setting Up a Classification Experiment

### Using the UI

To set up a classification problem using the AutoML UI, navigate to the **Experiments** page in the sidebar and select **Start training** on the **Classification** card. On the **Configure AutoML experiment page**, you configure the AutoML process by specifying the dataset, problem type, target or label column to predict, the evaluation metric, and stopping conditions. ^[classification-with-automl-databricks-on-aws.md]

In the **Compute** field, select a cluster running Databricks Runtime ML. Under **Dataset**, browse to and select the table you want to use; the table schema appears after selection. From Databricks Runtime 10.3 ML and above, you can specify which columns AutoML should use for training — you cannot remove the column selected as the prediction target or the time column used for splitting data. From Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed using the **Impute with** dropdown; otherwise, AutoML selects a default imputation method based on column type and content. ^[classification-with-automl-databricks-on-aws.md]

Click in the **Prediction target** field, select the column you want the model to predict from the dropdown, and optionally change the experiment name. From the **Advanced Configuration (optional)** section, you can set the primary evaluation metric, exclude training frameworks from consideration (from Databricks Runtime 10.4 LTS ML and above), and edit stopping conditions. Default stopping conditions for classification experiments are a 60-minute time limit (or 200 trials in Databricks Runtime 10.4 LTS ML and below; from Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition). AutoML also incorporates early stopping when the validation metric is no longer improving. ^[classification-with-automl-databricks-on-aws.md]

You can also select a time column to split the data for training, validation, and testing in chronological order, and specify a **Data directory** (leaving it empty triggers the default behavior of securely storing the dataset as an MLflow artifact). ^[classification-with-automl-databricks-on-aws.md]

## Running the Experiment and Monitoring Results

To start the AutoML experiment, click **Start AutoML**. The AutoML training page appears, from which you can stop the experiment at any time, open the data exploration notebook, monitor runs, and navigate to individual run pages. From Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential dataset issues such as unsupported column types or high cardinality columns; these warnings appear on the **Warnings** tab on the training page or the experiment page after completion. ^[classification-with-automl-databricks-on-aws.md]

## Viewing Results

When the experiment completes, you can register and deploy one of the models with [MLflow](/concepts/mlflow.md), select **View notebook for best model** to review and edit the notebook that created the best model, and select **View data exploration notebook** to open the data exploration notebook. You can also search, filter, and sort runs in the runs table. For any run, clicking into the [MLflow Run](/concepts/mlflow-run.md) reveals the generated notebook saved in the **Artifacts** section; this notebook can be downloaded and imported into the workspace if downloading artifacts is enabled by your workspace administrators. The run page also includes code snippets for making predictions with the model. ^[classification-with-automl-databricks-on-aws.md]

To return to an AutoML experiment later, find it on the Experiments page. The results of each AutoML experiment, including data exploration and training notebooks, are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. ^[classification-with-automl-databricks-on-aws.md]

## Registering and Deploying a Model

To register and deploy a model using the AutoML UI, select the link in the **Models** column for the model you want to register (the top row shows the best model based on the primary metric). Databricks recommends registering models to [Unity Catalog](/concepts/unity-catalog.md) for the latest features. After registration, you can deploy the model to a custom model serving endpoint. ^[classification-with-automl-databricks-on-aws.md]

### Troubleshooting: Pandas Module Compatibility

When serving a model built using AutoML with Model Serving, you may encounter the error: `No module named 'pandas.core.indexes.numeric`. This is caused by an incompatible `pandas` version between AutoML and the model serving endpoint environment. To resolve this, run the `add-pandas-dependency.py` script, which edits the `requirements.txt` and `conda.yaml` for your logged model to include the appropriate `pandas` dependency version (`pandas==1.5.3`). After modifying the script with the `run_id` of the [MLflow Run](/concepts/mlflow-run.md), re-register the model and try serving the new version. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML API Reference — Programmatic interface for classification experiments
- [AutoML Classification Data Preparation](/concepts/automl-classification-data-preparation.md) — Data preparation settings for classification
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management
- [Unity Catalog](/concepts/unity-catalog.md) — Model registry and governance
- [Model Serving](/concepts/model-serving.md) — Deploying models to endpoints
- AutoML Algorithms — Supported training frameworks
- [Feature Store Integration](/concepts/automl-feature-store-integration.md) — Using existing feature tables with AutoML

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
