---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43a3f19e3858136ab701b28e23c3947934f29803e3be9a3c84ae3707a22fe0fe
  pageDirectory: concepts
  sources:
    - distributed-training-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  contradictedBy:
    - slug: deepspeed-distributor
      reason: DeepSpeed distributor is explicitly recommended for models that require higher compute but are memory-constrained, suggesting distributed training has valid use cases.
    - slug: torchdistributor
      reason: TorchDistributor exists as a supported solution, implying distributed training is sometimes necessary.
  freshnessStatus: unverified
  aliases:
    - single-machine-preference-for-neural-networks
    - SPFNN
  citations:
    - file: distributed-training-databricks-on-aws.md
title: Single-Machine Preference for Neural Networks
description: Databricks recommendation to train neural networks on a single machine when possible, because distributed code is more complex and slower due to communication overhead
tags:
  - best-practice
  - neural-networks
  - databricks
timestamp: "2026-06-18T15:30:56.082Z"
---

# Single-Machine Preference for Neural Networks

**Single-Machine Preference for Neural Networks** refers to the recommendation, articulated by Databricks, to train neural networks on a single machine whenever possible, rather than distributing the workload across multiple machines. This guidance stems from the inherent complexity and performance trade-offs of distributed training.

## Overview

Databricks recommends training neural networks on a single machine whenever feasible. Distributed code for both training and inference is more complex to write, debug, and maintain than single-machine code, and it also suffers from communication overhead that can slow down execution. ^[distributed-training-databricks-on-aws.md]

## When to Consider Distributed Training

Despite the preference for single-machine training, distributed training and inference become necessary when either the model or the data are too large to fit in the memory of a single machine. ^[distributed-training-databricks-on-aws.md]

## Available Tools for Distributed Training

When distributed training is required, Databricks Runtime ML provides several built-in packages to support the workload:

- **[TorchDistributor](/concepts/torchdistributor.md)** – A PySpark module that enables distributed PyTorch training by launching `torch.distributed.run` jobs across worker nodes. ^[distributed-training-databricks-on-aws.md]
- **[DeepSpeed](/concepts/deepspeed.md) Distributor** – Built on top of TorchDistributor, it is recommended for models that require high compute power but are constrained by memory. DeepSpeed offers optimized memory usage, reduced communication overhead, and advanced pipeline parallelism. ^[distributed-training-databricks-on-aws.md]
- **Ray** – An open-source framework for parallel compute processing and scaling ML workflows and AI applications. ^[distributed-training-databricks-on-aws.md]
- **Spark ML** – The `pyspark.ml.connect` module allows distributed training for Spark ML models and inference. In Databricks Runtime 17.0 and above, Spark ML is enabled by default in Standard compute resources. ^[distributed-training-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- Neural Networks
- [Data Parallelism](/concepts/data-parallelism-spark.md)
- Model Parallelism
- [Pipeline Parallelism](/concepts/pipeline-parallelism-in-deepspeed.md)

## Sources

- distributed-training-databricks-on-aws.md

# Citations

1. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
