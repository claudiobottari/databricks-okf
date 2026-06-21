---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e95e05abea1e3731fab706494f476ebf5b1e9be758ee9419990c44504d014d08
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-lightning-for-distributed-training
    - PLFDT
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
title: PyTorch Lightning for Distributed Training
description: A lightweight PyTorch wrapper used for scaling deep learning model training across multiple GPUs in a distributed setting, demonstrated here for recommendation models.
tags:
  - pytorch
  - distributed-training
  - deep-learning
  - framework
timestamp: "2026-06-19T18:18:46.180Z"
---

```yaml
---
title: PyTorch Lightning for Distributed Training
summary: PyTorch Lightning is used as the framework for distributed training of recommendation models in the Databricks AI Runtime environment.
sources:
  - deep-learning-based-recommender-systems-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:46:10.419Z"
updatedAt: "2026-06-19T14:58:04.651Z"
tags:
  - pytorch
  - distributed-training
  - deep-learning
aliases:
  - pytorch-lightning-for-distributed-training
  - PLFDT
confidence: 0.85
provenanceState: extracted
inferredParagraphs: 0
---

# PyTorch Lightning for Distributed Training

**PyTorch Lightning** is a lightweight wrapper around PyTorch that simplifies the training loop and enables scaling to multi‑GPU and multi‑node environments. On Databricks, PyTorch Lightning is used for distributed training of recommendation models, as demonstrated in the two‑tower recommendation model tutorial. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

The underlying infrastructure for these workloads is [[AI Runtime]]. Single‑node PyTorch Lightning tasks run on AI Runtime under **Public Preview**, while multi‑GPU distributed training workloads use the distributed training API, which remains in **Beta**. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

The two‑tower recommendation model example ([Two-Tower Recommendation Model]) shows how to leverage PyTorch Lightning to scale training across multiple GPUs, enabling efficient training of deep learning recommendation models in a distributed manner. ^[deep-learning-based-recommender-systems-databricks-on-aws.md]

## Related Concepts

- [[AI Runtime]]
- [[Two-Tower Recommendation Model]]
- [[Distributed Data Parallel (DDP)]]
- [[Fully Sharded Data Parallel (FSDP)]]

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md
```

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
