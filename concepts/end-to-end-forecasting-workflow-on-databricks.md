---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 570f7db150eb307f6aa53faa4c2f218af42900eb8dcc7004f8cd80fc9a83dcc6
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - end-to-end-forecasting-workflow-on-databricks
    - EFWOD
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: End-to-End Forecasting Workflow on Databricks
description: Complete pipeline from data ingestion to visualization and evaluation for time-series forecasting on Databricks
tags:
  - workflow
  - databricks
  - time-series
timestamp: "2026-06-19T17:43:36.241Z"
---

# End-to-End Forecasting Workflow on Databricks

The **End-to-End Forecasting Workflow on Databricks** is a complete pipeline for performing probabilistic time-series forecasting using deep learning models on serverless GPU infrastructure. This workflow demonstrates how to integrate data ingestion, preprocessing, model training, prediction generation, visualization, and evaluation within a single Databricks notebook environment.

## Overview

This workflow leverages the Databricks platform's serverless GPU compute capabilities to run computationally intensive forecasting tasks. It is designed specifically for probabilistic time-series forecasting, where predictions are generated as probability distributions rather than single-point estimates. ^[classic-machine-learning-databricks-on-aws.md]

## Key Components

### Data Ingestion and Preprocessing
The workflow begins with loading time-series data, typically from external sources such as databases or data lakes. The data is then resampled to create a consistent time-frequency for modeling. Common resampling operations include converting irregularly-spaced timestamps to regular intervals like hourly or daily frequencies. ^[classic-machine-learning-databricks-on-aws.md]

### Model Architecture
The forecasting model uses **DeepAR**, a probabilistic forecasting model from the [GluonTS](/concepts/gluonts.md) library. DeepAR is an autoregressive recurrent neural network model that produces probabilistic forecasts by estimating a probability distribution for each time step in the prediction horizon. This enables the generation of prediction intervals and quantile forecasts alongside point estimates. ^[classic-machine-learning-databricks-on-aws.md]

### Training Infrastructure
Model training runs on a [Serverless GPU](/concepts/serverless-gpu-compute.md) cluster, which provides on-demand GPU resources without requiring manual cluster management. The notebook specification indicates using a [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) setup, provisioning eight NVIDIA H100 GPUs on a single compute node for high-throughput distributed training. ^[classic-machine-learning-databricks-on-aws.md]

### Prediction Generation
After training, the model generates probabilistic forecasts for the specified prediction horizon. These forecasts include:
- Point estimates (predicted mean values)
- Prediction intervals at specified confidence levels
- Quantile forecasts for different probability levels

^[classic-machine-learning-databricks-on-aws.md]

### Visualization and Evaluation
The workflow includes visualization of both historical data and forecast outputs, typically using time-series plotting libraries. Evaluation metrics are computed to assess forecast accuracy against hold-out data, including metrics such as:
- Mean Absolute Scaled Error (MASE)
- Root Mean Squared Error (RMSE)
- Quantile Loss
- Coverage probability

^[classic-machine-learning-databricks-on-aws.md]

## Implementation Details

The entire workflow is encapsulated within a single Databricks notebook that uses:
1. **PySpark** for data loading and preprocessing
2. **GluonTS** with PyTorch for model training
3. **Matplotlib** and **Pandas** for visualization
4. **Serverless GPU** compute for accelerated training

The notebook follows a typical machine learning pipeline structure: load → preprocess → train → predict → evaluate → visualize. ^[classic-machine-learning-databricks-on-aws.md]

## Use Cases

This workflow is particularly suitable for:
- Energy demand forecasting (as demonstrated with electricity consumption data)
- Retail demand planning
- Financial time-series forecasting
- Supply chain demand forecasting
- Operations capacity planning

^[classic-machine-learning-databricks-on-aws.md]

## Advantages

| Feature | Benefit |
|---------|---------|
| [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md) | Captures uncertainty in predictions |
| [Serverless GPU](/concepts/serverless-gpu-compute.md) | No infrastructure management required |
| DeepAR with GluonTS | Proven deep learning architecture for time series |
| [End-to-end pipeline](/concepts/end-to-end-forecasting-pipeline.md) | Single notebook for complete workflow |

## Related Concepts

- [Time Series Forecasting](/concepts/multi-series-forecasting.md)
- [Probabilistic Forecasting](/concepts/probabilistic-time-series-forecasting.md)
- Deep Learning
- [Serverless GPU Computing](/concepts/serverless-gpu-compute.md)
- [GluonTS](/concepts/gluonts.md)
- [DeepAR Model](/concepts/deepar-model.md)
- Concept Drift Monitoring
- Model Evaluation Metrics

## Sources

- classic-machine-learning-databricks-on-aws.md

---

## Instructions

- The page should be structured as a clear, readable markdown document
- Use headings, subheadings, bullet points, and tables where appropriate
- Only include information that is directly stated in the source material
- Add wikilinks to related concepts for cross-referencing
- Include a ## Sources section at the end with the source document citation
- Write in a neutral, informative tone
- Be thorough but concise

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
