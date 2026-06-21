---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e6745148e76928e7774e19366c66757d3d3fbb987e885a3de72873ae0c7ce34
  pageDirectory: concepts
  sources:
    - experiment-tracking-and-observability-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-pipeline-checkpointing
    - DPC
  citations:
    - file: experiment-tracking-and-observability-databricks-on-aws.md
title: Data Pipeline Checkpointing
description: Limitations of model checkpointing for data pipeline state and strategies for resuming training from the correct position in the dataset.
tags:
  - distributed-training
  - checkpointing
  - data-pipeline
  - machine-learning
timestamp: "2026-06-18T12:15:07.029Z"
---

# Data Pipeline Checkpointing

**Data Pipeline Checkpointing** refers to the practice of saving the state of a data processing pipeline — such as the current position within a dataset — to enable resumption from that point after an interruption. While model checkpointing captures model weights and optimizer state, data pipeline checkpointing tracks how far the pipeline has progressed through the input data. This distinction is critical for training workloads that must recover from failures without reprocessing the entire dataset. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## The Problem: Model Checkpoints Do Not Capture Data Position

A standard model checkpoint saves only the model parameters and optimizer state. It does **not** record the position of the data pipeline within the dataset — for example, which batch, shard, or sample was being processed when the checkpoint was taken. As a result, a resumed run cannot fast-forward to the exact sample where training stopped. Instead, it must either restart from the beginning of the dataset or rely on external tracking mechanisms. ^[experiment-tracking-and-observability-databricks-on-aws.md]

This limitation is especially relevant for distributed training on [AI Runtime](/concepts/ai-runtime.md), where interruptions (preemption, node failures) can occur mid-epoch. Without data pipeline checkpointing, the training loop may reprocess data that was already consumed, wasting compute time and potentially double-counting samples in metrics. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Approaches for Resume After Interruption

Source material suggests two strategies for handling the absence of built-in data pipeline position tracking: ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Restart from an Epoch Boundary

Configure the training loop to always restart at the beginning of the next epoch after a failure. This approach is simple and requires no custom state tracking. The trade-off is that any partially completed epoch is fully reprocessed, which can be acceptable if checkpoints are taken frequently enough (e.g., every 30–60 minutes). ^[experiment-tracking-and-observability-databricks-on-aws.md]

### Track Processed Samples or Shards Manually

Maintain a counter or shard index in the training state — stored alongside the model checkpoint — so that on resume the pipeline can skip previously processed data. This requires explicit implementation by the developer:

```python
# Pseudocode: store data position in the training state dict
state_dict = {
    "model": model.state_dict(),
    "optimizer": optimizer.state_dict(),
    "current_epoch": epoch,
    "batch_index": batch_idx,        # track position within epoch
    "shard_id": shard_id,            # for sharded datasets
}
```

On resume, the training loop reads these counters and advances the data loader past already-consumed samples. ^[experiment-tracking-and-observability-databricks-on-aws.md]

## Comparison with Model Checkpointing

| Aspect | Model Checkpointing | Data Pipeline Checkpointing |
|--------|---------------------|-----------------------------|
| **What is saved** | Model parameters, optimizer state | Position in dataset (epoch, batch, shard) |
| **Purpose** | Resume training from a specific weight state | Avoid reprocessing consumed data |
| **Built-in support** | Yes (MLflow, Torch DCP, etc.) | Not automatic; must be implemented by user |
| **Storage** | Usually companion to model checkpoint | Typically stored alongside the model checkpoint |

## Best Practices

- **Checkpoint frequently enough** to limit lost work in case of interruption — aim for one full checkpoint (model + data position) every 30–60 minutes, tuning based on step time and checkpoint size. ^[experiment-tracking-and-observability-databricks-on-aws.md]
- **Store data position in the same checkpoint file** as model and optimizer state to keep recovery atomic.
- **Test resume logic** by deliberately interrupting a training run mid-epoch and verifying that the DataLoader skips previously processed samples correctly.
- **Use Unity Catalog Volumes** for checkpoint storage in [AI Runtime](/concepts/ai-runtime.md); volumes provide governance and fast I/O when used with `UCVolumeWriter` and `UCVolumeReader`.

## Related Concepts

- Model Checkpointing — Saving model weights and optimizer state for recovery or fine-tuning
- [Torch Distributed Checkpoint](/concepts/pytorch-distributed-checkpoint-dcp.md) (DCP) — PyTorch API for saving and loading distributed checkpoints
- Unity Catalog Volumes — Governance-backed storage for checkpoints and training artifacts
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — Tracking training runs, parameters, and artifacts
- [AI Runtime](/concepts/ai-runtime.md) — Databricks serverless GPU runtime for training workloads
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Multi-GPU and multi-node training patterns
- Training Resume Strategies — Methods for recovering model state and data position after interruption

## Sources

- experiment-tracking-and-observability-databricks-on-aws.md

# Citations

1. [experiment-tracking-and-observability-databricks-on-aws.md](/references/experiment-tracking-and-observability-databricks-on-aws-4c27cc68.md)
