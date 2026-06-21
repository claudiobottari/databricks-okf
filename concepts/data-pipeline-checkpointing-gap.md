---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf5fb895ac97130623624f933669b48f4278880c9e04f3c79b2e3403da65e82d
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-pipeline-checkpointing-gap
    - DPCG
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Data Pipeline Checkpointing Gap
description: Model checkpoints capture model and optimizer state but not the data pipeline position, so resumed runs cannot fast-forward to the exact sample where training stopped.
tags:
  - checkpointing
  - data-pipeline
  - training
timestamp: "2026-06-19T18:45:07.507Z"
---

# Data Pipeline Checkpointing Gap

**Data Pipeline Checkpointing Gap** refers to the mismatch between model state and data pipeline state during distributed training checkpointing. A model checkpoint captures the model parameters and optimizer state, but **not** the position of the data pipeline within the dataset. When training resumes from a checkpoint, it cannot fast-forward to the exact sample or batch where it previously stopped, leading to redundant data processing or lost progress. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Overview

During distributed training, checkpoints are saved periodically to recover from interruptions. Standard checkpointing frameworks — such as [Torch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md) — save the model and optimizer state, but they do not automatically persist the state of the data loader or the dataset iterator. This means that on resume, the training loop starts from the beginning of the dataset or from a pre-determined epoch boundary, reprocessing data that was already consumed before the interruption. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Implications

The gap has two practical consequences:

- **Reprocessing of data**: Samples that were already used in training are fed again, which can skew learning if the model expects exactly one pass per sample (e.g., in some curriculum learning setups).
- **Inefficiency**: Resume may need to recompute gradients for repeated batches, slowing down overall training throughput.

## Mitigation Strategies

Because the pipeline state is not included in the checkpoint, training loops must account for the gap manually. The source recommends two approaches: ^[experiment-tracking-and-observability-databricks-on-aws.md]

1. **Restart from an epoch boundary** – Accept that the run will re-process the entire current epoch. This is the simplest approach and works well when epochs are short or when data shuffling is random.
2. **Track processed samples or shards in training state** – Manually record how many samples or shards have been consumed (e.g., in a counter stored in the checkpoint’s state dict). On resume, skip those samples or shards before continuing training.

The second approach is more precise but requires custom logic in the data loading pipeline.

## Related Concepts

- Model Checkpointing – Saving and loading model parameters and optimizer state.
- Data Pipeline – The sequence of data loading, preprocessing, and batching.
- Training Resumption – Recovering training after an interruption.
- [Torch Distributed Checkpoint (DCP)](/concepts/pytorch-distributed-checkpoint-dcp.md) – The API used for distributed checkpoint save/load.
- Checkpoint Frequency – Tuning how often checkpoints are saved to balance I/O overhead and fault tolerance.

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
