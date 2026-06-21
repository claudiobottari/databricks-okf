---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f1baab66feb1de3394e3e9fec2586cc2cc150dbe93bf78a09201f4a76916ae7
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-cluster-on-databricks
    - SGCOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: classic-machine-learning-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Serverless GPU Cluster on Databricks
description: A Databricks compute configuration that provides on-demand GPU resources without managing clusters, suitable for running deep learning workloads like time series forecasting.
tags:
  - infrastructure
  - databricks
  - gpu
  - serverless
timestamp: "2026-06-19T09:12:28.060Z"
---

# Serverless GPU Cluster on Databricks

**Serverless GPU Cluster on Databricks** refers to a compute configuration within the Databricks platform that provides on-demand, auto-scaling GPU resources without requiring users to manually provision or manage cluster infrastructure. Serverless GPU clusters enable data scientists and engineers to run GPU-accelerated workloads — such as deep learning training, large language model fine-tuning, and inference — with minimal operational overhead.

## Overview

Serverless GPU clusters eliminate the need to configure, start, stop, or resize clusters manually. Users define the required GPU type and resources, and Databricks automatically provisions the infrastructure, scales compute up or down based on workload demand, and terminates resources when idle. This model shifts infrastructure management from the user to the platform, allowing practitioners to focus on model development rather than cluster administration.

Serverless GPU clusters support a variety of GPU types offered by cloud providers, including NVIDIA A100, V100, T4, and others, depending on availability in the deployed cloud region. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Key Features

### Automatic Provisioning and Scaling

When a workload is submitted to a serverless GPU cluster, Databricks automatically provisions the required GPU nodes. As workload demands increase or decrease, the cluster scales accordingly. This auto-scaling behavior ensures cost efficiency by minimizing idle GPU hours. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### No Infrastructure Management

Users do not need to select instance types, configure auto-scaling policies, or manage cluster lifecycle. The serverless abstraction handles all infrastructure operations, including cluster creation, termination, and recovery from failures. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Supported Workloads

Serverless GPU clusters are suitable for a wide range of deep learning and machine learning tasks, including:

- Training and fine-tuning large language models (LLMs) and other deep neural networks
- Distributed training using frameworks like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) for models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range
- Batch inference and model serving
- Probabilistic time-series forecasting (e.g., with GluonTS DeepAR models)
- Natural language processing, computer vision, and recommendation engine workloads

^[classic-machine-learning-databricks-on-aws.md, best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Integration with MLflow

Serverless GPU clusters work natively with [MLflow](/concepts/mlflow.md) for experiment tracking, model registration, and evaluation. MLflow automatically logs training metrics, parameters, and artifacts when running on serverless GPU clusters, enabling reproducibility and collaboration.

## GPU Types and Availability

### Supported GPU Types

Serverless GPU clusters support the same GPU instance types available in the underlying cloud provider. Commonly available GPU types include:

- **NVIDIA A100** — High-performance GPU for large-scale training and inference. Typically has limited capacity; reserve capacity in advance from the cloud provider. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **NVIDIA V100** — Previous-generation high-performance GPU, still widely available.
- **NVIDIA T4** — Mid-range GPU optimized for inference and smaller training workloads.

For the complete list of supported GPU instance types, see the Databricks documentation on [supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Capacity Considerations

GPU capacity, particularly for high-end GPUs like A100s, is limited in cloud environments. Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance to ensure availability for workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Setting Up a Serverless GPU Cluster

1. In the Databricks workspace, navigate to **Compute** and select **Create compute**.
2. Under **Cluster mode**, select **Serverless**.
3. Choose the desired **GPU type** and **number of GPUs**.
4. Select a **Databricks Runtime** version that supports GPU workloads, such as the Databricks Runtime for Machine Learning.
5. Optionally configure a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to control spending on serverless GPU workloads.
6. Create the cluster and submit your workload.

## Cost Management

### Serverless Budget Policies

To control spending on serverless GPU workloads, administrators can configure [serverless budget policies](/concepts/serverless-budget-policy.md). These policies define spending limits and can be assigned to specific users, groups, or experiments. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Monitoring

Use the Databricks usage dashboard to monitor serverless GPU cluster costs, including GPU hours consumed, data processed, and other relevant metrics.

## Limitations and Considerations

- **403 PERMISSION_DENIED Serverless Budget Policy Error** — If a workspace disables the default serverless budget policy and no fallback policy is available, serverless workloads (including those created by MLflow) will fail with a `403 PERMISSION_DENIED` error. To resolve this, set a budget policy on the experiment or workspace. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **GPU availability** — High-end GPUs like A100s may have limited availability and require advance reservation.
- **Cold start latency** — Serverless clusters may take some time to provision initially, especially when starting from idle.

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-configured runtime with GPU support and deep learning libraries
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) — Strategies for scaling training across multiple GPUs and nodes
- GPU Scheduling — Optimizing GPU utilization for distributed workloads
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — Evaluation and monitoring of generative AI models
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying monitors on serverless infrastructure
- [When to use ABAC vs table-level row filters and column masks](/concepts/abac-policies-vs-table-level-row-filters-and-column-masks.md)

## Sources

- classic-machine-learning-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
