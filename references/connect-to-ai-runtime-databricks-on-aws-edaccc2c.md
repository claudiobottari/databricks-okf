---
title: Connect to AI Runtime | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/connecting
ingestedAt: "2026-06-18T08:08:20.819Z"
---

Public Preview

AI Runtime for single-node tasks is in [Public Preview](https://docs.databricks.com/aws/en/release-notes/release-types). The distributed training API for multi-GPU workloads remain in [Beta](https://docs.databricks.com/aws/en/release-notes/release-types).

This article describes how to connect to AI Runtime from interactive notebooks, scheduled jobs, and the Jobs API.

## Interactive (Notebooks)[​](#-interactive-notebooks "Direct link to -interactive-notebooks")

This is the primary way to use AI Runtime. To connect your notebook and configure the environment:

1.  From a notebook, click the compute drop-down menu at the top and select **Serverless GPU**.
2.  Click the ![Environment icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDE1TDQgMTIuNjQ2NUMyLjg0NTc1IDEyLjMyIDIgMTEuMjU4OCAyIDEwQzIgOC43NDEyMiAyLjg0NTc1IDcuNjc5OTggNCA3LjM1MzUyTDQgMUg1LjVMNS41IDcuMzUzNTJDNi42NTQyNSA3LjY3OTk4IDcuNSA4Ljc0MTIyIDcuNSAxMEM3LjUgMTEuMjU4OCA2LjY1NDI1IDEyLjMyIDUuNSAxMi42NDY1TDUuNSAxNUg0Wk00Ljc1IDExLjI1QzQuMDU5NjQgMTEuMjUgMy41IDEwLjY5MDQgMy41IDEwQzMuNSA5LjMwOTY0IDQuMDU5NjQgOC43NSA0Ljc1IDguNzVDNS40NDAzNiA4Ljc1IDYgOS4zMDk2NCA2IDEwQzYgMTAuNjkwNCA1LjQ0MDM2IDExLjI1IDQuNzUgMTEuMjVaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTAuNSAxTDEwLjUgMy4zNTM1MkM5LjM0NTc1IDMuNjc5OTggOC41IDQuNzQxMjIgOC41IDZDOC41IDcuMjU4NzggOS4zNDU3NSA4LjMyMDAyIDEwLjUgOC42NDY0OFYxNUgxMlY4LjY0NjQ4QzEzLjE1NDMgOC4zMjAwMiAxNCA3LjI1ODc4IDE0IDZDMTQgNC43NDEyMiAxMy4xNTQzIDMuNjc5OTggMTIgMy4zNTM1MkwxMiAxSDEwLjVaTTExLjI1IDQuNzVDMTAuNTU5NiA0Ljc1IDEwIDUuMzA5NjQgMTAgNkMxMCA2LjY5MDM2IDEwLjU1OTYgNy4yNSAxMS4yNSA3LjI1QzExLjk0MDQgNy4yNSAxMi41IDYuNjkwMzYgMTIuNSA2QzEyLjUgNS4zMDk2NCAxMS45NDA0IDQuNzUgMTEuMjUgNC43NVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) to open the **Environment** side panel.
3.  Select an accelerator from the **Accelerator** field. For distributed training workloads, select **8xH100**. See [Hardware options](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/#hardware-options) for guidance on choosing an accelerator.
4.  Select **None** for the [default environment](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment#default-env) or **AI v4** for the [AI environment](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment#ai-env) from the **Base environment** field.
5.  Click **Apply** and then **Confirm** that you want to apply the AI Runtime to your notebook environment.

note

Connection to your compute auto-terminates after 60 minutes of inactivity.

tip

For operations that do not require GPUs (for example, cloning a Git repository, converting data formats, or exploratory data analysis), attach your notebook to a CPU cluster to preserve GPU resources.

## Jobs (Scheduled)[​](#-jobs-scheduled "Direct link to -jobs-scheduled")

You can schedule notebooks that use serverless GPU as recurring jobs. See [Create and manage scheduled notebook jobs](https://docs.databricks.com/aws/en/notebooks/schedule-notebook-jobs) for more details.

After you open the notebook you want to use:

1.  Select the **Schedule** button on the top right.
2.  Select **Add schedule**.
3.  Populate the **New schedule** form with the _Job name_, _Schedule_, and _Compute_.
4.  Select **Create**.

You can also create and schedule jobs from the **Jobs and pipelines** UI. See [Create a new job](https://docs.databricks.com/aws/en/jobs/configure-job) for step-by-step guidance.

note

Adding dependencies using the **Environments** panel is not supported for serverless GPU scheduled jobs. Dependencies must be installed programmatically within your notebook (for example, `%pip install`). Auto-recovery is not supported — if your job fails due to incompatible packages, you must manually fix and re-run.

For workloads that may exceed the 7-day maximum runtime, implement manual checkpointing to allow resumption. We recommend using Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`. See [Model checkpointing](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/tracking-observability#model-checkpointing).

## Jobs API and Databricks Asset Bundles[​](#jobs-api-and-databricks-asset-bundles "Direct link to Jobs API and Databricks Asset Bundles")

You can programmatically create and manage AI Runtime jobs using the [Databricks Jobs API](https://docs.databricks.com/api/workspace/jobs) or [Databricks Asset Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/). Configure the compute type as serverless GPU in your job or bundle definition to automate deployment pipelines.

The following example shows a Databricks Asset Bundle configuration for an AI Runtime on serverless GPU job using the [default base environment](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment#default-env):

YAML

    resources:  jobs:    sample_job:      name: sample_job_h100      trigger:        periodic:          interval: 1          unit: DAYS      parameters:        - name: catalog          default: ${var.catalog}        - name: schema          default: ${var.schema}      environments:        - environment_key: default          spec:            environment_version: '4'      tasks:        - task_key: notebook_task          notebook_task:            notebook_path: /Workspace/Users/your_email/your_notebook          environment_key: default          compute:            hardware_accelerator: GPU_8xH100

To use the [Databricks AI environment](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/environment#ai-env) instead of the default base environment, set `base_environment` to the AI environment identifier (for example, `databricks_ai_v5` for AI v5) in the environment `spec` and reference it from the task's `environment_key`:

YAML

    resources:  jobs:    sample_job:      name: sample_job_aiv5_h100      trigger:        periodic:          interval: 1          unit: DAYS      parameters:        - name: catalog          default: ${var.catalog}        - name: schema          default: ${var.schema}      environments:        - environment_key: aiv5          spec:            base_environment: databricks_ai_v5      tasks:        - task_key: notebook_task          notebook_task:            notebook_path: /Workspace/Users/your_email/your_notebook          environment_key: aiv5          compute:            hardware_accelerator: GPU_8xH100
