---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c7be61006f3e80bf052cd6f83a9511b783dee16c30ff2565d307d395acfd2f8
  pageDirectory: concepts
  sources:
    - applicable-model-terms-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-on-aws-platform
    - DOAP
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: data-profiling-metric-tables-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: applicable-model-terms-databricks-on-aws.md
title: Databricks on AWS Platform
description: Databricks' unified analytics platform deployed on Amazon Web Services infrastructure.
tags:
  - databricks
  - aws
  - platform
timestamp: "2026-06-19T17:34:48.918Z"
---

# Databricks on AWS Platform

**Databricks on AWS** is a unified data analytics and machine learning platform that runs on Amazon Web Services. It combines a cloud-native architecture with Apache Spark, Delta Lake, and purpose-built compute options to support data engineering, data science, and ML workflows from a single workspace.

## Overview

Databricks on AWS provides a managed infrastructure layer that abstracts cluster management, storage, and networking. Users can create interactive notebooks, jobs, and ML experiments using object storage (S3) as the data lake and a choice of compute configurations — from general-purpose CPU clusters to GPU-accelerated nodes for deep learning. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Compute Options

### GPU Instances

Databricks supports [A100 GPUs](/concepts/a100-gpu-support-on-databricks.md) across all clouds, including AWS, for tasks such as training large language models (LLMs), natural language processing, object detection, and recommendation engines. A100 GPUs provide high compute throughput but typically have limited capacity; Databricks recommends contacting the cloud provider in advance to reserve capacity. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md, best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

For serverless GPU workloads, the platform offers [8xH100 single-node configurations](/concepts/8xh100-single-node-configuration.md) with eight NVIDIA H100 80GB HBM3 GPUs per node. These are selected through the notebook compute selector under **Serverless GPU** → **8xH100** accelerator, using the **AI v5** environment. The `serverless_gpu` Python library provides a `@distributed` decorator for multi-GPU parallelism on a single node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Serverless Budget Policies

When serverless workloads are created by [MLflow](/concepts/mlflow.md) — such as scheduled scorers, synthetic evaluation set generation, or agent evaluation — they use the workspace’s default serverless budget policy. If the default policy is disabled, MLflow returns a `403 PERMISSION_DENIED` error. This can be resolved by setting an explicit budget policy on the experiment via the UI or the API tag `mlflow.workload_creation_policy_id`. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Data Profiling and Monitoring

Databricks provides built-in [Data Profiling](/concepts/data-profiling.md) that computes summary statistics and drift metrics for tables. For Time Series Analysis and [Inference Log Analysis](/concepts/inferencelog-analysis.md) profile types, the system applies a [30-Day Lookback Window](/concepts/30-day-lookback-window.md) by default: only data from the 30 days preceding the profile creation time is included. This can cause partial analysis windows during the first profile run when the lookback boundary falls mid‑granularity (e.g., mid‑week). ^[data-profiling-metric-tables-databricks-on-aws.md]

Metrics are stored in a [Profile Metrics Table](/concepts/profile-metrics-table.md) and a [Drift Metrics Table](/concepts/drift-metrics-table.md), which support data slicing by custom expressions. A [Baseline Table](/concepts/baseline-table.md) can be used as a reference for drift computation. ^[data-profiling-metric-tables-databricks-on-aws.md]

## Distributed Training for Large Models

For training models in the [20B to 120B+ parameter](/concepts/20b-to-120b-parameter-model-training.md) range, Databricks recommends [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). FSDP shards parameters, gradients, and optimizer states across GPUs, reducing per‑GPU memory and enabling training of models that would not fit on a single GPU. Alternatives like [DeepSpeed](/concepts/deepspeed.md) are available when more advanced memory optimization is required. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

FSDP is preferred over standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) for models that exceed single‑GPU memory, while DDP remains suitable for smaller models that fit comfortably. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Model Serving and Acceptable Use

Databricks on AWS supports model serving through [Model Serving](/concepts/model-serving.md). The platform’s acceptable use policy governs which models can be deployed; users must comply with the applicable model terms as defined in the product documentation. ^[applicable-model-terms-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Delta Lake on AWS](/concepts/delta-lake.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Data Slicing](/concepts/data-slicing-expressions.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- GPU Scheduling

## Sources

- applicable-model-terms-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- data-profiling-metric-tables-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
4. [data-profiling-metric-tables-databricks-on-aws.md](/references/data-profiling-metric-tables-databricks-on-aws-8eea6c26.md)
5. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
6. [applicable-model-terms-databricks-on-aws.md](/references/applicable-model-terms-databricks-on-aws-2e13c689.md)
