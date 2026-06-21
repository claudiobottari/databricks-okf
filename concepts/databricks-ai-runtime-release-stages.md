---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6673bbf71e418023081925941364eb9f932c4eb7181ee5ec59a876fa7c2a5c31
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-release-stages
    - DARRS
    - Databricks Runtime ML Release Notes
    - Databricks Runtime ML release notes
    - Databricks Runtime Release Notes
    - Databricks Runtime release notes
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: Databricks AI Runtime release stages
description: "AI Runtime features are released in different stages: single-node tasks in Public Preview, multi-GPU distributed training in Beta."
tags:
  - databricks
  - release-management
  - machine-learning
timestamp: "2026-06-18T11:46:10.766Z"
---

# Databricks AI Runtime Release Stages

**Databricks AI Runtime** is a Databricks-managed ML runtime that provides pre-configured deep learning and distributed training environments for building and deploying machine learning models, including recommender systems, [large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md), and other AI workloads. The runtime is offered in different release stages depending on the workload type and scale.

## Release Stages

| Stage | Description | Scope |
|-------|-------------|-------|
| **Public Preview** | Generally available for evaluation and early adoption; covered by Databricks Terms of Service but not subject to SLA guarantees | Single-node tasks |
| **Beta** | Early access feature; available for testing; may have known limitations and is subject to change | Distributed training API for multi-GPU workloads |

^[deep-learning-based-recommender-systems-databricks-on-aws.md]

### Public Preview

The **Public Preview** stage applies to AI Runtime when used for **single-node tasks**. In this stage, the runtime is fully functional and ready for use. It is covered by the Databricks Terms of Service. However, it may not be subject to full service-level agreement (SLA) guarantees until it reaches General Availability (GA).

### Beta

The **Beta** stage applies specifically to the **distributed training API** when used for **multi-GPU (multi-node) workloads**. This includes features for scaling training across multiple GPUs. In the Beta stage, the API is available for testing and early adoption but may have known limitations or undergo changes before reaching GA.

## Scope of Each Stage

The release stage for AI Runtime depends on the workload type:

- **Single-node tasks** (AI Runtime): **Public Preview**
- **Multi-GPU workloads** (distributed training API): **Beta**

^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – Databricks managed ML runtime
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – Training across multiple GPUs/workers
- GPU-accelerated computation – GPU-based ML workloads
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – Framework used for distributed training in examples
- Recommender systems – Example use case for AI Runtime

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
