---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08af85faac2a21f2b6cbe744795b4d2d12b8f9014372a392f9e4c9fb84080a25
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-training-api-databricks
    - DTA(
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Distributed training API (Databricks)
description: A Beta API for multi-GPU distributed training workloads on Databricks, scoped to the Serverless GPU API.
tags:
  - databricks
  - distributed-training
  - multi-gpu
timestamp: "2026-06-18T14:23:32.225Z"
---

---
title: Distributed training API (Databricks)
summary: A Beta API within AI Runtime for scaling deep learning training across multiple GPUs and nodes using the Serverless GPU API.
sources:
  - ai-runtime-example-notebooks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - distributed-training
  - ai-runtime
  - multi-gpu
  - databricks
aliases:
  - distributed-training-api-databricks
  - DTAD
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Distributed training API (Databricks)

The **Distributed training API** is a component of [AI Runtime](/concepts/ai-runtime.md) that supports scaling deep learning workloads across multiple GPUs and nodes. As of the current release, this API remains in **Beta**. In contrast, the single-node task functionality of AI Runtime is in Public Preview. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

The distributed training API is designed for multi-GPU workloads, enabling users to train models such as large language models, computer vision models, and recommender systems across multiple accelerators. It leverages the **Serverless GPU API** to orchestrate training. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

Example notebooks demonstrating multi-GPU distributed training are available in the AI Runtime documentation. These examples cover scaling training across multiple GPUs and nodes. The API is intended for users who need to accelerate training by distributing the workload, rather than relying on a single GPU. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Status and Availability

The distributed training API is in **Beta**. Databricks recommends using it with awareness of its pre‑production status. AI Runtime for single‑node tasks is in Public Preview. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) — The runtime environment that hosts both single-node and distributed training capabilities.
- Multi-GPU training — The broader concept of distributing model training across multiple GPUs.
- [Serverless GPU API](/concepts/serverless-gpu-api.md) — The underlying compute API used by the distributed training API.
- [Large language models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — One of the typical use cases for distributed training.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
