---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6cedba4cd3610e500f202e9285ff2d4e701c65891ae07351f0c5f11661f2ac96
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sampling-large-datasets-in-automl
    - SLDIA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Sampling Large Datasets in AutoML
description: How AutoML handles large datasets by sampling, using stratified sampling for classification and simple sampling for regression to fit within single-node memory limits.
tags:
  - machine-learning
  - automl
  - sampling
timestamp: "2026-06-19T18:05:28.942Z"
---

# Sampling Large Datasets in AutoML

**Sampling Large Datasets in AutoML** is an automatic mechanism in Databricks AutoML that reduces the size of input datasets when they exceed the memory capacity of a single worker node, ensuring that each model training trial can complete within available resources.

## Overview

Although AutoML distributes hyperparameter tuning trials across the worker nodes of a cluster, each individual model is trained on a single worker node. When a dataset is too large to fit into the memory of a single worker, AutoML automatically estimates the memory required to load and train the dataset and samples the dataset to a manageable size. ^[data-preparation-for-classification-databricks-on-aws.md]

## Sampling Strategy by Problem Type

The sampling method differs based on the machine learning problem type:

- For **classification problems**, AutoML uses the PySpark `sampleBy` method for stratified sampling to preserve the target label distribution. This ensures that the relative frequencies of each class in the original dataset are maintained in the sampled subset. ^[data-preparation-for-classification-databricks-on-aws.md]
- For **regression problems**, AutoML uses the PySpark `sample` method, which performs simple random sampling without any stratification on the target variable. ^[data-preparation-for-classification-databricks-on-aws.md]

## Automatic Behavior

The sampling process is entirely automatic. AutoML determines whether sampling is necessary based on its own memory estimation and applies the appropriate PySpark method without user configuration. Users cannot directly control the sampling ratio or override the decision to sample. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning on Databricks
- [Data preparation for classification](/concepts/automl-data-preparation-for-classification.md) — Broader data preparation steps for classification problems
- Data preparation for regression — Broader data preparation steps for regression problems
- Stratified sampling — The technique used for classification to preserve class balance
- PySpark DataFrame sample — The PySpark API function used for random sampling
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — The distributed process that benefits from sampling to run more trials

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
