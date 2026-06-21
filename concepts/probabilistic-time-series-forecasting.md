---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f329b612dcb12008d8648f6f3b28ef61b1be3edea6a38d0febc0d8dfb3022311
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - probabilistic-time-series-forecasting
    - PTF
    - Probabilistic Forecasting
    - probabilistic forecasting|probabilistic forecasts
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: Probabilistic Time-Series Forecasting
description: A forecasting approach that produces probability distributions over future values rather than point estimates
tags:
  - machine-learning
  - time-series
  - forecasting
timestamp: "2026-06-19T17:43:06.389Z"
---

# Probabilistic Time-Series Forecasting

**Probabilistic time-series forecasting** is a forecasting approach that produces probability distributions over possible future values rather than single point estimates, enabling practitioners to quantify prediction uncertainty and generate confidence intervals around forecasts. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Overview

Unlike traditional point forecasting methods that predict a single future value, probabilistic forecasting outputs a range of possible outcomes with associated probabilities. This approach is particularly valuable for decision-making under uncertainty, such as inventory planning, energy load management, and financial risk assessment. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Implementation with GluonTS

[GluonTS](/concepts/gluonts.md) is a Python library focused on deep learning-based approaches for time series modeling. It provides a toolkit for forecasting and [Anomaly Detection](/concepts/anomaly-detection.md), with pre-built implementations of state-of-the-art models. GluonTS supports both PyTorch and MXNet implementations and includes essential components like neural network architectures, feature processing, and evaluation metrics. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### DeepAR Model

The [DeepAR](/concepts/deepar.md) model is a recurrent neural network architecture designed for probabilistic forecasting. It is one of the available models in GluonTS and is commonly used for time series with seasonal patterns. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

Key hyperparameters for DeepAR include:
- `freq`: The frequency of the time series data (e.g., hourly, daily)
- `prediction_length`: The number of time steps to forecast
- `context_length`: The number of past time steps used as input for predictions (often set to a multiple of `prediction_length`)^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Training Process

The training workflow for probabilistic time-series forecasting with GluonTS typically involves:

1. **Data preparation**: Loading and resampling time series data to a consistent frequency (e.g., from 15-minute to 1-hour intervals) to reduce data points and speed up training. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
2. **Train/test splitting**: Creating rolling windows for backtesting model performance. GluonTS provides a `DateSplitter` that splits the dataset into training and test sets and generates multiple test windows with configurable distance. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
3. **Model configuration**: Setting hyperparameters such as `freq`, `prediction_length`, `context_length`, and trainer options like `max_epochs`. Checkpoints can be saved after each epoch using a `ModelCheckpoint` callback. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
4. **Training**: Fitting the model on historical data. Training a DeepAR model for 10 epochs on a subset of data (e.g., 10 time series) takes approximately 60 seconds on a single GPU. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
5. **Prediction**: Generating forecasts with confidence intervals by sampling from the predictive distribution (e.g., 20 samples per forecast). The output includes the predicted median and intervals such as a 90% confidence interval. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
6. **Evaluation**: Calculating metrics using the GluonTS `Evaluator`. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

#### Resuming Training from Checkpoints

GluonTS supports resuming training from a previously saved checkpoint. When creating a new `DeepAREstimator` with an increased `max_epochs`, the `train()` method can accept a `ckpt_path` argument pointing to a saved checkpoint file. The model then continues training from that state. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Evaluation Metrics

The GluonTS Evaluator provides metrics for assessing probabilistic forecast quality, including:
- Mean Absolute Scaled Error (MASE)
- Root Mean Square Error (RMSE)
- Quantile losses at specified probability levels (e.g., 0.1, 0.5, 0.9)^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

These metrics can be obtained per time series (`item_metrics`) and aggregated across all series (`agg_metrics`). ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Confidence Intervals

A key output of probabilistic forecasting is the ability to visualize prediction uncertainty. Forecasts are typically displayed with:
- **Predicted median**: The central estimate of the forecast distribution
- **Confidence intervals**: Ranges that contain the true value with a specified probability (e.g., 90% confidence interval). In GluonTS, `forecast.plot(intervals=(0.9,))` shows the 90% confidence band around the median. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Use Cases

Probabilistic time-series forecasting is applied in domains where uncertainty quantification is critical:

- **Energy load forecasting**: Predicting electricity consumption with uncertainty bounds for grid management
- **Demand forecasting**: Inventory and supply chain planning with risk assessment
- **Financial forecasting**: Asset price prediction with confidence intervals
- **Anomaly detection**: Identifying unusual patterns by comparing actual values against forecast distributions^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The Python library for deep learning-based time series modeling
- [DeepAR](/concepts/deepar.md) — A recurrent neural network model for probabilistic forecasting
- Time Series Analysis — The broader field of analyzing time-ordered data
- [MLflow Tracking](/concepts/mlflow-tracking.md) — For logging and managing forecasting experiments
- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic experiment tracking for ML workflows
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — Compute infrastructure for training forecasting models
- [Electricity Load Forecasting](/concepts/electricity-consumption-forecasting.md) — A common application domain for probabilistic methods

## Sources

- classic-machine-learning-databricks-on-aws.md
- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
