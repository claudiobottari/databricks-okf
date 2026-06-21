---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa47e109c6b0da7c539dfaeadf3d636e9f4dccfc4f06619f423b56ecc2b02ae7
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-compute-for-classic-machine-learning
    - SGCFCML
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
title: Serverless GPU Compute for Classic Machine Learning
description: Using serverless GPU clusters on Databricks to accelerate classic machine learning workloads such as time series forecasting with deep learning models.
tags:
  - infrastructure
  - gpu-computing
  - databricks
timestamp: "2026-06-18T14:35:59.263Z"
---

# Serverless GPU Compute for Classic Machine Learning

**Serverless GPU Compute for Classic Machine Learning** refers to the use of on-demand, auto-scaling GPU infrastructure without requiring users to manage underlying cluster configuration, specifically for traditional machine learning workloads such as time series forecasting, classification, and regression — as opposed to large-scale deep learning or large language model (LLM) training.

## Overview

Serverless GPU compute enables data scientists and engineers to run classic machine learning workflows on GPU-accelerated infrastructure without the operational overhead of provisioning, configuring, or scaling clusters manually. This approach is particularly valuable for workloads that benefit from GPU acceleration but do not require the distributed training infrastructure necessary for large models.^[classic-machine-learning-databricks-on-aws.md]

## Use Cases

### Time Series Forecasting

Serverless GPU compute can be used for probabilistic time series forecasting tasks. For example, the GluonTS DeepAR model can run an end-to-end workflow that includes data ingestion, resampling, model training, prediction, visualization, and evaluation on a serverless GPU cluster. This demonstrates how classic machine learning techniques benefit from GPU acceleration without requiring manual infrastructure management.^[classic-machine-learning-databricks-on-aws.md]

## Benefits

- **No Infrastructure Management:** Users do not need to provision, configure, or scale GPU clusters manually.
- **Auto-Scaling:** Resources scale automatically based on workload demands.
- **Cost Efficiency:** Users pay only for the compute resources consumed during execution.
- **Accessibility:** Lowers the barrier to using GPU acceleration for classic machine learning tasks.

## Implementation

Serverless GPU compute for classic machine learning is available through platforms like Databricks, which provides serverless compute options that support GPU acceleration. Workflows can be structured as end-to-end pipelines that leverage serverless GPU clusters for computationally intensive steps such as model training and evaluation.^[classic-machine-learning-databricks-on-aws.md]

## Related Concepts

- Serverless Compute — General infrastructure model for on-demand, auto-scaling compute
- GPU Scheduling — Optimizing GPU utilization for training and inference
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — A classic ML task that benefits from GPU acceleration
- [GluonTS](/concepts/gluonts.md) — A probabilistic time series modeling library
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime with GPU support
- [DeepAR](/concepts/deepar.md) — A probabilistic forecasting model available in GluonTS

## Sources

- classic-machine-learning-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
