---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 117c8bd7a26a0c891b7c4a2e82667bfe3d109488724217694df7acf3c0dd7427
  pageDirectory: concepts
  sources:
    - regression-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-configuration
    - AEC
  citations:
    - file: regression-with-automl-databricks-on-aws.md
title: AutoML Experiment Configuration
description: Setup process for configuring an AutoML experiment including compute, dataset, prediction target, and advanced options
tags:
  - automl
  - configuration
  - databricks
timestamp: "2026-06-19T20:13:20.726Z"
---

# AutoML Experiment Configuration

**AutoML Experiment Configuration** refers to the settings and parameters used to define and run an automated machine learning (AutoML) experiment on Databricks. Using the AutoML UI, you can configure the problem type, dataset, prediction target, evaluation metric, training frameworks, stopping conditions, and data splitting behavior. The configuration process is illustrated here for a regression problem, but similar steps apply to classification and [forecasting](/concepts/forecast.md) experiments. ^[regression-with-automl-databricks-on-aws.md]

## Setting Up an Experiment with the UI

To create an AutoML experiment for regression, navigate to the **Experiments** sidebar and select **Start training** on the **Regression** card. The **Configure AutoML experiment page** opens, where you specify the following: ^[regression-with-automl-databricks-on-aws.md]

- **Compute** – Select a cluster running Databricks Runtime ML.
- **Dataset** – Browse to the table you want to use. The table schema appears after selection. In Databricks Runtime 10.3 ML and above, you can [specify which columns to use for training](https://docs.databricks.com/aws/en/machine-learning/automl/regression-data-prep#column-select); the prediction target column and the time column (if used) cannot be removed. In Databricks Runtime 10.4 LTS ML and above, you can choose how null values are imputed via the **Impute with** dropdown. ^[regression-with-automl-databricks-on-aws.md]
- **Prediction target** – Select the column the model should predict (the label column).
- **Experiment name** – A default name is provided; you can change it.

Optionally, you can open the **Advanced Configuration** section to adjust additional parameters or use existing feature tables from [Feature Store](/concepts/feature-store.md) to augment the input dataset. ^[regression-with-automl-databricks-on-aws.md]

## Advanced Configurations

The **Advanced Configuration (optional)** section exposes the following settings: ^[regression-with-automl-databricks-on-aws.md]

- **Evaluation metric** – The primary metric used to score runs (see the [AutoML API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference) for available metrics).
- **Exclude training frameworks** – In Databricks Runtime 10.4 LTS ML and above, you can exclude certain frameworks from the AutoML trial process. By default, all frameworks listed under AutoML algorithms are included.
- **Stopping conditions** – Control when AutoML stops training. Defaults:
  - For forecasting experiments: stop after 120 minutes.
  - For classification and regression experiments in Databricks Runtime 10.4 LTS ML and below: stop after 60 minutes or after 200 trials, whichever comes first. In Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition.
  - In Databricks Runtime 10.4 LTS ML and above, early stopping is enabled; AutoML stops training if the validation metric stops improving.
- **Time column** – In Databricks Runtime 10.4 LTS ML and above, you can select a time column to split the data into training, validation, and test sets in chronological order (applies to classification and regression).
- **Data directory** – Databricks recommends leaving this field empty. The default behavior stores the dataset securely as an [MLflow](/concepts/mlflow.md) artifact. If a DBFS path is specified, the dataset does not inherit the AutoML experiment's access permissions.

## Running the Experiment and Monitoring Results

Click **Start AutoML** to begin the experiment. The AutoML training page appears, where you can: ^[regression-with-automl-databricks-on-aws.md]

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual trial runs.
- Navigate to any run’s detail page.
- View warnings (Databricks Runtime 10.1 ML and above) about potential dataset issues such as unsupported column types or high cardinality columns.

The warnings tab appears on the training page and on the experiment page after the experiment completes. ^[regression-with-automl-databricks-on-aws.md]

## Viewing Results

When the experiment completes, you can: ^[regression-with-automl-databricks-on-aws.md]

- **Register and deploy** a model via the UI.
- **View notebook for best model** to review and edit the notebook that produced the best run.
- **View data exploration notebook**.
- **Search, filter, and sort** runs in the runs table.
- **View run details** – Click on a run’s **Models** or **Start Time** column to see parameters, metrics, tags, artifacts (including the generated notebook), and code snippets for making predictions.

The results of every AutoML experiment, including both the data exploration notebook and the training notebooks, are stored in a `databricks_automl` folder in the user’s [home folder](https://docs.databricks.com/aws/en/workspace/workspace-browser#home-folder). ^[regression-with-automl-databricks-on-aws.md]

## Registering and Deploying a Model

After a run completes, the best model (based on the primary metric) appears in the top row of the runs table. To register and deploy: ^[regression-with-automl-databricks-on-aws.md]

1. Select the link in the **Models** column.
2. Click the register button to save the model to [Unity Catalog](/concepts/unity-catalog.md) or to the [Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends using Unity Catalog for the latest features.
3. After registration, deploy the model to a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md) via [Model Serving](/concepts/model-serving.md).

### Troubleshooting: Missing pandas Dependency

When serving an AutoML-built model with Model Serving, you may encounter: ^[regression-with-automl-databricks-on-aws.md]

```
No module named 'pandas.core.indexes.numeric
```

This is caused by an incompatible `pandas` version between the AutoML environment and the serving endpoint. The fix is to run the [`add-pandas-dependency.py` script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py), which edits the logged model’s `requirements.txt` and `conda.yaml` to include `pandas==1.5.3`. After running the script, re-register the model and redeploy it. ^[regression-with-automl-databricks-on-aws.md]

## Related Concepts

- [Regression](/concepts/automl-regress-api.md) – The problem type demonstrated in the source material.
- [Classification](/concepts/data-classification.md) and [Forecasting](/concepts/forecast.md) – Other AutoML problem types with similar configuration UIs.
- AutoML algorithms – The list of frameworks considered by AutoML.
- [Feature Store](/concepts/feature-store.md) – Used to augment the input dataset with existing feature tables.
- [MLflow](/concepts/mlflow.md) – Tracks experiment runs, models, and artifacts.
- [Unity Catalog](/concepts/unity-catalog.md) – Recommended model registry destination for AutoML models.
- [Model Serving](/concepts/model-serving.md) – Deployment endpoint for registered models.

## Sources

- regression-with-automl-databricks-on-aws.md

# Citations

1. [regression-with-automl-databricks-on-aws.md](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
