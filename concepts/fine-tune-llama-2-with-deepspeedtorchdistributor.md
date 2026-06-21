---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 366c065d449b04d1e29816cfc88a50c0fc974251c4e2f579c5192cba888a1b97
  pageDirectory: concepts
  sources:
    - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fine-tune-llama-2-with-deepspeedtorchdistributor
    - FL2WD
  citations:
    - file: distributed-training-with-deepspeed-distributor-databricks-on-aws.md
title: Fine-tune Llama 2 with DeepSpeedTorchDistributor
description: An example notebook demonstrating fine-tuning of the Llama 2 7B Chat model using the DeepSpeedTorchDistributor on Databricks.
tags:
  - example
  - llama
  - fine-tuning
  - notebook
timestamp: "2026-06-18T15:33:56.453Z"
---

---

title: Fine-tune Llama 2 with DeepSpeedTorchDistributor
summary: Using the DeepSpeed distributor, built on TorchDistributor, to fine-tune Llama 2 models on Databricks, especially when GPU memory is limited.
sources:
  - distributed-training-with-deepspeed-distributor-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:00:00.000Z"
updatedAt: "2026-06-18T15:00:00.000Z"
tags:
  - deep-learning
  - distributed-training
  - deepspeed
  - llama-2
  - fine-tuning
  - databricks
aliases:
  - fine-tune-llama-2-with-deepspeedtorchdistributor
  - FTL2WDT
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Fine-tune Llama 2 with DeepSpeedTorchDistributor

**Fine-tune Llama 2 with DeepSpeedTorchDistributor** refers to the practice of using the [DeepSpeed](/concepts/deepspeed.md) distributor on Databricks to fine-tune Llama 2 language models. The DeepSpeed distributor is built on top of [TorchDistributor](/concepts/torchdistributor.md) and is recommended for customers whose models require higher compute power but are constrained by memory limitations. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Overview

The DeepSpeed library is an open-source library developed by Microsoft. It is available in Databricks Runtime 14.0 ML or above and offers optimized memory usage, reduced communication overhead, and advanced pipeline parallelism. These capabilities allow scaling of models and training procedures that would otherwise be unattainable on standard hardware. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

Fine-tuning a 7 billion parameter model like Llama 2 7B Chat is a typical use case. The DeepSpeed distributor addresses the memory and compute challenges that arise when training models of this size.

## When to Use DeepSpeedTorchDistributor

The DeepSpeed distributor is beneficial in the following scenarios ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]:

- **Low GPU memory** – When individual GPUs have insufficient memory to hold the model, gradients, and optimizer states.
- **Large model training** – For models with billions of parameters that cannot fit into a single GPU.
- **Large input data** – For tasks such as batch inference where the data volume is large.

## Example Notebook

Databricks provides an example notebook titled **Fine-tune Llama 2 7B Chat with DeepspeedTorchDistributor notebook**. This notebook demonstrates how to perform distributed training with the DeepSpeed distributor on a Llama 2 model. ^[distributed-training-with-deepspeed-distributor-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md) – The underlying optimization library.
- [TorchDistributor](/concepts/torchdistributor.md) – The base distributed training mechanism on Databricks.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General concepts for training models across multiple GPUs.
- Llama 2 – The open-source large language model family from Meta.
- Fine-tuning – The process of adapting a pre-trained model to a specific task.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime environment that includes DeepSpeed support.

## Sources

- distributed-training-with-deepspeed-distributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-deepspeed-distributor-databricks-on-aws.md](/references/distributed-training-with-deepspeed-distributor-databricks-on-aws-6ba03a5a.md)
