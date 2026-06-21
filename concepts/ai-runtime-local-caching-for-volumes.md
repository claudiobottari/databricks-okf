---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83f76028b210453ea33c663e58fa3b029844f025d734453a30da332812c22552
  pageDirectory: concepts
  sources:
    - load-data-on-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-local-caching-for-volumes
    - ARLCFV
  citations:
    - file: load-data-on-ai-runtime-databricks-on-aws.md
title: AI Runtime Local Caching for Volumes
description: Mechanism where files from Unity Catalog volumes are copied to local storage on first access, avoiding repeated FUSE reads across epochs.
tags:
  - data-loading
  - caching
  - databricks
  - performance
timestamp: "2026-06-19T19:14:19.404Z"
---

---
title: AI Runtime Local Caching for Volumes
summary: A local caching mechanism provided by `UCVolumeDataset` that copies files from Unity Catalog volumes to a fast local cache on first access, enabling efficient multi-epoch training and automatic distributed partitioning.
sources:
  - load-data-on-ai-runtime-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T20:00:00.000Z"
tags:
  - ai-runtime
  - data-loading
  - volumes
  - caching
  - distributed-training
aliases:
  - local-caching-for-volumes
  - UCVolumeDataset-caching
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# AI Runtime Local Caching for Volumes

**AI Runtime Local Caching for Volumes** refers to the built‑in caching mechanism provided by `UCVolumeDataset` (from the `serverless_gpu.data` package) that copies files from Unity Catalog Volumes to a fast local cache on first access. This avoids repeated reads from remote storage during multi‑epoch training and automatically handles data partitioning across distributed workers. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Overview

When training machine learning models on AI Runtime, data is often stored in Unity Catalog volumes, which are remote (FUSE) mounts. Reading files directly from the FUSE mount on every epoch incurs network latency and can become a performance bottleneck. `UCVolumeDataset` addresses this by:

- **Local caching**: Copying each file from the volume to a local cache directory on first access and serving subsequent reads from the cache. This eliminates re‑reading the volume in later epochs. ^[load-data-on-ai-runtime-databricks-on-aws.md]
- **Automatic partitioning**: When `torch.distributed` is initialized, files are partitioned across GPUs (ranks) and further divided across `DataLoader` workers, so each `(rank, worker)` pair receives a non‑overlapping slice without requiring a `DistributedSampler`. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Using `UCVolumeDataset`

`UCVolumeDataset` is a PyTorch IterableDataset that yields the **local cached file path** for each file in the volume. It is designed for unstructured data such as images, audio, and text files. ^[load-data-on-ai-runtime-databricks-on-aws.md]

**Requirements:**

- [GPU environment](/concepts/serverless-gpu-environment.md) version 5 or above is required for both `UCVolumeDataset` and `serverless_gpu.data.DataLoader`. ^[load-data-on-ai-runtime-databricks-on-aws.md]

### Example: Basic usage

```python
from serverless_gpu.data import UCVolumeDataset

path_dataset = UCVolumeDataset("/Volumes/catalog/schema/my_volume/images")
```

`UCVolumeDataset` outputs raw local paths. To decode those paths into tensors, wrap it in a second `IterableDataset` that applies your parsing logic. This separation keeps I/O and parsing concerns separate. ^[load-data-on-ai-runtime-databricks-on-aws.md]

### Example: Decoding images

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

The wrapper receives already‑cached local paths, so the parsing step never touches the FUSE mount. Additional wrappers can be chained for augmentation, tokenization, or filtering. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Local Caching Details

- **First‑access copy**: On the first iteration over a file, `UCVolumeDataset` copies it from the FUSE volume mount to a local cache directory. Subsequent iterations read from the local copy. ^[load-data-on-ai-runtime-databricks-on-aws.md]
- **Lazy caching**: Only files that are actually accessed get cached, unlike a manual `shutil.copytree` which copies the entire directory upfront. This is more efficient when training touches only a subset of the data. ^[load-data-on-ai-runtime-databricks-on-aws.md]
- **Multi‑epoch efficiency**: Because files are served from local storage after the first epoch, training throughput does not degrade for repeated epochs. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Automatic Partitioning for Distributed Training

When `UCVolumeDataset` is constructed inside a [@distributed Decorator](/concepts/distributed-decorator.md) (which initializes `torch.distributed`), it reads rank information at iteration time and partitions files across ranks automatically. No `DistributedSampler` is needed for file‑based volume data. The partitioning also accounts for `DataLoader` workers: files are divided into `world_size × num_workers` slices, with each `(rank, worker)` receiving a unique slice. All ranks **must use the same `num_workers`** value to avoid file duplication or skips. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Performance Optimizations

Pair `UCVolumeDataset` with `serverless_gpu.data.DataLoader` for best I/O performance. This subclass of the PyTorch `DataLoader` is tuned for serverless GPU I/O:

- Default `num_workers=6` (PyTorch default: 0)
- Default `prefetch_factor=4` (PyTorch default: 2)
- Logs per‑batch fetch timing to the active [MLflow](/concepts/mlflow.md) run, helping identify data‑loading bottlenecks.

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

Increasing `num_workers` raises parallel reads; increasing `prefetch_factor` deepens each worker’s prefetch queue. All ranks must use the same `num_workers` value for correct partitioning. ^[load-data-on-ai-runtime-databricks-on-aws.md]

Larger batch sizes also help by amortizing per‑batch file‑fetch overhead over more samples. If GPU memory is limited, combine a larger batch size with gradient accumulation. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Comparison with Manual Copy

Using `UCVolumeDataset` is preferred over a manual `shutil.copytree` because:

- **Lazy copying**: Only accessed files are copied, not the entire directory.
- **Automatic partitioning**: No manual file splitting logic required.
- **Integrated with distributed training**: Works seamlessly inside `@distributed` without extra setup. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Related Concepts

- Unity Catalog Volumes — The storage abstraction for unstructured data on Databricks.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute environment where `UCVolumeDataset` runs.
- [@distributed Decorator](/concepts/distributed-decorator.md) — The distributed training API for multi‑GPU workloads.
- Torch IterableDataset — The base class for streaming datasets.
- serverless_gpu.data.DataLoader — The optimized data loader for serverless GPU I/O.

## Sources

- load-data-on-ai-runtime-databricks-on-aws.md

# Citations

1. [load-data-on-ai-runtime-databricks-on-aws.md](/references/load-data-on-ai-runtime-databricks-on-aws-0b666631.md)
