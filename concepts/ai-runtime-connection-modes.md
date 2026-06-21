---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db24e49a7c0b1205dcc36d4dec8908e0e487062429c3e3cf42d3a6dfb2c13588
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-connection-modes
    - ARCM
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime connection modes
description: "Three primary ways to connect to AI Runtime: interactive notebooks, scheduled jobs, and Jobs API/Databricks Asset Bundles."
tags:
  - databricks
  - ai-runtime
  - connectivity
timestamp: "2026-06-18T11:08:59.659Z"
---

# AI Runtime connection modes

AI Runtime can be used in three connection modes: interactive notebooks, scheduled jobs, and programmatic job creation via the Jobs API or Databricks Asset Bundles. The choice of mode depends on whether you are developing interactively, running recurring production workloads, or automating deployment pipelines. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Interactive notebooks

Attaching a notebook to AI Runtime is the primary way to explore and prototype GPU-accelerated workloads. The connection is made through the notebook’s compute selector and environment side panel: ^[connect-to-ai-runtime-databricks-on-aws.md]

1. From a notebook, click the compute drop-down menu and select **Serverless GPU**.
2. Click the environment icon to open the **Environment** side panel.
3. Select an accelerator from the **Accelerator** field. For distributed training workloads, choose **8xH100**.
4. For the **Base environment**, select **None** (the default base environment) or **AI v4** (the AI environment).
5. Click **Apply** and confirm.

The connection auto-terminates after 60 minutes of inactivity. After attaching, you can install dependencies and run GPU-accelerated code interactively. For tasks that do not require GPUs (e.g., cloning a repository or converting data formats), attach the notebook to a CPU cluster to preserve GPU resources. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Scheduled jobs

Notebooks connected to AI Runtime can be scheduled as recurring jobs. From the notebook, click **Schedule** > **Add schedule**, then provide a job name, schedule, and compute configuration, and click **Create**. You can also create and schedule jobs from the **Jobs and pipelines** UI. ^[connect-to-ai-runtime-databricks-on-aws.md]

Note the following restrictions for serverless GPU scheduled jobs: ^[connect-to-ai-runtime-databricks-on-aws.md]

- Adding dependencies via the **Environments** panel is not supported. Dependencies must be installed programmatically inside the notebook (e.g., `%pip install`).
- Auto-recovery is not supported. If a job fails due to incompatible packages, you must manually fix and re-run.
- If the workload may exceed the 7-day maximum runtime, implement manual checkpointing using `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`. See [model checkpointing](/concepts/ai-runtime-model-checkpointing.md) for guidance.

## Jobs API and Databricks Asset Bundles

AI Runtime jobs can be created and managed programmatically using the Databricks Jobs API or Databricks Asset Bundles. The compute type must be configured as serverless GPU. ^[connect-to-ai-runtime-databricks-on-aws.md]

The following example shows a Databricks Asset Bundle configuration for a scheduled AI Runtime job using the default base environment ([environment version](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment#default-env) `4`): ^[connect-to-ai-runtime-databricks-on-aws.md]

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

To use the AI environment instead, set `base_environment` to the AI environment identifier (e.g., `databricks_ai_v5` for AI v5) and reference the environment key from the task: ^[connect-to-ai-runtime-databricks-on-aws.md]

```yaml
resources:
  jobs:
    sample_job:
      ...
      environments:
        - environment_key: aiv5
          spec:
            base_environment: databricks_ai_v5
      tasks:
        - task_key: notebook_task
          ...
          environment_key: aiv5
          compute:
            hardware_accelerator: GPU_8xH100
```

## Related concepts

- [AI Runtime environment](/concepts/ai-runtime-environments.md) – The default and AI base environment options
- Hardware options for AI Runtime – Accelerator choices and guidance
- Model checkpointing – Saving and resuming long-running workloads
- Databricks Asset Bundles – Infrastructure-as-code for job definitions
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – The compute type used by AI Runtime

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
