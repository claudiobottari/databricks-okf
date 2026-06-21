---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ec2777e07b257f53827ac7fafd1f2956d5f33bdd8abe6eb28df43d27ec75d31
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-splitting-strategies
    - DSS
    - Data Splitting
    - data split strategy
    - data-splitting-strategies-for-automl
    - DSSFA
    - data-splitting-strategies-in-automl
    - DSSIA
    - Split Strategies in AutoML
    - Data Splitting in AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Data Splitting Strategies
description: "Methods for splitting data into train, validation, and test sets: random stratified split, chronological split by time column, and manual split using a designated column."
tags:
  - data-splitting
  - train-test-split
  - automl
  - databricks
timestamp: "2026-06-19T14:41:21.483Z"
---

# Data Splitting Strategies

**Data Splitting Strategies** refer to the methods used to partition a dataset into distinct subsets — typically training, validation, and test sets — for the purpose of training and evaluating machine learning models. The choice of splitting strategy affects how well a model generalizes to unseen data and how reliably its performance can be measured.

## Overview

Proper data splitting helps prevent data leakage and ensures that model evaluation is unbiased. Depending on the type of machine learning problem and the structure of the data, different splitting strategies are appropriate. ^[data-preparation-for-classification-databricks-on-aws.md]

## Strategies

### Random Split

The default approach for many classification and regression tasks. The dataset is randomly divided into three subsets:

- **Training set:** 60% of the data
- **Validation set:** 20% of the data
- **Test set:** 20% of the data

For classification problems, a **stratified random split** ensures that each class is adequately represented in all three sets, preserving the original class proportions. ^[data-preparation-for-classification-databricks-on-aws.md]

### Chronological Split

When data has a temporal dimension — such as timestamps, dates, or integer time indicators — a chronological split can be used. The earliest data points form the training set, the next earliest form the validation set, and the most recent points form the test set. This approach is common in time-series forecasting and other sequential prediction tasks where the goal is to predict future events based on past observations. ^[data-preparation-for-classification-databricks-on-aws.md]

The time column can be a timestamp, integer, or string column. ^[data-preparation-for-classification-databricks-on-aws.md]

### Manual Split

A manual split allows the user to explicitly designate which rows belong to each subset. A separate **split column** is added to the dataset, with values `train`, `validate`, or `test` to label each row. Rows with any other value in the split column are ignored, and a corresponding alert is raised. ^[data-preparation-for-classification-databricks-on-aws.md]

This strategy is useful when the ideal split is known from domain knowledge or when external constraints (e.g., deployment schedules) dictate which data should be used for training versus testing.

## Related Concepts

- Training, Validation, and Test Sets
- Stratified Sampling
- Data Leakage
- [AutoML for Classification](/concepts/automl-classification-classify.md)
- Time-Series Forecasting

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
