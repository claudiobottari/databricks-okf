---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b23c2419f7988275fee4eb1b8ccbc2ea25896195d0db1c24a860ca4b2e575f5f
  pageDirectory: concepts
  sources:
    - pytorch-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-distributed-training-error-troubleshooting
    - PDTET
  citations:
    - file: pytorch-databricks-on-aws.md
title: PyTorch Distributed Training Error Troubleshooting
description: Common errors encountered with PyTorch DataParallel and DistributedDataParallel on Databricks and their solutions
tags:
  - troubleshooting
  - distributed-training
  - pytorch
  - databricks
timestamp: "2026-06-19T20:00:34.692Z"
---

# PyTorch Distributed Training Error Troubleshooting

**PyTorch Distributed Training Error Troubleshooting** covers common error messages and resolutions encountered when using `torch.nn.DataParallel` or `torch.nn.parallel.DistributedDataParallel` on Databricks. Many of these errors can be avoided by using [TorchDistributor](/concepts/torchdistributor.md), which is available on Databricks Runtime ML 13.0 and above. When `TorchDistributor` is not a viable option, the specific workarounds below apply. ^[pytorch-databricks-on-aws.md]

## Use TorchDistributor (Recommended)

`TorchDistributor` from PySpark simplifies distributed PyTorch training and avoids many of the pitfalls described below. The following example runs a training function across two processes in local mode:

```python
from pyspark.ml.torch.distributor import TorchDistributor

def train_fn(learning_rate):
    # ...

distributor = TorchDistributor(num_processes=2, local_mode=True)
distributor.run(train_fn, 1e-3)
```

^[pytorch-databricks-on-aws.md]

---

## Process 0 Terminated with Exit Code 1

**Error message:**  
`process 0 terminated with exit code 1`

This error often occurs when running notebooks on Databricks or locally. The root cause is the use of `torch.multiprocessing.spawn` with default settings.

**Solution:** Use `torch.multiprocessing.start_processes` with `start_method="fork"` instead of `torch.multiprocessing.spawn`. For example:

```python
import torch

def train_fn(rank, learning_rate):
    # required setup, e.g. setup(rank)
    # ...

num_processes = 2
torch.multiprocessing.start_processes(
    train_fn, args=(1e-3,), nprocs=num_processes, start_method="fork"
)
```

**Important caveat:** `start_method="fork"` is **not CUDA‑compatible**. Calling any `.cuda()` commands after initializing CUDA will cause failures. Add a guard before calling `start_processes`:

```python
if torch.cuda.is_initialized():
    raise Exception("CUDA was initialized; distributed training will fail.")
```

^[pytorch-databricks-on-aws.md]

---

## Server Socket Failed to Bind to Port

**Error message:**  
`The server socket has failed to bind to [::]:{PORT NUMBER} (errno: 98 - Address already in use).`

This error typically appears when a distributed training run is interrupted (e.g., a notebook cell is stopped) and then restarted without releasing the previous port binding.

**Solution:**

1. **Restart the cluster.** This releases all stale port bindings.
2. If restarting does not resolve the issue, check for errors in the training function code that may prevent clean shutdown of worker processes.

Because `start_method="fork"` is incompatible with CUDA, and this error scenario often involves CUDA operations, ensure that the CUDA‑initialization guard (shown above) is in place.

^[pytorch-databricks-on-aws.md]

---

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – Preferred wrapper for distributed PyTorch on Databricks.
- PyTorch DataParallel – One of the parallelism classes that can trigger these errors.
- [DistributedDataParallel](/concepts/distributed-data-parallel-ddp.md) – Another class that may encounter the same issues.
- [MLflow](/concepts/mlflow.md) – Integration for tracking and debugging PyTorch training runs.
- [TensorBoard](/concepts/tensorboard-on-databricks.md) – Monitoring tool for PyTorch models.

## Sources

- pytorch-databricks-on-aws.md

# Citations

1. [pytorch-databricks-on-aws.md](/references/pytorch-databricks-on-aws-b092c491.md)
