---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7780f14787142732724d17f05ba05619fcafc768433a53b1bd6d729b18db69f1
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
    - ai-runtime-example-notebooks-databricks-on-aws.md
    - deep-learning-databricks-on-aws.md
    - distributed-training-using-deepspeed-databricks-on-aws.md
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - user-guides-for-ai-runtime-databricks-on-aws.md
  confidence: 0.75
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - ai-runtime
    - AI Runtime (Preview)
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
    - file: experiment-tracking-and-observability-databricks-on-aws.md
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
    - file: user-guides-for-ai-runtime-databricks-on-aws.md
    - file: ai-runtime-cli-databricks-on-aws.md
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: AI Runtime
description: Databricks' on-demand serverless GPU compute platform for distributed training workloads.
tags:
  - databricks
  - gpu-compute
  - serverless
timestamp: "2026-06-19T17:30:23.859Z"
---

# AI Runtime

**AI Runtime** is Databricks' serverless GPU compute platform designed for deep learning workloads. It provides fully managed GPU infrastructure that scales automatically, eliminating the need to provision or manage clusters manually. AI Runtime integrates natively with notebooks, scheduled jobs, the Jobs API, and Databricks Asset Bundles, and supports experiment tracking through [MLflow](/concepts/mlflow.md) and model checkpointing via [Unity Catalog](/concepts/unity-catalog.md) volumes. ^[connect-to-ai-runtime-databricks-on-aws.md, experiment-tracking-and-observability-databricks-on-aws.md]

AI Runtime is available in two release stages: single-node tasks are in **Public Preview**, while the distributed training API for multi-GPU workloads remains in **Beta**. ^[ai-runtime-example-notebooks-databricks-on-aws.md, user-guides-for-ai-runtime-databricks-on-aws.md]

## Connecting to AI Runtime

### Interactive Notebooks

To connect a notebook to AI Runtime, select **Serverless GPU** from the compute drop-down menu, open the **Environment** side panel, choose an accelerator (e.g., **8xH100** for distributed training), and select a base environment – either **None** (the default minimal environment) or an AI environment such as **AI v4**. A notebook session auto-terminates after 60 minutes of inactivity. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Scheduled Jobs

Notebooks using AI Runtime can be scheduled as recurring jobs. After opening the notebook, click **Schedule** → **Add schedule**, provide a job name, schedule, and select the compute. Dependencies must be installed programmatically within the notebook (e.g., `%pip install`); the **Environments** panel is not supported for serverless GPU scheduled jobs. Auto-recovery is not available – job failures due to incompatible packages require manual intervention. ^[connect-to-ai-runtime-databricks-on-aws.md]

### Jobs API and Databricks Asset Bundles

