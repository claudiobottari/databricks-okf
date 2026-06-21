---
title: Forecasting (serverless) with AutoML | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/serverless-forecasting
ingestedAt: "2026-06-18T08:13:36.359Z"
---

This article shows you how to run a serverless forecasting experiment using the Databricks Model Training UI.

Databricks Model Training - forecasting simplifies forecasting time-series data by automatically selecting the best algorithm and hyperparameters, all while running on fully-managed compute resources.

To understand the difference between serverless forecasting and classic compute forecasting, see [Serverless forecasting vs. classic compute forecasting](#serverless-classic).

## Requirements[​](#requirements "Direct link to Requirements")

*   Training data with a time series column, saved as a Unity Catalog table.

*   If the workspace has [serverless egress control](https://docs.databricks.com/aws/en/security/network/serverless-network-security/network-policies) enabled, `pypi.org` must be added to the **Allowed domains** list. See [Manage network policies for serverless egress control](https://docs.databricks.com/aws/en/security/network/serverless-network-security/manage-network-policies).

## Create a forecasting experiment with the UI[​](#create-a-forecasting-experiment-with-the-ui "Direct link to Create a forecasting experiment with the UI")

Go to your Databricks landing page and click **Experiments** in the sidebar.

1.  In the **Forecasting** tile, select **Start training**.
    
2.  Select the **Training data** from a list of Unity Catalog tables that you can access.
    
    *   **Time column**: Select the column containing the time periods for the time series. The columns must be of type `timestamp` or `date`.
    *   **Forecast frequency**: Select the time unit that represents your input data's frequency. For example, minutes, hours, days, months. This determines the granularity of your time series.
    *   **Forecast horizon**: Specify how many units of the selected frequency to forecast into the future. Together with the forecast frequency, this defines both the time units and the number of time units to forecast.
    
    note
    
    To use the [Auto-ARIMA](https://alkaline-ml.com/pmdarima/) algorithm, the time series must have a regular frequency where the interval between any two points must be the same throughout the time series. AutoML handles missing time steps by filling in those values with the previous value.
    
3.  Select a **Prediction target column** that you want the model to predict.
    
4.  Optionally, specify a Unity Catalog table **Prediction data path** to store the output forecasts.
    
    ![Serverless forecasting UI screenshot.](https://docs.databricks.com/aws/en/assets/images/serverless-forecasting-cc2fbc5801a7b3025434de9efaf286b6.png)
    
5.  Select a **Model registration** Unity Catalog location and name.
    
6.  Optionally, set **Advanced options**:
    
    *   **Experiment name**: Provide an MLflow experiment name.
    *   **Time series identifier columns** - For multi-series forecasting, select the column(s) that identify the individual time series. Databricks groups the data by these columns as different time series and trains a model for each series independently.
    *   **Primary metric**: Choose the primary metric used to evaluate and select the best model.
    *   **Training framework**: Choose the frameworks for AutoML to explore.
    *   **Split column**: Select the column containing custom data split. Values must be “train” , “validate” , “test”
    *   **Weight column**: Specify the column to use for weighting time series. All samples for a given time series must have the same weight. The weight must be in the range \[0, 10000\].
    *   **Holiday region**: Select the holiday region to use as covariates in model training.
    *   **Timeout**: Set a maximum duration for the AutoML experiment.

## Run the experiment and monitor the results[​](#run-the-experiment-and-monitor-the-results "Direct link to Run the experiment and monitor the results")

To start the AutoML experiment, click **Start training**. From the experiment training page, you can do the following:

*   Stop the experiment at any time.
*   Monitor runs.
*   Navigate to the run page for any run.

Additionally, you can check the status of the experiment as it goes through the following stages:

1.  **Preprocessing:** Validate and prepare the input table by imputing missing values and splitting data into training, validation, and test sets. Automatic feature generation processing, like one-hot encoding for categorical features, also occurs during this stage.
2.  **Tuning:** Explore different forecasting algorithms and tune hyperparameters.
3.  **Training:** Train and evaluate the final model with the selected best configurations. Register the model in Unity Catalog if a path is specified.

## View results or use the best model[​](#view-results-or-use-the-best-model "Direct link to View results or use the best model")

After training completes, the prediction results are stored in specified Delta table and the best model is registered to Unity Catalog.

From the experiments page, you choose from the following next steps:

*   Select **View predictions** to see the forecasting results table.
*   Select **Batch inference notebook** to open a auto-generated notebook for batch inferencing using the best model.
*   Select **Create serving endpoint** to deploy the best model to a Model Serving endpoint.

## Serverless forecasting vs. classic compute forecasting[​](#serverless-forecasting-vs-classic-compute-forecasting "Direct link to serverless-forecasting-vs-classic-compute-forecasting")

The following table summarizes the differences between serverless forecasting and [forecasting with classic compute](https://docs.databricks.com/aws/en/machine-learning/automl/forecasting)
