---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae805b0ca778e7189b4d158aebc06f5c740b4094a436f17e7d1189a75c63af56
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-with-ray-train
    - DTWRT
    - Distributed Training with Mosaic Streaming
    - Distributed Training with PyTorch
    - Distributed training with PyTorch
    - distributed-training-with-ray-train-on-databricks
    - DTWRTOD
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Distributed training with Ray Train
description: A distributed data-parallel fine-tuning pattern using Ray Train's TorchTrainer across 8 H100 GPUs on a single node, with one worker per GPU.
tags:
  - distributed-training
  - ray
  - fine-tuning
timestamp: "2026-06-18T10:43:15.296Z"
---

# Distributed training with Ray Train

**Distributed training with Ray Train** is a workload pattern for fine-tuning machine learning models using Ray Train's `TorchTrainer` across multiple GPUs on a single node, with one worker per GPU. This approach leverages Ray's distributed computing framework to scale training workloads on AI Runtime's serverless GPU compute platform.

## Overview

Ray Train is a distributed training framework that provides a scalable API for data-parallel training. When used with the AI Runtime CLI, Ray Train workloads are defined in a YAML configuration file and submitted using the `air run` command. Each worker in the distributed setup operates on a separate GPU, processing distinct batches of data in parallel while synchronizing model gradients. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Example: Distributed data-parallel fine-tuning

The following example demonstrates distributed data-parallel fine-tuning with Ray Train's `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU.

#### Workload YAML (`train.yaml`)

```yaml
experiment_name: ray-train-distributed
environment:
  version: '4'
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100_80GB
code_source:
  type: snapshot
  snapshot:
    root_path: .
command: python $CODE_SOURCE_PATH/train.py
```

^[ai-runtime-cli-examples-databricks-on-aws.md]

#### Training script (`train.py`)

```python
import ray
from ray import train
from ray.train import ScalingConfig
from ray.train.torch import TorchTrainer

# Initialize Ray
ray.init(address="auto", ignore_reinit_error=True)

# Define your model, data loading, and training logic
def train_func():
    # Training function that runs on each worker
    # Each worker has access to one GPU
    import torch
    import torch.nn as nn
    from torch.utils.data import DataLoader
    from torch.optim import AdamW
    
    # Define a simple model
    model = nn.Linear(784, 10)
    model = train.torch.prepare_model(model)
    
    # Create dummy data
    dataset = torch.randn(1000, 784)
    labels = torch.randint(0, 10, (1000,))
    loader = DataLoader(list(zip(dataset, labels)), batch_size=32)
    
    # Training loop
    optimizer = AdamW(model.parameters(), lr=1e-3)
    for epoch in range(5):
        for batch, (data, target) in enumerate(loader):
            optimizer.zero_grad()
            output = model(data)
            loss = nn.functional.cross_entropy(output, target)
            loss.backward()
            optimizer.step()
        
        # Report metrics to Ray Train
        train.report({"epoch": epoch, "loss": loss.item()})

# Configure distributed training
scaling_config = ScalingConfig(
    num_workers=8,          # One worker per GPU
    use_gpu=True,
    resources_per_worker={"GPU": 1}
)

# Create and run the trainer
trainer = TorchTrainer(
    train_func,
    scaling_config=scaling_config
)
results = trainer.fit()

# Access results
print(f"Best loss: {results.metrics['loss']}")
```

^[ai-runtime-cli-examples-databricks-on-aws.md]

## Key concepts

### Scaling configuration

The `ScalingConfig` in Ray Train defines the distributed execution plan:

- `num_workers`: Sets the number of parallel workers (one per GPU)
- `use_gpu`: Enables GPU-accelerated training
- `resources_per_worker`: Specifies resource allocation per worker (e.g., `{"GPU": 1}`)

### TorchTrainer

`TorchTrainer` is Ray Train's built-in trainer for PyTorch models. It handles:

- Distributing the training function across workers
- Synchronizing gradients using data-parallel techniques
- Reporting metrics back to the driver

### Worker-per-GPU pattern

The example uses one worker per GPU, which is the standard pattern for data-parallel training. Each worker processes a different subset of the training data, and gradient synchronization ensures model consistency across workers.

## Related concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) — The distributed training framework
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The `air` CLI for submitting workloads
- AI Runtime CLI quickstart — Getting started with the CLI
- Workload YAML reference — Complete YAML configuration documentation
- [MLflow](/concepts/mlflow.md) — Experiment tracking integration
- Multi-GPU workload — In-notebook Python API alternative
- [Multi-node LLM fine-tuning with FSDP](/concepts/multi-node-llm-fine-tuning-with-fsdp.md) — Another distributed training example
- [Serverless environment versions](/concepts/serverless-environment-versioning.md) — Available environment versions
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — Hosted model endpoints
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance for AI assets

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
