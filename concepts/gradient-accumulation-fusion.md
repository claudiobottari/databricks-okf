---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1d2cb22a49a47e1771a3ee5792a9acc8391fd1fdb4e051552ed0498ea86ed6be
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gradient-accumulation-fusion
    - GAF
    - Gradient Accumulation
    - Gradient accumulation
    - gradient accumulation
    - accumulators
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: Gradient Accumulation Fusion
description: A DeepSpeed feature that fuses gradient accumulation steps to improve training efficiency and throughput
tags:
  - machine-learning
  - optimization
  - deep-speed
timestamp: "2026-06-19T18:36:12.999Z"
---


# Gradient Accumulation Fusion

**Gradient Accumulation Fusion** is an advanced memory optimization technique provided by [DeepSpeed](/concepts/deepspeed.md) for distributed training. It is listed as one of the additional features available in DeepSpeed beyond standard [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), alongside [CPU Offloading](/concepts/cpu-offloading.md) and ZeRO-stage optimizations. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## When to Use

DeepSpeed recommends using gradient accumulation fusion when you need advanced memory optimization beyond standard FSDP. It is particularly suited for large language models in the 1B to 100B+ parameter range and can be combined with ZeRO Stage 1, 2, or 3 and CPU offloading. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Related Concepts

- [DeepSpeed](/concepts/deepspeed.md)
- [ZeRO (Zero Redundancy Optimizer)](/concepts/zero-zero-redundancy-optimizer.md)
- [CPU Offloading](/concepts/cpu-offloading.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md)

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
