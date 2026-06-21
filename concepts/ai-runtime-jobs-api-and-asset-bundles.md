---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d6dea6c60ba35ac1474e8db38253d288f346d07308a4ed9b51496b8e1c262be
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-jobs-api-and-asset-bundles
    - Asset Bundles and AI Runtime Jobs API
    - ARJAAAB
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime Jobs API and Asset Bundles
description: Programmatic creation and management of AI Runtime jobs using the Databricks Jobs API or Databricks Asset Bundles with YAML configuration for serverless GPU compute.
tags:
  - databricks
  - ai-runtime
  - api
  - infrastructure-as-code
timestamp: "2026-06-19T09:23:13.702Z"
---

# AI Runtime Jobs API and Asset Bundles

The **AI Runtime Jobs API and Asset Bundles** page describes how to programmatically create, schedule, and manage [AI Runtime](/concepts/ai-runtime.md) workloads using the Databricks Jobs API or Databricks Asset Bundles. These interfaces enable automated deployment pipelines for serverless GPU‑based single‑node tasks and distributed training jobs. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Jobs API

The Databricks Jobs API allows you to create and manage AI Runtime jobs programmatically. When defining a job, you configure the compute type as `serverless GPU` to leverage GPU accelerators such as 8×H100. The job definition specifies a notebook task and a reference to an [AI Runtime environment](/concepts/ai-runtime-environments.md). ^[connect-to-ai-runtime-databricks-on-aws.md]

## Databricks Asset Bundles

Databricks Asset Bundles provide a declarative YAML format for defining jobs, including their compute, environment, and task configuration. You can include an AI Runtime job in a bundle by setting `hardware_accelerator: GPU_8xH100` under the `compute` section and referencing an environment key. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Using the Default Base Environment

The following example configures a scheduled job in a bundle using the default [AI Runtime environment](/concepts/ai-runtime-environments.md) (version `'4'`). The environment key `default` points to `environment_version: '4'` and the task references it via `environment_key: default`.

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

^[connect-to-ai-runtime-databricks-on-aws.md]

### Using the AI Environment

To use the [Databricks AI environment](/concepts/databricks-ai-runtime-environment.md) instead of the default, set `base_environment` to the AI environment identifier (e.g., `databricks_ai_v5` for AI v5). The environment key is then referenced in the task's `environment_key`.

```yaml
resources:
  jobs:
    sample_job:
      name: sample_job_aiv5_h100
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
        - environment_key: aiv5
          spec:
            base_environment: databricks_ai_v5
      tasks:
        - task_key: notebook_task
          notebook_task:
            notebook_path: /Workspace/Users/your_email/your_notebook
          environment_key: aiv5
          compute:
            hardware_accelerator: GPU_8xH100
```

^[connect-to-ai-runtime-databricks-on-aws.md]

## Considerations for Scheduled Jobs

- **Dependencies**: The **Environment** side panel is not supported for scheduled jobs. Install dependencies programmatically inside your notebook (e.g., `%pip install`). ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Auto‑recovery**: Not supported. If a job fails due to incompatible packages, you must manually fix and re‑run it. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Long‑running workloads**: Jobs that may exceed the 7‑day maximum runtime should implement manual checkpointing. Use Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`. See Model Checkpointing. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime Environment](/concepts/ai-runtime-environments.md) – The pre‑built environments (default and AI) available for serverless GPU.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The compute type used for AI Runtime jobs.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) – General job creation and scheduling.
- Databricks Asset Bundles – Declarative infrastructure‑as‑code for Databricks.
- Model Checkpointing – Saving and resuming training state for long workloads.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
