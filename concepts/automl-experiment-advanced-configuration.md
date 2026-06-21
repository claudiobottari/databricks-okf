---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 529129b398fa66d035540d1565fa45e3c61650a6fd2bf0a7a6e7541965a3a80b
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-advanced-configuration
    - AEAC
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: AutoML Experiment Advanced Configuration
description: Additional AutoML configuration options including evaluation metrics selection, framework exclusion, stopping conditions, early stopping, chronological data splitting, and data directory security.
tags:
  - automl
  - configuration
  - databricks
timestamp: "2026-06-19T10:37:32.895Z"
---

# AutoML Experiment Advanced Configuration

**AutoML Experiment Advanced Configuration** refers to the set of optional parameters available when setting up an AutoML experiment in Databricks (classification, regression, or forecasting). These parameters allow you to fine‑tune the training process by choosing evaluation metrics, excluding certain frameworks, adjusting stopping conditions, and controlling data storage behavior. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Prerequisites

The compute cluster must be running Databricks Runtime 10.0 ML or above for forecasting experiments. Classification and regression experiments have similar requirements but may support earlier runtimes. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Basic Experiment Configuration

Before expanding the advanced section, you must configure the core experiment parameters:

- **Compute** – Select a compatible cluster.
- **Dataset** – Browse and select a table.
- **Prediction target** – Choose the column to predict.
- **Time column** – (forecasting) Select the timestamp or date column.
- **Time series identifiers** – (multi‑series forecasting) Columns that define individual time series. If left blank, a single time series is assumed.
- **Forecast horizon and frequency** – Number of time periods to forecast and the unit (e.g., days, months).
- **Output Database** – (Databricks Runtime 11.3 LTS ML and above) Specify a database to save prediction results. Click **Browse** to select a database.
- **Experiment name** – A default name is provided; you may change it.

Once these are set, expand the **Advanced Configuration (optional)** section to access the parameters below. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Advanced Configuration Options

### Evaluation Metric

The evaluation metric is the primary metric used to score and compare trials. Databricks uses this metric to determine the best model. Choose from the available metrics relevant to your problem type (e.g., RMSE for forecasting, F1 for classification). ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Exclude Training Frameworks

By default, AutoML trains models using all frameworks listed in the AutoML algorithms documentation. In Databricks Runtime 10.4 LTS ML and above, you can exclude specific frameworks from consideration. This is useful if you know that certain algorithms are unsuitable for your data or compute constraints. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Stopping Conditions

You can edit the conditions that stop the AutoML experiment. Default values depend on the problem type:

- **Forecasting experiments**: Stop after 120 minutes.
- **Classification/regression experiments** (Databricks Runtime 10.4 LTS ML and below): Stop after 60 minutes or after completing 200 trials, whichever occurs first.
- **Classification/regression experiments** (Databricks Runtime 11.0 ML and above): The number of trials is no longer used as a stopping condition; only a time limit applies.
- **Early stopping** (Databricks Runtime 10.4 LTS ML and above for classification/regression): AutoML automatically stops training and tuning if the validation metric stops improving.

For forecasting, only a time limit is used. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Time Column for Data Split (Classification/Regression only)

In Databricks Runtime 10.4 LTS ML and above, you can select a **time column** to split the data for training, validation, and testing in chronological order. This option is available only for classification and regression experiments (not forecasting). It ensures that the model is evaluated on future data relative to the training period. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Data Directory

Databricks recommends leaving the **Data directory** field empty. When empty, the dataset is stored securely as an MLflow artifact, preserving the experiment’s access permissions. If you specify a DBFS path instead, the dataset does not inherit the AutoML experiment’s access controls. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Additional Notes

- **Auto‑ARIMA frequency requirement**: When using Auto‑ARIMA, the time series must have a regular frequency (consistent interval between observations) that matches the frequency unit specified in the UI or API. AutoML handles missing time steps by forward‑filling with the previous value. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Warnings tab**: In Databricks Runtime 10.1 ML and above, AutoML displays warnings about potential dataset issues (e.g., unsupported column types, high cardinality). Click the **Warnings** tab on the training page or experiment page after the experiment completes. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Output Database**: When specified (Runtime 11.3+), AutoML writes prediction results to a table in that database upon completion. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- [AutoML forecasting](/concepts/automl-forecast.md)
- [Evaluation metrics](/concepts/gluonts-evaluator.md)
- [MLflow experiments](/concepts/mlflow-experiment.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- Time series forecasting
- AutoML algorithms
- Primary metric
- [Feature Store integration for AutoML](/concepts/automl-feature-store-integration.md)

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
