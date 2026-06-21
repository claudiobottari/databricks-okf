---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fbbbd7349a085815c3e9beca5ae0aedd8627400576f367acee0d45bc55f7d227
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-model-checkpointing
    - ARMC
    - model checkpointing
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime Model Checkpointing
description: Manual checkpointing mechanism using UCVolumeWriter and UCVolumeReader from the serverless_gpu.data module to enable resumption of workloads that may exceed the 7-day maximum runtime.
tags:
  - databricks
  - ai-runtime
  - checkpointing
  - fault-tolerance
timestamp: "2026-06-19T09:23:25.741Z"
---

# AI Runtime Model Checkpointing

**AI Runtime Model Checkpointing** refers to the practice of saving the state of a model during training or inference on [AI Runtime](/concepts/ai-runtime.md) for single-node tasks or distributed training on serverless GPU. Checkpointing is essential for resilient long-running workloads, enabling job resumption in the event of failure without requiring a full re-start.

## Overview

When using AI Runtime for scheduled jobs, the maximum runtime is 7 days. Workloads that may exceed this limit — or that risk being interrupted by [auto-termination](/concepts/ai-runtime-idle-auto-termination.md) due to inactivity or job failure — require manual checkpointing to allow resumption. ^[connect-to-ai-runtime-databricks-on-aws.md]

Checkpointing is also important for operations that do not require GPUs. For tasks like cloning a Git repository, converting data formats, or exploratory data analysis, attaching a notebook to a CPU cluster instead of a GPU cluster preserves GPU resources. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Recommended Implementation

Databricks recommends using Unity Catalog volumes for checkpointing via the `UCVolumeWriter` and `UCVolumeReader` utilities from the `serverless_gpu.data` module. These utilities provide a native interface for reading and writing model checkpoints to Unity Catalog managed storage. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md)
- Unity Catalog volumes
- [Serverless GPU](/concepts/serverless-gpu-compute.md)
- [Scheduled jobs](/concepts/scheduled-jobs-with-ai-runtime.md)
- Model checkpointing
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- Auto-termination

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
