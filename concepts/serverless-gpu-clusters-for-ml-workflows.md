---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eeb5d532254dc32eb463aed57b7bfacb4e3c5c1c5d00c0d6b54d5c37b92f9fd7
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-clusters-for-ml-workflows
    - SGCFMW
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: classic-machine-learning-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Serverless GPU Clusters for ML Workflows
description: Databricks provides serverless GPU clusters for running machine learning workloads such as time-series forecasting with minimal infrastructure management.
tags:
  - databricks
  - infrastructure
  - gpu
  - machine-learning
timestamp: "2026-06-19T14:11:46.635Z"
---

# Serverless GPU Clusters for ML Workflows

**Serverless GPU Clusters for ML Workflows** refers to on-demand, auto‑scaling compute environments that provide GPU accelerators without requiring users to manage underlying infrastructure. On Databricks, serverless GPU clusters enable data scientists and ML engineers to run training, evaluation, and inference tasks using GPU resources that are provisioned and scaled automatically.

## Overview

Serverless GPU clusters eliminate the operational overhead of cluster management. Users select a GPU type and configuration from a simple interface, and the platform handles resource provisioning, scaling, and teardown. This model is particularly beneficial for deep learning workflows that require high‑throughput or large‑memory GPUs for short or intermittent jobs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## GPU Configurations

Databricks Serverless GPU compute offers configurations such as a single‑node setup with eight NVIDIA H100 80 GB HBM3 GPUs (640 GB total GPU memory). Users can choose this configuration from the notebook compute selector by picking **Serverless GPU**, then selecting **8xH100** as the accelerator, and applying the **AI v5** environment. The environment includes all libraries needed for distributed GPU workloads. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

Other GPU types, such as A100 GPUs, are supported across all cloud providers and are recommended for tasks like LLM training, NLP, and recommendation engines. However, A100 availability may be limited, so capacity reservation is advised. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Use Cases for ML Workflows

Serverless GPU clusters are well‑suited for:

- **Large model training** – workloads that benefit from high FLOPS and large HBM, such as Large Language Model (LLM) training.
- **Multi‑GPU distributed training** – leveraging the `@distributed` decorator from the `serverless_gpu` library to parallelize functions across GPUs on a single node.
- **Time series forecasting** – for example, using [GluonTS](/concepts/gluonts.md)’s DeepAR model to train on electricity consumption data. An end‑to‑end notebook demonstrates data ingestion, resampling, training, prediction, visualization, and evaluation on a serverless GPU cluster. ^[classic-machine-learning-databricks-on-aws.md]
- **Inference and evaluation** – running MLflow serverless workloads (e.g., scheduled scorers, synthetic evaluation set generation, agent evaluation) with controlled budget policies. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Distributed Programming with the `@distributed` Decorator

The `serverless_gpu` library provides a `@distributed` decorator to run a function across multiple GPUs on a single node. The `runtime` module offers local and global rank information for coordination. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(gpus=8, gpu_type='h100')
def train_model(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('Starting training:', name)
    return rt.get_global_rank()

result = train_model.distributed('MyModel')
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

- `gpus=8` runs the function on 8 processes, one per GPU.
- `rt.get_local_rank()` returns the rank within the node.
- `rt.get_global_rank()` returns the rank across all processes.

## Budget Policies for Serverless Workloads

When MLflow creates serverless workloads (e.g., for production monitoring or agent evaluation) on a GPU cluster, it uses a serverless budget policy. If the workspace’s default policy is disabled and no fallback policy is assigned, the **403 PERMISSION_DENIED Serverless Budget Policy Error** occurs. The fix is to set a budget policy on the MLflow experiment via the UI or the `mlflow.set_experiment_tag()` API. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – the specific serverless GPU setup with eight H100 GPUs.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – availability and best practices for A100 GPUs.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – memory‑efficient training for models larger than 20B parameters, often combined with serverless clusters.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – judge‑based evaluation that can run on serverless GPU compute.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – cost‑control mechanism for serverless GPU workloads.

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- classic-machine-learning-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
3. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
4. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
