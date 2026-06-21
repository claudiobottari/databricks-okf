---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 523b7b49479a77335c4a37ec163120e86e9f1abe391ab2f40694c8410efcf0a4
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - multi-gpu-training-apis-on-databricks
    - MTAOD
    - Multi-GPU Training on Databricks
    - Multi-GPU training on Databricks
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: Multi-GPU Training APIs on Databricks
description: "The two parallel approaches for multi-GPU workload training on Databricks: the AI Runtime CLI for laptop-based submission and the in-notebook Python API with @distributed and @ray_launch decorators"
tags:
  - distributed-training
  - databricks
  - gpu-computing
  - ray
timestamp: "2026-06-19T22:01:50.826Z"
---

# Multi-GPU Training APIs on Databricks

**Multi-GPU Training APIs on Databricks** encompass the tools and interfaces for submitting and managing distributed training workloads that span multiple GPUs. These APIs operate on [AI Runtime](/concepts/ai-runtime.md), the on-demand serverless GPU compute platform, and support both notebook‑based and CLI‑based workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Overview

Databricks provides two primary approaches for running multi‑GPU training jobs:

- **In‑notebook Python APIs** using the `@distributed` and `@ray_launch` decorators.
- **AI Runtime CLI** (`air`) – a command‑line interface that uses YAML‑based job configuration and integrates with [MLflow](/concepts/mlflow.md) and the Databricks Jobs run page.

The choice between them depends on the development environment and whether you prefer a declarative, source‑controlled workflow or an interactive notebook experience. ^[ai-runtime-cli-databricks-on-aws.md]

## In‑Notebook Python APIs

The Python APIs (`@distributed` and `@ray_launch`) are designed for interactive use inside a Databricks notebook. They allow you to launch functions across multiple GPUs on a single node without leaving the notebook environment. For a detailed example, see the [@distributed Decorator](/concepts/distributed-decorator.md) (as used in the 8xH100 single‑node configuration). ^[ai-runtime-cli-databricks-on-aws.md]

Use the in‑notebook API when you want to:

- Run distributed training experiments interactively.
- Prototype quickly in a notebook before moving to production.

## AI Runtime CLI

The AI Runtime CLI (`air`) submits and manages distributed training workloads from the command line. It is particularly useful when you want to:

- Submit GPU training jobs from your laptop and code editor without opening a notebook.
- Define training jobs declaratively in YAML so they can be checked into source control.

The CLI supports workspace‑based and git‑based code workflows. It integrates with MLflow for run tracking and with the Databricks Jobs run page for monitoring. ^[ai-runtime-cli-databricks-on-aws.md]

## When to Use Each API

| Use case | Recommended API |
|---|---|
| Interactive experimentation in a notebook | `@distributed` or `@ray_launch` |
| Declarative job definitions for CI/CD | AI Runtime CLI |
| Submitting jobs from a local editor | AI Runtime CLI |
| Quick prototyping | In‑notebook APIs |

All of these APIs target [AI Runtime](/concepts/ai-runtime.md) and can be combined with distributed training strategies such as [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). ^[ai-runtime-cli-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The on‑demand serverless GPU compute platform.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific hardware setup for multi‑GPU training.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – Model scales that often require FSDP.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory‑efficient parallelism for large models.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Standard parallelism for models that fit in a single GPU.
- [MLflow](/concepts/mlflow.md) – Experiment tracking integrated with the AI Runtime CLI.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
