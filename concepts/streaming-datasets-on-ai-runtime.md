---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a4ac92ae17883b4fb5b9c530e04359eef739ff6ea3d9887b0d24de17f9757dc
  pageDirectory: concepts
  sources:
    - load-data-on-ai-runtime-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - streaming-datasets-on-ai-runtime
    - SDOAR
  citations:
    - file: load-data-on-ai-runtime-databricks-on-aws.md
title: Streaming Datasets on AI Runtime
description: Strategies for handling very large datasets that don't fit in memory, including UCVolumeDataset, PyTorch IterableDataset, Hugging Face datasets streaming, and Ray Data.
tags:
  - data-loading
  - streaming
  - databricks
  - large-scale
timestamp: "2026-06-19T19:13:49.564Z"
---

# Streaming Datasets on AI Runtime

**Streaming datasets** on AI Runtime refers to techniques for loading very large datasets that do not fit entirely in memory, allowing you to iterate over data in a streaming fashion while training machine learning or deep learning models. These approaches are especially important for multi‑epoch training on large corpora stored in Unity Catalog volumes or on remote storage. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Overview

On AI Runtime, all data access goes through Unity Catalog. For large datasets, streaming avoids the memory overhead of converting the entire dataset into a pandas DataFrame or loading it all at once. The platform provides several built‑in streaming mechanisms, each suited to different data types and workflows. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Streaming Methods

### UCVolumeDataset

`UCVolumeDataset`, from the `serverless_gpu.data` package, is a PyTorch [`IterableDataset`](https://docs.pytorch.org/docs/stable/data.html#iterable-style-datasets) designed for unstructured data (images, audio, text files) stored in Unity Catalog volumes. It copies each file to a fast local cache on first access and yields the cached local file path. Subsequent epochs read from the cache, avoiding repeated network access. `UCVolumeDataset` automatically partitions files across distributed ranks and DataLoader workers so that each `(rank, worker)` pair receives a non‑overlapping slice with no manual setup. ^[load-data-on-ai-runtime-databricks-on-aws.md]

Because it yields raw local paths, you typically wrap it in a second `IterableDataset` that decodes the paths into tensors (e.g., using PIL for images). This separation keeps I/O and parsing concerns independent. ^[load-data-on-ai-runtime-databricks-on-aws.md]

`UCVolumeDataset` and `serverless_gpu.data.DataLoader` require [GPU environment 5](https://docs.databricks.com/aws/en/release-notes/serverless/environment-version/five-gpu) or above. ^[load-data-on-ai-runtime-databricks-on-aws.md]

### PyTorch IterableDataset

You can implement custom streaming logic by writing your own [`IterableDataset`](https://docs.pytorch.org/docs/stable/data.html#iterable-style-datasets). This is useful when you need fine‑grained control over how data is fetched, filtered, or augmented on the fly. The dataset yields one sample at a time, and the training loop consumes them sequentially without loading everything into memory. ^[load-data-on-ai-runtime-databricks-on-aws.md]

### Hugging Face Datasets with Streaming

For tabular or text datasets hosted on the Hugging Face Hub or stored as Parquet files in Unity Catalog volumes, use the [Hugging Face `datasets` library’s streaming mode](https://huggingface.co/docs/datasets/stream). This allows you to iterate over data without downloading the entire dataset. Combined with the Delta‑to‑Parquet export workflow recommended for large tables, streaming from Parquet files is an effective approach for both single‑GPU and distributed training. ^[load-data-on-ai-runtime-databricks-on-aws.md]

```python
from datasets import load_dataset
dataset = load_dataset("parquet", data_files="/Volumes/catalog/schema/my_volume/training_data/*.parquet", streaming=True)
```

### Ray Data

[Ray Data](https://docs.ray.io/en/latest/data/data.html) provides a distributed, streaming data processing framework. It can be used on AI Runtime for large‑scale batch processing and training pipelines that require reading data in parallel across multiple nodes. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Performance Considerations

- **Local caching with `UCVolumeDataset`**: Files are copied from the remote volume to local cache on first access. Subsequent epochs read from the cache, significantly improving throughput for multi‑epoch training. Prefer it over a manual `shutil.copytree`, which copies everything upfront even if training only uses a subset. ^[load-data-on-ai-runtime-databricks-on-aws.md]

- **`serverless_gpu.data.DataLoader`**: This drop‑in replacement for the stock PyTorch `DataLoader` is tuned for serverless GPU I/O. It defaults `num_workers` to 6 and `prefetch_factor` to 4, so files are fetched and cached concurrently while the GPU computes. It also logs per‑batch fetch timing to the active [MLflow Run](/concepts/mlflow-run.md). ^[load-data-on-ai-runtime-databricks-on-aws.md]

  All ranks must use the same `num_workers` value when using `UCVolumeDataset`, because file partitioning uses a global stride across `world_size × num_workers` slots. ^[load-data-on-ai-runtime-databricks-on-aws.md]

- **Increase batch size**: Larger batches amortize per‑batch data‑loading overhead over more samples. If GPU memory is a bottleneck, combine larger batches with gradient accumulation. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [UCVolumeDataset](/concepts/ucvolumedataset.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Unity Catalog Volumes
- [@distributed Decorator](/concepts/distributed-decorator.md)
- Data Loading on AI Runtime

## Sources

- load-data-on-ai-runtime-databricks-on-aws.md

# Citations

1. [load-data-on-ai-runtime-databricks-on-aws.md](/references/load-data-on-ai-runtime-databricks-on-aws-0b666631.md)
