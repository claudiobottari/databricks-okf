---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 683059491bded73d64d3aab2c3ca3503cb6ff42dcecb0fc2c53efe43e2676616
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - development-workflow-for-horovodrunner
    - DWFH
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: Development Workflow for HorovodRunner
description: The recommended development workflow on Databricks for preparing data and code before running distributed training with HorovodRunner.
tags:
  - best-practices
  - databricks
  - workflow
timestamp: "2026-06-19T09:58:04.117Z"
---

# Development Workflow for HorovodRunner

**HorovodRunner** is a distributed deep learning training utility on Databricks that integrates with the [Horovod](/concepts/horovod.md) distributed training framework. It enables data-parallel training across multiple worker nodes using synchronous allreduce operations.

## Recommended Development Workflow

The recommended development workflow for HorovodRunner follows a three-stage process designed to reduce debugging time and accelerate development. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Stage 1: Single-Node Prototype

1. **Develop on a single worker node** first, without using HorovodRunner. This allows you to:
   - Quickly iterate on model architecture, hyperparameters, and data pipeline.
   - Debug Keras and TensorFlow code without the overhead of distributed coordination.
   - Use smaller datasets or subsamples to speed up iterations.
   - Validate that the model runs correctly end-to-end.

2. **Confirm that the model trains correctly** on a single node before distributing.

### Stage 2: Multi-Node Integration

3. **Add HorovodRunner for distributed training** once the single-node model is working.

### Stage 3: Production Tuning

4. **Scale up and tune hyperparameters** in a distributed setting.

## Best Practices

- **Debug with small data first**: Use a subset of the training data or a smaller dataset to validate correctness before running on full data. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]
- **Use reproducible seeds**: Set random seeds for reproducibility across runs, especially when comparing single-node vs. distributed results.
- **Monitor worker resources**: Ensure each worker has enough GPU memory; HorovodRunner's allreduce operations can be memory-intensive.

## Example: MNIST with HorovodRunner

The source notebook demonstrates the full workflow using the [MNIST Dataset](/concepts/mnist-dataset.md) with TensorFlow and Keras. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
