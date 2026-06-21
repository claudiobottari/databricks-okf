---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4cf8dfd4102671fdbd411e508c6eb0802e938a0653f610d5330e0e941c2f2b9c
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - learning-from-sets-dataset-movielens
    - LFSD(
    - learning-from-sets-dataset-grouplens
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: Learning from Sets Dataset (MovieLens)
description: A public MovieLens-derived dataset used for training and evaluating recommendation models, preprocessed with rating binarization
tags:
  - datasets
  - recommender-systems
  - movielens
timestamp: "2026-06-18T15:31:42.272Z"
---

---
title: Learning from Sets Dataset (MovieLens)
summary: The Learning from Sets dataset (2019) from GroupLens, containing item ratings used for building a two-tower recommendation model with distributed training on Databricks.
sources:
  - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:09:03.358Z"
updatedAt: "2026-06-18T08:09:03.358Z"
tags:
  - group lens
  - dataset
  - recommender-system
  - movielens
aliases:
  - learning-from-sets-2019
  - item_ratings dataset
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Learning from Sets Dataset (MovieLens)

The **Learning from Sets Dataset** is a 2019 release from GroupLens that provides a collection of movie ratings. It is hosted at `https://files.grouplens.org/datasets/learning-from-sets-2019/` and distributed as a ZIP archive named `learning-from-sets-2019.zip`. The dataset is used to train recommender systems, most notably the [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) demonstrated in Databricks' distributed training examples. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Dataset Contents

Within the archive, the primary data file is `item_ratings.csv`, which contains rows with columns `userId`, `movieId`, and `rating`. In the Databricks example, the dataset is preprocessed by sorting and subsampling to 100,000 rows, encoding user IDs to contiguous integers, and binarizing ratings (converting them to 0 or 1 based on the mean rating). The processed DataFrame then contains `userId`, `movieId`, and `label` columns. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Usage in Distributed Training Example

The Databricks tutorial uses this dataset to illustrate distributed training of a two-tower recommendation model with [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) and TorchRec. After downloading and preprocessing, the data is split into training (70%), validation (21%), and test (9%) sets. The model is trained on 8 H100 GPUs using the `@distributed` decorator from the `serverless_gpu` Python library. The dataset's userId and movieId columns are treated as categorical features for embedding lookups, with embedding tables sized according to the number of unique users and movies present in the data. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- [Two-Tower Recommendation Model](/concepts/two-tower-recommendation-model.md) – The architecture trained on this dataset.
- GroupLens – The research lab that provides the dataset.
- MovieLens – The broader family of rating datasets from GroupLens.
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) – The framework used to define the training loop.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – The scale at which the model is trained (8 GPUs).

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
