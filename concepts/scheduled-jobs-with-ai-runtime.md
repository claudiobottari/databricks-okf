---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f604b27ccb0d262312fe0d7612e9a03937c44ebec3917a78b9925d8e4365c03
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scheduled-jobs-with-ai-runtime
    - SJWAR
    - Jobs API and AI Runtime
    - Scheduled Jobs
    - Scheduled jobs
    - Scheduling Notebook Jobs on AI Runtime
    - scheduled job
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Scheduled Jobs with AI Runtime
description: Recurring job execution on serverless GPU using AI Runtime, with restrictions on environment panel dependencies and auto-recovery.
tags:
  - databricks
  - jobs
  - scheduling
timestamp: "2026-06-18T14:43:42.577Z"
---

# Scheduled Jobs with AI Runtime

**Scheduled Jobs with AI Runtime** refers to the ability to run recurring notebook jobs on serverless GPU compute using Databricks AI Runtime. This feature enables automated execution of GPU-accelerated workloads — such as training runs, batch inference, or data processing — on a regular schedule without requiring a persistent cluster.

## Overview

AI Runtime supports scheduling notebooks as recurring jobs through the Databricks Jobs interface. This allows users to automate workloads that benefit from GPU acceleration, including large language model fine-tuning, deep learning inference, and other compute-intensive tasks. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Creating a Scheduled Job

### From a Notebook

To schedule a notebook that uses AI Runtime:

1. Open the notebook you want to schedule.
2. Select the **Schedule** button on the top right.
3. Select **Add schedule**.
4. Populate the **New schedule** form with the job name, schedule frequency, and compute configuration.
5. Select **Create**. ^[connect-to-ai-runtime-databricks-on-aws.md]

### From the Jobs and Pipelines UI

You can also create and schedule jobs from the **Jobs and pipelines** user interface. See the documentation on [configuring jobs](/concepts/yaml-based-job-configuration.md) for step-by-step guidance. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Limitations and Considerations

### Dependency Management

Adding dependencies using the **Environments** panel is not supported for serverless GPU scheduled jobs. Dependencies must be installed programmatically within your notebook — for example, using `%pip install` commands in a notebook cell. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Auto-Recovery

Auto-recovery is not supported for AI Runtime scheduled jobs. If a job fails due to incompatible packages or other errors, you must manually fix the issue and re-run the job. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Maximum Runtime

Jobs are subject to a maximum runtime of 7 days. For workloads that may exceed this limit, implement manual checkpointing to allow resumption. Databricks recommends using [Unity Catalog](/concepts/unity-catalog.md) volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`. See [model checkpointing](/concepts/ai-runtime-model-checkpointing.md) for more details. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Configuration Examples

### Using the Default Base Environment

The following Databricks Asset Bundle configuration shows a scheduled AI Runtime job using the default base environment:

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

To use the AI environment instead of the default base environment, set `base_environment` to the AI environment identifier (for example, `databricks_ai_v5` for AI v5) in the environment `spec` and reference it from the task's `environment_key`:

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

- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment that provides GPU-accelerated compute for machine learning workloads
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU compute that auto-terminates after 60 minutes of inactivity
- Model Checkpointing — Saving model state to enable job resumption for long-running workloads
- Databricks Asset Bundles — Infrastructure-as-code tool for defining and deploying jobs programmatically
- Jobs API — REST API for creating and managing job definitions

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
