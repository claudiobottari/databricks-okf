---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c0971e37769539bcab1f0c1dd9f16db6486ac7638409e6ee03668e19d8d5505
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - imbalanced-dataset-handling
    - IDH
    - Imbalanced Dataset Support
    - Imbalanced dataset support
    - imbalanced-dataset-handling-in-automl
    - IDHIA
    - Imbalanced Dataset Support in AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Imbalanced Dataset Handling
description: AutoML's strategy for reducing class imbalance by downsampling majority classes and applying inverse class weights during training.
tags:
  - classification
  - imbalanced-learning
  - automl
  - databricks
timestamp: "2026-06-19T14:41:18.630Z"
---

# Imbalanced Dataset Handling

**Imbalanced dataset handling** refers to techniques used to address skewed class distributions in classification problems. In Databricks AutoML, when an imbalanced dataset is detected, the training dataset is automatically balanced through a combination of **downsampling the majority class(es)** and **adding class weights**, while leaving the test and validation datasets untouched to preserve the true input distribution for evaluation. ^[data-preparation-for-classification-databricks-on-aws.md]

## How AutoML Balances Imbalanced Data

This feature is available in Databricks Runtime 11.3 LTS ML and above. AutoML applies balancing only to the **training dataset** (not to test or validation sets). The goal is to avoid biasing model evaluation and to ensure performance is measured on the real-world class distribution. ^[data-preparation-for-classification-databricks-on-aws.md]

### Downsampling and Class Weight Calculation

AutoML reduces imbalance by downsampling the majority class(es) and using class weights that are inversely proportional to the downsampling ratio. For example, given a training dataset of 100 samples with 95 in class A and 5 in class B, AutoML downsamples class A to 70 samples (a ratio of 70/95 ≈ 0.736) while keeping class B at 5 samples. To maintain proper calibration of the model's probability output, AutoML then scales the class weight for class A by the inverse of the downsampling ratio (1/0.736 ≈ 1.358) while keeping class B weight at 1. These adjusted class weights are passed as a parameter during model training so that samples from each class are weighted appropriately. ^[data-preparation-for-classification-databricks-on-aws.md]

## Why Test/Validation Sets Are Not Balanced

Balancing is intentionally not applied to test and validation datasets. By evaluating on the original, non-enriched class distribution, the resulting model performance metrics reflect how the model will behave on real-world data where the class imbalance exists. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- AutoML — Automated machine learning pipeline that handles data preparation, including imbalance.
- [Classification](/concepts/data-classification.md) — Supervised learning task where imbalance commonly occurs.
- Class Weight — Technique to penalize misclassifications of minority classes more heavily.
- Downsampling — Reducing the number of samples from the majority class to balance the dataset.
- Imbalanced Data — Datasets where one class significantly outnumbers others.
- [Data Preparation for Classification](/concepts/automl-data-preparation-for-classification.md) — Broader topic covering imputation, column selection, and splitting.

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
