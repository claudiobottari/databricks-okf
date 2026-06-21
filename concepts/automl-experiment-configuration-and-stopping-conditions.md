---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 415458246faf0e58a34e1e13e248d0bd0bc1e71da8cc1ededd818d6f2d6688b6
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - automl-experiment-configuration-and-stopping-conditions
    - Stopping Conditions and AutoML Experiment Configuration
    - AECASC
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: AutoML Experiment Configuration and Stopping Conditions
description: Standard configuration parameters for AutoML experiments including compute selection, dataset browsing, prediction target, time column, evaluation metrics, and stopping conditions (default 120 minutes for forecasting).
tags:
  - automl
  - configuration
  - databricks
timestamp: "2026-06-19T18:53:43.693Z"
---

# AutoML Experiment Configuration and Stopping Conditions

**AutoML Experiment Configuration and Stopping Conditions** refers to the settings and termination criteria that control how an automated machine learning (AutoML) experiment runs on Databricks. These configurations define the dataset, problem type, evaluation metrics, training frameworks, and conditions under which the experiment stops.

## Configuring an AutoML Experiment

When setting up an AutoML experiment through the UI, users configure several key parameters on the **Configure AutoML experiment page**. These include selecting the compute cluster, specifying the dataset, choosing the prediction target column, and defining the problem type. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Basic Configuration

The following fields are required for any AutoML experiment:

- **Compute**: A cluster running Databricks Runtime 10.0 ML or above (for forecasting experiments).
- **Dataset**: The table containing the training data.
- **Prediction target**: The column the model should predict.
- **Experiment name**: A name for the experiment (default provided).

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Forecasting-Specific Configuration

For forecasting experiments, additional configuration is required:

- **Time column**: The column containing time periods for the time series (must be `timestamp` or `date` type).
- **Time series identifiers**: Columns that identify individual time series for multi-series forecasting. If left blank, AutoML assumes a single time series.
- **Forecast horizon and frequency**: The number of time periods into the future to forecast and the units (e.g., days, weeks, months).

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

For Auto-ARIMA, the time series must have a regular frequency where the interval between any two points is consistent throughout the series. The frequency must match the frequency unit specified in the UI or API. AutoML handles missing time steps by filling in those values with the previous value. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Output Database

In Databricks Runtime 11.3 LTS ML and above, users can save prediction results by specifying a database in the **Output Database** field. AutoML writes the prediction results to a table in this database. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Advanced Configuration Options

The **Advanced Configuration (optional)** section provides additional parameters for fine-tuning the experiment.

### Evaluation Metric

The evaluation metric is the primary metric used to score and compare experiment runs. Users can select from available metrics appropriate for their problem type. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Training Frameworks

In Databricks Runtime 10.4 LTS ML and above, users can exclude specific training frameworks from consideration. By default, AutoML trains models using all available frameworks listed under AutoML algorithms. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Data Splitting

In Databricks Runtime 10.4 LTS ML and above, users can select a time column to split the data for training, validation, and testing in chronological order. This applies to classification and regression experiments. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Data Directory

Databricks recommends leaving the **Data directory** field empty. Not populating this field triggers the default behavior of securely storing the dataset as an MLflow artifact. A DBFS path can be specified, but in this case, the dataset does not inherit the AutoML experiment's access permissions. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Stopping Conditions

Stopping conditions define when an AutoML experiment terminates. These conditions prevent experiments from running indefinitely and help manage compute resources.

### Default Stopping Conditions

The default stopping conditions vary by experiment type:

- **Forecasting experiments**: Stop after 120 minutes.
- **Classification and regression experiments (Databricks Runtime 10.4 ML and below)**: Stop after 60 minutes or after completing 200 trials, whichever happens first.
- **Classification and regression experiments (Databricks Runtime 11.0 ML and above)**: The number of trials is not used as a stopping condition.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Early Stopping

In Databricks Runtime 10.4 LTS ML and above, AutoML incorporates early stopping for classification and regression experiments. It stops training and tuning models if the validation metric is no longer improving, preventing wasted compute on unpromising model configurations. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Editing Stopping Conditions

Users can edit the stopping conditions in the advanced configuration section to customize the experiment duration and termination criteria based on their specific needs. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Running and Monitoring the Experiment

After configuration, clicking **Start AutoML** begins the experiment. The AutoML training page displays, allowing users to:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs.
- Navigate to the run page for any trial.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

With Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential issues with the dataset, such as unsupported column types or high cardinality columns. These warnings can be viewed in the **Warnings** tab on the training page or experiment page after the experiment completes. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- AutoML Algorithms — The training frameworks available for AutoML experiments.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for AutoML runs and results.
- Forecasting with AutoML — Specific configuration for time series forecasting problems.
- Classification with AutoML — Configuration for classification problems.
- Regression with AutoML — Configuration for regression problems.
- [Feature Store Integration](/concepts/automl-feature-store-integration.md) — Using existing feature tables to augment input datasets.
- [Model Serving](/concepts/model-serving.md) — Deploying AutoML-generated models to serving endpoints.

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
