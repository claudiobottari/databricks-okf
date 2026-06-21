---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 616176cbaee1a1bbc5dceec8689d43d692420ad5345c52a688069c6c59847d28
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tensorflowdistributestrategy
    - TensorFlow Distributed Strategy
    - TensorFlow Distribution Strategies
    - TensorFlow distributed strategy
    - TensorFlow Strategy
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: tensorflow.distribute.Strategy
description: TensorFlow 2's native API for distributed training strategies, serving as the foundation for spark-tensorflow-distributor
tags:
  - tensorflow
  - distributed-training
  - api
timestamp: "2026-06-19T10:19:33.805Z"
---

---

title: tensorflow.distribute.Strategy
summary: TensorFlow 2's native API for distributed training strategies, providing the foundation for spark-tensorflow-distributor
sources:
  - distributed-training-with-tensorflow-2-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:08:45.584Z"
updatedAt: "2026-06-18T15:34:33.171Z"
tags:
  - tensorflow
  - distributed-training
  - api
aliases:
  - tensorflowdistributestrategy
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# tensorflow.distribute.Strategy

**`tensorflow.distribute.Strategy`** is a major feature of TensorFlow 2 that provides a native API for distributed training. It is the underlying API on which the open‑source package `spark-tensorflow-distributor` is built, enabling distributed training on Apache Spark clusters. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

`tensorflow.distribute.Strategy` is one of the major features introduced in TensorFlow 2. It serves as the core mechanism for distributing training across multiple devices and workers. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## In Spark Environments

The `spark-tensorflow-distributor` package is an open‑source, native TensorFlow package that helps users perform distributed training with TensorFlow on their Spark clusters. It is built directly on top of `tensorflow.distribute.Strategy`. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Related Concepts

- TensorFlow – The machine learning framework that provides the Strategy API.
- Apache Spark – The distributed computing engine on which `spark-tensorflow-distributor` runs.
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md) – General approaches to training models across multiple workers.
- [spark-tensorflow-distributor](/concepts/spark-tensorflow-distributor.md) – The Spark‑based package built on top of `tensorflow.distribute.Strategy`.

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
