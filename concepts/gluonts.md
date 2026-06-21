---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d5bc7a817d0c44544bde0a03e171bb09dab08b8d2898d148d84bceded3acb34
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - gluonts
    - Gluon
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
title: GluonTS
description: A library for probabilistic time-series forecasting, used with the DeepAR model on Databricks
tags:
  - machine-learning
  - time-series
  - library
timestamp: "2026-06-19T17:42:56.190Z"
---

# GluonTS

**GluonTS** is an open-source Python library for probabilistic time series modeling, forecasting, and anomaly detection. It provides a comprehensive toolkit with pre-built implementations of state-of-the-art deep learning models, supporting both PyTorch and MXNet backends.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Overview

GluonTS offers a complete framework for time series analysis, including neural network architectures, feature processing components, evaluation metrics, and dataset handling utilities. The library is designed to streamline the end-to-end workflow of building and deploying probabilistic time series models.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Key Features

- **Pre-built models**: Includes implementations of state-of-the-art models for time series forecasting, with documentation available for each model's capabilities and performance characteristics.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Probabilistic forecasting**: Produces predictions with confidence intervals rather than single-point estimates, enabling uncertainty quantification.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Multiple deep learning frameworks**: Supports both PyTorch and MXNet implementations, allowing users to choose their preferred backend.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Evaluation metrics**: Includes a comprehensive evaluator with metrics such as MASE, RMSE, and quantile losses.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Dataset handling**: Provides utilities like `PandasDataset` for easy conversion from Pandas DataFrames and `DateSplitter` for creating train/test splits for backtesting.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Deployment on Databricks

GluonTS can be deployed on Databricks serverless GPU compute for accelerated training and inference. On Databricks, GluonTS models can leverage GPU acceleration and store model checkpoints using Unity Catalog Volumes for persistence.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Installation

On a Databricks cluster, install GluonTS with PyTorch support using:

```python
%pip install -q --upgrade gluonts[torch] wget
dbutils.library.restartPython()
```

^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Workflow

A typical GluonTS forecasting workflow on Databricks includes:

1. **Data preparation**: Load and resample time series data (e.g., from 15-minute to hourly intervals to reduce computation time).^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
2. **Conversion to GluonTS format**: Convert Pandas DataFrames to `PandasDataset` objects.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
3. **Train/test splitting**: Use `DateSplitter` to create rolling window splits for backtesting.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
4. **Model training**: Train models like [DeepAR](/concepts/deepar.md), a recurrent neural network for probabilistic forecasting.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
5. **Prediction**: Generate forecasts with confidence intervals (e.g., 90% confidence intervals).^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
6. **Evaluation**: Calculate metrics using the GluonTS `Evaluator`.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
7. **Checkpoint management**: Save and resume training from model checkpoints stored in Unity Catalog volumes.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Example: DeepAR Training

The following example demonstrates training a DeepAR model for probabilistic time series forecasting:

```python
from gluonts.torch import DeepAREstimator
from lightning.pytorch.callbacks import ModelCheckpoint

# Configure model hyperparameters
model_hyperparameters = {
    "freq": "1h",
    "prediction_length": 168,  # 7 days
    "context_length": 672,     # 4x prediction length
}

# Configure trainer
trainer_hyperparameters = {
    "accelerator": "auto",
    "max_epochs": 10,
    "callbacks": [checkpoint_cb],
}

# Create and train estimator
deepar_estimator = DeepAREstimator(
    **model_hyperparameters,
    trainer_kwargs=trainer_hyperparameters,
)
deepar_predictor = deepar_estimator.train(train_ds)
```

^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Available Models

GluonTS provides a growing collection of pre-built models documented in its [available models](https://ts.gluon.ai/stable/getting_started/models.html) reference. These include various neural network architectures suitable for different time series characteristics and forecasting horizons.^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Applications

GluonTS is commonly used for:

- Electricity consumption forecasting (supports datasets with hundreds of individual time series) ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- [Anomaly Detection](/concepts/anomaly-detection.md) in time series data ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- Probabilistic demand forecasting ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- Backtesting model performance with rolling window evaluation ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

## Related Concepts

- [DeepAR](/concepts/deepar.md) — A recurrent neural network model for probabilistic forecasting available in GluonTS
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md) — The core methodology behind GluonTS predictions
- Time Series Analysis — The broader field that GluonTS addresses
- [MLflow Tracking](/concepts/mlflow-tracking.md) — For logging GluonTS experiments and model parameters
- PyTorch — One of the deep learning backends supported by GluonTS

## Sources

- classic-machine-learning-databricks-on-aws.md
- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
