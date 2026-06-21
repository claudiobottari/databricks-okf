---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1ed4adc089b9ca03e5fd76db7b7181a3b2d05bcd4a2f668096701b25eddd3091
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchrec-embeddingbagcollection
    - EmbeddingBagCollection
    - EmbeddingBagConfig
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: TorchRec EmbeddingBagCollection
description: TorchRec module that manages multiple EmbeddingBag tables for large-scale categorical features, pooling sparse features into dense embeddings for downstream neural networks.
tags:
  - pytorch
  - recommender-systems
  - embeddings
timestamp: "2026-06-19T18:34:37.858Z"
---

---

title: TorchRec EmbeddingBagCollection
summary: A TorchRec module that manages a collection of embedding bags for large-scale sparse features in recommendation models, configured with a list of EmbeddingBagConfig objects.
sources:
  - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:31:13.893Z"
updatedAt: "2026-06-19T10:16:48.120Z"
tags:
  - torchrec
  - recommender-systems
  - embeddings
aliases:
  - torchrec-embeddingbagcollection
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# TorchRec EmbeddingBagCollection

**TorchRec `EmbeddingBagCollection`** is a component from the TorchRec library that manages a collection of embedding bags for large-scale recommendation models. It efficiently handles sparse features with high cardinality by leveraging optimized GPU kernels and is designed for distributed training. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Overview

`EmbeddingBagCollection` takes a list of `EmbeddingBagConfig` objects and a device specification. Each `EmbeddingBagConfig` defines an embedding table with a unique name, embedding dimension, number of embeddings, and the names of the features that will be looked up in that table. The collection provides a forward pass that accepts a KeyedJaggedTensor and returns pooled embeddings for each configured feature. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Usage in a Two‑Tower Model

In the two‑tower recommendation model example, the collection is created with two `EmbeddingBagConfig`s – one for user IDs and one for movie IDs – both sharing the same embedding dimension. The assertion `len(embedding_bag_collection.embedding_bag_configs()) == 2` enforces that exactly two embedding bags are present. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

The typical creation pattern from the source code is:

```python
from torchrec.modules.embedding_configs import EmbeddingBagConfig
from torchrec.modules.embedding_modules import EmbeddingBagCollection

eb_configs = [
    EmbeddingBagConfig(
        name=f"t_{feature_name}",
        embedding_dim=args.embedding_dim,
        num_embeddings=emb_counts[feature_idx],
        feature_names=[feature_name],
    )
    for feature_idx, feature_name in enumerate(cat_cols)
]

ebc = EmbeddingBagCollection(tables=eb_configs, device=device)
```

The collection is then passed into the `TwoTowerModel`, where the forward method calls `self.ebc(kjt)` to obtain pooled embeddings. These embeddings are split into query and candidate towers via separate projection MLPs. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Integration with PyTorch Lightning

`EmbeddingBagCollection` is used inside a `LightningModule` (e.g., `LitTwoTower`). The Lightning module creates the collection, wraps it in a `TwoTowerModel`, and handles batch transformation from plain dictionaries to the `KeyedJaggedTensor` format required by the collection. For consistent multi‑GPU training, the optimizer is created via `KeyedOptimizerWrapper` using the model’s named parameters. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## EmbeddingBagConfig

Each `EmbeddingBagConfig` requires:

- `name` – a unique identifier for the embedding table.
- `embedding_dim` – the dimensionality of the output embeddings.
- `num_embeddings` – the number of distinct IDs in the table (e.g., number of users or movies).
- `feature_names` – the names of the sparse features that will be looked up in this table.

Both configs in a two‑tower model must have the same `embedding_dim`. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) – The model architecture that uses `EmbeddingBagCollection`.
- [EmbeddingBagConfig](/concepts/torchrec-embeddingbagcollection.md) – Configuration for a single embedding table.
- KeyedJaggedTensor – Sparse data format consumed by `EmbeddingBagCollection`.
- TorchRec – The library providing large‑scale recommendation primitives.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – The training framework used to orchestrate distributed training with the collection.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – How the model is scaled across multiple GPUs.

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
