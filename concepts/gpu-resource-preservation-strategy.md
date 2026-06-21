---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48678b491278dc004bdad6a6e1a83b082a02782f33175565fae035ff9f6c29d1
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-resource-preservation-strategy
    - GRPS
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: GPU resource preservation strategy
description: Operations that don't require GPUs (e.g., Git cloning, data conversion, EDA) should use a CPU cluster instead of serverless GPU to preserve GPU resources.
tags:
  - databricks
  - best-practice
  - gpu
timestamp: "2026-06-18T11:09:19.056Z"
---

# GPU Resource Preservation Strategy

**GPU resource preservation strategy** refers to the set of practices for reducing unnecessary consumption of GPU compute capacity in [AI Runtime](/concepts/ai-runtime.md) and serverless GPU environments. Because GPU time is a premium resource, avoiding waste during tasks that do not require GPU acceleration helps control costs and improves availability for workloads that genuinely need it.^[connect-to-ai-runtime-databricks-on-aws.md]

## Core Strategies

### Use CPU clusters for non-GPU operations

For operations that do not require GPUs—such as cloning a Git repository, converting data formats, or performing exploratory data analysis—attach your notebook to a CPU cluster instead of a serverless GPU compute. This preserves GPU resources for training, inference, and other GPU‑intensive tasks.^[connect-to-ai-runtime-databricks-on-aws.md]

In the interactive notebook environment, select a CPU cluster from the compute drop‑down menu rather than **Serverless GPU** when working on non‑GPU operations.^[connect-to-ai-runtime-databricks-on-aws.md]

### Leverage automatic idle timeout

Serverless GPU compute attached to an interactive notebook auto‑terminates after 60 minutes of inactivity. This idle timeout prevents GPU resources from being left running when a notebook is not actively in use. To avoid losing work, save results before stepping away, or rely on the timeout to automatically release resources.^[connect-to-ai-runtime-databricks-on-aws.md]

### Implement checkpointing for long-running jobs

AI Runtime scheduled jobs have a maximum runtime of 7 days. For workloads that may exceed this limit, implement manual checkpointing to allow resumption from the last saved state rather than restarting from scratch. Use Unity Catalog volumes via `UCVolumeWriter` and `UCVolumeReader` from `serverless_gpu.data` to persist intermediate results. This avoids wasting GPU time on recomputation if a job is interrupted or times out.^[connect-to-ai-runtime-databricks-on-aws.md]

### Choose the appropriate accelerator for the task

Select a hardware accelerator that matches the workload requirements. For distributed training workloads, the recommended option is **8xH100**. For smaller single‑node tasks, a less powerful accelerator may be sufficient, avoiding over‑provisioning of GPU resources. The choice is made in the **Environment** side panel of the notebook UI or in the job configuration when using the Jobs API or Databricks Asset Bundles.^[connect-to-ai-runtime-databricks-on-aws.md]

### Avoid using the Environments panel for job dependencies

For scheduled serverless GPU jobs, adding dependencies through the **Environments** panel is not supported. Dependencies must be installed programmatically within the notebook (e.g., using `%pip install`). If a job fails due to incompatible packages, auto‑recovery is not supported—the job must be manually fixed and re‑run. Following this guideline reduces the risk of failed job runs that waste GPU time on retries.^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The serverless GPU environment for machine learning workloads
- [Serverless GPU](/concepts/serverless-gpu-compute.md) — The compute type that provides on‑demand GPU capacity
- Cluster policies — Rules governing compute resource allocation
- Notebook jobs — Scheduled or triggered execution of notebooks
- Unity Catalog volumes — Storage for checkpointing and intermediate data
- Jobs API — Programmatic interface for creating and managing jobs
- Databricks Asset Bundles — Infrastructure‑as‑code for job definitions

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
