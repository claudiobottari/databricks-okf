---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e0736976fba5810bff86d42e376e10735fbe11d54bd7c34b5b7efb698188281
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-for-single-node-tasks
    - ARFST
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: AI Runtime for single-node tasks
description: Public Preview feature of Databricks AI Runtime for running single-node machine learning workloads on GPU instances.
tags:
  - databricks
  - single-node
  - public-preview
  - gpu
timestamp: "2026-06-19T22:03:58.147Z"
---

# AI Runtime for single-node tasks

**AI Runtime for single-node tasks** is a compute option on Databricks currently in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types) that provides GPU-accelerated environments for machine learning workloads running on a single compute node. It is designed for tasks such as fine-tuning [large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md), computer vision, deep learning–based recommendation systems, and classic machine learning that can benefit from GPU acceleration without requiring multi-node distributed training. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

AI Runtime for single-node tasks offers a serverless GPU compute experience that automatically manages infrastructure so that practitioners can focus on model development rather than cluster management. The distributed training API for multi-GPU workloads remains in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types). ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example Workloads

AI Runtime supports a variety of single-node GPU workloads, with example notebooks available for each domain: ^[ai-runtime-example-notebooks-databricks-on-aws.md]

- **Large language models (LLMs):** Fine-tuning LLMs including parameter-efficient methods like [Low-Rank Adaptation (LoRA)](/concepts/low-rank-adaptation-lora.md) and full supervised fine-tuning.
- **Computer vision:** Object detection and image classification tasks.
- **Deep learning based recommender systems:** Building recommendation systems using modern approaches like [two-tower models](/concepts/two-tower-recommendation-model.md).
- **Classic ML:** Traditional machine learning tasks including XGBoost model training and time series forecasting.
- **Multi-GPU distributed training:** Scaling training across multiple GPUs and nodes using the Serverless GPU API (Beta).

## Related Concepts

- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute infrastructure powering AI Runtime.
- Databricks Runtime — The broader runtime environment.
- [MLflow](/concepts/mlflow.md) — Experiment tracking and model management.
- Model checkpointing — Techniques for resuming long-running training jobs.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
