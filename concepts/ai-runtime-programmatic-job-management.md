---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eea9f540cddab02089b6b9c3acd200b76b0129a4f81bf0f238b6f4a7f77c2dd4
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-programmatic-job-management
    - ARPJM
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime programmatic job management
description: AI Runtime jobs can be created and managed programmatically using the Databricks Jobs API or Databricks Asset Bundles with YAML configuration specifying serverless GPU compute and environment settings.
tags:
  - databricks
  - ai-runtime
  - api
  - automation
timestamp: "2026-06-18T11:09:24.388Z"
---

# AI Runtime programmatic job management

**AI Runtime programmatic job management** covers how to create, schedule, and manage [AI Runtime](/concepts/ai-runtime.md) workloads — including both interactive notebooks and programmatic jobs — using the Databricks Jobs API and Databricks Asset Bundles. This allows you to automate ML training, fine-tuning, and inference pipelines on serverless GPU compute without manual setup. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Scheduled notebook jobs

Notebooks that use serverless GPU can be scheduled as recurring jobs through the Databricks UI. After opening the notebook:

1. Select the **Schedule** button in the top right.
2. Select **Add schedule**.
3. Fill in the job name, schedule, and compute.
4. Select **Create**.

You can also create and schedule jobs from the **Jobs and pipelines** UI. See Create and manage scheduled notebook jobs for detailed guidance. ^[connect-to-ai-runtime-databricks-on-aws.md]

> **Limitation:** Adding dependencies using the **Environments** panel is not supported for serverless GPU scheduled jobs. Dependencies must be installed programmatically within the notebook (for example, `%pip install`). Auto-recovery is not supported — if a job fails due to incompatible packages, you must manually fix and re-run. ^[connect-to-ai-runtime-databricks-on-aws.md]

For workloads that may exceed the 7-day maximum runtime, implement manual checkpointing to allow resumption. Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data` are recommended. See Model checkpointing for details. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Jobs API and Databricks Asset Bundles

You can programmatically create and manage AI Runtime jobs using the Databricks Jobs API or Databricks Asset Bundles. Configure the compute type as serverless GPU in your job or bundle definition to automate deployment pipelines. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Example: Databricks Asset Bundle (default environment)

The following YAML bundle configuration defines a scheduled AI Runtime job using the default base environment (`environment_version: '4'`) with an `8xH100` accelerator: ^[connect-to-ai-runtime-databricks-on-aws.md]

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

### Example: Using the AI environment

To use the [Databricks AI environment](/concepts/databricks-ai-runtime-environment.md) (e.g., AI v5) instead of the default base environment, set `base_environment` to the AI environment identifier (for example, `databricks_ai_v5`) in the environment `spec` and reference it from the task's `environment_key`: ^[connect-to-ai-runtime-databricks-on-aws.md]

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

## Best practices

- **Use programmatic dependency installation** when scheduling jobs. The **Environments** panel is not supported for serverless GPU scheduled jobs; install packages directly in the notebook with `%pip install`. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Implement manual checkpointing** for long-running workloads (exceeding 7 days). Use `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data` to save and resume state. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Attach to CPU clusters for non-GPU work** (e.g., clone repos, convert data, exploratory analysis) to preserve GPU resources. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related concepts

- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute infrastructure for AI Runtime jobs
- [AI Runtime Environments](/concepts/ai-runtime-environments.md) — Base and AI environment types
- [Hardware options](/concepts/ai-runtime-hardware-options.md) — Choosing the right accelerator
- Model checkpointing — Resuming long-running training jobs
- Create and manage scheduled notebook jobs
- Databricks Asset Bundles
- Databricks Jobs API

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
