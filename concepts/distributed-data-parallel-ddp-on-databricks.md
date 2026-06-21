---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2901bb343664bccecf9aa4fb7a70b58fa75b7ff36752f2b8a3bdad2fe850a271
  pageDirectory: concepts
  sources:
    - multi-gpu-workload-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-data-parallel-ddp-on-databricks
    - DDP(OD
  citations:
    - file: multi-gpu-workload-databricks-on-aws.md
title: Distributed Data Parallel (DDP) on Databricks
description: PyTorch's standard multi-GPU data parallelism integrated with the serverless_gpu @distributed API for distributed training.
tags:
  - pytorch
  - distributed-training
  - databricks
  - parallelism
timestamp: "2026-06-19T19:47:45.703Z"
---

# Distributed Data Parallel (DDP) on Databricks

**Distributed Data Parallel (DDP)** is a standard multi‑GPU data parallelism strategy available on Databricks through the `serverless_gpu` Python API. It replicates the model across multiple GPUs, splits the batch across replicas, and synchronizes gradients after each backward pass. DDP is one of the supported distributed training frameworks that can be launched with the `@distributed` decorator. ^[multi-gpu-workload-databricks-on-aws.md]

## Supported Frameworks

The `@distributed` API integrates with several major distributed training libraries, including:

- **PyTorch Distributed Data Parallel (DDP)** — standard multi‑GPU data parallelism.
- **Fully Sharded Data Parallel (FSDP)** — memory‑efficient training for large models.
- **DeepSpeed** — Microsoft's optimization library for large model training.

^[multi-gpu-workload-databricks-on-aws.md]

## Using DDP with the `serverless_gpu` API

The `serverless_gpu` API is preinstalled on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) sessions. To run DDP, wrap your training logic in a function decorated with `@distributed` and specify the number of GPUs and GPU type. The `gpu_type` parameter must match the accelerator your notebook is connected to; mismatches cause the workload to fail. ^[multi-gpu-workload-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_train(num_epochs: int, batch_size: int) -> None:
    import torch
    import torch.distributed as dist
    import torch.nn as nn
    from torch.nn.parallel import DistributedDataParallel as DDP

    # 1. Set up multi-GPU environment
    torch.cuda.set_device(int(os.environ["LOCAL_RANK"]))
    dist.init_process_group("nccl")

    # 2. Create model and wrap with DDP
    device = torch.device(f"cuda:{int(os.environ['LOCAL_RANK'])}")
    model = SimpleMLP().to(device)
    model = DDP(model, device_ids=[device])

    # 3. Load data with DistributedSampler
    from torch.utils.data import DataLoader, DistributedSampler, TensorDataset
    dataset = TensorDataset(x, y)
    sampler = DistributedSampler(dataset)
    dataloader = DataLoader(dataset, sampler=sampler, batch_size=batch_size)

    # 4. Training loop
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_fn = nn.MSELoss()
    for epoch in range(num_epochs):
        sampler.set_epoch(epoch)
        model.train()
        for xb, yb in dataloader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            loss = loss_fn(model(xb), yb)
            loss.backward()
            optimizer.step()

    # 5. Cleanup
    dist.destroy_process_group()
```

Call the distributed function with `run_train.distributed(num_epochs=3, batch_size=1)`. ^[multi-gpu-workload-databricks-on-aws.md]

## Best Practices

- **Place data loading inside the decorated function.** The dataset size may exceed pickle limits, so generate or load data after the `@distributed` decorator. ^[multi-gpu-workload-databricks-on-aws.md]
- For file‑based data stored in Unity Catalog Volumes, use `UCVolumeDataset` from `serverless_gpu.data`. It streams files with local caching and partitions them across ranks. Use `UCVolumeWriter` and `UCVolumeReader` for checkpointing. ^[multi-gpu-workload-databricks-on-aws.md]
- Set up the distributed environment (`dist.init_process_group("nccl")`) and clean up (`dist.destroy_process_group()`) inside the function. ^[multi-gpu-workload-databricks-on-aws.md]

## Comparison with TorchDistributor

The `serverless_gpu` API is the recommended approach for new deep learning workloads on Databricks. [TorchDistributor](/concepts/torchdistributor.md) remains available for workloads tightly coupled with Spark clusters. ^[multi-gpu-workload-databricks-on-aws.md]

## Distributed Execution Details

When using `@distributed`:

- The function is serialized and distributed across the specified number of GPUs.
- Each GPU runs a copy of the function with the same parameters.
- The environment is synchronized across all GPUs.
- Results are collected and returned from all GPUs.

^[multi-gpu-workload-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory‑efficient alternative for very large models.
- [DeepSpeed](/concepts/deepspeed.md) — Optimization library that offers additional memory‑saving strategies.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The infrastructure that provisions H100 GPUs on demand.
- [PyTorch Distributed Data Parallel](/concepts/distributed-data-parallel-ddp.md) — The underlying PyTorch library.
- [TorchDistributor](/concepts/torchdistributor.md) — Alternative Spark‑based approach for distributed PyTorch.
- [MLflow](/concepts/mlflow.md) — For tracking metrics and runs during training.
- Unity Catalog Volumes — Recommended storage for large datasets and checkpoints.

## Sources

- multi-gpu-workload-databricks-on-aws.md

# Citations

1. [multi-gpu-workload-databricks-on-aws.md](/references/multi-gpu-workload-databricks-on-aws-c6af01f5.md)
