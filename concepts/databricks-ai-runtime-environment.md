---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f1cde921d7aa5eb39e9f8e2147878b807fb5e8e66ddc764e6da39ef0e219440
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-environment
    - DARE
    - Databricks AI environment
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Databricks AI Runtime Environment
description: A pre-configured runtime environment (AI v5) on Databricks that bundles all required libraries for running serverless GPU compute workloads with H100 accelerators.
tags:
  - databricks
  - runtime
  - environment
  - configuration
timestamp: "2026-06-19T19:00:08.067Z"
---

# Databricks AI Runtime Environment

The **Databricks AI Runtime Environment** is a pre-configured compute environment for AI and machine learning workloads on Databricks. It bundles libraries, frameworks, and optimizations needed for tasks such as distributed GPU training, model serving, and data profiling. The environment is available through the compute selector when using serverless GPU compute. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Environment Versions

The AI Runtime Environment includes versioned releases. As of the current documentation, **AI v5** is a supported environment that contains all required libraries for running distributed GPU workloads, such as the `serverless_gpu` Python library and dependencies for multi-GPU training. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Usage

To use the AI Runtime Environment with serverless GPU compute:

1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab on the right panel, select the desired environment version (e.g., **AI v5**).
3. Choose an accelerator configuration (e.g., **8xH100** for eight H100 GPUs on a single node).
4. Click **Apply**.

The environment is automatically provisioned with all necessary libraries, enabling direct use of distributed programming patterns via the `@distributed` decorator and runtime utilities. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The on-demand GPU infrastructure that uses the AI Runtime Environment.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific accelerator configuration available within the environment.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – A training strategy that can be run inside the environment for large models.
- [MLflow experiments](/concepts/mlflow-experiment.md) – Can be configured with serverless budget policies that apply to workloads running in the AI Runtime Environment.
- [Data Profiling](/concepts/data-profiling.md) – Statistical analysis that can be performed on data using tools included in the environment.

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
