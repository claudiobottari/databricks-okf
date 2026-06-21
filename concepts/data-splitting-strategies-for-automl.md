---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21d6b226135c14ba281b13704b9c60ac75c10cb8864918e3d49ba326b3dbe99d
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-splitting-strategies-for-automl
    - DSSFA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Data Splitting Strategies for AutoML
description: "Methods to divide data into training, validation, and test sets in AutoML: random split (default, 60/20/20), chronological split (by time column), and manual split (by designated split column)."
tags:
  - automl
  - data-splitting
  - train-test-split
timestamp: "2026-06-19T18:06:18.970Z"
---

---

title: Data Splitting Strategies for AutoML
summary: "Methods for partitioning data into train/validation/test sets in Databricks AutoML: random split (stratified for classification, simple for regression), chronological split by time column, and manual split using a designated column."
sources:
  - data-preparation-for-classification-databricks-on-aws.md
  - data-preparation-for-regression-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:59:42.024Z"
updatedAt: "2026-06-19T09:42:40.624Z"
tags:
  - databricks
  - automl
  - data-splitting
  - train-test-split
  - regression
aliases:
  - data-splitting-strategies-for-automl
  - DSSFA
confidence: 1
provenanceState: extracted
inferredParagraphs: 2

---

# Data Splitting Strategies for AutoML

**Data Splitting Strategies for AutoML** describe how AutoML divides a dataset into training, validation, and test sets before model training and evaluation. The choice of split strategy affects model performance, especially for time-series data or imbalanced classification problems. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Supported Split Methods

AutoML supports three methods for splitting data, configurable in the UI or via the [AutoML Python API reference|AutoML Python API](/concepts/automl-python-api.md). The same options are available for both classification and regression problems. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

### Random Split (Default) ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

If no data split strategy is specified, the dataset is randomly divided into:

- **60%** training set
- **20%** validation set
- **20%** test set ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

For classification problems, a **stratified random split** is used to ensure that each class is adequately represented in all three splits. ^[data-preparation-for-classification-databricks-on-aws.md] For regression problems, the random split is a simple random split without stratification. ^[data-preparation-for-regression-databricks-on-aws.md]

### Chronological Split ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

Available in Databricks Runtime 10.4 LTS ML and above, this method uses a **time column** (timestamp, integer, or string) to order the data:

- The earliest data points become the training set.
- The next earliest become the validation set.
- The latest points become the test set. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

This is appropriate for forecasting or any problem where temporal ordering matters.

### Manual Split ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

Available in Databricks Runtime 15.3 ML and above (API only). Users specify a **split column** containing the values `train`, `validate`, or `test` to assign each row to a specific partition. Rows with other values are ignored and a corresponding alert is raised. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Sampling Large Datasets ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

AutoML automatically estimates the memory required to load and train a dataset and samples the data if necessary. The sampling method differs by problem type:

- **Classification**: Uses PySpark's `sampleBy` method for stratified sampling, preserving the target label distribution. ^[data-preparation-for-classification-databricks-on-aws.md]
- **Regression**: Uses PySpark's `sample` method (random sampling). ^[data-preparation-for-regression-databricks-on-aws.md]

Each model is trained on a single worker node, although hyperparameter tuning trials are distributed across the cluster. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- [AutoML for Classification](/concepts/automl-classification-classify.md)
- [AutoML for Regression](/concepts/automl-regress.md)
- [Data Preparation for Classification](/concepts/automl-data-preparation-for-classification.md)
- Data Preparation for Regression
- [Imbalanced Dataset Handling](/concepts/imbalanced-dataset-handling.md)
- [Semantic Type Detection](/concepts/semantic-type-detection.md)
- PySpark DataFrame Sampling

## Sources

- data-preparation-for-classification-databricks-on-aws.md
- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
2. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
