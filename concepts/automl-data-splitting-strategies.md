---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b4f0a368393f0d88150633cb5881832349b0a67650d588e51408db94ee5c7568
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-data-splitting-strategies
    - ADSS
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: AutoML Data Splitting Strategies
description: Methods for dividing datasets into training, validation, and test sets in Databricks AutoML, including random, chronological, and manual splits.
tags:
  - machine-learning
  - automl
  - data-preparation
timestamp: "2026-06-19T14:42:09.158Z"
---

# AutoML Data Splitting Strategies

**AutoML Data Splitting Strategies** refer to the methods Databricks AutoML uses to divide a dataset into training, validation, and test sets for machine learning model development. AutoML supports three splitting strategies: random split, chronological split, and manual split. The choice of strategy depends on the type of ML problem and the nature of the data. ^[data-preparation-for-regression-databricks-on-aws.md]

## Default: Random Split

If no data split strategy is specified, AutoML randomly splits the dataset into 60% training, 20% validation, and 20% test sets. For [AutoML Classification](/concepts/automl-classification-classify.md) problems, AutoML uses a stratified random split to ensure that each class is adequately represented in all three splits. For [AutoML Regression](/concepts/automl-regress.md) problems, a standard random split is applied. ^[data-preparation-for-regression-databricks-on-aws.md]

## Chronological Split

Available in Databricks Runtime 10.4 LTS ML and above, the chronological split uses a time column to create temporally ordered train, validation, and test splits. The earliest data points are used for training, the next earliest for validation, and the latest points for testing. The time column can be a timestamp, integer, or string column. ^[data-preparation-for-regression-databricks-on-aws.md]

This strategy is particularly useful for [Time Series Forecasting](/concepts/multi-series-forecasting.md) or any scenario where temporal ordering matters and you want to avoid Data Leakage from future information influencing model training. ^[data-preparation-for-regression-databricks-on-aws.md]

## Manual Split

Available in Databricks Runtime 15.3 ML and above, the manual split strategy allows you to explicitly control which rows belong to which split using the API. You specify a split column containing the values `train`, `validate`, or `test` to identify rows for each dataset. Any rows with split column values other than these three are ignored, and AutoML raises a corresponding alert. ^[data-preparation-for-regression-databricks-on-aws.md]

## Configuring Split Strategies

You can adjust the splitting strategy during experiment setup in the AutoML UI or through the [AutoML API](/concepts/automl-python-api.md). In the UI, select the desired split method and specify any required parameters (such as the time column for chronological splits). In the API, use the appropriate parameters to configure the split. ^[data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- [AutoML Classification](/concepts/automl-classification-classify.md) — Classification-specific data preparation, including stratified splitting
- [AutoML Regression](/concepts/automl-regress.md) — Regression-specific data preparation
- Data Leakage — The risk of information from the future or test set influencing training
- Stratified Sampling — The technique used for random splits in classification to preserve class distribution
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — A use case that benefits from chronological splitting
- [AutoML API](/concepts/automl-python-api.md) — Programmatic configuration of data splitting parameters

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
