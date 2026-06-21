---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 54c2c8345690490a7e3f2333a50f491a968dff3aa7355805fc20ed3d876036af
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sampling-large-datasets-for-automl
    - SLDFA
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Sampling Large Datasets for AutoML
description: Automatic memory-based sampling of large datasets in AutoML, using stratified sampling for classification (sampleBy) and simple sampling for regression (sample).
tags:
  - automl
  - large-data
  - sampling
timestamp: "2026-06-19T18:06:18.911Z"
---

# Sampling Large Datasets for AutoML

**Sampling Large Datasets for AutoML** refers to the automatic data subsetting technique that Databricks AutoML applies when training datasets are too large to fit in the memory of a single worker node. Although AutoML distributes hyperparameter tuning trials across the worker nodes of a cluster, each individual model is trained on a single worker node. To accommodate this constraint, AutoML automatically estimates the memory required to load and train your dataset and samples the dataset if necessary. ^[data-preparation-for-regression-databricks-on-aws.md]

## Sampling Strategy by Problem Type

The sampling method AutoML uses depends on the type of machine learning problem:

- **For classification problems**: AutoML uses the PySpark `sampleBy` method for stratified sampling. This approach preserves the target label distribution in the sampled subset, ensuring that rare classes remain proportionally represented. ^[data-preparation-for-regression-databricks-on-aws.md]
- **For regression problems**: AutoML uses the PySpark `sample` method. Unlike classification, regression sampling does not require stratified sampling to preserve a label distribution. ^[data-preparation-for-regression-databricks-on-aws.md]

## When Sampling Is Triggered

AutoML estimates the memory footprint required to load and train a given dataset. If that estimate exceeds the available memory on a single worker node, AutoML automatically applies sampling to reduce the dataset size. This sampling occurs before any training trial begins. ^[data-preparation-for-regression-databricks-on-aws.md]

## User Control Over Sampling

You can influence sampling behavior through the AutoML UI or API. For example, you can specify which columns to include or exclude (excluding columns reduces memory pressure and may avoid sampling). For regression problems, you can also configure the impute missing values method or choose a [data split strategy](/concepts/data-splitting-strategies.md) (random, chronological, or manual), which may change the size of the training subset. ^[data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- [AutoML on Databricks](/concepts/automl-on-databricks.md) – Overview of the automated machine learning pipeline.
- Data preparation for regression – Full guide for configuring regression data in AutoML.
- [Data preparation for classification](/concepts/automl-data-preparation-for-classification.md) – Equivalent guide for classification data.
- PySpark sampleBy – Stratified sampling method used for classification.
- PySpark sample – Uniform sampling method used for regression.
- [Single-node training](/concepts/single-node-gpu-training-on-databricks.md) – The limitation on which AutoML's sampling is based.
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) – The distributed search that AutoML runs alongside sampling.

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
