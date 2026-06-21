---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f9f54e4f3fe6efe6c2082f3146d16585497ec14bfd0a3b2326dbd417df4569e7
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-v5-environment
    - DAVE
    - Databricks AI environment
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Databricks AI v5 Environment
description: A Databricks runtime environment pre-packaged with libraries for AI/ML GPU workloads on Serverless GPU compute
tags:
  - databricks
  - environment
  - ai
  - ml
timestamp: "2026-06-19T10:45:02.354Z"
---

# Databricks AI v5 Environment

**Databricks AI v5 Environment** is a pre-configured runtime environment for Databricks Serverless GPU compute that includes all the libraries required to run GPU-accelerated workloads, particularly those using H100 accelerators. It is selected from the **Environment** drop-down in the compute configuration panel, alongside the choice of accelerator (such as 8xH100). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Usage

To use the AI v5 environment:

1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab (right panel), select **AI v5**.
3. Optionally, choose an accelerator like **8xH100** for multiple GPU chips.

The environment bundles the `serverless_gpu` Python library and other dependencies needed for distributed GPU computing, such as the `@distributed` decorator and `runtime` module shown in the H100 starter notebook. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## When to Use

The AI v5 environment is recommended for large model **training** tasks that benefit from high FLOPS and high-bandwidth memory provided by H100 GPUs. It supports distributed execution across multiple GPUs with minimal setup. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- H100 GPUs
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- serverless_gpu Python Library|serverless_gpu library

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
