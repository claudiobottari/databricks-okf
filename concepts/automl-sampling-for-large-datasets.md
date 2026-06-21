---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 530a4816ee5278da81758393da4d874d365cae267d355fa4ddba177ffbd05104
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-sampling-for-large-datasets
    - ASFLD
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: AutoML Sampling for Large Datasets
description: Automatic memory-aware dataset sampling in AutoML, using stratified sampling for classification and random sampling for regression.
tags:
  - machine-learning
  - automl
  - scalability
timestamp: "2026-06-19T14:42:01.197Z"
---

# AutoML Sampling for Large Datasets

**AutoML Sampling for Large Datasets** refers to the automatic data sampling mechanism in Databricks AutoML that reduces dataset size when necessary to fit within the memory constraints of a single worker node during model training. This sampling is essential because, although AutoML distributes hyperparameter tuning trials across worker nodes, each individual model is trained on a single worker node. ^[data-preparation-for-regression-databricks-on-aws.md]

## Overview

When training machine learning models with AutoML, the framework automatically estimates the memory required to load and train a given dataset. If the estimated memory requirement exceeds the available memory on a single worker node, AutoML samples the dataset to reduce its size. This sampling occurs transparently to the user, allowing model training to proceed without manual intervention. ^[data-preparation-for-regression-databricks-on-aws.md]

## Sampling Methods

AutoML uses different sampling strategies depending on the type of machine learning problem:

- **For classification problems:** AutoML uses the PySpark `sampleBy` method for stratified sampling. This approach preserves the target label distribution in the sampled dataset, ensuring that rare classes remain proportionally represented. ^[data-preparation-for-regression-databricks-on-aws.md]

- **For regression problems:** AutoML uses the PySpark `sample` method, which performs random sampling without stratification. ^[data-preparation-for-regression-databricks-on-aws.md]

## Relationship to Data Splitting

Sampling for large datasets is distinct from the data splitting strategies AutoML uses to create train, validation, and test sets. While data splitting divides the full dataset into partitions for model development and evaluation, sampling reduces the overall dataset size before that splitting occurs. ^[data-preparation-for-regression-databricks-on-aws.md]

The available data splitting methods — random split (default), [chronological split](/concepts/chronological-data-splitting-in-automl.md), and manual split — all operate on the dataset after any necessary sampling has been applied. ^[data-preparation-for-regression-databricks-on-aws.md]

## Limitations

- Each model trained by AutoML runs on a single worker node, making the memory capacity of that node the practical upper bound for dataset size without sampling. ^[data-preparation-for-regression-databricks-on-aws.md]
- While hyperparameter tuning is distributed across worker nodes, the sampling decision is per-model and therefore does not benefit from the full cluster's aggregate memory. ^[data-preparation-for-regression-databricks-on-aws.md]
- Users cannot directly disable sampling or configure sample size through the AutoML UI or API; the framework handles it automatically. ^[data-preparation-for-regression-databricks-on-aws.md]

## Best Practices

- **Monitor cluster size:** If AutoML samples frequently, consider using a worker node type with more memory to accommodate the full dataset.
- **Pre-sample manually:** For very large datasets, consider pre-sampling or aggregating data before passing it to AutoML to maintain control over the sampling strategy.
- **Review trial outputs:** Sampled datasets may produce models with different characteristics than those trained on the full dataset, particularly for imbalanced classification problems where stratified sampling may alter feature distributions.

## Related Concepts

- AutoML Regression Data Preparation — Configurable data settings for regression training
- [AutoML Classification](/concepts/automl-classification-classify.md) — Classification-specific AutoML behavior, including stratified sampling
- PySpark Sampling Methods — The underlying `sampleBy` and `sample` APIs used by AutoML
- [Train-Validation-Test Split](/concepts/trainvalidationsplit.md) — How AutoML partitions data for model evaluation
- [Supported Feature Types in AutoML](/concepts/supported-feature-types-in-automl.md) — Data types that AutoML accepts for training

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
