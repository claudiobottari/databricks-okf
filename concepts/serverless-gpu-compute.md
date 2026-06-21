---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2af3d1c11de201fa1615c4f7368aa6d26aefed95f86db3a5b3b5b7765591332b
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-gpu-compute
    - SGC
    - Serverless Compute
    - Serverless GPU Computing
    - Serverless GPU cluster
    - Serverless compute
    - serverless GPU cluster
    - serverless compute
    - GPU clusters
    - Serverless Compute Clusters
    - Serverless GPU
    - serverless_gpu
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: Serverless GPU Compute
description: On-demand, auto-scaling GPU compute in Databricks that powers AI Runtime workloads and auto-terminates after 60 minutes of inactivity.
tags:
  - compute
  - gpu
  - databricks
timestamp: "2026-06-19T14:24:49.099Z"
---

# Serverless GPU Compute

**Serverless GPU Compute** is an on-demand compute offering on Databricks that automatically provisions and manages GPU infrastructure for deep learning workloads. Users connect to a serverless cluster without manually configuring clusters, scaling, or instance types — the platform handles resource allocation, lifecycle, and termination. ^[connect-to-ai-runtime-databricks-on-aws.md] ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Connecting to Serverless GPU Compute

### Interactive Notebooks

To use Serverless GPU Compute from a notebook:

1. From the compute drop-down menu at the top of the notebook, select **Serverless GPU**.
2. Click the **Environment** icon on the right panel to open the side panel.
3. Select an accelerator from the **Accelerator** field. For distributed training workloads, select **8xH100**.
4. Choose a **Base environment** — either **None** (default environment) or **AI v4** (AI environment).
5. Click **Apply** and then **Confirm**.

The connection auto-terminates after 60 minutes of inactivity. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Scheduled Jobs

Notebooks using serverless GPU can be scheduled as recurring jobs. To schedule a notebook:

1. Open the notebook and click **Schedule** (top right).
2. Select **Add schedule**.
3. Populate the form with a job name, schedule, and compute.
4. Click **Create**.

Dependencies must be installed programmatically within the notebook (e.g., `%pip install`); the Environments panel is not supported for scheduled jobs. Auto-recovery is not supported — failed jobs must be manually fixed and re-run. For workloads that may exceed the 7-day maximum runtime, implement manual checkpointing using Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Jobs API and Databricks Asset Bundles

Serverless GPU jobs can be created programmatically using the [Databricks Jobs API](https://docs.databricks.com/api/workspace/jobs) or [Databricks Asset Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/). Configure the compute type as serverless GPU in the job or bundle definition. For example, a bundle YAML specifies `hardware_accelerator: GPU_8xH100` and optionally sets the base environment to `databricks_ai_v5` for the AI environment. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Hardware Options

### 8xH100 Single-Node Configuration

The **8xH100** configuration provides eight NVIDIA H100 80GB HBM3 GPUs on a single compute node, offering 640 GB total GPU memory. It is intended for large model training workloads that require high FLOPS and high-bandwidth memory. To select it from a notebook: choose **8xH100** in the Accelerator field and select **AI v5** environment. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node. The `runtime` module gives access to local and global GPU ranks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### A100 GPU Support

Databricks supports NVIDIA A100 GPUs on all cloud providers. A100 GPUs are recommended for training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. However, A100 capacity is typically limited in cloud environments; users should contact their cloud provider for resource allocation or reserve capacity in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Serverless Budget Policy

Serverless workloads created by [MLflow](/concepts/mlflow.md) (e.g., scheduled scorers, synthetic evaluation set generation, agent evaluation) use the workspace’s default serverless budget policy. If that default policy is disabled and no fallback is available, MLflow returns a `403 PERMISSION_DENIED` error. To resolve this, set a serverless budget policy on the MLflow experiment — either via the experiment UI’s **Budget policy** field or by setting the `mlflow.workload_creation_policy_id` tag using `mlflow.set_experiment_tag()`. Users must have permission to use the assigned policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Distributed Training Best Practices

For training models in the 20B to 120B+ parameter range, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is the recommended approach. FSDP shards model parameters, gradients, and optimizer states across GPUs, reducing per-GPU memory footprint. Alternatives like [DeepSpeed](/concepts/deepspeed.md) offer additional memory optimization features. Standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) is appropriate only for models that fit entirely within a single GPU’s memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Best Practices Overview

- Use CPU clusters for non-GPU operations (e.g., Git cloning, data conversion, exploratory analysis) to preserve GPU resources. ^[connect-to-ai-runtime-databricks-on-aws.md]
- For distributed training across multiple nodes, coordinate 8xH100 nodes using DDP or FSDP.
- Implement manual checkpointing for jobs that risk exceeding the 7-day maximum runtime. ^[connect-to-ai-runtime-databricks-on-aws.md]
- Set a serverless budget policy on MLflow experiments to avoid permission errors for serverless evaluation workloads.

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- 403 PERMISSION_DENIED Serverless Budget Policy Error

## Sources

- connect-to-ai-runtime-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
4. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
5. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
