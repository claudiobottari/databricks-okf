---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 202add733af7b00b0f9215e969b594a40c214bdd04b27b44db9264e08d3f4d0f
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - classic-compute-forecasting
    - CCF
    - Classic Compute
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: Classic Compute Forecasting
description: The non-serverless alternative to Databricks Serverless Forecasting that requires managing compute resources, presented as a comparison to the serverless approach.
tags:
  - forecasting
  - classic-compute
  - Databricks
  - compute
timestamp: "2026-06-18T12:23:28.057Z"
---

# Classic Compute Forecasting

**Classic Compute Forecasting** is a Databricks feature that automates the training and selection of forecasting models using user-managed compute clusters, as opposed to [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) which uses fully-managed compute resources. Both approaches share the same core AutoML capabilities for time-series prediction, but differ in their compute infrastructure and management overhead. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Overview

Classic Compute Forecasting simplifies forecasting time-series data by automatically selecting the best algorithm and hyperparameters, running on compute resources that you provision and manage. This approach gives you full control over cluster configuration, library installation, and resource allocation. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Comparison with Serverless Forecasting

The key differences between classic compute forecasting and serverless forecasting include: ^[forecasting-serverless-with-automl-databricks-on-aws.md]

| Aspect | Classic Compute Forecasting | Serverless Forecasting |
|--------|---------------------------|----------------------|
| Compute infrastructure | User-managed clusters | Fully-managed, serverless compute |
| Cluster configuration | Full control over cluster settings | No cluster management required |
| Resource allocation | Manual scaling and configuration | Automatic, on-demand scaling |
| Workspace requirements | Requires running clusters | Works within serverless compute limits |

## Requirements

- Training data with a time series column, saved as a [Unity Catalog](/concepts/unity-catalog.md) table or a workspace file.
- A running compute cluster with appropriate Databricks Runtime version.
- The cluster must have the AutoML library installed and configured.

## Creating a Forecasting Experiment

You can create a classic compute forecasting experiment through the Databricks UI or programmatically using the Python API.

### Using the UI

1. Go to your Databricks landing page and click **Experiments** in the sidebar.
2. In the **Forecasting** tile, select **Start training**.
3. Configure the experiment parameters including training data, time column, forecast frequency, and forecast horizon.
4. Select a compute cluster for the experiment to run on.
5. Click **Start training** to begin the experiment.

### Using the Python API

```python
import databricks.automl

summary = databricks.automl.forecast(
    dataset=df,
    time_col="date",
    target_col="sales",
    frequency="day",
    horizon=30,
    output_database="default",
    experiment_name="/Users/you@example.com/forecast_experiment",
)
```

## Key Parameters

### Required Parameters

- **Training data**: A DataFrame or Unity Catalog table containing time-series data.
- **Time column**: The column containing time periods for the series, must be of type `timestamp` or `date`.
- **Forecast frequency**: The time unit representing input data frequency (e.g., minutes, hours, days, months).
- **Forecast horizon**: The number of units of the selected frequency to forecast into the future.

### Optional Parameters

- **Time series identifier columns**: For multi-series forecasting, columns that identify individual time series.
- **Primary metric**: The metric used to evaluate and select the best model.
- **Training framework**: Limit the frameworks for AutoML to explore.
- **Weight column**: Column to use for weighting time series.
- **Holiday region**: Holiday region to use as covariates in model training.
- **Timeout**: Maximum duration for the experiment.
- **Output database**: Unity Catalog database to store prediction results.
- **Experiment name**: Name for the MLflow experiment.

## Experiment Pipeline Stages

During execution, the experiment progresses through several stages: ^[forecasting-serverless-with-automl-databricks-on-aws.md]

1. **Preprocessing**: Validate and prepare the input data by imputing missing values and splitting data into training, validation, and test sets. This stage includes automatic feature generation such as one-hot encoding for categorical features.
2. **Tuning**: Explore different forecasting algorithms and tune hyperparameters.
3. **Training**: Train and evaluate the final model with the selected best configurations. The model can be registered in Unity Catalog if a path is specified.

## Algorithm Support

Classic compute forecasting supports multiple algorithms including:

- **Prophet**: For handling seasonality and holiday effects.
- **Auto-ARIMA**: For autoregressive integrated moving average models. The time series must have a regular frequency where the interval between any two points remains constant. AutoML handles missing time steps by filling in values with the previous value. ^[forecasting-serverless-with-automl-databricks-on-aws.md]
- **Gradient Boosted Trees**: For capturing complex non-linear patterns.
- **Linear Regression**: For simple trend-based forecasting.

## Viewing Results and Using the Best Model

After training completes, you can:

- **View predictions** to see the forecasting results table stored in Delta format.
- **Open a batch inference notebook** — an auto-generated notebook for batch inferencing using the best model.
- **Create a serving endpoint** to deploy the best model to a [Model Serving](/concepts/model-serving.md) endpoint.

## Best Practices

- **Use a regular time series frequency** to ensure compatibility with all algorithms, particularly Auto-ARIMA.
- **Set a reasonable timeout** to prevent experiments from running indefinitely.
- **Use time series identifier columns** when working with multiple related time series.
- **Choose an appropriate holiday region** if your data exhibits seasonal patterns tied to holidays.
- **Monitor cluster resources** to ensure sufficient memory and compute for your dataset size.

## Limitations

- Requires an active compute cluster, which incurs costs even when idle.
- Cluster configuration and scaling must be managed manually.
- Library dependencies must be installed on the cluster.
- Experiment runtime is limited by cluster resources.

## Related Concepts

- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) — The serverless alternative with fully-managed compute
- AutoML — The automated machine learning framework
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The broader domain of time-series prediction
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The tracking infrastructure for experiment runs
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for data and models
- [Model Serving](/concepts/model-serving.md) — The deployment option for trained models

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
