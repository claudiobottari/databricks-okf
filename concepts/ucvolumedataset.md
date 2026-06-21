---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 675b6956018e0acf92d110353455813aa1941bb4b232397e804f23b8451723d5
  pageDirectory: concepts
  sources:
    - load-data-on-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ucvolumedataset
    - Volumes
    - volumes
  citations:
    - file: load-data-on-ai-runtime-databricks-on-aws.md
title: UCVolumeDataset
description: A PyTorch IterableDataset that streams unstructured data (images, audio, text) from Unity Catalog volumes with automatic local caching and distributed partitioning.
tags:
  - data-loading
  - pytorch
  - databricks
  - distributed-training
timestamp: "2026-06-19T19:13:30.964Z"
---

# UCVolumeDataset

**UCVolumeDataset** is a PyTorch [`IterableDataset`](https://pytorch.org/docs/stable/data.html#iterable-style-datasets) provided by the `serverless_gpu.data` package. It is designed to load unstructured data (images, audio, text files) stored in [Unity Catalog](/concepts/unity-catalog.md) volumes directly into a distributed training workflow without manual data management. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Overview

`UCVolumeDataset` copies each file from the Unity Catalog volume’s FUSE mount to a fast local cache on first access and yields the cached local file path. It handles performance and distribution concerns that would otherwise require manual implementation: ^[load-data-on-ai-runtime-databricks-on-aws.md]

- **Local caching** – Files are copied to a local cache directory on first read and served from the cache afterward, avoiding repeated network reads during multi-epoch training.
- **Automatic partitioning** – When `torch.distributed` is initialized, files are partitioned across ranks and further divided across `DataLoader` workers. Each `(rank, worker)` pair receives a non-overlapping slice with no extra setup.

No explicit `DistributedSampler` is needed because `UCVolumeDataset` reads rank information at iteration time and partitions files automatically. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Requirements

- GPU environment version 5 or above (see [Serverless GPU environment releases](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu)). ^[load-data-on-ai-runtime-databricks-on-aws.md]
- Data must reside in a Unity Catalog volume.
- The `serverless_gpu.data` module must be imported.

## Basic usage

`UCVolumeDataset` yields raw local file paths. To decode those paths into tensors, wrap it in a second `IterableDataset` that consumes the path stream and applies parsing logic. This separation keeps I/O and parsing concerns independent. ^[load-data-on-ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu.data import UCVolumeDataset
from torch.utils.data import IterableDataset
from PIL import Image
import torchvision.transforms.functional as TF

class ImageDataset(IterableDataset):
    """Decodes each cached file path from UCVolumeDataset into a tensor."""
    def __init__(self, path_dataset: UCVolumeDataset):
        self._path_dataset = path_dataset

    def __iter__(self):
        for local_path in self._path_dataset:
            image = Image.open(local_path).convert("RGB")
            yield TF.to_tensor(image)

path_dataset = UCVolumeDataset("/Volumes/catalog/schema/my_volume/images")
dataset = ImageDataset(path_dataset)
```

The wrapper receives already-cached local paths, so the parsing step never touches the FUSE mount. Additional wrappers can be chained for augmentation, tokenization, or filtering. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Performance with `DataLoader`

For optimal performance, pair `UCVolumeDataset` with serverless_gpu.data.DataLoader rather than the stock PyTorch `DataLoader`. The `serverless_gpu` version is tuned for serverless GPU I/O: it defaults to `num_workers=6` and `prefetch_factor=4` (compared to PyTorch’s defaults of 0 and 2), so files are fetched and cached concurrently while the GPU computes. It also logs per-batch fetch timing to the active [MLflow](/concepts/mlflow.md) run, which helps identify data-loading bottlenecks. ^[load-data-on-ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu.data import DataLoader

loader = DataLoader(
    dataset,
    batch_size=32,
    pin_memory=True,
    # num_workers=6, by default
    # prefetch_factor=4, by default
)
```

All ranks must use the same `num_workers` value because `UCVolumeDataset` partitions files using a global stride across `world_size × num_workers` slots. Mismatched values cause files to be duplicated or skipped. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Usage with `@distributed`

When using the [@distributed Decorator](/concepts/distributed-decorator.md) for multi-GPU training, construct the `UCVolumeDataset` inside the decorated function to avoid pickle serialization errors for large datasets. When constructed inside the decorator, the dataset reads `torch.distributed` rank information at iteration time and partitions files automatically. ^[load-data-on-ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_train():
    path_dataset = UCVolumeDataset("/Volumes/catalog/schema/my_volume/images")
    # ... use path_dataset ...
```

## Related concepts

- serverless_gpu.data.DataLoader – Optimized DataLoader subclass for serverless GPU environments.
- [@distributed Decorator](/concepts/distributed-decorator.md) – Launches functions across multiple GPUs.
- Unity Catalog volumes – Storage location for unstructured data.
- IterableDataset – PyTorch base class for streaming datasets.
- [Data loading on AI Runtime](/concepts/databricks-ai-runtime.md) – General guide for loading data in AI Runtime contexts.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The compute infrastructure that hosts these datasets.

## Sources

- load-data-on-ai-runtime-databricks-on-aws.md

# Citations

1. [load-data-on-ai-runtime-databricks-on-aws.md](/references/load-data-on-ai-runtime-databricks-on-aws-0b666631.md)
