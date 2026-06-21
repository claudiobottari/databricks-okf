---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9af8d07dee9e9e099935c054047dc620f09097c123dda8b0c20071a6ff4e989c
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-ai-runtime
    - SAR
    - Single Node
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Single-node AI Runtime
description: Databricks AI Runtime configured for single-node ML tasks, currently in Public Preview
tags:
  - databricks
  - single-node
  - machine-learning
timestamp: "2026-06-19T08:57:15.570Z"
---

# Single-node AI Runtime

**Single-node AI Runtime** refers to the capability of [AI Runtime](/concepts/ai-runtime.md) on Databricks that supports training and inference tasks running on a single node, typically utilizing one or more GPUs within that node. It is designed for workloads that do not require distributed training across multiple nodes, such as fine-tuning moderate-sized models, computer vision tasks, and classic machine learning pipelines. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Status

AI Runtime for single-node tasks is in **Public Preview**. In contrast, the distributed training API for multi-GPU workloads remains in **Beta**. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Example Notebooks

Databricks provides a set of example notebooks that demonstrate how to use AI Runtime for single-node tasks across several domains: ^[ai-runtime-example-notebooks-databricks-on-aws.md]

- **Large Language Models (LLMs)** – Example notebooks for fine-tuning large language models, including parameter-efficient methods.
- **Computer Vision** – Example notebooks for object detection and image classification.
- **Deep Learning Based Recommender Systems** – Example notebooks for building recommendation systems using modern approaches like two-tower models.
- **Classic ML** – Example notebooks for traditional machine learning tasks, including XGBoost model training and time series forecasting.
- **Multi-GPU Distributed Training** – Example notebooks for scaling training across multiple GPUs and nodes using the [Serverless GPU API](/concepts/serverless-gpu-api.md).

While the first four categories are associated with single-node tasks, the Multi-GPU distributed training notebooks illustrate the Beta distributed training API.

## Usage

Single-node AI Runtime is suitable for users who need GPU acceleration for workloads that fit within a single node’s compute resources. It can be used directly in Databricks notebooks with the appropriate runtime version, and the provided example notebooks serve as starting points for common use cases.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- GPU Scheduling
- [Serverless GPU API](/concepts/serverless-gpu-api.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
