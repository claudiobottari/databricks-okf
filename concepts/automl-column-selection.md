---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b7bba3595a390145aefaca000c8906a49e311e184b90c5a7c714ff340bf99e1
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - automl-column-selection
    - ACS
    - Column Selection
    - ColumnSelection
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
    - file: data-preparation-for-regression-databricks-on-aws.md
title: AutoML Column Selection
description: Ability to specify which columns AutoML uses for training, including excluding columns via UI checkbox or API parameter, with restrictions on dropping target or time columns.
tags:
  - feature-selection
  - automl
  - databricks
  - column-management
timestamp: "2026-06-19T14:41:26.520Z"
---

# AutoML Column Selection

**AutoML Column Selection** refers to the ability to specify which columns in a dataset Databricks AutoML uses for training a model. This feature is available starting in Databricks Runtime 10.3 ML for both [AutoML Classification](/concepts/automl-classification-classify.md) and [AutoML Regression](/concepts/automl-regress.md) workflows. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Usage

### In the AutoML UI

You can exclude a column from training by unchecking it in the **Include** column of the table schema displayed during experiment setup. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

### Via the AutoML API

Use the `exclude_cols` parameter to specify a list of column names to exclude. See the [AutoML Python API Reference](/concepts/automl-python-api.md) for more details. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Restrictions

You cannot drop the column selected as the prediction target. Additionally, you cannot drop the column selected as the time column when using a [chronological split](/concepts/chronological-data-splitting-in-automl.md) for data splitting. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Default Behavior

By default, all columns in the input dataset are included for training. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- [AutoML Data Preparation](/concepts/automl-data-preparation.md) — Overall process of preparing data for AutoML
- [AutoML Classification Data Preparation](/concepts/automl-classification-data-preparation.md) — Data preparation specifics for classification
- AutoML Regression Data Preparation — Data preparation specifics for regression
- [AutoML Impute Missing Values](/concepts/automl-missing-value-imputation.md) — Option to specify imputation methods per column
- [AutoML Semantic Type Detection](/concepts/semantic-type-detection.md) — Automatic detection of column semantic types

## Sources

- data-preparation-for-classification-databricks-on-aws.md
- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
2. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
