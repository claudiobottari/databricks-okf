---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb19f2637b2715a5a460655b752504ee841caa1469d9b7a91655d1db881127ab
  pageDirectory: concepts
  sources:
    - ai-runtime-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ai-runtime-hardware-options
    - ARHO
    - Hardware options
    - hardware options
  citations:
    - file: ai-runtime-databricks-on-aws.md
title: AI Runtime Hardware Options
description: The supported GPU accelerators for AI Runtime, currently limited to A10 and H100 types, each provisioned on a single node with a specific number of GPUs depending on the accelerator type.
tags:
  - databricks
  - gpu
  - hardware
  - infrastructure
timestamp: "2026-06-19T08:56:48.913Z"
---

# AI Runtime Hardware Options

**AI Runtime Hardware Options** refers to the set of GPU accelerators available for serverless deep learning workloads on [AI Runtime](/concepts/ai-runtime.md), the Databricks compute offering for deep learning. Hardware is provisioned as a single node per accelerator type, with the number of GPUs varying by accelerator. ^[ai-runtime-databricks-on-aws.md]

## Available Accelerators

AI Runtime supports the following accelerator types, each provisioning a single node with the number of GPUs and total GPU memory shown below: ^[ai-runtime-databricks-on-aws.md]

| Accelerator | GPUs | Total GPU Memory |
|-------------|------|------------------|
| 1× A10      | 1    | 24 GB            |
| 4× A10      | 4    | 96 GB            |
| 1× H100     | 1    | 80 GB            |
| 8× H100     | 8    | 640 GB           |

The 1× H100 accelerator is in **Beta**. A workspace admin must enable the "AI Runtime Beta Feature" preview from the **Previews** page before it can be used. ^[ai-runtime-databricks-on-aws.md]

## Supported Accelerators

Only NVIDIA A10 and H100 accelerators are supported by AI Runtime. ^[ai-runtime-databricks-on-aws.md]

## Use Cases

The A10 and H100 accelerators are well-suited for custom model training involving deep learning, including:

- LLM fine-tuning (LoRA, QLoRA, full fine-tuning)
- Computer vision (object detection, image classification)
- Deep-learning-based recommender systems
- Reinforcement learning
- Deep-learning-based time series forecasting

^[ai-runtime-databricks-on-aws.md]

## Requirements

- Workspace must be in one of the following AWS regions: `us-west-2`, `us-west-1`, `us-east-1`, `us-east-2`, `ca-central-1`, `sa-east-1`.
- AI Runtime preview must be enabled via workspace admin settings.
- The 1× H100 accelerator additionally requires the AI Runtime Beta Feature preview to be enabled. ^[ai-runtime-databricks-on-aws.md]

## Limitations

- AI Runtime **only** supports A10 and H100 accelerators.
- AI Runtime is **not supported for compliance security profile workspaces** (such as HIPAA or PCI). Processing regulated data is not supported.
- Maximum runtime for any workload is seven days. For longer training, implement checkpointing and restart jobs.
- GPU capacity may be constrained or unavailable during periods of high demand. AI Runtime may leverage cross-region GPUs in such cases, incurring possible egress costs and network limitations. ^[ai-runtime-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The overarching compute offering for deep learning on Databricks.
- [GPU Accelerators](/concepts/gpu-accelerated-xgboost-training.md) – General GPU hardware types available in Databricks.
- [Deep Learning on Databricks](/concepts/deep-learning-on-databricks.md) – Best practices for training and tuning models.
- Serverless Compute – The serverless architecture powering AI Runtime.
- H100 GPU / A10 GPU – Specific GPU models used.

## Sources

- ai-runtime-databricks-on-aws.md

# Citations

1. [ai-runtime-databricks-on-aws.md](/references/ai-runtime-databricks-on-aws-a734dca1.md)
