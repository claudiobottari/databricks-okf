---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c06597cb80d89ca194f6da2a1cafc60ff487de2c2870fef2441a2e4d0810a0f3
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepar-estimator
    - DeepAREstimator
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: DeepAR Estimator
description: A probabilistic forecasting model in GluonTS using recurrent neural networks (RNNs) to produce prediction intervals and point forecasts for time series data.
tags:
  - deep-learning
  - probabilistic-forecasting
  - rnn
  - gluonts
timestamp: "2026-06-18T12:23:46.872Z"
---

# DeepAR Estimator

**DeepAR Estimator** is a probabilistic forecasting model based on recurrent neural networks (RNNs) that is part of the [GluonTS](/concepts/gluonts.md) library. It is designed for time series forecasting and employs a deep learning approach to generate probabilistic predictions, particularly suited for large-scale, multi-item time series data. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Overview

DeepAR is an implementation of the DeepAR algorithm, a recurrent neural network model that produces both point forecasts and prediction intervals. Unlike traditional forecasting methods, DeepAR learns a global model from all available time series, which allows it to capture complex patterns and relationships across different time series within a dataset. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

Key characteristics of DeepAR include:

- **Probabilistic forecasting**: Outputs predictions with uncertainty estimates in the form of confidence intervals.
- **Multi-item support**: Can handle hundreds or thousands of related time series simultaneously.
- **Autoregressive architecture**: Uses previous time steps as inputs to predict future values.

## Architecture

DeepAR employs a recurrent neural network (RNN) architecture, typically using long short-term memory (LSTM) or gated recurrent unit (GRU) cells. The model processes a sequence of past observations and produces a probability distribution over future values, allowing it to generate quantile forecasts and prediction intervals. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Training

DeepAR is trained using a likelihood-based objective function. The model learns to estimate the parameters of a probability distribution (e.g., Gaussian, negative binomial) for each time step, enabling it to capture both point estimates and uncertainty. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

Training involves:
1. **Context length**: The number of past observations used as input.
2. **Prediction length**: The forecast horizon (number of future steps to predict).
3. **Number of epochs**: Iterations over the training data to optimize the model.
4. **Checkpointing**: Saving model state at regular intervals for resumption or evaluation.

## Usage

DeepAR is accessed through the `DeepAREstimator` class in the GluonTS library. The estimator is configured with hyperparameters and then trained on a dataset to produce a `DeepARPredictor` object capable of generating forecasts. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Basic Example

```python
from gluonts.torch import DeepAREstimator
from gluonts.dataset.pandas import PandasDataset

# Define hyperparameters
estimator = DeepAREstimator(
    freq="1h",                    # Frequency of the time series
    prediction_length=168,        # Forecast horizon (7 days)
    context_length=672,            # Context length (4x prediction length)
    trainer_kwargs={"max_epochs": 10}
)

# Train the model
predictor = estimator.train(training_data)

# Generate predictions
forecasts = predictor.predict(test_data, num_samples=100)
```

^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Backtesting and Evaluation

DeepAR supports backtesting through rolling window evaluation, where the model is evaluated on multiple test windows to assess its forecasting accuracy. Key evaluation metrics include: ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

- Mean Absolute Scaled Error (MASE)
- Root Mean Squared Error (RMSE)
- Quantile loss at various confidence levels

## Use Cases

DeepAR is commonly applied in:

- **Energy forecasting**: Electricity consumption and load prediction.
- **Retail demand forecasting**: Sales and inventory planning for multiple products.
- **Anomaly detection**: Identifying unusual patterns in time series data.

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The Python library providing DeepAR and other forecasting models.
- Probabilistic forecasting — The broader field of generating probability distributions over future values.
- Time series forecasting — The domain of predicting future values based on historical data.
- RNN-based forecasting — Recurrent neural networks for sequence prediction.
- Model checkpointing — Saving model state during training.

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
