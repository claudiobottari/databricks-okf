---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 807a4e2f21d0d90d0dc253635b8426205d537c3523aeb57c9714934da881b829
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-import-scoping-for-pickling
    - TISFP
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: TorchDistributor Import Scoping for Pickling
description: Pattern of placing import statements inside the training function to avoid pickling errors during distributed PyTorch training with TorchDistributor
tags:
  - best-practice
  - pytorch
  - pickling
timestamp: "2026-06-19T18:38:41.923Z"
---

# TorchDistributor Import Scoping for Pickling

**TorchDistributor Import Scoping for Pickling** refers to the practice of placing Python import statements (e.g., `import torch`) inside the training function that is passed to `TorchDistributor.run()`, rather than at the top of the notebook or module. This scoping pattern is necessary to avoid pickling errors when TorchDistributor serializes the training function and distributes it to worker executors across a Spark cluster.

## Background

TorchDistributor is an open‑source module in PySpark that enables distributed training of PyTorch models on Spark clusters. Under the hood, it initializes communication channels between workers and uses the CLI command `torch.distributed.run` to launch distributed training across nodes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

When a training function is submitted to `TorchDistributor.run()`, PySpark must serialise (pickle) the function and send it to the executors. If the function references libraries that are not available on the executors—or if those libraries were only imported at module level in the driver—the pickled function may be missing needed objects, causing a `PicklingError` or a runtime failure. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## The scoping solution

To prevent pickling errors, the recommended development workflow for notebooks is to **move all necessary imports inside the training function**. This ensures that each executor imports the libraries locally when the function is executed, rather than relying on the driver’s module‑level imports being serialised. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

Concretely, the tutorial states:

> Add the necessary imports, such as `import torch`, within the training function. Doing so allows you to avoid common pickling errors. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Implementation guidelines

1. **Place all imports at the top of the training function** — every library used inside the function should be imported again, even if the same import already exists at the top of the notebook.
2. **Include imports in all nested functions** — if the training function calls other user‑defined functions, those functions must also contain their own import statements. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
3. **Assign the device from the environment** — inside the training function, obtain the local rank via `int(os.environ["LOCAL_RANK"])` to set the correct GPU device. This does not directly relate to pickling but is part of the standard preparation for distributed training. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Example snippet

```python
from pyspark.ml.torch.distributor import TorchDistributor

def train(learning_rate, use_gpu):
    import torch
    import torch.distributed as dist
    import torch.nn.parallel.DistributedDataParallel as DDP
    from torch.utils.data import DistributedSampler, DataLoader

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

In this example, `import torch`, `import torch.distributed`, etc. are placed inside `train()`. This pattern applies to any library that the function uses. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Troubleshooting: missing objects when pickling

A common error in the notebook workflow is that objects cannot be found or pickled when running distributed training. The root cause is that import statements are not distributed to other executors. The fix is to repeat all relevant imports inside the training function and inside any user‑defined functions that the training method calls. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related concepts

- [TorchDistributor](/concepts/torchdistributor.md) — the PySpark module that launches distributed PyTorch training.
- Distributed training with PyTorch — general patterns for multi‑GPU and multi‑node training.
- Pickling in PySpark — the serialisation mechanism used to transfer functions to executors.
- [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — the underlying parallelisation strategy often used with TorchDistributor.
- LOCAL_RANK environment variable — used inside the training function to determine the GPU device index.

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
