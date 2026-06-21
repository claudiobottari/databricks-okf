---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4af1fb316c67422402aa2cce9db2570a835fbd1b7816c0abe5ad7fa09ccfe27c
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-classification-on-databricks
    - ACOD
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Classification on Databricks
description: Automated machine learning service on Databricks that automatically finds the best classification algorithm and hyperparameter configuration to predict a label or category from input data.
tags:
  - machine-learning
  - automl
  - classification
  - databricks
timestamp: "2026-06-19T14:12:08.508Z"
---

# AutoML Classification on Databricks

**AutoML Classification on Databricks** is a feature that automatically finds the best classification algorithm and hyperparameter configuration to predict the label or category of a given input. It trains and evaluates multiple models, selecting the top performer based on a primary evaluation metric.^[classification-with-automl-databricks-on-aws.md]

## Setting Up a Classification Experiment with the UI

You can set up a classification experiment using the AutoML UI in the Databricks workspace:

1. In the sidebar, select **Experiments**.
2. In the **Classification** card, select **Start training**.
3. In the **Compute** field, select a cluster running [Databricks Runtime ML](/concepts/databricks-runtime-ml.md).
4. Under **Dataset**, select **Browse** to navigate to the table you want to use. The table schema appears.
5. Click in the **Prediction target** field and select the column you want the model to predict.
6. The **Experiment name** field shows a default name, which you can change.

Additional options include specifying which columns AutoML should use for training (Databricks Runtime 10.3 ML and above), configuring how null values are imputed (Databricks Runtime 10.4 LTS ML and above), and using existing feature tables from the [Feature Store](/concepts/feature-store.md) to augment the input dataset.^[classification-with-automl-databricks-on-aws.md]

## Advanced Configuration Options

The **Advanced Configuration (optional)** section provides access to the following parameters:

- **Evaluation metric**: The primary metric used to score the runs. See the AutoML API Reference for available metrics.
- **Excluded training frameworks**: In Databricks Runtime 10.4 LTS ML and above, you can exclude specific training frameworks from consideration.
- **Stopping conditions**: Default stopping conditions are 60 minutes (or 200 trials in Databricks Runtime 10.4 LTS ML and below; Databricks Runtime 11.0 ML and above no longer uses trial count as a stopping condition). For forecasting experiments, the default is 120 minutes.
- **Early stopping**: Available in Databricks Runtime 10.4 LTS ML and above for classification and regression experiments. AutoML stops training if the validation metric is no longer improving.
- **Time column for data splitting**: Available in Databricks Runtime 10.4 LTS ML and above, you can select a time column to split data chronologically for training, validation, and testing.
- **Data directory**: Databricks recommends leaving this field empty to securely store the dataset as an [MLflow](/concepts/mlflow.md) artifact. A DBFS path can be specified but does not inherit the AutoML experiment's access permissions.^[classification-with-automl-databricks-on-aws.md]

## Running the Experiment and Monitoring Results

To start the experiment, click **Start AutoML**. The AutoML training page displays, showing the runs table. From this page you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs and navigate to their run pages.
- View warnings for potential dataset issues (Databricks Runtime 10.1 ML and above), such as unsupported column types or high cardinality columns, accessible via the **Warnings** tab.^[classification-with-automl-databricks-on-aws.md]

## Viewing Results

When the experiment completes, you can:

- Register and deploy one of the trained models with [MLflow](/concepts/mlflow.md).
- Select **View notebook for best model** to review and edit the notebook that created the best model.
- Select **View data exploration notebook** to open the data exploration notebook.
- Search, filter, and sort runs in the runs table.
- View details for any run, including parameters, metrics, tags, and artifacts such as the model.

The results of each AutoML experiment, including the data exploration and training notebooks, are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment.^[classification-with-automl-databricks-on-aws.md]

## Registering and Deploying a Model

To register and deploy a model using the AutoML UI:

1. When a run completes, select the link in the **Models** column for the model you want to register.
2. Select the register model button to register it to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends registering models to Unity Catalog for the latest features.
3. After registration, you can deploy the model to a custom [Model Serving](/concepts/model-serving.md) endpoint.^[classification-with-automl-databricks-on-aws.md]

### Troubleshooting: No module named 'pandas.core.indexes.numeric'

When serving a model built using AutoML with Model Serving, you may encounter the error `No module named 'pandas.core.indexes.numeric`. This is caused by an incompatible `pandas` version between AutoML and the model serving endpoint environment. To resolve:

1. Run the `add-pandas-dependency.py` script, which edits the `requirements.txt` and `conda.yaml` files for the logged model to include `pandas==1.5.3`.
2. Modify the script to include the `run_id` of the [MLflow](/concepts/mlflow.md) run where your model was logged.
3. Re-register the model to Unity Catalog or the model registry.
4. Try serving the new version of the MLflow model.^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML Regression on Databricks](/concepts/automl-on-databricks.md) — The regression counterpart to AutoML Classification
- [AutoML Forecasting on Databricks](/concepts/automl-forecasting-forecast.md) — Time-series forecasting using AutoML
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The logging component that records AutoML experiment results
- [MLflow PySpark ML Autologging](/concepts/mlflow-pyspark-ml-autologging.md) — Automated MLflow tracking for PySpark ML models
- [Feature Store](/concepts/feature-store.md) — Feature management for machine learning
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The optimized runtime for ML workloads

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
