---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85819924a9cf644eb89464ee1dfd0eb3baf544e726d2c61334bceca40f8e9049
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-troubleshooting-import-pickling-errors
    - TTIPE
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: "TorchDistributor Troubleshooting: Import Pickling Errors"
description: Common error when library imports are not distributed to executors; resolved by placing all import statements inside the training function passed to TorchDistributor.run().
tags:
  - troubleshooting
  - pyspark
  - distributed-training
timestamp: "2026-06-18T12:09:23.614Z"
---

# TorchDistributor Troubleshooting: Import Pickling Errors

When using [TorchDistributor](/concepts/torchdistributor.md) in a notebook workflow, you may encounter a pickling error where objects cannot be found or serialized during distributed training. This page explains the cause and provides a solution.

## Cause

TorchDistributor launches distributed PyTorch training across Spark executors using `torch.distributed.run`. For the training function to execute correctly on every worker, the function and its dependencies must be serializable and available on all nodes. The most common cause of pickling errors in this context is that library import statements (such as `import torch`) are placed at the top of the notebook cell rather than inside the training function itself. When PySpark tries to serialize the training function, it cannot locate the imported modules on the remote executors, resulting in a `PicklingError` or `AttributeError`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Solution

To avoid pickling errors, move all necessary import statements *inside* the training function that you pass to `TorchDistributor.run()`. Include the imports at the top of the training function and also inside any other user-defined functions that are called within it. This ensures that each executor imports the required modules locally before executing the training code. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

The same principle applies when you need to determine the device ID for distributed data parallelism: use `int(os.environ["LOCAL_RANK"])` inside the training function. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Example

The following snippet shows the correct pattern — all imports are inside the `train` function:

```python
from pyspark.ml.torch.distributor import TorchDistributor

def train(learning_rate, use_gpu):
    import torch
    import torch.distributed as dist
    import torch.nn.parallel.DistributedDataParallel as DDP
    from torch.utils.data import DistributedSampler, DataLoader
    import os

    backend = "nccl" if use_gpu else "gloo"
    dist.init_process_group(backend)
    device = int(os.environ["LOCAL_RANK"]) if use_gpu else "cpu"
    model = DDP(createModel(), **kwargs)
    sampler = DistributedSampler(dataset)
    loader = DataLoader(dataset, sampler=sampler)
    output = train(model, loader, learning_rate)
    dist.cleanup()
    return output

distributor = TorchDistributor(num_processes=2, local_mode=False, use_gpu=True)
distributor.run(train, 1e-3, True)
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Best Practice

When developing distributed training code inside a notebook, adopt the habit of placing all `import` statements (including `import torch`, `import torch.nn`, etc.) inside the training function. Avoid importing them at the notebook's top-level scope, as those imports are not automatically distributed to Spark executors. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Topics

- [TorchDistributor](/concepts/torchdistributor.md) – The PySpark module for distributed PyTorch training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The PyTorch parallelism strategy used with TorchDistributor
- LOCAL_RANK – Environment variable that identifies the GPU device on each worker
- Pickling (serialization) – The serialization mechanism that can fail when imports are external
- PySpark – The underlying framework that distributes the training function
- [NCCL Errors with TorchDistributor](/concepts/torchdistributor.md) – Another common error related to GPU communication
- Gloo Errors with TorchDistributor – Connection refused errors on CPU instances

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
