---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70134af8eea660623ca9312872e5086c9e70e293a531cfdb303902cdace64992
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - classic-ml-on-ai-runtime
    - CMOAR
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Classic ML on AI Runtime
description: Notebook examples for traditional ML tasks including XGBoost training and time series forecasting on AI Runtime
tags:
  - machine-learning
  - xgboost
  - time-series
  - databricks
timestamp: "2026-06-19T08:57:21.099Z"
---

# Classic ML on AI Runtime

**Classic ML on AI Runtime** refers to the use of Databricks' AI Runtime for traditional machine learning tasks, including gradient-boosted tree models (such as XGBoost), time series forecasting, and other conventional ML workflows that do not involve deep neural networks. AI Runtime provides GPU-accelerated infrastructure that can benefit even classic ML workloads by reducing training times and enabling larger-scale experimentation. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

While AI Runtime is often associated with large language models and deep learning, it also supports classic machine learning tasks. The runtime provides pre-configured environments with popular ML libraries, GPU acceleration, and optimized compute resources that can accelerate training for traditional algorithms. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Supported Classic ML Tasks

AI Runtime includes example notebooks for the following classic ML workloads:

- **XGBoost model training** – Gradient-boosted decision tree models for classification and regression tasks.
- **Time series forecasting** – Statistical and ML-based approaches for predicting future values based on historical data.

These examples demonstrate how to leverage GPU resources within AI Runtime to accelerate training for algorithms that are not inherently deep learning-based. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Availability

AI Runtime for single-node tasks is in **Public Preview**. The distributed training API for multi-GPU workloads remains in **Beta**. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The underlying compute environment for ML workloads on Databricks.
- GPU-Accelerated Machine Learning – Using GPUs to speed up ML training beyond deep learning.
- XGBoost on Databricks – Training gradient-boosted tree models in the Databricks environment.
- Time Series Forecasting on Databricks – Approaches for forecasting using Databricks infrastructure.
- [Large Language Models (LLMs) on AI Runtime](/concepts/large-language-models-llms-on-databricks.md) – Deep learning workloads also supported by AI Runtime.
- [Computer Vision on AI Runtime](/concepts/computer-vision-on-databricks-ai-runtime.md) – GPU-accelerated vision tasks.
- [Deep Learning Based Recommender Systems on AI Runtime](/concepts/deep-learning-based-recommender-systems-on-databricks.md) – Recommendation system examples.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
