---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 40e6af0f6cb211e95618d58c5dc83270d3b7db11121a023b988c95fb9c715c6a
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-clusters
    - DSGC
    - Databricks GPU Clusters
    - Serverless GPU Clusters
    - Serverless GPU clusters
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: Databricks serverless GPU clusters
description: A compute environment on Databricks (AWS) that enables serverless GPU-accelerated workloads for classic machine learning tasks
tags:
  - databricks
  - gpu
  - serverless
  - infrastructure
timestamp: "2026-06-18T10:56:36.197Z"
---

# Databricks serverless GPU clusters

**Databricks serverless GPU clusters** are a compute offering in the Databricks platform that provide on-demand, auto-scaling GPU infrastructure without requiring users to manually configure or manage clusters. These clusters are designed for machine learning and deep learning workloads that benefit from GPU acceleration, such as training and inference with large models.

Serverless GPU clusters eliminate the overhead of provisioning and sizing clusters, allowing data scientists and ML engineers to focus on model development. They automatically scale compute resources based on workload demands and charge only for the resources consumed. The serverless model simplifies infrastructure management and enables faster iteration for GPU-intensive tasks.

## Usage with time series forecasting

A published notebook demonstrates an end-to-end workflow for probabilistic time-series forecasting using the GluonTS library and its DeepAR model on a serverless GPU cluster. The workflow covers data ingestion, resampling, model training, prediction, visualization, and evaluation.^[classic-machine-learning-databricks-on-aws.md]

This example illustrates how serverless GPU clusters can handle complex forecasting tasks that benefit from GPU acceleration during model training and inference.

## Related concepts

- GPU Clusters — Standard GPU-enabled compute clusters in Databricks
- Serverless Compute — The broader Databricks serverless compute model
- [GluonTS](/concepts/gluonts.md) — A probabilistic time series modeling library
- [DeepAR](/concepts/deepar.md) — A deep learning model for time series forecasting
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — Common ML use case on GPU clusters

## Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
