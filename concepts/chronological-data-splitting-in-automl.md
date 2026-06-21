---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a972b670dcdaf54f1b87c1097158716c9e07ec38a9d555b8dab45ec5811d96a
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chronological-data-splitting-in-automl
    - CDSIA
    - chronological data split
    - chronological split
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: Chronological Data Splitting in AutoML
description: Using a time column to split data chronologically into training, validation, and test sets for classification and regression experiments, ensuring temporal order is preserved.
tags:
  - automl
  - data-preparation
  - time-series
timestamp: "2026-06-19T10:37:38.244Z"
---

Here is the wiki page for "Chronological Data Splitting in AutoML", written solely from the provided source material.

---

## Chronological Data Splitting in AutoML

**Chronological Data Splitting in AutoML** is a technique available in Databricks AutoML that splits time-series data into training, validation, and testing sets in chronological order. This approach ensures that the model is trained on past data and evaluated on future data, more accurately simulating real-world forecasting scenarios.

### Overview

When working with time-series data, it is critical to avoid "look-ahead bias" where a model is evaluated on data from a period preceding its training data. Chronological data splitting addresses this by using a specified time column to order the data and then dividing it sequentially. This is distinct from the random splitting used for non-temporal problems like classification or regression. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Configuration

This feature is enabled through the **Advanced Configuration (optional)** section of the AutoML experiment setup UI. The key step is selecting a **time column** that AutoML will use to determine the chronological order of the dataset. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Applicable Problem Types

This splitting method is specifically available for two problem types:

- **Classification** experiments, used to control the data split.
- **Regression** experiments, used to control the data split.

It is not described as an option for the [Forecasting with AutoML (classic compute)](/concepts/automl-forecasting-classic-compute.md) problem type itself, which has its own dedicated mechanism for managing time-series splits. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Availability

Chronological data splitting is available in Databricks Runtime 10.4 LTS ML and above for both classification and regression experiments. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

### Related Concepts

- AutoML Classic Compute
- [Forecasting with AutoML (classic compute)](/concepts/automl-forecasting-classic-compute.md)
- Classification and Regression with AutoML
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

### Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
