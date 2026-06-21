---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 913825a6a3af19535464282c0d9c104f6984ae32ffc9588b6b4988b0b91e29a7
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-forecasting
    - DSF
    - Serverless Forecasting
    - Serverless forecasting
    - serverless forecasting
    - databricks-serverless-forecasting-with-automl
    - DSFWA
    - Serverless Forecasting with AutoML
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Databricks Serverless Forecasting
description: A fully-managed AutoML forecasting capability on Databricks that automatically selects algorithms and hyperparameters for time-series prediction using serverless compute.
tags:
  - databricks
  - forecasting
  - serverless
  - mlops
timestamp: "2026-06-19T18:52:53.199Z"
---

```markdown
---
title: Databricks Serverless Forecasting
summary: A managed AutoML service for time-series forecasting that automatically selects algorithms and hyperparameters using the Model Training UI on serverless compute.
sources:
  - forecasting-serverless-with-automl-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:23:17.570Z"
updatedAt: "2026-06-18T12:23:17.570Z"
tags:
  - forecasting
  - serverless
  - AutoML
  - Databricks
aliases:
  - databricks-serverless-forecasting
  - DSF
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Serverless Forecasting

**Databricks Serverless Forecasting** is a fully managed AutoML capability that simplifies building time-series forecasting models. It automatically selects the best algorithm and hyperparameters using serverless compute, removing the need to provision or manage clusters. The service is accessed through the Databricks Model Training UI.^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Requirements

- Training data must include a time-series column and be saved as a [[Unity Catalog]] table.^[forecasting-serverless-with-automl-databricks-on-aws.md]
- If the workspace has [serverless egress control](https://docs.databricks.com/aws/en/security/network/serverless-network-security/network-policies) enabled, `pypi.org` must be added to the allowed domains list. See [Manage network policies for serverless egress control](https://docs.databricks.com/aws/en/security/network/serverless-network-security/manage-network-policies).^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Creating a Forecasting Experiment

To start a serverless forecasting experiment via the Databricks UI:

1. Go to your Databricks landing page and click **Experiments** in the sidebar.
2. In the **Forecasting** tile, select **Start training**.
3. Select a Unity Catalog table as the **Training data**.
4. Configure the time-series parameters:
   - **Time column**: A `timestamp` or `date` column representing time periods.
   - **Forecast frequency**: The time unit of the input data (e.g., minutes, hours, days, weeks, months).
   - **Forecast horizon**: The number of time units to forecast into the future.
5. Select a **Prediction target column** to predict.
6. Optionally, specify a Unity Catalog table as the **Prediction data path** to store forecasts.
7. Choose a **Model registration** Unity Catalog location and name.
8. Under **Advanced options**, you can set:
   - **Experiment name**: An [[MLflow]] experiment name.
   - **Time series identifier columns**: For multi-series forecasting, columns that distinguish individual series. Each series is trained independently.
   - **Primary metric**: The evaluation metric used to select the best model.
   - **Training framework**: The algorithms for AutoML to explore.
   - **Split column**: A column with values `"train"`, `"validate"`, `"test"` for custom data splits.
   - **Weight column**: A column for weighting time series. Weights must be in [0, 10000] and consistent per series.
   - **Holiday region**: A covariate region for holidays.
   - **Timeout**: Maximum duration for the experiment.

Click **Start training** to begin.^[forecasting-serverless-with-automl-databricks-on-aws.md]

> **Note**: To use the Auto-ARIMA algorithm, the time series must have a regular frequency (equal intervals between all points). AutoML handles missing time steps by forward-filling with the previous value.^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Running and Monitoring

During the experiment, the UI shows status across three stages:

1. **Preprocessing**: Validation, imputation of missing values, data splitting into train/validation/test, and automatic feature generation (e.g., one-hot encoding for categorical features).^[forecasting-serverless-with-automl-databricks-on-aws.md]
2. **Tuning**: Exploration of different forecasting algorithms and hyperparameter search.^[forecasting-serverless-with-automl-databricks-on-aws.md]
3. **Training**: Final model training and evaluation using the best configuration. The model is registered in Unity Catalog if a path was specified.^[forecasting-serverless-with-automl-databricks-on-aws.md]

You can stop the experiment at any time, monitor individual runs, and navigate to run pages for detailed inspection.^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Viewing Results

After training completes:
- Predictions are stored in the Delta table specified as the prediction data path.
- The best model is registered in Unity Catalog.

From the experiments page, you can:
- **View predictions**: See the forecast results table.
- **Batch inference notebook**: Open an auto-generated notebook for batch inference using the best model.
- **Create serving endpoint**: Deploy the model to a [[Model Serving]] endpoint.^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Comparison with Classic Compute Forecasting

The following table summarizes key differences between serverless forecasting and [[AutoML Forecasting (Classic Compute)|Forecasting with Classic Compute]]:

| Feature | Serverless Forecasting | Classic Compute Forecasting |
|---------|------------------------|-----------------------------|
| Compute management | Fully managed, no cluster setup required | Requires a running cluster or Databricks Runtime |
| Scalability | Automatic resource allocation | Manual cluster configuration |
| Infrastructure overhead | Minimal | User manages cluster size and lifecycle |
| Egress network control | Subject to serverless egress policies | Subject to classic network policies |

Serverless forecasting simplifies the user experience by abstracting infrastructure, while classic compute gives more control over the runtime environment.^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML – Automated machine learning for classification, regression, and forecasting.
- [[Unity Catalog]] – Data governance catalog for storing training data and models.
- [[MLflow]] – Experiment tracking and model registry.
- [[Model Serving]] – Deploying models as endpoints.
- [[Multi-Series Forecasting|Time Series Forecasting]] – General methodology for predicting future values.
- Serverless Compute – Databricks serverless infrastructure.
- Auto-ARIMA – A specific algorithm used in forecasting.

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md
```

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
