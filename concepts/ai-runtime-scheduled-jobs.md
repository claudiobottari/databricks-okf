---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07281722688ce19891becd5aa831f5ab8517eaa98715dbd80c9241729f7c83dc
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-scheduled-jobs
    - ARSJ
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime Scheduled Jobs
description: Scheduling notebooks that use serverless GPU as recurring jobs with limitations on dependency management and auto-recovery.
tags:
  - databricks
  - ai-runtime
  - jobs
  - scheduling
timestamp: "2026-06-19T09:23:18.252Z"
---

# AI Runtime Scheduled Jobs

**AI Runtime Scheduled Jobs** allow you to run AI Runtime workloads on a recurring basis using [Serverless GPU Compute](/concepts/serverless-gpu-compute.md). Scheduled jobs can be created from interactive notebooks or the Jobs UI, and configured programmatically through the Jobs API or Databricks Asset Bundles. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Overview

AI Runtime supports scheduling notebooks that use serverless GPU compute as recurring jobs. This is useful for periodic training runs, batch inference, or any GPU-intensive workload that must run on a schedule. Scheduled jobs using AI Runtime are subject to certain limitations, including a 7-day maximum runtime and the need to install dependencies programmatically within the notebook. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Creating Scheduled Jobs

### Using the Notebook UI

To schedule a notebook running on AI Runtime: ^[connect-to-ai-runtime-databricks-on-aws.md]

1. Open the notebook you want to schedule.
2. Select the **Schedule** button on the top right.
3. Select **Add schedule**.
4. Populate the **New schedule** form with the _Job name_, _Schedule_, and _Compute_.
5. Select **Create**.

### Using the Jobs UI

You can also create and schedule jobs from the **Jobs and pipelines** UI. See Create and manage jobs for step-by-step guidance. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Jobs API and Databricks Asset Bundles

You can programmatically create and manage AI Runtime jobs using the Databricks Jobs API or Databricks Asset Bundles. Configure the compute type as serverless GPU in your job or bundle definition to automate deployment pipelines. ^[connect-to-ai-runtime-databricks-on-aws.md]

The following example shows a Databricks Asset Bundle configuration for an AI Runtime job using the default base environment: ^[connect-to-ai-runtime-databricks-on-aws.md]

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

To use the [Databricks AI environment](/concepts/databricks-ai-runtime-environment.md) instead of the default base environment, set `base_environment` to the AI environment identifier (for example, `databricks_ai_v5` for AI v5) in the environment `spec` and reference it from the task's `environment_key`: ^[connect-to-ai-runtime-databricks-on-aws.md]

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

## Limitations and Best Practices

- **Dependencies**: Adding dependencies using the **Environments** panel is **not supported** for serverless GPU scheduled jobs. Dependencies must be installed programmatically within your notebook (for example, `%pip install`). ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Auto-recovery**: Not supported — if your job fails due to incompatible packages, you must manually fix and re-run. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Maximum runtime**: For workloads that may exceed the 7-day maximum runtime, implement manual checkpointing to allow resumption. Databricks recommends using Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`. See Model checkpointing with AI Runtime. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Create and manage jobs
- Databricks Jobs API
- Databricks Asset Bundles
- [Databricks AI environment](/concepts/databricks-ai-runtime-environment.md)
- [AI Runtime](/concepts/ai-runtime.md)
- Model checkpointing with AI Runtime
- Scheduled notebook jobs

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
