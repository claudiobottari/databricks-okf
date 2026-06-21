---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c5e3543c928ea8ce1bb563f08413bdb8b4302437682e9f3feff33ea379c43b4
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-runtime-usage-constraints
    - ARUC
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: AI Runtime Usage Constraints
description: "Key operational constraints for AI Runtime: 60-minute auto-termination on inactivity, no Environments panel for scheduled jobs, no auto-recovery on failure, 7-day maximum job runtime, and required manual checkpointing for long-running workloads."
tags:
  - databricks
  - ai-runtime
  - limitations
  - best-practices
timestamp: "2026-06-19T09:24:14.244Z"
---

# AI Runtime Usage Constraints

**AI Runtime Usage Constraints** describe the operational limits, resource restrictions, and configuration rules that apply when using AI Runtime on Databricks for single-node and distributed training workloads. Understanding these constraints is essential for planning, executing, and troubleshooting AI workloads effectively.

## Overview

AI Runtime is a serverless compute environment designed for machine learning and deep learning tasks on Databricks. It provides both single-node capabilities (in Public Preview) and multi-GPU distributed training (in Beta). The environment imposes specific constraints on how users can interact with it, including connection limits, scheduling rules, and resource management requirements. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Connection and Auto-Termination Constraints

When a notebook is connected to AI Runtime, the connection to the compute resource **auto-terminates after 60 minutes of inactivity**. This means that if no code is executed within the notebook within that window, the serverless GPU resources are released. Users must re-establish the connection by re-attaching the notebook to the compute resource. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Best Practice for Non-GPU Workloads

For operations that do not require GPUs—such as cloning a Git repository, converting data formats, or exploratory data analysis—users should **attach their notebook to a CPU cluster** instead of using AI Runtime. This preserves GPU resources for actual training and inference tasks and avoids unnecessary consumption of limited GPU capacity. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Scheduled Job Constraints

When using AI Runtime for scheduled jobs (recurring notebook executions), several constraints apply:

- **Dependency installation**: Adding dependencies using the **Environments** panel is **not supported** for serverless GPU scheduled jobs. All dependencies must be installed programmatically within the notebook itself (for example, using `%pip install` commands). ^[connect-to-ai-runtime-databricks-on-aws.md]

- **Auto-recovery**: Automatic recovery from failures is **not supported**. If a scheduled job fails due to incompatible packages, users must manually fix the issue and re-run the job. There is no mechanism for automatic rollback or re-execution. ^[connect-to-ai-runtime-databricks-on-aws.md]

- **Maximum runtime**: Scheduled jobs may **exceed the 7-day maximum runtime** limit. For workloads that require longer execution, the source material recommends implementing manual checkpointing to allow resumption. This involves using Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data` for model checkpointing. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Environment Configuration Constraints

The **Environment** side panel in notebooks allows users to configure AI Runtime settings. However, there are specific constraints on what can be selected:

- **Default environment**: Users must select **None** for the default environment or **AI v4** (or later versions) for the AI environment from the **Base environment** field. Other environment versions may not be compatible with certain workloads. ^[connect-to-ai-runtime-databricks-on-aws.md]

- **Accelerator selection**: For distributed training workloads, users must select **8xH100** as the accelerator. Other accelerator configurations may not be supported for multi-GPU distributed training. See the [Hardware options](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/#hardware-options) documentation for guidance on choosing the correct accelerator. ^[connect-to-ai-runtime-databricks-on-aws.md]

## API and Asset Bundle Constraints

When using the **Databricks Jobs API** or **Databricks Asset Bundles** to programmatically create AI Runtime jobs, the following constraints apply:

- **Compute type**: The compute type must be configured as **serverless GPU** in job or bundle definitions. Other compute types (such as CPU clusters) are not supported for AI Runtime workloads. ^[connect-to-ai-runtime-databricks-on-aws.md]

- **Environment version**: For jobs using the default base environment, the `environment_version` must be set to `'4'` (or a compatible version). For jobs using the AI environment (for example, AI v5), the `base_environment` must be set to the appropriate identifier (such as `databricks_ai_v5`). ^[connect-to-ai-runtime-databricks-on-aws.md]

- **Hardware accelerator**: The `hardware_accelerator` must be explicitly specified (for example, `GPU_8xH100` for 8xH100 configurations). Other accelerators may not be available or supported. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Resource and Capacity Constraints

- **GPU availability**: A100 and H100 GPUs typically have **limited capacity** in cloud environments. Users should contact their cloud provider for resource allocation or reserve capacity in advance to ensure availability for workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **Memory constraints**: Models in the **20B to 120B+ parameter** range cannot fit in a single GPU's memory. This necessitates the use of [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or other distributed training strategies to overcome per-GPU memory limitations. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

- **Serverless budget policy**: If a workspace's default serverless budget policy is disabled, MLflow serverless workloads (such as scheduled scorers and agent evaluations) may fail with a **403 PERMISSION_DENIED** error. Users must set an explicit serverless budget policy on the MLflow experiment to resolve this. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU](/concepts/serverless-gpu-compute.md) – The compute type for AI Runtime on Databricks.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – The recommended distributed training strategy for models that do not fit in single-GPU memory.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – An alternative approach suitable for models that fit in a single GPU.
- [MLflow](/concepts/mlflow.md) – The experiment tracking and model management framework that interacts with AI Runtime.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – The control mechanism for serverless workload spending.
- Model checkpointing – Manual techniques for resuming long-running AI Runtime jobs.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer used for checkpointing via `UCVolumeWriter` and `UCVolumeReader`.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
2. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
3. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
4. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
