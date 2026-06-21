---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d70c9dbe5e0a25cd934801b56ea0bf31b63502686cfe9ce4b9eab5b8e3353048
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduling-ai-runtime-jobs
    - SARJ
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Scheduling AI Runtime Jobs
description: Method for running recurring GPU-accelerated notebook jobs on serverless GPU with specific limitations on dependencies and auto-recovery
tags:
  - databricks
  - jobs
  - scheduling
timestamp: "2026-06-19T17:51:35.245Z"
---

# Scheduling AI Runtime Jobs

**Scheduling AI Runtime Jobs** refers to the process of running [AI Runtime](/concepts/ai-runtime.md) workloads on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) as recurring or programmatically triggered jobs using the Databricks Jobs system. This enables automated execution of notebooks that require GPU acceleration, such as Large Language Model (LLM) training or inference.

## Overview

AI Runtime is available in Public Preview for single-node tasks and in Beta for distributed multi-GPU workloads. Users can schedule notebooks that use Serverless GPU compute as recurring jobs, or create and manage jobs programmatically via the Databricks Jobs API or Databricks Asset Bundles (DABs). ^[connect-to-ai-runtime-databricks-on-aws.md]

## Scheduled Notebook Jobs

To schedule an existing notebook that uses Serverless GPU compute:

1. From the notebook, click the **Schedule** button at the top right.
2. Select **Add schedule**.
3. Fill in the **New schedule** form with the job name, schedule, and compute configuration.
4. Click **Create**.

Alternatively, you can create and schedule jobs from the **Jobs and pipelines** UI by following the standard Databricks job creation workflow. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Limitations and Considerations

- **Dependencies**: Adding dependencies via the **Environments** side panel is not supported for scheduled serverless GPU jobs. All third-party packages must be installed programmatically inside the notebook, for example using `%pip install`. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Auto-recovery**: Auto-recovery is not supported. If a job fails due to incompatible packages, you must manually fix the issue and re-run the job. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Runtime limit**: Scheduled notebook jobs have a maximum runtime of 7 days. For workloads that may exceed this limit, implement manual checkpointing to allow resumption. Databricks recommends using Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from the `serverless_gpu.data` module. ^[connect-to-ai-runtime-databricks-on-aws.md]
- **Auto-termination**: Interactive notebook sessions connected to AI Runtime auto-terminate after 60 minutes of inactivity. This does not affect scheduled jobs, which run independently. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Jobs API and Databricks Asset Bundles

You can programmatically create and manage AI Runtime jobs using the Databricks Jobs API or Databricks Asset Bundles. The compute type must be configured as serverless GPU in the job or bundle definition. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Example: Using the Default Base Environment

The following Databricks Asset Bundle configuration defines a scheduled job that runs a notebook on serverless GPU with the default base environment (`AI v4`):

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

### Example: Using the AI Environment

To use the [AI Runtime Environment](/concepts/ai-runtime-environments.md) (AI v5) instead of the default base environment, set `base_environment: databricks_ai_v5` in the environment spec and reference the corresponding `environment_key` from the task:

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

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The managed environment for GPU-accelerated machine learning on Databricks.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – On-demand GPU compute resources used by AI Runtime jobs.
- Model Checkpointing – Techniques for saving and resuming training state, recommended for long-running jobs.
- Databricks Asset Bundles – Infrastructure-as-code tool for defining and deploying jobs.
- Hardware Options for AI Runtime – Guidance on selecting accelerators (e.g., 8xH100).

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
