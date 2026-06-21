---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 31ee093950895785b8ea7c8993077269d21d430af8cd4a115e2ba97f932fafe2
  pageDirectory: concepts
  sources:
    - distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - learning-from-sets-dataset-grouplens
    - LFSD(
  citations:
    - file: distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md
title: Learning from Sets Dataset (GroupLens)
description: A movie rating dataset from GroupLens (Learning from Sets 2019) used for training the two-tower recommendation model, preprocessed with label binarization.
tags:
  - dataset
  - recommender-systems
  - benchmark
timestamp: "2026-06-19T10:16:48.623Z"
---

# Learning from Sets Dataset (GroupLens)

The **Learning from Sets Dataset** is a publicly available recommendation dataset published by GroupLens. It is distributed as a ZIP archive containing CSV files of item ratings and is commonly used for evaluating recommendation algorithms, including [two tower models](/concepts/two-tower-recommendation-model.md). ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Access

The dataset can be downloaded from the GroupLens website at:
```
https://files.grouplens.org/datasets/learning-from-sets-2019/learning-from-sets-2019.zip
```
^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Contents

The ZIP archive includes a CSV file `item_ratings.csv` with columns for user ID (`userId`), movie ID (`movieId`), and rating (`rating`). ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Typical Usage

The dataset is suitable for building and evaluating recommendation systems. In common preprocessing pipelines, ratings are binarized (e.g., based on the mean rating) to create binary labels for implicit feedback tasks. The resulting data is then split into training, validation, and test sets. ^[distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md]

## Related Concepts

- GroupLens – Research group that publishes this and other movie rating datasets.
- [Two Tower Model](/concepts/two-tower-recommendation-model.md) – A common deep learning architecture for recommendation that uses this dataset.
- Recommendation System – The broader domain for which this dataset is designed.
- Item Ratings Dataset – General category of datasets with user-item rating matrices.

## Sources

- distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md

# Citations

1. [distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws.md](/references/distributed-training-of-two-tower-recommendation-model-using-lightning-databricks-on-aws-093d5979.md)
