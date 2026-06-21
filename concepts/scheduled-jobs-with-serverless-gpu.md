---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35557898c0f156b316dc4bc24ba6f342e7de3ef1e03a5d2e58642931bdb28a6c
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduled-jobs-with-serverless-gpu
    - SJWSG
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Scheduled Jobs with Serverless GPU
description: Recurring notebook jobs on serverless GPU compute, with limitations on environment panel usage and auto-recovery, plus a 7-day maximum runtime.
tags:
  - jobs
  - scheduling
  - databricks
timestamp: "2026-06-19T14:25:32.371Z"
---

# Scheduled Jobs with Serverless GPU

**Scheduled Jobs with Serverless GPU** refers to the ability to run Databricks notebooks that use [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) as recurring, automated jobs on a defined schedule. This feature enables production-grade, periodic execution of GPU-accelerated workloads — such as large language model (LLM) training, [model fine-tuning](/concepts/multi-node-llm-fine-tuning-with-fsdp.md), or [batch inference](/concepts/batch-inference-on-databricks.md) — without requiring persistent GPU clusters.

## Overview

Serverless GPU compute provisions GPU resources on demand and terminates them after a period of inactivity. When used with scheduled jobs, this compute model allows teams to run GPU-intensive tasks automatically — daily, hourly, or at any custom interval — while paying only for the compute time consumed during each run. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Scheduling a Notebook Job

To schedule a notebook that uses serverless GPU as a recurring job:

1. Open the notebook you want to schedule.
2. Select the **Schedule** button at the top right.
3. Select **Add schedule**.
4. Populate the **New schedule** form with:
   - **Job name** – A descriptive identifier for the job.
   - **Schedule** – The recurrence interval (e.g., daily, hourly).
   - **Compute** – Automatically inherits the serverless GPU configuration from the notebook.
5. Select **Create**.

^[connect-to-ai-runtime-databricks-on-aws.md]

You can also create and schedule jobs from the **Jobs and pipelines** UI. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Dependencies and Package Management

For scheduled serverless GPU jobs, adding dependencies using the **Environments** panel is **not supported**. All required libraries and packages must be installed programmatically within the notebook itself — for example, using `%pip install` commands in the notebook cells. ^[connect-to-ai-runtime-databricks-on-aws.md]

```python
# Example: Install a library within the notebook
%pip install transformers torch
```

## Auto-Recovery

Auto-recovery is **not supported** for serverless GPU scheduled jobs. If a job fails due to incompatible package versions, dependency conflicts, or other runtime errors, you must manually diagnose the issue, fix the notebook code, and re-submit the job. There is no automatic retry or fallback mechanism. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Runtime Limits and Checkpointing

Serverless GPU jobs have a **maximum runtime of 7 days**. For workloads that may exceed this limit — such as very long training sessions — you must implement manual checkpointing to allow resumption from the last saved state. ^[connect-to-ai-runtime-databricks-on-aws.md]

The recommended approach is to use [Unity Catalog](/concepts/unity-catalog.md) volumes for checkpoint storage, leveraging the `UCVolumeWriter` and `UCVolumeReader` classes from the `serverless_gpu.data` module. See Model checkpointing for detailed guidance. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Job API and Databricks Asset Bundles

You can programmatically create and manage serverless GPU jobs using:

- **Databricks Jobs API** – REST API for job creation and management.
- **Databricks Asset Bundles** – Infrastructure-as-code (YAML-based) definitions for defining jobs, environments, and compute configurations.

In either approach, you must configure the compute type as `hardware_accelerator: GPU_8xH100` (for 8× H100 GPUs) or the appropriate accelerator in your job or bundle definition. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Example: Databricks Asset Bundle Configuration

The following YAML snippet defines a scheduled job using serverless GPU with an H100 accelerator: ^[connect-to-ai-runtime-databricks-on-aws.md]

```yaml
resources:
  jobs:
    sample_job:
      name: sample_job_h100
      trigger:
        periodic:
          interval: 1
          unit: DAYS
      parameters:
        - name: catalog
          default: ${var.catalog}
        - name: schema
          default: ${var.schema}
      environments:
        - environment_key: default
          spec:
            environment_version: '4'
      tasks:
        - task_key: notebook_task
          notebook_task:
            notebook_path: /Workspace/Users/your_email/your_notebook
          environment_key: default
          compute:
            hardware_accelerator: GPU_8xH100
```

To use the [Databricks AI environment](/concepts/databricks-ai-runtime-environment.md) instead of the default base environment, set `base_environment` to the AI environment identifier (e.g., `databricks_ai_v5`) in the environment `spec` and reference it from the task's `environment_key`. ^[connect-to-ai-runtime-databricks-on-aws.md]

```yaml
environments:
  - environment_key: aiv5
    spec:
      base_environment: databricks_ai_v5
      # ...
tasks:
  - task_key: notebook_task
    environment_key: aiv5
    compute:
      hardware_accelerator: GPU_8xH100
```

## Use Cases

Scheduled serverless GPU jobs are well-suited for:

- **Daily model retraining** – Keeping models updated with new data.
- **Periodic batch inference** – Running predictions on large datasets at regular intervals.
- **Nightly evaluation runs** – Scoring agent configurations against a fixed evaluation dataset for A/B comparison.
- **Automated data pipelines** – Extracting, transforming, and loading (ETL) data with GPU-accelerated processing.

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The underlying compute infrastructure for on-demand GPU provisioning.
- [AI Runtime](/concepts/ai-runtime.md) – The Databricks environment for GPU-accelerated machine learning.
- Model checkpointing – Saving and resuming training state for long-running jobs.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for storing checkpoints and artifacts.
- Databricks Asset Bundles – Infrastructure-as-code for defining jobs and environments.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – The specific hardware configuration used for distributed GPU workloads.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
