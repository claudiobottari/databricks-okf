---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad0ca0c527a02d19d5c860449a2cb934457e2504bb750276c28c16c7b73bd0e8
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deepar
    - deepar-estimator
    - DeepAREstimator
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: DeepAR
description: A recurrent neural network (RNN) model for probabilistic forecasting that produces prediction intervals alongside point forecasts.
tags:
  - time-series
  - deep-learning
  - probabilistic-forecasting
timestamp: "2026-06-19T18:53:24.706Z"
---

# DeepAR

**DeepAR** is a probabilistic forecasting method based on autoregressive recurrent neural networks. It is designed to produce accurate probabilistic predictions for time series data, particularly in scenarios involving many related time series. DeepAR is available through the [GluonTS](/concepts/gluonts.md) library, which provides a toolkit for deep learning-based time series modeling. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Overview

DeepAR is a recurrent neural network (RNN) model that excels at probabilistic forecasting. Unlike traditional time series methods that produce point forecasts, DeepAR generates probabilistic predictions with confidence intervals, allowing practitioners to quantify uncertainty in their forecasts. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

The model learns global patterns across multiple related time series, making it particularly effective when working with groups of time series that share underlying patterns, such as electricity consumption data from multiple households. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Architecture

DeepAR uses an autoregressive approach where the model predicts future values based on its own previous predictions alongside observed historical data. The recurrent architecture allows the model to capture complex temporal dependencies and seasonal patterns in the data. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Key Features

- **Probabilistic forecasts**: Produces prediction intervals (e.g., 90% confidence intervals) rather than single point estimates. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Multi-series learning**: Trains on multiple related time series simultaneously to capture shared patterns. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Autoregressive design**: Uses its own predictions as inputs for subsequent predictions in the forecast horizon. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Configurable context length**: Can be set to use a multiple of the prediction length for historical context. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Implementation with GluonTS on Databricks

DeepAR is implemented through the `DeepAREstimator` class in GluonTS, which supports PyTorch backend. On Databricks serverless GPU compute, DeepAR can be trained efficiently using GPU acceleration. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Configuration

The estimator accepts various hyperparameters, including:

- `freq`: The frequency of the time series data (e.g., hourly). ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- `prediction_length`: The number of time steps to forecast. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- `context_length`: The number of historical time steps used as input (often set to a multiple of `prediction_length`). ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- `trainer_kwargs`: Additional training parameters such as `max_epochs` and `accelerator` settings. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Training and Checkpointing

DeepAR training supports model checkpointing through PyTorch Lightning's `ModelCheckpoint` callback, allowing models to be saved after each epoch and resumed later from checkpoints. Checkpoints can be stored in [Unity Catalog](/concepts/unity-catalog.md) volumes for persistence. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

```python
from gluonts.torch import DeepAREstimator
from lightning.pytorch.callbacks import ModelCheckpoint

checkpoint_cb = ModelCheckpoint(
    dirpath=CHECKPOINT_PATH,
    filename="deepar-{epoch:02d}-{step}",
    save_top_k=-1,
    every_n_epochs=1,
    save_on_train_epoch_end=True,
)

deepar_estimator = DeepAREstimator(
    freq="1h",
    prediction_length=168,  # 7 days
    context_length=672,     # 28 days
    trainer_kwargs={
        "accelerator": "auto",
        "max_epochs": 10,
        "callbacks": [checkpoint_cb]
    }
)

deepar_predictor = deepar_estimator.train(train_ds)
```

### Generating Forecasts

After training, the predictor generates probabilistic forecasts by sampling from the learned distribution:

```python
forecasts = deepar_predictor.predict(test_pairs.input, num_samples=20)
```

## Evaluation

DeepAR predictions can be evaluated using the GluonTS `Evaluator`, which calculates metrics such as:

- Mean Absolute Scaled Error (MASE)
- Root Mean Squared Error (RMSE)
- Quantile losses at specified probability levels

These metrics can be computed across multiple test windows for robust backtesting. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Example Application: Electricity Forecasting

DeepAR has been demonstrated on an electricity consumption dataset containing readings from 370 clients between 2011-2014, with values recorded every 15 minutes. The model can forecast consumption over horizons such as 7 days (168 hours) and produce 90% confidence intervals alongside median predictions. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) — The library providing DeepAR and other forecasting models
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md) — Generating predictions with uncertainty estimates
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — The broader domain of predicting future values from historical data
- Recurrent Neural Networks — The underlying architecture used by DeepAR
- Model Checkpointing — Saving and resuming model training
- [Backtesting](/concepts/rolling-window-backtesting.md) — Evaluating forecast accuracy using historical data

## Sources

- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