AI Runtime jobs can be created and managed programmatically with the [Databricks Jobs API](https://docs.databricks.com/api/workspace/jobs) or through Databricks Asset Bundles. In the bundle configuration, set `hardware_accelerator` to a value such as `GPU_8xH100`. To use the AI environment instead of the default base environment, specify `base_environment: databricks_ai_v5` in the environment spec and reference it from the task. ^[connect-to-ai-runtime-databricks-on-aws.md]

### AI Runtime CLI (Beta)

The `air` command-line interface submits and manages distributed training workloads on AI Runtime. The CLI uses YAML-based job configuration, integrates with MLflow, and supports workspace-based and git-based code workflows. Use the AI Runtime CLI when you want to submit GPU training workloads from your laptop and code editor without opening a notebook, or define training jobs declaratively in YAML for source control. ^[ai-runtime-cli-databricks-on-aws.md]

## Hardware Options

AI Runtime supports single-node GPU accelerators. The available GPU types are:

- **A10** – General availability.
- **H100 (Beta)** – Requires workspace admin to enable the Beta feature preview. The 8xH100 configuration provides eight NVIDIA H100 80GB HBM3 GPUs on a single node, offering 640 GB of total GPU memory and high throughput for large model training. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Environments

Two base environments are available:

- **Default (None)** – A minimal environment with only core libraries, providing maximum flexibility to install custom dependencies.
- **AI environment** – A pre-configured environment (e.g., AI v5) that includes popular ML frameworks such as PyTorch and Transformers, as well as the `serverless_gpu` Python library for distributed training APIs. ^[connect-to-ai-runtime-databricks-on-aws.md]

The AI environment identifier for use in Databricks Asset Bundles is `databricks_ai_v5`. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Distributed Training

AI Runtime supports distributed training across multiple GPUs on a single node. The `serverless_gpu` library provides a `@distributed` decorator for launching multi-GPU workloads. For advanced memory optimization, use [DeepSpeed](/concepts/deepspeed.md) (ZeRO Stage 1, 2, or 3) when training large language models in the 1 billion to 100+ billion parameter range. DeepSpeed offers features such as gradient accumulation fusion and CPU offloading that go beyond standard [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md). ^[distributed-training-using-deepspeed-databricks-on-aws.md]

For simpler use cases, consider [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) or [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) for PyTorch-native large model training. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Experiment Tracking and Observability

### MLflow Integration

AI Runtime integrates natively with [MLflow](/concepts/mlflow.md) for experiment tracking, model logging, and metric visualization. Key recommendations:

- Upgrade MLflow to version 3.7 or newer.
- Enable autologging for PyTorch Lightning with `mlflow.pytorch.autolog()`.
- Customize [MLflow Run](/concepts/mlflow-run.md) names using `mlflow.start_run(run_name="...")`.
- Use absolute paths for the `MLFLOW_EXPERIMENT_NAME` environment variable.
- Resume previous training by setting `MLFLOW_RUN_ID`.

A serverless GPU session automatically creates an MLflow experiment with the default name `/Users/{WORKSPACE_USER}/{get_notebook_name()}`, which can be overridden. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Viewing Logs

- **Notebook output** – Standard output and errors appear in cell output.
- **MLflow logs** – The MLflow experiment UI displays training metrics, parameters, and artifacts.

### Model Checkpointing

For distributed training, use `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data` with the Torch Distributed Checkpoint API. These backends stage I/O through a fast local NVMe directory and upload to or download from Unity Catalog volumes. Asynchronous saves allow training to continue while checkpoints upload. Checkpoint every 30 minutes to an hour to balance overhead and lost-work risk. ^[experiment-tracking-and-observability-databricks-on-aws.md]

### GPU Resource Monitoring

The **GPU resources** pane shows per-GPU utilization, memory usage, and temperature. It polls metrics every 10 seconds, retains up to 2 hours of history, and pauses after 5 minutes of inactivity. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Migrating Classic GPU Workloads to Serverless

When moving an existing deep learning workload from a classic Databricks cluster (with Databricks Runtime ML) to serverless (with AI Runtime), follow these steps:

1. **Replace cluster-dependent code** – Remove references to Spark-based distributed training (e.g., `TorchDistributor`) and replace them with the `@distributed` decorator from `serverless_gpu`.
2. **Update data loading** – Replace direct DBFS paths with Unity Catalog volumes paths (`/Volumes/...`). Replace local Spark DataFrame operations with Spark Connect. For streaming file-based data from volumes, use `UCVolumeDataset` from `serverless_gpu.data`.
3. **Reinstall dependencies** – Do not rely on Databricks Runtime ML pre-installed libraries. Add explicit `%pip install` commands for all required packages.
4. **Update checkpoint paths** – Move checkpoints from DBFS or local storage to Unity Catalog volumes. For distributed checkpointing, use `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data`.
5. **Update MLflow configuration** – Ensure experiment names use absolute paths and configure run names for easy restart.
6. **Test interactively first** – Validate your workload in an interactive notebook before scheduling it as a job.

^[user-guides-for-ai-runtime-databricks-on-aws.md]

## Usage and Costs

AI Runtime charges per GPU hour on the Model Training SKU. Prices include:
- H100 on demand: $7.00/GPU hour (US East)
- A10 on demand: $2.50/GPU hour (US East)

Monitor AI Runtime GPU spend by querying the billable usage system table (`system.billing.usage`). ^[user-guides-for-ai-runtime-databricks-on-aws.md]

## Limitations

- Maximum runtime for a workload is 7 days. Implement manual checkpointing and job resumption for longer training runs.
- GPU capacity may be constrained; cross-region GPUs may be used during high demand, incurring egress costs.
- The default environment does not include deep learning frameworks; they must be installed explicitly.
- For scheduled jobs, the **Environments** panel is not supported; install dependencies programmatically.
- Auto-recovery for incompatible package versions is not supported.
- AI Runtime is not supported for compliance security profile workspaces (HIPAA or PCI). ^[connect-to-ai-runtime-databricks-on-aws.md, experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Databricks Asset Bundles
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md)

## Sources

- connect-to-ai-runtime-databricks-on-aws.md
- distributed-training-using-deepspeed-databricks-on-aws.md
- experiment-tracking-and-observability-databricks-on-aws.md
- ai-runtime-cli-databricks-on-aws.md
- ai-runtime-example-notebooks-databricks-on-aws.md
- user-guides-for-ai-runtime-databricks-on-aws.md
- deep-learning-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
2. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
3. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
4. [user-guides-for-ai-runtime-databricks-on-aws.md](/references/user-guides-for-ai-runtime-databricks-on-aws-495c5d9c.md)
5. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
6. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
