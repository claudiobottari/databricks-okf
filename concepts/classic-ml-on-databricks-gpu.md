---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 311307f65fa4df1c339a90d36bb17e5d6120d8b165043b42b1f0af2e82fcf287
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - classic-ml-on-databricks-gpu
    - CMODG
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Classic ML on Databricks GPU
description: Notebook examples for traditional machine learning tasks on Databricks AI Runtime, including XGBoost model training and time series forecasting.
tags:
  - databricks
  - classic-ml
  - xgboost
  - time-series
timestamp: "2026-06-19T22:04:08.090Z"
---

# Classic ML on Databricks GPU

**Classic ML on Databricks GPU** refers to the use of GPU-accelerated compute on the Databricks platform for traditional machine learning tasks, including gradient-boosted tree models (such as XGBoost) and time series forecasting. While GPUs are commonly associated with deep learning, they can also accelerate certain classical machine learning workloads. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

Databricks provides AI Runtime environments that include GPU support for single-node and multi-node workloads. For classic machine learning tasks, the platform offers example notebooks demonstrating how to leverage GPU acceleration for traditional ML algorithms. These examples are part of the broader AI Runtime example notebook collection. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Supported Workloads

Classic ML on Databricks GPU supports the following traditional machine learning tasks:

- **XGBoost model training** — Gradient-boosted decision tree training can benefit from GPU acceleration, particularly for large datasets with many features. ^[ai-runtime-example-notebooks-databricks-on-aws.md]
- **Time series forecasting** — Traditional time series models can be trained on GPU hardware to reduce computation time for large-scale forecasting problems. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Availability

AI Runtime for single-node tasks is in **Public Preview**. The distributed training API for multi-GPU workloads remains in **Beta**. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime environment optimized for AI and machine learning workloads.
- XGBoost on Databricks — Specific guidance for running XGBoost with GPU acceleration.
- Time Series Analysis — Forecasting and analysis of time-ordered data.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU infrastructure for ML workloads.
- GPU-Accelerated Machine Learning — Broader category of ML tasks that benefit from GPU hardware.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
