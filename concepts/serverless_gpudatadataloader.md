---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 255dcd814a44cedcec38fa12f14786728a4168a284354279f7ba92d1328577f9
  pageDirectory: concepts
  sources:
    - load-data-on-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless_gpudatadataloader
    - serverless_gpu.data.DataLoader
    - Serverless GPU Data Loading
  citations:
    - file: load-data-on-ai-runtime-databricks-on-aws.md
title: serverless_gpu.data.DataLoader
description: A drop-in PyTorch DataLoader subclass tuned for serverless GPU I/O on Databricks, with higher default num_workers and prefetch_factor, plus MLflow timing logs.
tags:
  - data-loading
  - performance
  - databricks
  - pytorch
timestamp: "2026-06-19T19:13:50.911Z"
---

# `serverless_gpu.data.DataLoader`

`serverless_gpu.data.DataLoader` is a drop-in subclass of the PyTorch [`torch.utils.data.DataLoader`](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader) that is tuned for serverless GPU I/O on Databricks AI Runtime. It is designed to parallelize file fetching and caching from Unity Catalog volumes while the GPU computes, reducing data-loading bottlenecks during distributed training. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Overview

The standard PyTorch `DataLoader` uses conservative defaults for `num_workers` (0) and `prefetch_factor` (2). `serverless_gpu.data.DataLoader` raises these defaults to `num_workers=6` and `prefetch_factor=4`, so that files are fetched and cached concurrently across multiple worker processes while the GPU processes the current batch. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Key Features

- **Optimised defaults** – `num_workers` defaults to 6 and `prefetch_factor` defaults to 4, compared to PyTorch’s 0 and 2. This improves throughput when reading from remote Unity Catalog storage. ^[load-data-on-ai-runtime-databricks-on-aws.md]
- **MLflow integration** – Each batch’s fetch timing is logged to the active [MLflow Run](/concepts/mlflow-run.md), helping identify data-loading bottlenecks. ^[load-data-on-ai-runtime-databricks-on-aws.md]
- **Seamless compatibility** – Accepts any PyTorch dataset (including [UCVolumeDataset](/concepts/ucvolumedataset.md)) and provides the same API as `torch.utils.data.DataLoader`. ^[load-data-on-ai-runtime-databricks-on-aws.md]
- **Required for `UCVolumeDataset`** – When using [UCVolumeDataset](/concepts/ucvolumedataset.md) in a multi‑GPU setting, all ranks must use the same `num_workers` value because `UCVolumeDataset` partitions files across a global stride of `world_size × num_workers` slots. Mismatched values cause files to be duplicated or skipped. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Requirements

- **GPU environment 5 or above** – `serverless_gpu.data.DataLoader` and `UCVolumeDataset` require [GPU environment 5](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu) or later. ^[load-data-on-ai-runtime-databricks-on-aws.md]
- **Unity Catalog** – All data access on AI Runtime goes through Unity Catalog; tables and volumes must be registered and accessible to the user or service principal. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Usage Example

```python
from serverless_gpu.data import DataLoader, UCVolumeDataset

path_dataset = UCVolumeDataset("/Volumes/catalog/schema/my_volume/images")
# Wrap with a decoding dataset (see UCVolumeDataset docs)
dataset = ImageDataset(path_dataset)

loader = DataLoader(
    dataset,
    batch_size=32,
    pin_memory=True,
    # num_workers=6,  # default
    # prefetch_factor=4,  # default
)
```

The example above pairs `DataLoader` with a `UCVolumeDataset` that caches files locally. To increase parallelism, raise `num_workers`; to deepen each worker’s prefetch queue, raise `prefetch_factor`. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [UCVolumeDataset](/concepts/ucvolumedataset.md) – The recommended dataset class for streaming unstructured data from Unity Catalog volumes.
- [serverless_gpu](/concepts/serverless-gpu-compute.md) – The Python library providing distributed training utilities on Databricks.
- Data loading performance – General guidance on optimising I/O for serverless GPU training.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The underlying compute infrastructure.

## Sources

- load-data-on-ai-runtime-databricks-on-aws.md

# Citations

1. [load-data-on-ai-runtime-databricks-on-aws.md](/references/load-data-on-ai-runtime-databricks-on-aws-0b666631.md)
