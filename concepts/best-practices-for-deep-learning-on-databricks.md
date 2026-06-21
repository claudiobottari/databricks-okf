---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 79a25690a1f8279e101ac1f68d26e94338442998078e92eb24349032562e9054
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - best-practices-for-deep-learning-on-databricks
    - BPFDLOD
  citations:
    - file: deep-learning-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Best Practices for Deep Learning on Databricks
description: Optimization guidelines and recommended workflows for developing and fine-tuning deep learning models efficiently on the Databricks platform.
tags:
  - deep-learning
  - best-practices
  - databricks
  - optimization
timestamp: "2026-06-19T14:58:16.804Z"
---

# Best Practices for Deep Learning on Databricks

**Best Practices for Deep Learning on Databricks** provides guidelines for optimizing deep learning workflows, including model training, distributed computing, GPU utilization, and experiment tracking on the Databricks platform.

## Overview

Deep learning on Databricks involves using frameworks like PyTorch and TensorFlow within [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which includes pre-installed libraries and GPU support. Following best practices ensures efficient resource utilization, faster training times, and reproducible results. ^[deep-learning-databricks-on-aws.md]

## GPU Selection and Configuration

### Supported GPU Types

Databricks supports [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) across all cloud providers (AWS, Azure, GCP). A100 GPUs are recommended for training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

For the complete list of supported GPU instance types, see the Databricks documentation on [supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Availability Planning

A100 GPUs typically have limited capacity in cloud environments. Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance to ensure availability for workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Framework Selection

### PyTorch

PyTorch is included in Databricks Runtime ML and provides GPU-accelerated tensor computation and high-level functionalities for building deep learning networks. You can perform single-node training or distributed training with PyTorch on Databricks. For an end-to-end tutorial notebook using PyTorch and MLflow, see the MLflow 3 deep learning workflow. ^[deep-learning-databricks-on-aws.md]

### TensorFlow

Databricks Runtime ML includes TensorFlow and TensorBoard, so you can use these libraries without installing any packages. TensorFlow supports deep learning and general numerical computations on CPUs, GPUs, and clusters of GPUs. TensorBoard provides visualization tools to help debug and optimize machine learning and deep learning workflows. ^[deep-learning-databricks-on-aws.md]

## Distributed Training Strategies

Because deep learning models are data- and computation-intensive, distributed training is often important. Databricks supports several distributed training integrations:

- **Ray** – For distributed computing and reinforcement learning workloads
- **TorchDistributor** – For PyTorch-native distributed training
- **DeepSpeed** – For memory optimization in large model training

For examples of distributed deep learning using these integrations, see the [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) documentation. ^[deep-learning-databricks-on-aws.md]

## Experiment Tracking

Tracking remains a cornerstone of the MLflow ecosystem and is especially vital for the iterative nature of deep learning. Databricks uses [MLflow](/concepts/mlflow.md) to track deep learning training runs and model development. Use MLflow Tracking to log parameters, metrics, artifacts, and models throughout the training lifecycle. ^[deep-learning-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime with GPU support and deep learning libraries
- GPU Scheduling – Optimizing GPU utilization for distributed training and inference
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory-efficient training for large models
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Standard parallelism strategy for multi-GPU training
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On-demand GPU provisioning for deep learning workloads
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) – Common deep learning workload on Databricks

## Sources

- deep-learning-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
