---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4682c4806d54cd270e55af80411e04cd355d2d5ad0b6f43a8220ee715dbc38c9
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorflow-on-databricks
    - TOD
    - TensorFlow Installation on Databricks
  citations:
    - file: deep-learning-databricks-on-aws.md
title: TensorFlow on Databricks
description: Using TensorFlow and TensorBoard within Databricks Runtime ML for deep learning and general numerical computations on CPUs, GPUs, and GPU clusters.
tags:
  - tensorflow
  - deep-learning
  - databricks
timestamp: "2026-06-19T18:18:59.701Z"
---

```markdown
---
title: TensorFlow on Databricks
summary: Deep learning and numerical computation with TensorFlow and [[tensorboard-on-databricks|TensorBoard on Databricks]] Runtime ML, supporting CPUs, GPUs, and GPU clusters.
sources:
  - deep-learning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:00:00.000Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - tensorflow
  - deep-learning
  - databricks
aliases:
  - tensorflow-on-databricks
  - TOD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# TensorFlow on Databricks

**TensorFlow** is an open-source machine learning framework created by Google that supports deep learning and general numerical computations on CPUs, GPUs, and clusters of GPUs. On Databricks, TensorFlow is included in [[Databricks Runtime ML]] along with [[TensorBoard on Databricks|TensorBoard]], allowing you to use these libraries without installing any additional packages. ^[deep-learning-databricks-on-aws.md]

## Overview

Databricks Runtime ML includes TensorFlow and TensorBoard, so you can use these libraries without installing any packages. TensorFlow supports deep‑learning and general numerical computations on CPUs, GPUs, and clusters of GPUs. TensorBoard provides visualization tools to help you debug and optimize machine learning and deep learning workflows. ^[deep-learning-databricks-on-aws.md]

For single node and distributed training examples, see the dedicated [TensorFlow documentation](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorflow). ^[deep-learning-databricks-on-aws.md]

## Capabilities

TensorFlow on Databricks provides:

- **GPU‑accelerated tensor computation** for deep learning and general numerical operations. ^[deep-learning-databricks-on-aws.md]
- **TensorBoard integration** – the visualization tool is bundled with Databricks Runtime ML and can be used to debug and optimize training workflows. ^[deep-learning-databricks-on-aws.md]
- **Single‑node and distributed training** – you can perform single node training or distributed training with TensorFlow on Databricks. See [[Workload YAML for Distributed Training|Distributed training]] for examples using integrations with Ray, TorchDistributor, and DeepSpeed. ^[deep-learning-databricks-on-aws.md]

## Getting Started

Because TensorFlow is pre‑installed in Databricks Runtime ML, you can import it directly into a notebook or script:

```python
import tensorflow as tf
```

For an end‑to‑end tutorial notebook using TensorFlow, MLflow, and distributed training, refer to the official [TensorFlow page](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorflow). ^[deep-learning-databricks-on-aws.md]

## Tracking Experiments

Training runs are tracked using [[MLflow]], which is essential for the iterative nature of deep learning development. Databricks uses MLflow to track deep learning training runs and model development. See Track model development using MLflow for guidance. ^[deep-learning-databricks-on-aws.md]

## Related Concepts

- [[Deep learning on Databricks]] – broader overview of PyTorch, TensorFlow, and best practices.
- [[Databricks Runtime ML]] – the pre‑configured environment that includes TensorFlow.
- [[TensorBoard on Databricks|TensorBoard]] – visualization tool included in Databricks Runtime ML.
- [[Workload YAML for Distributed Training|Distributed training]] – techniques for scaling deep learning on Databricks.
- [[AI Runtime]] – serverless GPU option for deep learning workloads.
- [[PyTorch on Databricks]] – the other major deep learning framework available on Databricks.

## Sources

- deep-learning-databricks-on-aws.md
```

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
