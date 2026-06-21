---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 783a448b6916f005ba3b3aa67bd82febd7c466e616553f3dd24966a49e9b682e
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - end-to-end-forecasting-pipeline
    - EFP
    - End-to-end pipeline
    - end-to-end-forecasting-workflow
    - EFW
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: End-to-End Forecasting Pipeline
description: A complete workflow for time-series forecasting covering data ingestion, resampling, model training, prediction, visualization, and evaluation stages.
tags:
  - pipeline
  - machine-learning
  - workflow
timestamp: "2026-06-19T14:11:50.880Z"
---

# End-to-End Forecasting Pipeline

An **End-to-End Forecasting Pipeline** refers to a complete workflow for building, training, deploying, and monitoring a time-series forecasting model. On Databricks, such a pipeline can be executed on a serverless GPU cluster and typically includes all stages from raw data ingestion to final evaluation and visualization. The pipeline is designed to produce probabilistic forecasts — predictions that include uncertainty estimates — for use cases such as electricity consumption planning, demand forecasting, and resource allocation.

## Overview

The end-to-end forecasting pipeline demonstrated in the Databricks documentation uses the [GluonTS](/concepts/gluonts.md) probabilistic time-series modeling library with the [DeepAR](/concepts/deepar.md) algorithm. The pipeline is run on a [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) cluster, which provides on-demand GPU resources for training deep learning models without the need to manage infrastructure. The complete workflow covers data ingestion, resampling, model training, prediction, visualization, and evaluation. ^[classic-machine-learning-databricks-on-aws.md]

## Pipeline Steps

Although the source material names the steps in sequence, each stage serves a distinct purpose in a production-grade forecasting pipeline:

- **Data Ingestion** – Loading raw time-series data (e.g., electricity consumption records) into the Databricks environment, typically from cloud storage or external databases.
- **Resampling** – Converting irregularly spaced or differently sampled time series to a consistent frequency (e.g., hourly), which is required by many forecasting models.
- **Model Training** – Fitting the [DeepAR](/concepts/deepar.md) model on the resampled data using a [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) cluster. DeepAR is a recurrent neural network (RNN) architecture that produces probabilistic forecasts by learning a distribution over future values.
- **Prediction** – Generating forecasts for a specified horizon. The output includes both point forecasts and prediction intervals that quantify uncertainty.
- **Visualization** – Plotting historical data against predicted values, often including confidence bands to communicate forecast uncertainty.
- **Evaluation** – Measuring forecast accuracy using metrics such as RMSE or [CRPS](/concepts/compute-resource-specification.md) (continuous ranked probability score) for probabilistic forecasts.

All of these stages are executed in a single notebook environment, making the pipeline reproducible and easy to adapt. ^[classic-machine-learning-databricks-on-aws.md]

## Application

The example pipeline is applied to [Probabilistic Time-Series Forecasting](/concepts/probabilistic-time-series-forecasting.md) of electricity consumption data. Probabilistic forecasting is especially valuable in energy domains, where decisions about generation capacity and pricing require an understanding of risk and uncertainty. The same pipeline can be adapted to other time-series domains such as retail demand, network traffic, or financial metrics. ^[classic-machine-learning-databricks-on-aws.md]

## Related Concepts

- [GluonTS](/concepts/gluonts.md) – The library used for probabilistic time-series modeling.
- [DeepAR](/concepts/deepar.md) – The specific RNN-based forecasting algorithm.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) – The broader machine learning discipline.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The infrastructure that enables GPU-accelerated training.
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md) – The paradigm of predicting distributions rather than single points.
- Databricks Notebooks – The execution environment for the pipeline.

## Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
