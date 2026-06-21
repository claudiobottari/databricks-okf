---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55248c5e5bd47cd8679c1e82100ef3f694013193f8cba05839e6c985aebfb3e7
  pageDirectory: concepts
  sources:
    - deep-learning-based-recommender-systems-databricks-on-aws.md
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - two-tower-recommendation-model
    - TRM
    - Two‑Tower Recommendation Model
    - Two‑tower recommendation model
    - Two Tower Model
    - Two-Tower Model
    - Two-tower model
    - Two-tower models
    - TwoTowerModel
    - two tower models
    - two-tower models
  citations:
    - file: deep-learning-based-recommender-systems-databricks-on-aws.md
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
    - file: train-recommender-models-databricks-on-aws.md
title: Two-Tower Recommendation Model
description: A deep learning architecture for recommendation systems that uses two separate neural network towers (one for queries/users, one for items/candidates) to learn embeddings for matching.
tags:
  - deep-learning
  - recommendation-systems
  - model-architecture
timestamp: "2026-06-19T18:19:04.543Z"
---

Here is the updated wiki page for "Two-Tower Recommendation Model", incorporating the new source material and following your formatting requirements.

---

# Two-Tower Recommendation Model

The **Two-Tower Recommendation Model** is a deep neural network architecture for large-scale personalization and retrieval tasks. It processes user (query) data and item (candidate) data through two separate neural network "towers," each producing a dense embedding vector. These embeddings are then combined via a similarity measure, typically the dot product, to predict the likelihood of user-item interaction. ^[deep-learning-based-recommender-systems-databricks-on-aws.md, distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

Unlike larger reranking models like DLRM, the two-tower model is lightweight enough for the retrieval stage, efficiently scoring hundreds or thousands of candidates from a set of millions. This makes it well-suited for applications such as movie recommendations from a large catalog. ^[train-recommender-models-databricks-on-aws.md]

## Architecture

The two-tower model is composed of two independent sub-networks: a **query tower** (for users or context) and a **candidate tower** (for items). Each tower typically begins with an embedding lookup table, often implemented using TorchRec's `EmbeddingBagCollection`, which maps categorical features like user IDs and product IDs to dense vectors. These initial embeddings are then passed through a multi-layer perceptron (MLP) projection head to produce the final user and item embeddings. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

The interaction between the towers is computed as the sum of the element-wise product of the two output embeddings (equivalent to a dot product). A sigmoid activation is then applied to produce a binary prediction (e.g., positive or negative interaction). The model is most often trained with user ID and product ID as inputs and a binary label indicating a positive interaction. The architecture can be extended to support multiple sparse and dense feature vectors for both users and items. ^[train-recommender-models-databricks-on-aws.md, distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Training

Training is typically performed with [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) and TorchRec, often in a distributed fashion across multiple GPUs. On Databricks, the AI Runtime for single-node tasks is currently in **Public Preview**, while the distributed training API for multi-GPU workloads remains in **Beta**. A tutorial notebook demonstrates how to create a two-tower model using the PyTorch Lightning `Trainer` API with the `@distributed` decorator from the `serverless_gpu` library, enabling training across 8 H100 GPUs on a single node. ^[deep-learning-based-recommender-systems-databricks-on-aws.md, distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

The standard training workflow includes: installing necessary packages (e.g., TorchRec, FBGEMM), downloading and preparing a dataset (e.g., the Learning from Sets dataset), defining the model architecture, creating the training function, running distributed training, performing inference, and registering the model in [MLflow](/concepts/mlflow.md) for serving. To simplify inference serving, the model can be wrapped in an MLflow PyFunc. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Use Cases

Because the two-tower model produces separate embeddings for users and items, these embeddings can be stored in a vector index (e.g., Databricks AI Search) and used for similarity-search-based retrieval. For a given user, the system can query the vector store to find the top-N items whose embeddings are most similar to the user's embedding. This makes the model ideal for generating a large number of good-quality recommendations efficiently. ^[train-recommender-models-databricks-on-aws.md]

## Comparison with DLRM

The two-tower model and DLRM serve different stages of a recommendation funnel. The two-tower model acts as a lightweight retrieval model, capable of scanning millions of candidates quickly. In contrast, DLRM is a larger reranking model that can incorporate more dense features and provide fine-grained, highly specific recommendations. The choice between them depends on the trade-off between scale and precision: two-tower for breadth, DLRM for depth. ^[train-recommender-models-databricks-on-aws.md]

## Related Concepts

- DLRM
- TorchRec
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [Distributed training](/concepts/workload-yaml-for-distributed-training.md)
- [MLflow](/concepts/mlflow.md)
- Embedding
- [Retrieval-augmented generation](/concepts/retrieval-augmented-generation-rag.md)
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)

## Sources

- deep-learning-based-recommender-systems-databricks-on-aws.md
- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
- train-recommender-models-databricks-on-aws.md

# Citations

1. [deep-learning-based-recommender-systems-databricks-on-aws.md](/references/deep-learning-based-recommender-systems-databricks-on-aws-9c825c28.md)
2. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
3. [train-recommender-models-databricks-on-aws.md](/references/train-recommender-models-databricks-on-aws-b4714239.md)
