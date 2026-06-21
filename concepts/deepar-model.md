---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9c5aaf38c30cfb4fbbc04c92bc597850511c16d508f50aeda55b0455435e683
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepar-model
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: DeepAR Model
description: A probabilistic forecasting model from GluonTS used for time-series prediction of electricity consumption
tags:
  - machine-learning
  - time-series
  - deep-learning
timestamp: "2026-06-19T17:42:58.989Z"
---

# DeepAR Model

**DeepAR** is a probabilistic time-series forecasting model provided by the [GluonTS](/concepts/gluonts.md) library. It is demonstrated on an end-to-end workflow for forecasting electricity consumption data on a [serverless GPU cluster](/concepts/databricks-serverless-gpu-cluster.md). The workflow covers data ingestion, resampling, model training, prediction, visualization, and evaluation.^[classic-machine-learning-databricks-on-aws.md]

## Overview

DeepAR produces probabilistic forecasts, meaning it outputs a distribution over future values rather than a single point estimate. This allows for uncertainty quantification alongside predictions. The model is designed to work with multiple related time series and can capture seasonal patterns, trends, and dependencies.^[classic-machine-learning-databricks-on-aws.md]

The notebook example uses [GluonTS](/concepts/gluonts.md)’s DeepAR implementation and runs on a serverless GPU cluster provided by [Databricks on AWS](/concepts/databricks-on-aws.md). It ingests historical electricity consumption data, resamples it to a consistent frequency, trains the model, generates future predictions, and visualizes the results alongside evaluation metrics.^[classic-machine-learning-databricks-on-aws.md]

## Workflow Steps

1. **Data ingestion** – Load time-series data (e.g., electricity consumption records)
2. **Resampling** – Convert raw data to a consistent frequency and handle missing values
3. **Model training** – Fit the DeepAR model on the prepared dataset using GluonTS
4. **Prediction** – Generate probabilistic forecasts for future time periods
5. **Visualization** – Plot observed data alongside forecasted quantiles to inspect prediction quality
6. **Evaluation** – Assess forecast accuracy using appropriate metrics

^[classic-machine-learning-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) – The library that provides the DeepAR implementation
- Probabilistic forecasting – The broader category of forecasting that outputs distributions
- [Serverless GPU cluster](/concepts/serverless-gpu-compute.md) – The compute environment used in the demonstration
- Time series forecasting – The general domain of predicting future values from historical data
- [Electricity Consumption Forecasting](/concepts/electricity-consumption-forecasting.md) – Example application demonstrated in the notebook

## Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
