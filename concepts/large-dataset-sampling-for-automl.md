---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8c8b6f6d0afc19d7673f64813f135e9d2ef8d4640f7568b791895fec1d7ae5e9
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - large-dataset-sampling-for-automl
    - LDSFA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Large Dataset Sampling for AutoML
description: AutoML's automatic memory estimation and stratified/random sampling of large datasets to fit single-worker-node training constraints.
tags:
  - sampling
  - scalability
  - automl
  - databricks
timestamp: "2026-06-19T14:41:29.443Z"
---

# Large Dataset Sampling for AutoML

**Large Dataset Sampling for AutoML** refers to the automatic data reduction technique used by Databricks AutoML when a dataset is too large to fit into the memory of a single worker node during model training. Although AutoML distributes hyperparameter tuning trials across worker nodes, each individual model is trained on a single worker node, which imposes memory constraints. ^[data-preparation-for-classification-databricks-on-aws.md]

## How AutoML Handles Large Datasets

AutoML automatically estimates the memory required to load and train the dataset. If the dataset exceeds the available memory on a single worker node, AutoML applies sampling to reduce the data size before training. The sampling strategy is chosen based on the type of machine learning problem: ^[data-preparation-for-classification-databricks-on-aws.md]

- **Classification**: AutoML uses PySpark’s `sampleBy` method, which performs stratified sampling. This ensures that the target label distribution in the sampled dataset closely matches the distribution in the original dataset, preserving class balance. ^[data-preparation-for-classification-databricks-on-aws.md]
- **Regression**: AutoML uses PySpark’s `sample` method, which performs simple random sampling without stratification, since there is no categorical target to preserve. ^[data-preparation-for-classification-databricks-on-aws.md]

This automatic sampling is applied transparently; users do not need to manually downsample their data before running an AutoML experiment.

## Implications for Model Performance

Because the model is trained on a sample rather than the full dataset, some information may be lost. However, for very large datasets, a representative sample often yields a model with comparable performance while drastically reducing training time and memory usage. Users should validate the final model on the full test or validation set (which is not sampled) to ensure generalization. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning on Databricks
- [Classification](/concepts/data-classification.md) — Target variable is categorical; stratified sampling applies
- [Regression](/concepts/automl-regress-api.md) — Target variable is continuous; simple random sampling applies
- PySpark sampleBy — Stratified sampling method for DataFrames
- PySpark sample — Random sampling method for DataFrames
- [Data preparation for classification](/concepts/automl-data-preparation-for-classification.md) — Full guide on data handling for classification AutoML
- [Imbalanced dataset support](/concepts/imbalanced-dataset-handling.md) — AutoML’s handling of class imbalance, which interacts with sampling decisions

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
