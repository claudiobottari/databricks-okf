---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0608afa0fca3990d1c02e38c34b3a181291f3c2a6492c490577365554d5f44a4
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - a100-gpu-support-on-databricks
    - AGSOD
    - A10 GPU Support on Databricks
    - A10 GPU Support on Databricks|A10
    - A10 GPU support on Databricks
    - GPU Support on Databricks
    - H100 GPU Support on Databricks
    - H100 GPU Support on Databricks|H100
    - H100 GPU support on Databricks
    - A100 GPU support
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: A100 GPU Support on Databricks
description: Databricks supports A100 GPUs across all clouds for deep learning tasks like LLM training, NLP, object detection, and recommendation engines, though availability may be limited
tags:
  - databricks
  - gpu
  - a100
  - infrastructure
timestamp: "2026-06-18T14:33:25.717Z"
---

# A100 GPU Support on Databricks

**A100 GPU Support on Databricks** refers to the availability and recommended use of NVIDIA A100 GPUs for deep learning workloads within the Databricks platform. A100 GPUs provide high-performance compute for training and inference tasks, particularly for large-scale models.

## Overview

Databricks supports A100 GPUs on all cloud providers. They are considered an efficient choice for many deep learning tasks, including training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Cloud and Instance Support

A100 GPUs are available across all major clouds (AWS, Azure, GCP). For the complete list of supported GPU instance types, see the Databricks documentation on [supported instance types](https://docs.databricks.com/aws/en/compute/gpu#gpu-list). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Availability Considerations

A100 GPUs typically have limited capacity in cloud environments. Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance to ensure availability for workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- GPU Scheduling – Optimizing GPU utilization for distributed training and inference.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime that includes GPU support and common deep learning libraries.
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md) – General guidance for deep learning workflows.
- Supported GPU Types on Databricks – Full list of GPU instances available across clouds.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
