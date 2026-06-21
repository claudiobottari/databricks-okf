---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d7fc2f55aed26d233220456fe1c5f11394710879cea87db556149cf9fb68db9d
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workload-yaml-for-distributed-training
    - WYFDT
    - Ray for Distributed Training
    - Distributed ML Training
    - Distributed Training
    - Distributed training
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Workload YAML for Distributed Training
description: Declarative YAML configuration files (e.g., train.yaml) used with the air CLI to define and submit end-to-end distributed training workloads on Databricks
tags:
  - yaml
  - configuration
  - workloads
timestamp: "2026-06-19T22:02:40.296Z"
---

# Workload YAML for Distributed Training

**Workload YAML for Distributed Training** refers to a YAML configuration file used with the `air` CLI to define and submit distributed training jobs on Databricks. The file, typically named `train.yaml`, is passed to the `air run -f` command and contains the complete specification of a distributed training workload, including the launcher script and training code. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Overview

The workload YAML enables users to submit end-to-end distributed training patterns directly from the command line. Each YAML file describes a real distributed-training workload that runs on H100 GPUs. The `air` CLI processes the YAML and orchestrates the execution of the training job across the specified compute resources. ^[ai-runtime-cli-examples-databricks-on-aws.md]

A complete workload bundle consists of three components:
- The **workload YAML** (`train.yaml`) that defines the job configuration
- A **launcher script** that initializes the distributed runtime
- The **training code** that implements the model logic

## Example Workloads

The `air` CLI documentation provides two canonical examples of distributed training workloads, both using H100 GPUs:

### Multi-Node LLM Fine-tuning with FSDP

This workload performs supervised fine-tuning of a Llama-3.1-8B model across 16 H100 GPUs distributed across two nodes. It uses `torchrun` for process launching and PyTorch [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) for memory-efficient distributed training. The workload logs metrics to MLflow and saves checkpoints to a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

### Distributed Training with Ray Train

This workload demonstrates distributed data-parallel fine-tuning using Ray Train's `TorchTrainer` across 8 H100 GPUs on a single node, with one worker per GPU. It showcases a different distributed programming model compared to FSDP. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Usage

To submit a workload, run the following command from the directory containing the YAML file:

```bash
air run -f train.yaml
```

The `-f` flag specifies the path to the workload YAML file. Before running the examples, users are advised to review the AI Runtime CLI quickstart guide. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface used to submit workload YAML files.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Sharding strategy used in the multi-node LLM example.
- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed training library used in the single-node example.
- H100 GPU Support on Databricks – GPU type used in both examples.
- Torchrun – Process launcher used for multi-node training.
- [Unity Catalog](/concepts/unity-catalog.md) – Used for checkpoint storage in the multi-node example.

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
