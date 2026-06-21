---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5fff596a65cb3e3d86e18a4bf7870b08ca63fda5da2fbc5c27d74e9d483b5be
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-genie-code-support
    - ARGCS
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Genie Code Support
description: Integration with Genie Code to assist with deep learning code generation, library debugging, optimization suggestions on AI Runtime.
tags:
  - assistance
  - code-generation
  - deep-learning
timestamp: "2026-06-19T13:57:47.308Z"
---

# AI Runtime Genie Code Support

**AI Runtime Genie Code Support** refers to the integration of Genie Code with [AI Runtime](/concepts/ai-runtime.md) on Databricks to assist with deep learning workloads. Genie Code provides AI-powered assistance for code generation, troubleshooting, and optimization when working with AI Runtime environments. ^[ai-runtime-databricks-on-aws.md]

## Overview

Genie Code supports deep learning workloads running on AI Runtime. It is designed to help data scientists and developers streamline the model development process by providing intelligent code suggestions and debugging help directly within the notebook interface. ^[ai-runtime-databricks-on-aws.md]

## Capabilities

Genie Code on AI Runtime can assist with the following tasks:

- **Generating training code** – Write or complete code for training deep learning models, including fine-tuning and distributed training setups.
- **Resolving library installation errors** – Diagnose and fix dependency or environment issues that arise during package installation.
- **Suggesting optimizations** – Recommend performance improvements for training workflows, such as batching, data loading, or parallelization strategies.
- **Debugging common issues** – Identify and explain errors in training scripts, configuration, or data pipelines. ^[ai-runtime-databricks-on-aws.md]

## Integration with AI Runtime

Genie Code is available in notebooks that use AI Runtime compute. It leverages the deep learning libraries and GPU infrastructure provided by AI Runtime to offer context-aware assistance. For detailed instructions on using Genie Code for data science tasks, see the official Databricks documentation on [Use Genie Code for data science](https://docs.databricks.com/aws/en/notebooks/ds-agent). ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The compute offering for deep learning workloads on Databricks.
- [Genie Code](/concepts/genie-code.md) – The broader AI assistant for code generation across Databricks notebooks.
- [Deep Learning on Databricks](/concepts/deep-learning-on-databricks.md) – General workflows for training models on the platform.
- [Distributed Training on AI Runtime](/concepts/distributed-training-on-ai-runtime.md) – Multi-GPU training with the `@distributed` decorator.

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
