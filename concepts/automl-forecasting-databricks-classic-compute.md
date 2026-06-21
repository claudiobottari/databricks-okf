---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fd84157a57ea3218d8aea3ea44ce59ea98ac4a16a1fa885d9dcff4c4ad4211b
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-databricks-classic-compute
    - AF(CC
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: AutoML Forecasting (Databricks Classic Compute)
description: Automated machine learning workflow on Databricks for time-series forecasting using classic (non-serverless) compute, requiring Databricks Runtime 10.0 ML+
tags:
  - machine-learning
  - automl
  - forecasting
  - databricks
timestamp: "2026-06-18T12:24:09.681Z"
---

# AutoML Forecasting (Databricks Classic Compute)

**AutoML Forecasting (Databricks Classic Compute)** is a feature of AutoML on Databricks that automatically searches for the best forecasting algorithm and hyperparameter configuration for time‑series data using a user‑specified classic compute cluster (as opposed to the serverless forecasting experience). It is available starting with Databricks Runtime 10.0 ML. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Overview

AutoML Forecasting simplifies the process of building high‑quality [Time Series Forecasting](/concepts/multi-series-forecasting.md) models by automatically training and tuning multiple algorithms, evaluating them against a chosen metric, and presenting the best‑performing model. The classic compute experience requires the user to select a cluster running Databricks Runtime 10.0 ML or above. The UI defaults to serverless forecasting; to use classic compute the user must select **revert back to the old experience** on the forecasting card. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Setting Up a Forecasting Experiment

### Using the UI

1. In the sidebar, select **Experiments**.
2. In the **Forecasting** card, select **Start training**.
3. On the **Configure AutoML experiment** page, select a compute cluster running Databricks Runtime 10.0 ML or above.
4. Under **Dataset**, browse to the input table and click **Select**. The table schema appears.
5. In **Prediction target**, choose the column to forecast.
6. In **Time column**, choose a column of type `timestamp` or `date` that defines the time periods of the series.
7. For multi‑series forecasting, select one or more **Time series identifiers** to group the data into separate time series. If left blank, the dataset is treated as a single time series.
8. In **Forecast horizon and frequency**, specify the number of future periods to predict (integer) and the time unit (e.g., days, weeks).  
   *Note:* To use Auto‑ARIMA, the time series must have a regular frequency matching the chosen unit. AutoML fills missing time steps with the previous value.
9. In Databricks Runtime 11.3 LTS ML and above, you can specify an **Output Database** to save prediction results. AutoML writes the forecasts to a table in that database.
10. The **Experiment name** can be changed from the default. Click **Start AutoML** to begin.

### Advanced Configuration

Open the **Advanced Configuration (optional)** section to adjust:

- **Evaluation metric** – The primary metric used to score trials (see AutoML API Reference).
- **Excluded training frameworks** – In Databricks Runtime 10.4 LTS ML and above, you can prevent certain frameworks from being tried (the default set is listed under [AutoML algorithms](https://docs.databricks.com/aws/en/machine-learning/automl/#automl-algorithm)).
- **Stopping conditions** – The default maximum time is 120 minutes for forecasting. For Runtime 10.4 LTS ML and above, earlier stopping conditions (e.g., number of trials) are not used for forecasting; instead AutoML uses early stopping when the validation metric stops improving.
- **Time column for data split** – In Runtime 10.4 LTS ML and above (for classification and regression), a time column can be used to split data chronologically into training, validation, and test sets.
- **Data directory** – Databricks recommends leaving this field empty; the dataset is then stored securely as an MLflow artifact. A DBFS path can be entered, but the dataset will not inherit the AutoML experiment’s access permissions.

## Running the Experiment and Monitoring Progress

After clicking **Start AutoML**, the training page displays. From this page you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs and navigate to their run pages.
- In Runtime 10.1 ML and above, view potential dataset **warnings** (e.g., unsupported column types, high cardinality) on a **Warnings** tab during or after training.

## Viewing Results

When the experiment completes, the results page presents:

- The best model (top row) based on the primary metric.
- **View notebook for best model** – review and edit the generated training notebook.
- **View data exploration notebook** – examine the exploratory analysis.
- A searchable, filterable table of all trial runs.
- For any trial run, clicking the **Models** or **Start Time** column opens the [MLflow Run](/concepts/mlflow-run.md) page, which includes parameters, metrics, tags, artifacts, and code snippets for making predictions. The generated notebook for a trial is saved under **Artifacts** and can be downloaded (if allowed by workspace policies).

All AutoML experiment results (data exploration and training notebooks) are stored in a `databricks_automl` folder in the **home folder** of the user who ran the experiment. Later, the experiment can be found on the **Experiments** page.

## Registering and Deploying a Model

1. On the results page, select the link in the **Models** column for the desired model.
2. Click the **Register model** button to register it to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md) (Databricks recommends Unity Catalog for the latest features).
3. After registration, the model can be deployed to a custom [Model Serving](/concepts/model-serving.md) endpoint.

## Troubleshooting

### No module named 'pandas.core.indexes.numeric'

When serving an AutoML‑built model with Model Serving, this error may appear due to an incompatible `pandas` version. To resolve:

1. Run the [add‑pandas‑dependency.py](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py) script, modifying it to include the `run_id` of the [MLflow Run](/concepts/mlflow-run.md).
2. The script edits `requirements.txt` and `conda.yaml` to add `pandas==1.5.3`.
3. Re‑register the model to Unity Catalog or the model registry.
4. Retry serving.

## Related Concepts

- AutoML – The broader automated machine learning framework on Databricks.
- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) – The alternative, serverless forecasting experience.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – The underlying problem domain.
- [MLflow](/concepts/mlflow.md) – The platform used to track experiments, log models, and manage artifacts.
- [Model Serving](/concepts/model-serving.md) – Deploying AutoML models for real‑time inference.
- [Unity Catalog](/concepts/unity-catalog.md) – Recommended model registry for governance.
- [Feature Store](/concepts/feature-store.md) – Integration to augment training data with pre‑computed features.
- AutoML API Reference – Programmatic configuration and metrics.

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
