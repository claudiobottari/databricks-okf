---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99a703fb471714a9ee1f13d66c83e52bb3ad5abc9202bbe857da48781eccba39
  pageDirectory: concepts
  sources:
    - load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - shared-storage-for-model-checkpointing
    - SSFMC
  citations:
    - file: load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md
title: Shared Storage for Model Checkpointing
description: Using shared storage for data loading and model checkpointing in distributed deep learning training on Databricks.
tags:
  - deep-learning
  - checkpointing
  - distributed-training
  - storage
timestamp: "2026-06-19T19:13:21.979Z"
---

# Shared Storage for Model Checkpointing

**Shared Storage for Model Checkpointing** refers to the use of a common, network-accessible storage location that multiple nodes or processes in a distributed training job can read from and write to simultaneously. This is essential for saving and loading model checkpoints during [Distributed Training](/concepts/workload-yaml-for-distributed-training.md), particularly for [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) and Deep Learning workloads that span multiple GPUs or nodes.

## Overview

Machine learning applications often require shared storage for model checkpointing, especially in the context of distributed deep learning. When training large models across multiple GPUs or nodes, each process must be able to write its portion of the model state (parameters, optimizer states, gradients) to a location that all other processes can access. Without shared storage, recovering from a failure or resuming training across different hardware configurations would be impractical. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

## Storage Solutions on Databricks

Databricks provides [Unity Catalog](/concepts/unity-catalog.md) as a unified governance solution for data and AI assets. You can use Unity Catalog for accessing data on a cluster using both Spark and local file APIs, making it suitable for storing and retrieving model checkpoints during distributed training runs. ^[load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md]

Common shared storage backends include:
- Cloud object storage (AWS S3, Azure Blob Storage, Google Cloud Storage)
- Network File Systems (NFS)
- DBFS (Databricks File System)

## Importance for Distributed Training

In distributed training frameworks like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) and [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), shared storage enables:

- **Fault tolerance**: If a node fails mid-training, the checkpoint saved to shared storage allows recovery from the last saved state rather than restarting from scratch.
- **Consistency**: All processes save and load from the same location, ensuring that the model state is synchronized across the cluster.
- **Resumability**: Training can be paused and resumed on different hardware or cluster configurations by loading the checkpoint from shared storage.

## Performance Considerations

For very large models (20B to 120B+ parameters), checkpointing to shared storage can be I/O intensive. Strategies to mitigate this include:

- Asynchronous checkpointing to avoid blocking training progress
- Sharded checkpoint formats where each rank saves only its own portion of the model to the shared filesystem
- Using high-throughput cloud storage with optimized I/O paths

## Related Concepts

- Model Checkpointing
- Fault Tolerance in Distributed Training
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Load Data for Machine Learning](/concepts/loading-data-for-machine-learning-on-databricks.md)

## Sources

- load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md

# Citations

1. [load-data-for-machine-learning-and-deep-learning-databricks-on-aws.md](/references/load-data-for-machine-learning-and-deep-learning-databricks-on-aws-dfd2be96.md)
