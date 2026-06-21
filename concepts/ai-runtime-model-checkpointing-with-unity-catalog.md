---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b080869338d16ea0e3be8627b04af078619996c95949448cfb33d937f052adb2
  pageDirectory: concepts
  sources:
    - connect-to-ai-runtime-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-model-checkpointing-with-unity-catalog
    - ARMCWUC
  citations:
    - file: connect-to-ai-runtime-databricks-on-aws.md
title: AI Runtime model checkpointing with Unity Catalog
description: For long-running workloads exceeding 7 days, implement manual checkpointing using UCVolumeWriter and UCVolumeReader from serverless_gpu.data with Unity Catalog volumes.
tags:
  - databricks
  - ai-runtime
  - checkpointing
  - unity-catalog
timestamp: "2026-06-18T11:09:30.974Z"
---

# AI Runtime model checkpointing with Unity Catalog

**AI Runtime model checkpointing with Unity Catalog** refers to the practice of manually saving and resuming the state of long-running training or evaluation workloads on serverless GPU by writing intermediate model snapshots to Unity Catalog volumes. This technique is essential for workloads that may exceed the 7‑day maximum runtime of a single serverless GPU job. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Why checkpointing is needed

Serverless GPU jobs in [AI Runtime](/concepts/ai-runtime.md) have a 7‑day runtime limit. For training runs, large model fine‑tuning, or data processing pipelines that take longer than seven days, the job is terminated automatically. Without checkpointing, all progress is lost and the workload must restart from the beginning. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Recommended approach: Unity Catalog volumes

Databricks recommends using Unity Catalog volumes for checkpoint storage. The `serverless_gpu.data` module provides two utility classes for this purpose: ^[connect-to-ai-runtime-databricks-on-aws.md]

- `UCVolumeWriter` – writes checkpoint data to a Unity Catalog volume.
- `UCVolumeReader` – reads previously saved checkpoint data from a volume.

By periodically saving checkpoints during a job, you can later resume from the latest checkpoint if the job is interrupted or reaches the time limit. This manual checkpointing pattern must be implemented explicitly in your notebook or job code; it is not automatic. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Usage context

Checkpointing is especially relevant for scheduled notebook jobs that are created via the Jobs UI, Jobs API, or Databricks Asset Bundles and configured to use a serverless GPU compute type. When defining such a job, you must also ensure that dependencies (including any checkpointing libraries) are installed programmatically inside the notebook (for example, using `%pip install`). The Environments panel for dependency management is not supported for serverless GPU scheduled jobs. ^[connect-to-ai-runtime-databricks-on-aws.md]

## Related concepts

- Unity Catalog volumes – the storage layer used for checkpoint data.
- [AI Runtime](/concepts/ai-runtime.md) – the serverless GPU environment for notebooks and jobs.
- Model checkpointing – the general technique of saving and resuming training state (see the full Databricks documentation on model checkpointing for detailed API usage of `UCVolumeWriter` and `UCVolumeReader`).
- Databricks Asset Bundles – declarative tool for defining AI Runtime jobs.
- [Serverless GPU](/concepts/serverless-gpu-compute.md) – the compute type used by AI Runtime.

## Sources

- connect-to-ai-runtime-databricks-on-aws.md

# Citations

1. [connect-to-ai-runtime-databricks-on-aws.md](/references/connect-to-ai-runtime-databricks-on-aws-edaccc2c.md)
