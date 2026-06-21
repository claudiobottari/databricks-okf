---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 893e658569dc0a6ecd1812a492bb9e6d142f427cec25114ff9a77845ea5da524
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pickling-errors-in-distributed-pytorch
    - PEIDP
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Pickling Errors in Distributed PyTorch
description: A common distributed training issue where library imports are not distributed to executors, solved by placing import statements inside the training function.
tags:
  - troubleshooting
  - pytorch
  - distributed-training
timestamp: "2026-06-19T10:19:50.623Z"
---

# Pickling Errors in Distributed PyTorch

**Pickling Errors in Distributed PyTorch** are a common failure mode when running distributed training on PyTorch models across Spark clusters. These errors occur when serialization (pickling) fails for Python objects that must be transferred between the driver and executor processes in a distributed environment. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Causes

Pickling errors typically arise because library imports are not properly distributed to all worker nodes. When using [TorchDistributor](/concepts/torchdistributor.md), the training function and any user-defined functions it calls are serialized and shipped to executors. If a function references modules or objects that were imported outside the function's scope, those dependencies may not be available on the remote workers, causing the pickling process to fail. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

The most common scenario is when `import` statements (such as `import torch`) are placed at the top of a notebook cell but not inside the training function. The driver can resolve these imports, but the executors — which receive only the serialized function — cannot. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Symptoms

When pickling errors occur, the system raises an exception indicating that an object cannot be found or pickled. The error message typically references missing modules or attributes that are not recognized by the remote workers. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Prevention

To avoid pickling errors in distributed PyTorch workflows, follow these practices:

### Move imports into the training function

Include all necessary import statements (for example, `import torch`) inside the training function that is called with `TorchDistributor(...).run(<func>)`. This ensures that every executor has access to the required modules when the function executes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

Python

```python
def train(learning_rate, use_gpu):
    import torch
    import torch.distributed as dist
    import torch.nn.parallel.DistributedDataParallel as DDP
    from torch.utils.data import DistributedSampler, DataLoader
    # ... rest of training code ...
```

### Apply the same rule to all user-defined functions

Any other user-defined functions called within the training method must also include their import statements inside the function body. This prevents pickling failures when nested function calls are serialized. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Avoid relying on global or notebook-scoped imports

Do not assume that imports defined at the notebook level will be available to the training function. The notebook scope exists only on the driver node; executors cannot access it. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Relationship to TorchDistributor

[TorchDistributor](/concepts/torchdistributor.md) works by initializing the environment and communication channels between workers, then using the CLI command `torch.distributed.run` to launch distributed training across nodes. During this process, it serializes the training function and distributes it to worker processes. Pickling errors specifically occur during this serialization/distribution step, before training begins. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — The PySpark module for distributed PyTorch training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — PyTorch's standard distributed training paradigm
- PyTorch serialization — The broader topic of saving and loading PyTorch objects
- Spark executor environment — Understanding how dependencies are distributed in Spark
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) — General best practices for distributed ML workflows

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
