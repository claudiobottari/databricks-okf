---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed159b530c424944560777aaca45959d8abfecb620b7d3c8417835a6cdeaff5e
  pageDirectory: concepts
  sources:
    - prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dataset-size-estimation-with-load_dataset_builder
    - DSEWL
  citations:
    - file: prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md
title: Dataset Size Estimation with load_dataset_builder
description: Using Hugging Face's load_dataset_builder to inspect download and dataset sizes before committing to a large download
tags:
  - hugging-face
  - data-management
  - utilities
timestamp: "2026-06-19T19:57:47.490Z"
---

# Dataset Size Estimation with `load_dataset_builder`

**`load_dataset_builder`** is a utility from the Hugging Face Datasets library that allows you to inspect a dataset’s metadata — including its expected download and on‑disk sizes — before actually downloading the data. This is useful for planning storage, bandwidth, and compute resources, especially when working with large datasets on platforms like Databricks.

## Overview

When you call `load_dataset("imdb")`, the dataset is downloaded immediately. Some datasets on the Hugging Face Hub expose their **download size** (the compressed size of files to be fetched) and **dataset size** (the size after decompression). `load_dataset_builder` lets you read these sizes without triggering a download. You can then decide whether to proceed with `load_dataset`. ^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

## Usage

`load_dataset_builder` returns a `DatasetBuilder` object whose `.info` attribute contains optional fields `download_size` and `dataset_size` (both in bytes). If the uploader has not provided these values, the fields are `None`. The following example defines a helper function that prints the sizes if they are available:

```python
from datasets import load_dataset_builder
from psutil._common import bytes2human

def print_dataset_size_if_provided(*args, **kwargs):
    dataset_builder = load_dataset_builder(*args, **kwargs)
    if dataset_builder.info.download_size and dataset_builder.info.dataset_size:
        print(f'download_size={bytes2human(dataset_builder.info.download_size)}, '
              f'dataset_size={bytes2human(dataset_builder.info.dataset_size)}')
    else:
        print('Dataset size is not provided by uploader')

print_dataset_size_if_provided("imdb")
```

^[prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md]

The `bytes2human` function from the `psutil` library converts byte counts into human‑readable strings (e.g., “1.2 GiB”).

## Why Size Estimation Matters

Knowing the dataset size in advance helps you:

- Choose an appropriate Unity Catalog volume path for caching, so that temporary data survives cluster termination.
- Decide whether to use SSD‑backed temporary storage (`/local_disk0/tmp`) for large datasets to speed up writes.
- Estimate download time and allocate sufficient cluster resources.

For best practices on downloading and preparing datasets of various sizes on Databricks, see the Download datasets from Hugging Face best practices notebook.

## Related Concepts

- load_dataset – The function that actually fetches the data.
- Hugging Face Datasets – The library providing `load_dataset_builder` and `load_dataset`.
- [Unity Catalog](/concepts/unity-catalog.md) – Used for persistent storage of cached datasets on Databricks.
- Data caching – How `datasets` caches processed data to avoid re‑downloading.

## Sources

- prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md

# Citations

1. [prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws.md](/references/prepare-data-for-fine-tuning-hugging-face-models-databricks-on-aws-b70184e4.md)
