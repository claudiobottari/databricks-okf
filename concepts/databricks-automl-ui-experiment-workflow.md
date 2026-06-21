---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53af58ee13e4b93d5419516158bd739a0888541203ab2e4913faefc3e5f3d1f9
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-automl-ui-experiment-workflow
    - DAUEW
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Databricks AutoML UI Experiment Workflow
description: End-to-end process for setting up, running, and monitoring a forecasting AutoML experiment through the Databricks UI, including compute selection, dataset browsing, and progress tracking
tags:
  - user-interface
  - automl
  - workflow
timestamp: "2026-06-18T12:24:22.117Z"
---

# Databricks AutoML UI Experiment Workflow

The Databricks AutoML UI provides a guided workflow to automatically train and tune machine learning models. This page describes the workflow for setting up a **forecasting** experiment using the classic (non-serverless) AutoML experience. The steps for classification and regression experiments follow a similar pattern, though some configuration fields differ. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Accessing the AutoML UI

To start a forecasting experiment:

1. In the sidebar, select **Experiments**.
2. In the **Forecasting** card, select **Start training**.

The forecasting UI defaults to serverless forecasting. To use classic compute, select **revert back to the old experience**. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Configuring the AutoML Experiment

On the **Configure AutoML experiment page**, you specify the dataset, problem type, prediction target, evaluation metric, and stopping conditions. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

1. **Compute**: Select a cluster running Databricks Runtime 10.0 ML or above. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
2. **Dataset**: Click **Browse**, navigate to the desired table, and click **Select**. The table schema is displayed. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
3. **Prediction target**: Choose the column the model should predict. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
4. **Time column**: Select a column of type `timestamp` or `date` that defines the time periods. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
5. **Time series identifiers**: For multi-series forecasting, select the columns that identify individual time series. If left blank, AutoML assumes a single time series. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
6. **Forecast horizon and frequency**: Enter the number of time periods to forecast and the units (e.g., days, months). ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

   > **Note**: To use Auto-ARIMA, the time series must have a regular frequency matching the specified unit. AutoML handles missing time steps by filling with the previous value. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

7. **Output Database** (Databricks Runtime 11.3 LTS ML and above): Optionally, specify a database where AutoML writes prediction results to a table. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
8. **Experiment name**: The default name can be changed as needed. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

You can also use [Feature Store](/concepts/feature-store.md) to augment the dataset with feature tables. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Advanced Configurations

Open the **Advanced Configuration (optional)** section to adjust further parameters:

- **Evaluation metric**: The primary metric used to score runs. See the AutoML API Reference for available metrics. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Excluded frameworks**: In Databricks Runtime 10.4 LTS ML and above, you can remove training frameworks from consideration. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Stopping conditions**: Defaults are 120 minutes for forecasting. For classification/regression, defaults vary by runtime version. Early stopping is available from Databricks Runtime 10.4 LTS ML and above. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Time column for split** (classification/regression only): Optionally select a time column for chronological train/validation/test split. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Data directory**: Leave empty to store the dataset securely as an MLflow artifact. Specifying a DBFS path does not inherit the experiment's access permissions. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Running and Monitoring the Experiment

Click **Start AutoML** to begin. The AutoML training page displays a runs table; click the refresh button to update. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

During the experiment you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs.
- Navigate to the run page for any trial.

With Databricks Runtime 10.1 ML and above, AutoML shows warnings for potential dataset issues (e.g., unsupported column types, high cardinality). Warnings appear on the **Warnings** tab during and after the experiment. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Viewing Results

When the experiment completes:

- The top row in the runs table shows the best model based on the primary metric. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- Select **View notebook for best model** to review and edit the generated notebook.
- Select **View data exploration notebook** to open the data exploration notebook.
- Search, filter, and sort runs.
- Click a run’s **Models** or **Start Time** to view its page, which includes parameters, metrics, tags, artifacts, and code snippets for making predictions. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

All AutoML experiment results (including notebooks) are stored in a `databricks_automl` folder in the user’s home folder. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Registering and Deploying a Model

From the runs table:

1. Click the link in the **Models** column for the best model.
2. Click the register model button to save it to [Unity Catalog](/concepts/unity-catalog.md) or to the [MLflow Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends Unity Catalog for the latest features. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
3. After registration, deploy the model to a [Model Serving](/concepts/model-serving.md) endpoint. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Troubleshooting: No module named 'pandas.core.indexes.numeric'

When serving an AutoML-built model you may encounter:
```
No module named 'pandas.core.indexes.numeric'
```
This is caused by an incompatible `pandas` version. To fix, run the `add-pandas-dependency.py` script to add `pandas==1.5.3` to the model’s `requirements.txt` and `conda.yaml`, then re-register the model. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Next Steps

- Forecasting API – Programmatic interface for AutoML forecasting.
- Forecasting Data Preparation Settings – Guidelines for preparing time series data.
- Forecast with Covariates – Using external regressors in forecasting.

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

## Related Wiki Pages

- AutoML API Reference
- AutoML Classification UI Workflow
- [AutoML Regression UI Workflow](/concepts/automl-regression-regress.md)
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md)
- [Feature Store Integration with AutoML](/concepts/automl-feature-store-integration.md)

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
