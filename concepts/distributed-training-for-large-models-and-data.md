---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b00deda6e0923fb78f74c0f928fbd3b8d3b9db4da4ea6d9fd41a6053bfe61cb0
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-for-large-models-and-data
    - Data and Distributed Training for Large Models
    - DTFLMAD
  citations:
    - file: distributed-training-databricks-on-aws.md
title: Distributed Training for Large Models and Data
description: A strategy on Databricks for training neural networks when model or data exceeds single-machine memory capacity, using distributed frameworks
tags:
  - distributed-training
  - large-models
  - scalability
timestamp: "2026-06-19T10:16:25.972Z"
---

# Distributed Training for Large Models and Data

**Distributed Training for Large Models and Data** refers to the practice of training machine learning models across multiple machines and GPUs when a model or dataset exceeds the memory capacity of a single machine. While single-machine training is preferred for simplicity and performance, distributed approaches become necessary when model parameters or training data cannot fit within available memory.^[distributed-training-databricks-on-aws.md]

## When to Use Distributed Training

Databricks recommends training neural networks on a single machine whenever possible. Distributed code is inherently more complex than single-machine code and introduces communication overhead that can slow training.^[distributed-training-databricks-on-aws.md]

Consider distributed training in two primary scenarios:

- **Model size exceeds memory**: The model parameters, gradients, and optimizer states cannot fit on a single GPU.
- **Data volume exceeds capacity**: The training dataset is too large to be processed efficiently on a single machine.

For these workloads, Databricks Runtime ML includes several distributed training frameworks.^[distributed-training-databricks-on-aws.md]

## Distributed Training Frameworks on Databricks

### DeepSpeed Distributor

The [DeepSpeed](/concepts/deepspeed.md) distributor is built on top of [TorchDistributor](/concepts/torchdistributor.md) and is the recommended solution for models requiring higher compute power while being constrained by memory. Developed by Microsoft as an open-source library, DeepSpeed offers optimized memory usage, reduced communication overhead, and advanced pipeline parallelism. It is particularly suited for training very large models that benefit from [pipeline parallelism](/concepts/pipeline-parallelism-in-deepspeed.md) and [ZeRO optimization](/concepts/deepspeed-zero-stage-3.md).^[distributed-training-databricks-on-aws.md]

### TorchDistributor

[TorchDistributor](/concepts/torchdistributor.md) is an open-source module in PySpark that enables distributed training with PyTorch on Spark clusters. It allows users to launch PyTorch training jobs as Spark jobs. Under the hood, TorchDistributor initializes the environment and communication channels between workers, then uses the CLI command `torch.distributed.run` to execute distributed training across worker nodes.^[distributed-training-databricks-on-aws.md]

### Ray

Ray is an open-source framework specializing in parallel compute processing for scaling ML workflows and AI applications. Databricks integrates Ray for distributed training workloads that benefit from its flexible parallel computing model. See [What is Ray on Databricks?](/concepts/ray-on-databricks.md) for more information.^[distributed-training-databricks-on-aws.md]

### Spark ML

The `pyspark.ml.connect` module provides distributed training for Spark ML models and model inference. In Databricks Runtime 17.0 and above, Spark ML is enabled by default in Standard compute resources, allowing users to leverage Spark's distributed machine learning capabilities without managing a full cluster. See [Train Spark ML models on Databricks Connect with pyspark.ml.connect](/concepts/spark-ml-distributed-training-with-pysparkmlconnect.md).^[distributed-training-databricks-on-aws.md]

## Considerations

- **Communication overhead**: Distributed training requires synchronization of gradients and model parameters across nodes, which adds latency compared to single-machine training.
- **Complexity**: Debugging, monitoring, and maintaining distributed training code is more challenging than single-machine equivalents.
- **Hardware requirements**: Distributed training benefits significantly from high-bandwidth interconnects (e.g., NVLink, InfiniBand) between GPUs and nodes.

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Data Parallelism](/concepts/data-parallelism-spark.md)
- Model Parallelism
- [Pipeline Parallelism](/concepts/pipeline-parallelism-in-deepspeed.md)
- [ZeRO Optimization](/concepts/deepspeed-zero-stage-3.md)
- GPU Scheduling
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md)

## Sources

- distributed-training-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
