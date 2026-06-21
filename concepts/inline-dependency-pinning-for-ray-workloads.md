---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 091b798b701a69bb6cb039b450aac2faf82160641ad777a9d6871c83f0fe8801
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inline-dependency-pinning-for-ray-workloads
    - IDPFRW
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: Inline Dependency Pinning for Ray Workloads
description: Declaring Python dependencies directly in the workload YAML environment section rather than in a separate requirements file, including pinning transitive dependencies like fsspec that conflict with newer library versions.
tags:
  - dependency-management
  - ray
  - databricks
timestamp: "2026-06-19T18:38:09.554Z"
---

# Inline Dependency Pinning for Ray Workloads

**Inline Dependency Pinning for Ray Workloads** is a technique for specifying Python package dependencies and their version constraints directly in the workload configuration YAML file, eliminating the need for a separate `requirements.txt` or environment launcher script. This pattern is used in the Databricks AI Runtime `air` CLI when running [Ray Train](/concepts/ray-train-resource-allocation.md) or other distributed jobs. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

When defining a Ray workload with the `air` CLI, dependencies are declared inline under the `environment` key of the YAML file. The `environment` block contains a `version` field (referring to the client image version) and a `dependencies` list of pip-installable packages. The workload command then runs directly without an additional dependency file or launcher script. This inline approach keeps the entire workload definition in a single file and makes it easy to pin specific versions of libraries. ^[distributed-training-with-ray-train-databricks-on-aws.md]

Inline pinning is especially useful when the base image ships a library version that is too old for the workload's needs. The example below pins `fsspec>=2024.6.1` because the base image ships `fsspec 2023.5.0`, which breaks model and dataset downloads with modern Hugging Face libraries. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## How It Works

In the `train.yaml` file:

1. Set `environment.version` to the desired AI Runtime version (e.g., `'4'`).
2. List every required package under `environment.dependencies` using standard pip version specifiers (`>=`, `==`, `~=`, etc.).
3. The `command` field starts a Ray cluster and runs the training script *after* the dependencies are installed by the runtime.
4. No separate `requirements.txt` or environment management step is needed in the command.

## Example

The following snippet from a Ray Train distributed fine‑tuning workload shows inline dependency pinning:

```yaml
environment:
  version: '4'
  dependencies:
    - ray[default,train]>=2.30
    - transformers>=4.45
    - datasets>=3.0
    - huggingface_hub>=0.34
    # The base image ships fsspec 2023.5.0, which is too old for modern
    # huggingface_hub and breaks dataset/model downloads. Pin a newer fsspec.
    - fsspec>=2024.6.1
```

The full workload requests a single `GPU_8xH100` node, uses a snapshot code source, and runs a bootstrap command that starts a Ray head, executes the training driver (`train_ray.py`), and then stops the cluster. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Benefits

- **Single‑file definition** – the entire job (compute, code, environment, command) lives in one YAML file.
- **Reproducibility** – explicit version constraints prevent unexpected breakage when base images are updated.
- **Overriding base image defaults** – packages that are present but too old (e.g., `fsspec`) can be upgraded without modifying the base image.
- **Simpler CI/CD** – no need to manage and upload a separate `requirements.txt`.

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) – the distributed training framework used in the example workload.
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) – Ray Train’s API for PyTorch workloads.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – the parallelism strategy used in the example.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – the command‑line tool that interprets the workload YAML.
- [Workload YAML Reference](/concepts/workload-yaml-configuration.md) – the full schema for `air` YAML files.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – an alternative parallelism strategy for larger models.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
