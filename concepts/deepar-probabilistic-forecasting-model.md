---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e83019f35dc9894acf147c61fea3ba691f0c0d410c69433d47ae9d62ecb357d9
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - deepar-probabilistic-forecasting-model
    - DPFM
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: DeepAR Probabilistic Forecasting Model
description: A neural network-based model from GluonTS that produces probabilistic forecasts for time series data, demonstrated in an electricity consumption forecasting workflow.
tags:
  - time-series
  - probabilistic-modeling
  - deep-learning
timestamp: "2026-06-18T14:35:37.856Z"
---

# DeepAR Probabilistic Forecasting Model

**DeepAR Probabilistic Forecasting Model** is a time-series forecasting model available in the [GluonTS](/concepts/gluonts.md) library that produces probabilistic predictions, such as prediction intervals and quantiles, rather than single point estimates. It is designed for applications like electricity consumption forecasting where uncertainty quantification is important. ^[classic-machine-learning-databricks-on-aws.md]

## Overview

DeepAR is a deep learning–based forecasting method that models the conditional distribution of future time series values given past observations and optional covariates. The model can be trained on a single time series or across a large collection of related time series, capturing both global patterns and seasonality. Probabilistic outputs allow downstream decisions that account for forecast uncertainty.

## Usage on Databricks

Databricks supports running DeepAR as part of an end-to-end forecasting workflow on serverless GPU clusters. A typical workflow includes: ^[classic-machine-learning-databricks-on-aws.md]

- **Data ingestion**: Loading historical time-series data (e.g., electricity consumption records).
- **Resampling**: Aligning data to regular time intervals for model input.
- **Model training**: Fitting the DeepAR model using [GluonTS](/concepts/gluonts.md) and a GPU-enabled Databricks cluster.
- **Prediction**: Generating probabilistic forecasts for future time points.
- **Visualization**: Plotting predictions with confidence intervals.
- **Evaluation**: Measuring forecast accuracy using metrics such as Mean Absolute Scaled Error (MASE) or pinball loss.

## Integration with GluonTS

DeepAR is implemented within the [GluonTS](/concepts/gluonts.md) framework, an open-source probabilistic time-series modeling toolkit built on Apache MXNet. GluonTS provides data loaders, evaluators, and pre-built models like DeepAR, simplifying the development of forecasting pipelines.

## Related Concepts

- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md)
- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [GluonTS](/concepts/gluonts.md)
- [Serverless GPU Cluster on Databricks](/concepts/serverless-gpu-cluster-on-databricks.md)
- Prediction Intervals
- [Electricity Consumption Forecasting](/concepts/electricity-consumption-forecasting.md)

## Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
