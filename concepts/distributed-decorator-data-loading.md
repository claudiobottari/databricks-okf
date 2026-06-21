---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0cb4ece646084a54a41c7a7b6ef118adfeec301b17ca1ea73eea83a070d48123
  pageDirectory: concepts
  sources:
    - load-data-on-ai-runtime-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-decorator-data-loading
    - "@DDL"
  citations:
    - file: filename.md
    - file: source-a.md
    - file: source-b.md
    - file: filename.md:START-END
    - file: filename.md#LSTART-LEND
    - file: load-data-on-ai-runtime-databricks-on-aws.md
title: "@distributed Decorator Data Loading"
description: Best practice to load data inside the @distributed decorator to avoid pickle serialization issues when datasets are too large.
tags:
  - distributed-training
  - databricks
  - serialization
timestamp: "2026-06-19T19:14:13.184Z"
---

You are a wiki author. Write a clear, well-structured markdown page about "@distributed Decorator Data Loading".
Draw facts only from the provided source material.
Include a ## Sources section at the end listing the source document.
Suggest wikilinks to related concepts where appropriate.
Write in a neutral, informative tone. Be concise but thorough.

Source attribution: at the end of each prose paragraph, append a citation
marker showing which source file(s) the paragraph drew from.
Format: ^[filename.md] for single-source, ^[source-a.md, source-b.md] for multi-source.
When a single sentence makes a specific factual claim and you can identify the
exact line range it came from, you may use the claim-level form
^[filename.md:START-END] (or ^[filename.md#LSTART-LEND]) at the end of that
sentence — START and END are 1-indexed line numbers in the source file.
Paragraph-level citations remain the default; only switch to claim-level form
when it materially improves verifiability and the line range is unambiguous.
Place citations only at the end of prose paragraphs or sentences — not on
headings, list items, or code blocks.
Source filenames are visible as `--- SOURCE: filename.md ---` headers in the content below.

If a paragraph is your inference rather than a direct extraction, leave it
uncited — downstream lint rules will count uncited paragraphs as 'inferred'
to compute the page's provenance metadata.



Related wiki pages for cross-referencing:

- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- [30-Day Lookback Window Limitation](/concepts/30-day-lookback-window.md)
- [30-Day Lookback Window](/concepts/30-day-lookback-window.md)
- 403 PERMISSION_DENIED Serverless Budget Policy Error
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

Here is the wiki page for "@distributed Decorator Data Loading".

---

The **@distributed Decorator Data Loading** pattern refers to the recommended practice of moving all data loading and dataset generation code *inside* the `@distributed` decorator body when using the [Serverless GPU API](/concepts/serverless-gpu-api.md) for distributed training on [AI Runtime](/concepts/ai-runtime.md). This prevents pickle serialization errors that can occur when a dataset object is constructed outside the decorator and then implicitly serialized when the decorator distributes the function across multiple GPUs. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Motivation

When the `@distributed` decorator is used, the function it wraps is serialized and broadcast to each GPU process via pickle. If the dataset object is large—for example, a PyTorch Dataset holding many file paths or tensors—it can exceed the maximum size allowed by pickle, causing a ``PicklingError`` (or an equivalent serialization failure). ^[load-data-on-ai-runtime-databricks-on-aws.md]

The source material warns:

```python
from serverless_gpu import distributed

# This may cause a pickle error if the dataset is too large
dataset = get_dataset(file_path)

@distributed(gpus=8, gpu_type='H100')
def run_train():
    ...
```

The fix is to regenerate (or load) the dataset inside the decorator body rather than passing it in as a captured variable. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## How to Apply the Pattern

Move data-loading code into the function that the `@distributed` decorator wraps. ^[load-data-on-ai-runtime-databricks-on-aws.md]

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def run_train():
    # Load data inside the decorator to avoid pickle serialization issues
    dataset = get_dataset(file_path)
    ...
```

This ensures that each GPU process constructs its own copy of the dataset from the same source path, eliminating the serialization bottleneck. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Interaction with `UCVolumeDataset`

When you construct a [UCVolumeDataset](/concepts/ucvolumedataset.md) inside the decorated function, it automatically reads `torch.distributed` rank information at iteration time and partitions files across ranks. This means you do not need a DistributedSampler for file-based volume data when using this pattern. ^[load-data-on-ai-runtime-databricks-on-aws.md]

## Related Concepts

- [@distributed Decorator](/concepts/distributed-decorator.md) — The primary API for launching multi-GPU distributed functions.
- Pickle Serialization — The underlying mechanism that causes the error when large datasets are captured outside the decorator.
- [UCVolumeDataset](/concepts/ucvolumedataset.md) — A PyTorch IterableDataset for streaming files from [Unity Catalog](/concepts/unity-catalog.md) volumes.
- [Serverless GPU API](/concepts/serverless-gpu-api.md) — The Python API that provides the `@distributed` decorator.
- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment in which distributed training runs.

## Sources

- load-data-on-ai-runtime-databricks-on-aws.md (Lines 49–61, 72–77)

# Citations

1. filename.md
2. source-a.md
3. source-b.md
4. filename.md:START-END
5. filename.md#LSTART-LEND
6. [load-data-on-ai-runtime-databricks-on-aws.md](/references/load-data-on-ai-runtime-databricks-on-aws-0b666631.md)
