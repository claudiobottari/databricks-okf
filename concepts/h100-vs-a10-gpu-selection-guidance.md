---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1307c071c02e49e92bce5cd29e35540f36e198ce3dcae123440e73eb176b3cbd
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - h100-vs-a10-gpu-selection-guidance
    - HVAGSG
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: H100 vs A10 GPU Selection Guidance
description: "Guidance on when to use H100 GPUs over A10 GPUs: H100s are recommended for large model training requiring high throughput and large GPU memory due to larger FLOPS and HBM capacity."
tags:
  - gpu-selection
  - hardware-comparison
  - workload-optimization
timestamp: "2026-06-19T19:00:02.153Z"
---

# H100 vs A10 GPU Selection Guidance

**H100 vs A10 GPU Selection Guidance** provides criteria for choosing between NVIDIA H100 80GB HBM3 and A10 GPUs on Databricks Serverless GPU compute. The primary consideration is workload type: H100 GPUs are optimized for large model training, while A10 GPUs are better suited for inference and smaller-scale workloads.

## Overview

Databricks Serverless GPU compute offers both H100 and A10 GPU configurations. The choice between them depends on the computational requirements of the workload, particularly whether the task is training or inference, and the size of the model being used. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## H100 GPUs

H100 GPUs offer larger floating-point operations per second (FLOPS) and high-bandwidth memory (HBM) compared to A10 GPUs. They are recommended for large model **training** where high throughput and/or large GPU memory is needed. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

The 8xH100 single-node configuration provides eight NVIDIA H100 80GB HBM3 GPUs on a single compute node, delivering 640 GB of total GPU memory (8 × 80 GB) and substantial compute throughput for distributed training tasks. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### When to Use H100

- Large model training workloads
- Multi-GPU distributed training jobs
- Memory-intensive deep learning training tasks
- Workloads requiring high FLOPS and large HBM capacity

## A10 GPUs

A10 GPUs are the alternative option on Databricks Serverless GPU compute. While the source material does not provide detailed specifications for A10 GPUs, it establishes that H100s are the superior choice for training workloads due to their larger FLOPS and HBM. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### When to Use A10

Based on the guidance that H100s are for training, A10 GPUs are implicitly more appropriate for:
- Inference workloads
- Smaller model training that fits within A10 memory constraints
- Cost-sensitive workloads where H100 performance is not required

## Selection Decision Matrix

| Workload Type | Recommended GPU | Rationale |
|---|---|---|
| Large model training | H100 | Larger FLOPS and HBM for high throughput |
| Small model training | A10 | Sufficient for models that fit in A10 memory |
| Inference | A10 | Cost-effective for inference workloads |
| Memory-intensive training | H100 | 80 GB HBM3 per GPU provides ample capacity |

## Configuration Options

### H100 Configuration

To use H100 GPUs from a Databricks notebook:
1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab, select **8xH100** for your accelerator.
3. Choose the **AI v5** environment.
4. Click **Apply**.

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### A10 Configuration

A10 GPU configuration follows a similar process but selects the A10 accelerator option instead of 8xH100.

## Verification

Use the `nvidia-smi` command to confirm GPU type and configuration. H100 GPUs report as "NVIDIA H100 80GB HBM3" with 81,559 MiB of total memory and a maximum power draw of 700 W. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Detailed setup for H100 multi-GPU nodes
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure for on-demand GPU resources
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Common parallelism strategy for multi-GPU training
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for very large models
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md) — Typical workload for H100 GPUs

## Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
