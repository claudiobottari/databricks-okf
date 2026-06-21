---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f2a3244f2ac9c672d679a0951e5c70ea87a34c1339b937612fd29daee610e41
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gluonts-for-time-series-forecasting
    - GFTSF
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: GluonTS for Time Series Forecasting
description: GluonTS is a probabilistic time-series forecasting toolkit used for end-to-end workflows including data ingestion, resampling, model training, prediction, visualization, and evaluation.
tags:
  - time-series
  - forecasting
  - machine-learning
timestamp: "2026-06-19T14:11:29.078Z"
---

# GluonTS for Time Series Forecasting

**GluonTS** is a deep learning library for probabilistic time series forecasting. It provides tools for building, training, and evaluating forecasting models, including the **DeepAR** model. On Databricks, GluonTS can be used on a serverless GPU cluster to perform end-to-end forecasting workflows. ^[classic-machine-learning-databricks-on-aws.md]

## Workflow

A typical GluonTS workflow for time series forecasting includes the following steps:

- **Data ingestion**: Load historical time series data (e.g., electricity consumption data).
- **Resampling**: Transform raw data to a consistent frequency.
- **Model training**: Train a probabilistic model such as [DeepAR](/concepts/deepar.md) on a [serverless GPU cluster](/concepts/databricks-serverless-gpu-cluster.md).
- **Prediction**: Generate forecasts for future time steps.
- **Visualization and evaluation**: Compare predicted distributions against actual values to assess model performance.

This end-to-end process is demonstrated in a Databricks notebook that uses GluonTS on electricity consumption data. ^[classic-machine-learning-databricks-on-aws.md]

## Related Concepts

- Probabilistic forecasting
- [DeepAR](/concepts/deepar.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Time series analysis
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

## Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
