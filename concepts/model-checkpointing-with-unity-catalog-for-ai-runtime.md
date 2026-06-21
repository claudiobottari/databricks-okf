---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4756f173ccae1f5009a00064427b4376cb30b774c785694e1358b861491e9324
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-checkpointing-with-unity-catalog-for-ai-runtime
    - MCWUCFAR
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: Model Checkpointing with Unity Catalog for AI Runtime
description: Recommended checkpointing strategy for long-running AI Runtime jobs using UCVolumeWriter and UCVolumeReader from serverless_gpu.data
tags:
  - databricks
  - checkpointing
  - Unity-Catalog
timestamp: "2026-06-19T17:51:36.792Z"
---

# Model Checkpointing with Unity Catalog for AI Runtime

**Model Checkpointing with Unity Catalog for AI Runtime** refers to the practice of periodically saving model training state to [Unity Catalog](/concepts/unity-catalog.md) volumes during distributed training jobs on the Databricks [AI Runtime](/concepts/ai-runtime.md). This technique enables resumption of long-running workloads that might exceed the platform’s maximum runtime limits.

## Overview

When training large models on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md), scheduled jobs have a maximum runtime of 7 days. For workloads that may exceed this limit, manual checkpointing must be implemented to allow resumption of training from a saved state. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Recommended Approach

Databricks recommends using Unity Catalog volumes for storing and loading checkpoints. The `serverless_gpu.data` module provides two utilities for this purpose:

- **`UCVolumeWriter`** — saves model checkpoints to a specified Unity Catalog volume.
- **`UCVolumeReader`** — loads previously saved checkpoints from a Unity Catalog volume.

These utilities handle the underlying storage operations and allow checkpoints to be accessed across job restarts. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Usage Context

Model checkpointing with Unity Catalog is particularly relevant for **scheduled notebook jobs** that use AI Runtime with serverless GPU compute. If a job is expected to run longer than 7 days, implementing checkpointing logic within the notebook is necessary. The checkpoint data persists in Unity Catalog volumes, which are durable and accessible across job invocations. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance and storage layer for data and AI assets in Databricks.
- Unity Catalog Volumes — Non-tabular data storage that can hold binary checkpoint files.
- [AI Runtime](/concepts/ai-runtime.md) — The Databricks runtime optimized for AI and ML workloads, including serverless GPU.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU infrastructure used for training jobs.
- serverless_gpu Python Library|serverless_gpu (Python library) — The Python package that provides `UCVolumeWriter` and `UCVolumeReader`.
- Job Scheduling in Databricks — How to schedule recurring notebook jobs.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
