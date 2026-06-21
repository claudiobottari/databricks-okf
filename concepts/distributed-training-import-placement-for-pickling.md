---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 755b1b772dcc7e8d800097f254955a3eab528ff6a91bb96c55ce847d715f487c
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-import-placement-for-pickling
    - DTIPFP
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Distributed Training Import Placement for Pickling
description: Best practice of placing all imports inside the training function to avoid pickling errors when distributing code to executors
tags:
  - pytorch
  - distributed-training
  - pickling
  - troubleshooting
timestamp: "2026-06-18T15:34:55.897Z"
---

# Distributed Training Import Placement for Pickling

**Distributed Training Import Placement for Pickling** refers to the practice of positioning Python import statements inside the training function (and any user-defined helper functions it calls) when using [TorchDistributor](/concepts/torchdistributor.md) for distributed PyTorch training. This placement prevents pickling errors that occur because import statements defined at the notebook or module level are not automatically distributed to all executor processes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## The Problem

When a PyTorch training script is launched via `TorchDistributor.run()`, the training function and its arguments are serialized (pickled) and shipped to each worker process. If library imports such as `import torch` or `import torch.distributed` are placed only at the top of the notebook cell or module, they reside in the driver’s namespace and are not included in the pickled closure. The executor then encounters `AttributeError` or `ModuleNotFoundError` because those names are missing. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## The Solution

### Move imports into the training function

Place all necessary imports **inside** the function that will be passed to `TorchDistributor.run()`. This ensures that when the function is unpickled on each worker, the imports are executed locally and the required modules are available. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
def train(learning_rate, use_gpu):
    import torch
    import torch.distributed as dist
    import torch.nn.parallel.DistributedDataParallel as DDP
    from torch.utils.data import DistributedSampler, DataLoader

    backend = "nccl" if use_gpu else "gloo"
    dist.init_process_group(backend)
    device = int(os.environ["LOCAL_RANK"]) if use_gpu else "cpu"
    model = DDP(createModel(), device_ids=[device])
    sampler = DistributedSampler(dataset)
    loader = DataLoader(dataset, sampler=sampler)
    output = train(model, loader, learning_rate)
    dist.cleanup()
    return output
```

### Duplicate imports inside helper functions

Any user-defined function that is called **from within** the training function must also contain its own import statements. This is necessary because Python’s closure captures references, not the imported names themselves; when the helper function is executed on a worker, it may not have access to the imports from the outer training function’s scope if they were not properly inlined. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
def train(learning_rate, use_gpu):
    import torch  # required here
    # ...
    def compute_loss(output, target):
        import torch.nn.functional as F  # required again inside helper
        return F.cross_entropy(output, target)
    loss = compute_loss(output, target)
```

> **Best Practice:** Include import statements both at the top of the training function called with `TorchDistributor.run()` **and** inside any other user-defined functions invoked within that training method. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## How This Fits into the Development Workflow

The standard workflow for converting single-node code to distributed training with TorchDistributor includes a dedicated step: “Move imports within training function.” After preparing single-node code and converting it to use `DistributedDataParallel`, you must relocate all imports into the training function to avoid pickling errors. The `device_id` is then determined from the environment variable `LOCAL_RANK`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The PySpark module that launches distributed PyTorch training.
- PyTorch Distributed Training – General distributed training with PyTorch, including DDP.
- Pickling in Python – Serialization mechanism used by TorchDistributor to ship functions to workers.
- [DistributedDataParallel](/concepts/distributed-data-parallel-ddp.md) – PyTorch’s model wrapper for data‑parallel training.
- LOCAL_RANK – Environment variable indicating the local GPU index for each process.

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
