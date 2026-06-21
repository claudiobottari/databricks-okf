---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f50d5ab5320c6133400d99b4b6ce2f16f3c01da404f9e2843f87237fb57e24b
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-classification-experiment-setup
    - ACES
    - AutoML Experiment Setup
    - AutoML experiment setup
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Classification Experiment Setup
description: Step-by-step process for configuring and launching a classification experiment using the Databricks AutoML UI
tags:
  - databricks
  - automl
  - classification
  - ui-workflow
timestamp: "2026-06-19T17:43:24.801Z"
---

# AutoML Classification Experiment Setup

**AutoML Classification Experiment Setup** describes how to configure and run an automated machine learning experiment to find the best classification algorithm and hyperparameter configuration for predicting a label or category from tabular data. The setup is performed through the Databricks AutoML user interface (UI) and is designed to streamline the model development process. ^[classification-with-automl-databricks-on-aws.md]

## Set Up a Classification Experiment with the UI

To create a classification experiment using the AutoML UI:

1. In the sidebar, select **Experiments**.
2. On the **Classification** card, click **Start training**.
3. On the **Configure AutoML experiment page**, specify the dataset, problem type, target column, evaluation metric, and stopping conditions.
4. In the **Compute** field, select a cluster running [Databricks Runtime ML](/concepts/databricks-runtime-ml.md).
5. Under **Dataset**, click **Browse** and navigate to the desired table. After selecting it, the table schema appears.
   - In Databricks Runtime 10.3 ML and above, you can specify which columns AutoML should use for training. The prediction target column and the time column (if used for splitting) cannot be removed.
   - In Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed using the **Impute with** dropdown. AutoML selects a default method based on column type and content.
6. Click the **Prediction target** field and select the column the model should predict.
7. Optionally, change the **Experiment name**.

Additional options include using existing feature tables from [Feature Store](/concepts/feature-store.md) to augment the dataset, and opening the **Advanced Configuration (optional)** section to fine-tune the experiment. ^[classification-with-automl-databricks-on-aws.md]

## Advanced Configurations

The **Advanced Configuration** section allows you to adjust:

- **Evaluation metric**: The primary metric used to score and compare runs.
- **Excluded training frameworks** (Databricks Runtime 10.4 LTS ML and above): By default, AutoML trains models using the algorithms listed in the [AutoML algorithms](https://docs.databricks.com/aws/en/machine-learning/automl/#automl-algorithm) documentation. You can remove frameworks from consideration.
- **Stopping conditions**: Default values vary by experiment type:
  - For forecasting experiments: stop after 120 minutes.
  - For classification and regression (Databricks Runtime 10.4 LTS ML and below): stop after 60 minutes or after 200 trials, whichever occurs first. In Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition.
  - Early stopping is enabled in Databricks Runtime 10.4 LTS ML and above; training and tuning stop if the validation metric is no longer improving.
- **Time column** (Databricks Runtime 10.4 LTS ML and above): Select a column to split data chronologically into training, validation, and test sets.
- **Data directory**: Databricks recommends leaving this field empty so the dataset is stored securely as an MLflow artifact. If a DBFS path is specified, the dataset does not inherit the AutoML experiment's access permissions. ^[classification-with-automl-databricks-on-aws.md]

## Run the Experiment and Monitor Results

Click **Start AutoML** to begin the experiment. The AutoML training page displays, showing a runs table that can be refreshed. From this page you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs.
- Navigate to the run page for any trial.

With Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential dataset issues such as unsupported column types or high cardinality columns. These warnings appear on a **Warnings** tab during or after the experiment. Databricks notes that the warnings may not be comprehensive. ^[classification-with-automl-databricks-on-aws.md]

## View Results

When the experiment completes, you can:

- Register and deploy one of the models using [MLflow](/concepts/mlflow.md).
- Select **View notebook for best model** to review and edit the notebook that generated the best model.
- Select **View data exploration notebook** to open the exploratory analysis notebook.
- Search, filter, and sort runs in the runs table.
- Click into any run to see its details: the generated notebook is saved in the **Artifacts** section of the [MLflow Run](/concepts/mlflow-run.md) page and can be downloaded (if enabled by workspace administrators). The run page also shows parameters, metrics, tags, the model artifact, and code snippets for making predictions.

All results—including data exploration and training notebooks—are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. The experiment itself appears in the table on the [Experiments page](/concepts/mlflow-experiment.md). ^[classification-with-automl-databricks-on-aws.md]

## Register and Deploy a Model

To register a model from the AutoML UI:

1. In the runs table, click the link in the **Models** column for the best model (based on the primary metric).
2. Click the **Register model** button to save it to [Unity Catalog](/concepts/unity-catalog.md) (recommended) or the [Model Registry](/concepts/mlflow-model-registry.md).
3. After registration, the model can be deployed to a custom model serving endpoint via [Model Serving](/concepts/model-serving.md). ^[classification-with-automl-databricks-on-aws.md]

### Troubleshooting: No module named 'pandas.core.indexes.numeric'

When serving an AutoML-built model with Model Serving, you might encounter the error `No module named 'pandas.core.indexes.numeric`. This is caused by an incompatible `pandas` version between AutoML and the serving endpoint environment. To resolve it:

1. Download and run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py), which edits the `requirements.txt` and `conda.yaml` in the logged model to include `pandas==1.5.3`.
2. Modify the script to use the `run_id` of the [MLflow Run](/concepts/mlflow-run.md) where the model was logged.
3. Re-register the model to Unity Catalog or the model registry.
4. Retry serving the new version. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML – Overview of automated machine learning on Databricks.
- [Classification](/concepts/data-classification.md) – The supervised learning task for categorical outcomes.
- [MLflow](/concepts/mlflow.md) – Platform for managing the machine learning lifecycle.
- [Feature Store](/concepts/feature-store.md) – Tool for feature management and reuse.
- [Unity Catalog](/concepts/unity-catalog.md) – Centralized governance for data and AI assets.
- [Model Serving](/concepts/model-serving.md) – Endpoint deployment for real-time inference.
- [Model Registry](/concepts/mlflow-model-registry.md) – Version control for models.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – Pre-configured runtime for ML workloads.
- DBFS – Databricks File System for data storage.
- [Experiments page](/concepts/mlflow-experiment.md) – Dashboard for tracking ML experiments.

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
