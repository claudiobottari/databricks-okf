---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fa19ba8b25d5e419a780d6df3c7e506e062516b8978f8d833cc6be40c29982bf
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-dataset-sampling
    - ADS
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: AutoML Dataset Sampling
description: Automatic stratified (classification) or random (regression) sampling of large datasets in Databricks AutoML to fit within single-worker-node memory limits.
tags:
  - machine-learning
  - data-preparation
  - automl
timestamp: "2026-06-18T11:29:05.276Z"
---

# AutoML Dataset Sampling

AutoML automatically adjusts the dataset size when memory constraints necessitate sampling, and optionally rebalances training data when class imbalance is detected. Sampling strategies differ by problem type and are configurable through experiment setup in the UI or the AutoML API. ^[data-preparation-for-classification-databricks-on-aws.md]

## Sampling for Large Datasets

Although AutoML distributes hyperparameter tuning trials across worker nodes, each model is trained on a single worker node. AutoML automatically estimates the memory required to load and train the dataset and samples the dataset if necessary. ^[data-preparation-for-classification-databricks-on-aws.md]

### Problem-Type‑Specific Sampling

- **Classification**: AutoML uses PySpark’s `sampleBy` method for stratified sampling to preserve the target label distribution in the sample. ^[data-preparation-for-classification-databricks-on-aws.md]
- **Regression**: AutoML uses PySpark’s `sample` method, which performs uniform random sampling without stratification. ^[data-preparation-for-classification-databricks-on-aws.md]

Sampling is applied only during training; validation and test sets remain unsampled to provide an unbiased evaluation of model performance.

## Imbalanced Dataset Support (Classification)

In Databricks Runtime 11.3 LTS ML and above, AutoML detects when a classification dataset is imbalanced and attempts to reduce the imbalance of the *training* dataset by downsampling the majority class(es) and adding class weights. Validation and test sets are not balanced; this ensures that model performance is always evaluated on the true input class distribution. ^[data-preparation-for-classification-databricks-on-aws.md]

### Downsampling Example

Consider a training dataset with 100 samples: 95 belong to class A and 5 belong to class B. AutoML reduces this imbalance by downsampling class A to 70 samples (a ratio of 70/95 ≈ 0.736) while keeping class B at 5 samples. To preserve correct model calibration and maintain the original probability distribution, AutoML scales up the class weight for class A by the inverse of the downsampling ratio (1/0.736 ≈ 1.358) while keeping the weight for class B as 1. These class weights are passed as a parameter during model training so that samples from each class are weighted appropriately. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- AutoML – Overview of automated machine learning on Databricks
- [Data preparation for classification](/concepts/automl-data-preparation-for-classification.md) – Broader data handling for classification experiments
- PySpark – Distributed data processing engine used for sampling
- Stratified sampling – Sampling method that preserves class proportions
- [Classification](/concepts/data-classification.md) – Problem type where stratified sampling is applied
- [Regression](/concepts/automl-regress-api.md) – Problem type where random sampling is applied

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
