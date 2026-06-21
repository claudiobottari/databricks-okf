---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 784924cd44f426ec8a87baf71692f07733718fe7d52038c8f79a84d290dc4c5e
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-pipeline-state-vs-model-checkpointing
    - DPSVMC
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Data Pipeline State vs Model Checkpointing
description: Model checkpoints capture model and optimizer state but not data pipeline position, requiring explicit tracking of processed shards or epoch-boundary resumption strategies.
tags:
  - distributed-training
  - checkpointing
  - data-pipeline
timestamp: "2026-06-19T10:26:16.513Z"
---

# Data Pipeline State vs Model Checkpointing

**Data Pipeline State vs Model Checkpointing** refers to the distinction between saving the state of a model's training process (model checkpointing) and tracking the position of the data loading pipeline within a dataset (data pipeline state). Understanding this difference is critical when resuming interrupted training runs to ensure correct behavior and avoid data leakage.

## Overview

When training large models, it is common practice to save checkpoints periodically so that training can be resumed after an interruption. However, a standard model checkpoint captures only the model parameters and optimizer state — it does **not** record where the data pipeline was in the dataset at the time of the checkpoint. This mismatch must be accounted for when implementing resume logic.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Model Checkpointing

Model checkpoints are persistent snapshots of the model's parameters, optimizer state, and (optionally) learning rate schedules. They allow training to resume from a specific point in the optimization process without starting from scratch. On Databricks, model checkpoints can be saved asynchronously to Unity Catalog volumes using `UCVolumeWriter` from the `serverless_gpu.data` package, which stages I/O through NVMe-backed local storage before uploading to the volume.^[experiment-tracking-and-observability-databricks-on-aws.md]

Checkpoint frequency should balance the cost of lost work against I/O overhead. A recommended starting point is one checkpoint every 30 minutes to an hour, tuned based on step time and checkpoint size.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Data Pipeline State

Data pipeline state tracks which samples, shards, or batches have already been consumed from the training dataset. Unlike model checkpoints, this state is **not** automatically saved by standard checkpointing mechanisms. When training resumes from a model checkpoint that lacks data pipeline state, the data loader starts from the beginning of the dataset.^[experiment-tracking-and-observability-databricks-on-aws.md]

### Implications for Resumed Training

Because a model checkpoint does not capture data pipeline position, a resumed run cannot fast-forward to the exact sample where training stopped. This means that simply loading a model checkpoint and restarting the data pipeline from the beginning will re-process samples that were already seen, potentially causing data leakage in evaluation metrics or overfitting on early training data.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Strategies for Handling the Mismatch

Two approaches are commonly used to account for the gap between model checkpointing and data pipeline state:^[experiment-tracking-and-observability-databricks-on-aws.md]

### 1. Restart from an Epoch Boundary

Resume training from the next epoch boundary, accepting that some samples in the current epoch will be re-processed. This is the simplest approach and works well when the dataset is large enough that reprocessing a fractional epoch is negligible.

### 2. Track Processed Samples in Training State

Explicitly track the number of processed samples, shards, or batches in your own training state dictionary that is saved alongside the model checkpoint. On resume, use this information to skip already-consumed data. This approach requires custom logic in the training loop and data loader.

## Best Practices

- **Checkpoint frequently enough** to limit lost work, but not so often that I/O overhead dominates training time.^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Account for data pipeline position** in your resume logic to avoid unintended data leakage or skewed training statistics.^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Use asynchronous checkpointing** with `dcp.async_save()` and a `UCVolumeWriter` to save checkpoints in the background while training continues, reducing idle GPU time.^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Store shared training code** in `/Workspace/Shared` to enable multi-user collaboration on training pipelines.^[experiment-tracking-and-observability-databricks-on-aws.md]

## Related Concepts

- Model Checkpointing — Saving model and optimizer state for resumption
- Unity Catalog Volumes — Governance-aware storage for checkpoints
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) — API for saving and loading distributed checkpoints
- [Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — Logging metrics, parameters, and artifacts with MLflow
- Resilient Training — Handling interruptions in large-scale training
- Data Pipeline Design for Training — Structuring data ingestion to support resumable training

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
