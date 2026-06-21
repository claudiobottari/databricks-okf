---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64026927de71133e8289ac6f08746e04915c20ce309f4e584510e0fe30dc7cdd
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - end-to-end-forecasting-workflow
    - EFW
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: End-to-end forecasting workflow
description: A complete pipeline for time series forecasting covering data ingestion, resampling, training, prediction, visualization, and evaluation
tags:
  - workflow
  - pipeline
  - time-series
timestamp: "2026-06-18T10:56:36.075Z"
---

# End-to-end forecasting workflow

An **end-to-end forecasting workflow** is a complete pipeline that takes raw time-series data from ingestion through model training, prediction, visualization, and evaluation. A canonical example is the probabilistic time-series forecasting workflow using [GluonTS](/concepts/gluonts.md)'s DeepAR model on a serverless GPU cluster, which demonstrates all major stages of such a pipeline. ^[classic-machine-learning-databricks-on-aws.md]

## Workflow stages

The end-to-end forecasting workflow typically includes the following stages, as illustrated by the GluonTS-based example:

1. **Data ingestion** – Loading raw time-series data into the environment.
2. **Resampling** – Aligning the time series to a consistent frequency or resolution.
3. **Model training** – Fitting a forecasting model such as [DeepAR](/concepts/deepar.md) to the historical data.
4. **Prediction** – Generating probabilistic forecasts for future time points.
5. **Visualization** – Plotting the observed data alongside the predictions and uncertainty intervals.
6. **Evaluation** – Measuring forecast accuracy using appropriate metrics (e.g., CRPS, MAE, RMSE).

The whole pipeline can be executed on a serverless GPU cluster to accelerate training of deep-learning-based forecasting models. ^[classic-machine-learning-databricks-on-aws.md]

## Related concepts

- Probabilistic forecasting – Generating predictions as probability distributions rather than point estimates.
- [GluonTS](/concepts/gluonts.md) – A deep-learning toolkit for time-series modeling.
- [DeepAR](/concepts/deepar.md) – An autoregressive recurrent neural network model for probabilistic forecasting.
- Time-series analysis – The broader field of analyzing ordered data points.
- [Databricks AutoML](/concepts/databricks-automl.md) – Automated machine learning that can also produce forecasting models.
- [Serverless GPU clusters](/concepts/databricks-serverless-gpu-clusters.md) – On-demand compute resources suitable for training deep learning models.

## Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
