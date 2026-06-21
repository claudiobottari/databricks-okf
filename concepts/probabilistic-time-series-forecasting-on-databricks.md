---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 75c2538c3b1ba6d49c9e27298e9a8ba024d895d5f84354aeaed54902f9aa8ea2
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - probabilistic-time-series-forecasting-on-databricks
    - PTSFOD
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: Probabilistic Time Series Forecasting on Databricks
description: An end-to-end workflow for probabilistic time series forecasting on Databricks, covering data ingestion, resampling, model training, prediction, visualization, and evaluation.
tags:
  - time-series
  - databricks
  - machine-learning-pipeline
timestamp: "2026-06-18T14:36:04.648Z"
---

Here is the wiki page for "Probabilistic Time Series Forecasting on Databricks".

---

## Probabilistic Time Series Forecasting on Databricks

**Probabilistic Time Series Forecasting on Databricks** refers to the practice of generating predictions that include a measure of uncertainty, rather than single-point estimates, for time series data using the Databricks platform. This approach is essential for applications where understanding the range of possible future outcomes is critical for decision-making, such as demand planning, resource allocation, and risk management.

### Overview

Probabilistic forecasting produces a probability distribution over future values, allowing you to understand the likelihood of different outcomes. This is in contrast to point forecasting, which provides only a single expected value. The Databricks platform supports this workflow through integration with specialized libraries and GPU-accelerated clusters. ^[classic-machine-learning-databricks-on-aws.md]

### Tools and Libraries

#### GluonTS
[GluonTS](https://gluon-ts.mxnet.io/) is a probabilistic time series modeling library built on Apache MXNet. It provides a suite of pre-built deep learning models for forecasting. ^[classic-machine-learning-databricks-on-aws.md]

#### DeepAR
The [DeepAR](https://gluon-ts.mxnet.io/api/gluon_ts.model.deepar.html) model, available through GluonTS, is a popular autoregressive recurrent neural network (RNN) designed for probabilistic forecasting. It can learn complex patterns across multiple related time series, known as "global modeling," and outputs a distribution for each prediction horizon. ^[classic-machine-learning-databricks-on-aws.md]

### Typical Workflow

An end-to-end workflow for probabilistic time series forecasting on Databricks generally involves the following steps, as demonstrated in the example with electricity consumption data: ^[classic-machine-learning-databricks-on-aws.md]

1.  **Data Ingestion:** Loading the historical time series data (e.g., electricity consumption records) into a Databricks DataFrame.
2.  **Data Resampling:** Converting the ingested data into a consistent time frequency suitable for modeling, such as hourly or daily intervals.
3.  **Model Training:** Training the probabilistic forecasting model (e.g., DeepAR) on the resampled data. This step can be accelerated using GPU-accelerated clusters, such as those available on Databricks. ^[classic-machine-learning-databricks-on-aws.md]
4.  **Prediction:** Generating probabilistic forecasts from the trained model.
5.  **Visualization and Evaluation:** Plotting the predictions with confidence intervals (e.g., the 90% prediction interval) and evaluating the model's performance against a held-out test set.

### Benefits on Databricks

- **GPU Acceleration:** Training deep learning probabilistic models like DeepAR can be computationally intensive. Databricks serverless GPU clusters can significantly reduce training time. ^[classic-machine-learning-databricks-on-aws.md]
- **Unified Platform:** The entire workflow—from data ingestion and preprocessing to model training, inference, and evaluation—can be executed within a single platform, simplifying the development and deployment pipeline.
- **Scalability:** Databricks can handle large volumes of time series data from multiple sources, enabling the training of robust global forecasting models.

### Example Use Case

A typical use case demonstrated in Databricks documentation involves forecasting electricity consumption. The workflow uses historical consumption data to train a DeepAR model, which then generates probabilistic forecasts. The output includes both a point forecast (median prediction) and an uncertainty range (prediction interval), allowing analysts to assess the potential variability in future electricity demand. ^[classic-machine-learning-databricks-on-aws.md]

### Related Concepts

- [GluonTS](/concepts/gluonts.md)
- [DeepAR Model](/concepts/deepar-model.md)
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md)
- Time Series Analysis
- GPU Computing on Databricks
- [Serverless GPU Clusters](/concepts/databricks-serverless-gpu-clusters.md)

### Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
