---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c35b18f328520889379b2f0ca1a3f0d5b4201346951f340679e15d6da646cdd1
  pageDirectory: concepts
  sources:
    - adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-pytorch-training-with-horovod
    - DPTWH
    - Distributed training with Horovod
  citations:
    - file: adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md
title: Distributed PyTorch training with Horovod
description: Technique for scaling PyTorch model training across multiple nodes using Horovod, demonstrated via an MNIST example on Databricks.
tags:
  - pytorch
  - horovod
  - distributed-training
timestamp: "2026-06-19T21:57:31.639Z"
---

# Distributed PyTorch training with Horovod

**Distributed PyTorch training with Horovod** is a method for scaling deep learning training across multiple GPUs and nodes using the Horovod distributed training framework. Horovod provides a straightforward API for converting single-node PyTorch training code into distributed training code with minimal changes. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Overview

Horovod is a distributed deep learning framework that uses an all-reduce approach to synchronize gradients across workers. Unlike data parallel approaches that require a parameter server, Horovod uses Ring AllReduce for gradient aggregation, which scales efficiently across multiple GPUs and nodes. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

When adapting single-node PyTorch code for distributed training with Horovod, the recommended development workflow is to first train the model on a single node, and then adapt the code using Horovod for distributed execution. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Key Concepts

### Distributed Initialization

Horovod must be initialized in the training script. This is typically done early in the training loop:

```python
import horovod.torch as hvd

hvd.init()
```

### Data Parallelism

To distribute data across workers, use a distributed sampler with a DataLoader:

```python
train_dataset = ...  # your dataset
train_sampler = torch.utils.data.distributed.DistributedSampler(
    train_dataset,
    num_replicas=hvd.size(),
    rank=hvd.rank(),
)
train_loader = torch.utils.data.DataLoader(
    train_dataset,
    batch_size=batch_size,
    sampler=train_sampler,
)
```

### Gradient Synchronization

Horovod wraps the PyTorch optimizer to synchronize gradients across all workers after each backward pass:

```python
optimizer = optim.SGD(model.parameters(), lr=learning_rate)
optimizer = hvd.DistributedOptimizer(
    optimizer,
    named_parameters=model.named_parameters(),
    backward_passes_per_step=1,
)
```

### Broadcasting Initial Model State

To ensure all workers start with the same model parameters, broadcast the initial model state from rank 0:

```python
hvd.broadcast_parameters(model.state_dict(), root_rank=0)
hvd.broadcast_optimizer_state(optimizer, root_rank=0)
```

### Pin GPU to Local Rank

Each worker should use a specific GPU based on its local rank:

```python
torch.cuda.set_device(hvd.local_rank())
model.cuda()
```

### Saving Checkpoints

Only the worker with rank 0 should save checkpoints to avoid file conflicts:

```python
if hvd.rank() == 0:
    torch.save(model.state_dict(), checkpoint_path)
```

## Training Loop Adjustments

In the epoch loop, each epoch should use the sampler's `set_epoch` method to ensure proper shuffling across workers:

```python
for epoch in range(num_epochs):
    train_sampler.set_epoch(epoch)
    for batch_idx, (data, target) in enumerate(train_loader):
        # training step
        pass
```

## Databricks Integration

On Databricks, distributed PyTorch training with Horovod can be executed using [HorovodRunner](/concepts/horovodrunner.md), which provides a managed runtime for running Horovod jobs on Spark clusters. The development workflow typically consists of:

1. Train the model on a single node to validate the code
2. Adapt the code using Horovod primitives
3. Run the distributed training via HorovodRunner

## Best Practices

- **Use consistent learning rate scaling**: When using multiple workers, the batch size effectively increases. Learning rates may need to be adjusted proportionally (linear scaling rule). ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]
- **Make idempotent workers**: Each worker should be able to produce the same results regardless of rank, except for checkpointing operations. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]
- **Handle data ordering**: Use distributed samplers to ensure each worker processes a unique subset of the data. ^[adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — Databricks integration for running Horovod distributed training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Alternative PyTorch-native distributed training approach
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient distributed training for large models
- AllReduce — The underlying communication primitive used by Horovod
- [Multi-GPU Training](/concepts/multi-gpu-distributed-training-api.md) — Broader topic of scaling training across multiple GPUs

## Sources

- adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md

# Citations

1. [adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws.md](/references/adapt-single-node-pytorch-to-distributed-deep-learning-databricks-on-aws-7a436585.md)
