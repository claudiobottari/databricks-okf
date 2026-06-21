---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a9f88d39761330d6b81f8d0027e065ccb02fa51a4580aeb8308ff107cadda382
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-environment-configuration
    - AREC
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime environment configuration
description: Configuration of AI Runtime involves selecting a serverless GPU compute, an accelerator type, and a base environment (None/default or AI v4/v5).
tags:
  - databricks
  - ai-runtime
  - configuration
timestamp: "2026-06-18T11:09:20.346Z"
---

# AI Runtime environment configuration

**AI Runtime environment configuration** refers to the process of selecting and applying the appropriate runtime environment, accelerator, and compute type for workloads running on Databricks AI Runtime. AI Runtime is designed for GPU-accelerated machine learning tasks such as training, fine-tuning, and inference, and supports both interactive notebooks and scheduled jobs.^[connect-to-ai-runtime-databricks-on-aws.md]

## Available Environments

AI Runtime provides two base environment options that determine the pre-installed libraries and dependencies available to your notebook or job:^[connect-to-ai-runtime-databricks-on-aws.md]

| Environment | Identifier | Description |
|---|---|---|
| **Default (Base) environment** | `4` (version) | The standard AI Runtime environment with core ML libraries |
| **AI environment** | `databricks_ai_v5` (AI v5) | An enhanced environment with additional AI/ML frameworks and tools |

The base environment selection affects which packages are available by default. For scheduled jobs, additional dependencies must be installed programmatically within your notebook (for example, using `%pip install`) — the **Environments** panel is not supported for serverless GPU scheduled jobs.^[connect-to-ai-runtime-databricks-on-aws.md]

## Hardware Accelerators

AI Runtime supports several GPU accelerator options. The primary option for distributed training workloads is **8xH100**, which provides eight H100 GPUs for multi-GPU training. The appropriate accelerator should be selected based on workload requirements, as documented in the [hardware options](/concepts/ai-runtime-hardware-options.md) guidance.^[connect-to-ai-runtime-databricks-on-aws.md]

For operations that do not require GPUs — such as cloning a Git repository, converting data formats, or exploratory data analysis — it is recommended to attach your notebook to a CPU cluster to preserve GPU resources for workloads that need them.^[connect-to-ai-runtime-databricks-on-aws.md]

## Configuring the Environment for Interactive Notebooks

To configure AI Runtime for an interactive notebook:

1. From a notebook, click the compute drop-down menu at the top and select **Serverless GPU**.
2. Click the **Environment** icon to open the **Environment** side panel.
3. Select an accelerator from the **Accelerator** field. For distributed training workloads, select **8xH100**.
4. Select **None** for the default environment or **AI v4** for the AI environment from the **Base environment** field.
5. Click **Apply** and then **Confirm** to apply the AI Runtime to your notebook environment.

Connection to your compute auto-terminates after 60 minutes of inactivity.^[connect-to-ai-runtime-databricks-on-aws.md]

## Configuring the Environment for Scheduled Jobs

You can schedule notebooks that use serverless GPU as recurring jobs. To schedule a notebook:

1. Open the notebook you want to use.
2. Select the **Schedule** button on the top right.
3. Select **Add schedule**.
4. Populate the **New schedule** form with the job name, schedule, and compute.
5. Select **Create**.

Alternatively, you can create and schedule jobs from the **Jobs and pipelines** UI. See [configure-job](/concepts/yaml-based-job-configuration.md) for step-by-step guidance.^[connect-to-ai-runtime-databricks-on-aws.md]

### Limitations for Scheduled Jobs

- Adding dependencies using the **Environments** panel is not supported for serverless GPU scheduled jobs. Dependencies must be installed programmatically within your notebook.
- Auto-recovery is not supported — if your job fails due to incompatible packages, you must manually fix and re-run.
- For workloads that may exceed the 7-day maximum runtime, manual checkpointing is recommended to allow resumption. Use [Unity Catalog](/concepts/unity-catalog.md) volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`.^[connect-to-ai-runtime-databricks-on-aws.md]

## Configuring the Environment via Jobs API and Databricks Asset Bundles

You can programmatically create and manage AI Runtime jobs using the Databricks Jobs API or Databricks Asset Bundles. Configure the compute type as **serverless GPU** in your job or bundle definition to automate deployment pipelines.^[connect-to-ai-runtime-databricks-on-aws.md]

### Example: Default Base Environment

The following Databricks Asset Bundle configuration uses the default base environment with an 8xH100 accelerator:

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

### Example: AI Environment

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

- [AI Runtime](/concepts/ai-runtime.md) — The underlying GPU-accelerated runtime for ML workloads
- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute type used by AI Runtime
- Databricks Asset Bundles — Infrastructure-as-code for job definitions
- Databricks Jobs API — Programmatic job management
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and checkpoint storage
- Model checkpointing — Saving and resuming training progress

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
