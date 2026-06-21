---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55645d635cc9f5ee278060250f3d402018a9368d6ea64191be2472e916c47b7a
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-checkpointing-with-unity-catalog
    - MCWUC
    - ai-runtime-model-checkpointing-with-unity-catalog
    - ARMCWUC
    - model-checkpointing-with-unity-catalog-for-ai-runtime
    - MCWUCFAR
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Model Checkpointing with Unity Catalog
description: Using UCVolumeWriter and UCVolumeReader from serverless_gpu.data to implement manual checkpointing for long-running AI Runtime jobs that may exceed the 7-day maximum runtime.
tags:
  - checkpointing
  - unity-catalog
  - databricks
timestamp: "2026-06-19T14:24:40.538Z"
---

# Model Checkpointing with Unity Catalog

**Model Checkpointing with Unity Catalog** refers to the practice of saving intermediate model states during long-running training jobs on Databricks Serverless GPU compute, using [Unity Catalog](/concepts/unity-catalog.md) volumes as the storage backend. This technique enables job resumption after failures or timeouts, which is critical for workloads that may exceed the 7-day maximum runtime limit for serverless GPU jobs. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Overview

When training large models on serverless GPU infrastructure, jobs can be interrupted by timeouts, infrastructure failures, or other issues. Model checkpointing provides a mechanism to periodically save the model's state — including parameters, optimizer states, and training step — so that training can resume from the last saved checkpoint rather than starting from scratch. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Recommended Storage: Unity Catalog Volumes

Databricks recommends using Unity Catalog volumes for storing checkpoints. The `serverless_gpu.data` library provides dedicated utilities for this purpose: ^[connect-to-ai-runtime-databricks-on-aws.md]

- **`UCVolumeWriter`** — Writes checkpoint data to a Unity Catalog volume.
- **`UCVolumeReader`** — Reads checkpoint data from a Unity Catalog volume.

These utilities are designed to work with the serverless GPU environment and handle the underlying storage operations reliably. ^[connect-to-ai-runtime-databricks-on-aws.md]

## When to Use Checkpointing

Checkpointing is recommended for any workload that may exceed the 7-day maximum runtime for serverless GPU jobs. This includes: ^[connect-to-ai-runtime-databricks-on-aws.md]

- Large-scale model training runs
- Training jobs with extensive hyperparameter tuning
- Any distributed training workload where recovery time would be costly

## Implementation

To implement checkpointing, you must manually save and load checkpoints within your training code. The general pattern involves: ^[connect-to-ai-runtime-databricks-on-aws.md]

1. Periodically writing the model state to a Unity Catalog volume using `UCVolumeWriter`.
2. At job startup, checking for existing checkpoints and loading them with `UCVolumeReader` if available.
3. Resuming training from the loaded checkpoint state.

## Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure where checkpointing is particularly important.
- Unity Catalog Volumes — The recommended storage backend for checkpoints.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Training workloads that benefit most from checkpointing.
- Job Scheduling on Databricks — Scheduled jobs that may require checkpointing for long-running tasks.
- Model Training Best Practices — General guidance for reliable training workflows.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
