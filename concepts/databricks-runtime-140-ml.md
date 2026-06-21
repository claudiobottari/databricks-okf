---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec9570e3d6b6b23f5e47dc22debd4b93baa7de635fac537068fe86101967736f
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-140-ml
    - DR1M
    - Databricks Runtime 10.4 LTS ML
    - Databricks Runtime 10.5 ML
    - Databricks Runtime 12.0 ML
    - Databricks Runtime 14.0
    - Databricks Runtime 14.1
    - Databricks Runtime 14.2
    - Databricks Runtime 15.4 LTS ML
    - Databricks Runtime 18.0 ML
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: Databricks Runtime 14.0 ML
description: The ML runtime version on Databricks that introduced support for the DeepSpeed library, enabling advanced distributed training capabilities.
tags:
  - databricks
  - runtime
  - machine-learning
timestamp: "2026-06-19T10:19:10.778Z"
---

Here is the wiki page for "Databricks Runtime 14.0 ML", written solely from the provided source material.

---

## Databricks Runtime 14.0 ML

**Databricks Runtime 14.0 ML** is a version of the [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). It includes the [DeepSpeed](/concepts/deepspeed.md) library, an open-source distributed training library developed by Microsoft, which enables optimized memory usage, reduced communication overhead, and advanced pipeline parallelism for scaling models and training procedures that would otherwise be unattainable on standard hardware.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### DeepSpeed Integration

DeepSpeed is available in Databricks Runtime 14.0 ML and above. Using the [DeepSpeed Distributor](/concepts/deepspeed-distributor.md), which is built on top of the [TorchDistributor](/concepts/torchdistributor.md), users can perform distributed training on PyTorch models that require higher compute power but are limited by memory constraints. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

Typical use cases for the DeepSpeed distributor include:
- Low GPU memory scenarios
- Large model training
- Large input data, such as batch inference

These capabilities make Databricks Runtime 14.0 ML a suitable choice for fine-tuning large language models like Llama 2 7B.^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

### Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) – The library integrated into this runtime.
- [TorchDistributor](/concepts/torchdistributor.md) – The underlying distributed training mechanism.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) – General guidance for multi‑GPU workloads.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The family of runtimes that includes 14.0 ML.

## Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
