---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 293c9dadc26f0357cfced58595021058d5b438e561e8d23473e1193b1d6ba4d0
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-volumes-for-checkpointing
    - UCVFC
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Unity Catalog Volumes for Checkpointing
description: Using Unity Catalog volumes as persistent storage for model checkpoints during distributed training workloads on Databricks
tags:
  - storage
  - checkpointing
  - databricks
timestamp: "2026-06-19T22:02:34.443Z"
---

# Unity Catalog Volumes for Checkpointing

**Unity Catalog Volumes for Checkpointing** refers to the practice of using Unity Catalog volumes as the storage destination for model checkpoints during distributed training on Databricks. This approach provides a managed, governed storage location for saving intermediate model states that can be used for recovery, evaluation, or downstream deployment.

## Overview

When conducting distributed training across multiple GPU nodes, checkpointing is an essential practice for saving model state at regular intervals. Checkpoints allow training to resume from a saved state if interrupted, and they can be used for model evaluation or deployment. Unity Catalog volumes provide a centralized, governed storage location for these checkpoints within the Databricks environment. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Use Case: Multi-Node LLM Fine-Tuning

A common example of Unity Catalog volumes for checkpointing is in multi-node, large-scale language model (LLM) fine-tuning. In supervised fine-tuning of models like Llama-3.1-8B across 16 H100 GPUs (2 nodes), the training pipeline uses `torchrun` and PyTorch Fully Sharded Data Parallel (FSDP) and logs checkpoints to a Unity Catalog volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

This pattern demonstrates:
- **Multi-node distributed training** using FSDP across multiple compute nodes
- **Checkpointing to a Unity Catalog volume** as the storage destination
- **Integration with MLflow** for experiment tracking alongside checkpoint storage

## Benefits

Using Unity Catalog volumes for checkpointing provides:
- **Centralized governance** through Unity Catalog's data management and access control
- **Persistence** across compute sessions, as checkpoints survive cluster teardown
- **Discoverability** within the Databricks environment for downstream use

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – The distributed training strategy used in conjunction with checkpointing to Unity Catalog volumes
- [MLflow](/concepts/mlflow.md) – Experiment tracking and logging system that can be used alongside checkpoint storage
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) – Training that spans multiple compute nodes, requiring networked checkpoint storage
- Checkpointing – The general practice of saving model state during training for recovery and evaluation
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks' unified governance solution for data and AI assets
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface for submitting distributed training workloads on Databricks

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
