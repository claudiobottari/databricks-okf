---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72ae461aa5a62b24e785e8c4f6dfed97415c79b564f9b28542c600d84384e96c
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - use-cases-for-deepspeed-distributor
    - UCFDD
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: Use cases for DeepSpeed distributor
description: "Scenarios where DeepSpeed distributor is beneficial: low GPU memory, large model training, and large input data such as batch inference."
tags:
  - distributed-training
  - use-cases
  - deep-learning
timestamp: "2026-06-19T10:19:03.232Z"
---

# Use cases for DeepSpeed distributor

**Use cases for DeepSpeed distributor** describes the scenarios where the [DeepSpeed](/concepts/deepspeed.md) distributor, a distributed training solution built on top of [TorchDistributor](/concepts/torchdistributor.md) and available in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) 14.0 ML and above, is most beneficial. The DeepSpeed distributor addresses memory and compute limitations that standard hardware cannot overcome by leveraging the DeepSpeed library’s advanced optimizations. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Low GPU memory

When GPU memory is constrained — for example, when a single GPU cannot hold the full model, gradients, and optimizer states — DeepSpeed provides memory-saving techniques such as ZeRO optimization, gradient checkpointing, and mixed-precision training. The distributor automatically shards model parameters, gradients, and optimizer states across multiple GPUs, enabling training that would otherwise fail due to out-of-memory errors. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Large model training

Training models with billions of parameters (e.g., Llama 2 7B or larger) often exceeds the memory capacity of a single GPU. The DeepSpeed distributor supports advanced pipeline parallelism, which partitions the model layers across devices, and reduces communication overhead between nodes. This makes it feasible to train very large models on clusters of GPUs without requiring specialized hardware. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Large input data (batch inference)

During batch inference, the input data can be so large that it saturates GPU memory or slows down processing. DeepSpeed’s optimizations for memory usage and communication allow it to handle large batch sizes efficiently. The distributor distributes the input data across workers, processing larger volumes in parallel while maintaining low latency. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Key benefits

- **Optimized memory usage**: Techniques such as ZeRO-2 and ZeRO-3 reduce the per-GPU memory footprint for parameters, gradients, and optimizer states.
- **Reduced communication overhead**: Efficient all-reduce and gradient accumulation strategies minimize network bandwidth usage.
- **Advanced pipeline parallelism**: Model layers are split across GPUs, enabling training of models that are too large to fit on any single device.

These benefits make the DeepSpeed distributor the recommended solution for customers whose models require higher compute power but are limited by memory constraints. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Related concepts

- [DeepSpeed](/concepts/deepspeed.md) – The underlying open-source library developed by Microsoft.
- [TorchDistributor](/concepts/torchdistributor.md) – The base distributor on which DeepSpeed distributor is built.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – General techniques for training models across multiple GPUs.
- [ZeRO optimization](/concepts/deepspeed-zero-stage-3.md) – Memory sharding strategy used by DeepSpeed.
- [Pipeline parallelism](/concepts/pipeline-parallelism-in-deepspeed.md) – Splitting model layers across devices.

## Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
