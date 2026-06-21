---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bd674e482719907a4596d1c592582a826ef4a71c76491277c81684d4f51e07c0
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-with-ray-train-on-databricks
    - DTWRTOD
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Distributed training with Ray Train on Databricks
description: Distributed data-parallel fine-tuning using Ray Train's TorchTrainer across 8 H100 GPUs on a single node, with one worker per GPU.
tags:
  - distributed-training
  - Ray
  - databricks
timestamp: "2026-06-19T08:56:11.507Z"
---

# Distributed Training with Ray Train on Databricks

**Distributed training with Ray Train on Databricks** refers to the practice of using [Ray Train](/concepts/ray-train-resource-allocation.md), a distributed training library within the Ray ecosystem, to scale machine learning workloads across multiple GPUs on Databricks infrastructure. Ray Train provides a framework-agnostic API for distributed training, supporting popular deep learning frameworks through specialized trainers such as `TorchTrainer` for PyTorch workloads. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

On Databricks, distributed training with Ray Train is typically submitted through the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`), which provides a streamlined interface for launching distributed training jobs on GPU clusters. This approach enables practitioners to leverage data-parallel fine-tuning across multiple GPUs without manually managing worker orchestration. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Architecture

### Training Strategy

Ray Train on Databricks uses a distributed data-parallel (DDP) architecture, where each GPU worker holds a complete copy of the model and processes a different shard of the training data. Gradients are synchronized across workers after each training step to ensure consistent model updates. This approach is well-suited for models that fit within a single GPU's memory. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Compute Configuration

A common configuration uses a single node with 8 H100 GPU Support on Databricks|H100 GPUs, allocating one Ray Train worker per GPU. This provides efficient scaling within a node while avoiding the complexity of multi-node communication. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Workflow Components

A complete Ray Train workload on Databricks consists of three components submitted together using `air run -f <workload>.yaml`: ^[ai-runtime-cli-examples-databricks-on-aws.md]

1. **Workload YAML file** — Defines the job configuration, including compute resources, GPU count, and entry point
2. **Launcher script** — Sets up and executes the Ray Train training run, configuring `TorchTrainer` with the appropriate number of workers
3. **Training code** — Contains the model definition, dataset loading, training loop, and any logging logic

### Example Structure

```yaml
# train.yaml
name: ray-train-example
compute:
  gpu_count: 8
  gpu_type: h100
  node_count: 1
entry_point: launcher.py
```

```python
# launcher.py
import ray
from ray.train.torch import TorchTrainer

trainer = TorchTrainer(
    train_loop_per_worker=train_func,
    scaling_config={"num_workers": 8},
)
trainer.fit()
```

## Comparison with Other Distributed Training Approaches

| Approach | Architecture | Use Case |
|----------|-------------|----------|
| Ray Train with TorchTrainer | Distributed data parallel (DDP) | Single-node, multi-GPU fine-tuning for models fitting in GPU memory |
| [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) | Model sharding across GPUs | [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) that cannot fit on a single GPU |
| [DeepSpeed](/concepts/deepspeed.md) | Advanced memory optimization (ZeRO stages) | Very large models requiring aggressive memory optimization |
| Multi-node FSDP | Cross-node model sharding | Models requiring multiple nodes (e.g., 16+ GPUs) |

Ray Train with DDP is particularly well-suited for models that fit within a single GPU's memory, where data parallelism provides sufficient scaling without the complexity of model sharding. For models requiring memory efficiency beyond DDP, FSDP or DeepSpeed are more appropriate. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) — The core distributed training library
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — Command-line tool for submitting distributed training jobs
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) — Ray Train's integration for PyTorch
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The underlying parallelism strategy
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — An alternative for larger models
- [DeepSpeed](/concepts/deepspeed.md) — An alternative with advanced memory optimization
- H100 GPU Support on Databricks — GPU infrastructure for distributed training
- [Multi-node LLM Fine-tuning](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) — Cross-node distributed training with FSDP

## Best Practices

- **Use single-node configurations** when possible to avoid inter-node communication overhead and simplify debugging
- **Log training metrics to [MLflow](/concepts/mlflow.md)** for experiment tracking and model comparison
- **Save checkpoints to Unity Catalog volumes** for durability and accessibility across sessions
- **Benchmark GPU utilization** to ensure all workers are fully utilized and there are no bottlenecks in data loading

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
