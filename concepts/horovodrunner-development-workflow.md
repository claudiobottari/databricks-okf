---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d173f9b16ae4d399f5313294ce2dee926bc928eb7991b87051248bbf3ca91310
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodrunner-development-workflow
    - HDW
    - Development Workflow
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: HorovodRunner development workflow
description: The recommended workflow for developing distributed deep learning models using HorovodRunner on Databricks.
tags:
  - workflow
  - deep-learning
  - databricks
timestamp: "2026-06-19T18:19:10.953Z"
---

# HorovodRunner Development Workflow

**HorovodRunner development workflow** is the recommended approach for building distributed deep learning models on Databricks using [HorovodRunner](/concepts/horovodrunner.md). This workflow is demonstrated in an example notebook that applies TensorFlow and Keras to the MNIST dataset. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Overview

The recommended development workflow is illustrated by a notebook that walks through the process of adapting a single‑node TensorFlow/Keras model for distributed training with HorovodRunner. The notebook serves as a concrete guide for applying the workflow. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Prerequisites

Before running the notebook, data must be prepared for distributed training. The specific data preparation steps are part of the notebook’s setup. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — Databricks wrapper for running Horovod training jobs on Spark clusters.
- [Horovod](/concepts/horovod.md) — Distributed deep learning framework supporting TensorFlow, Keras, and PyTorch.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General techniques for training models across multiple GPUs.
- TensorFlow with Horovod — Using Horovod with TensorFlow and Keras.

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
