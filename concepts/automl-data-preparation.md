---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea9a9324bb094c98a52c0157b08531f5d1975d22a2626d30fc7eb384ebc27a70
  pageDirectory: concepts
  sources:
    - regression-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-data-preparation
    - ADP
    - Data Preparation for AutoML
  citations:
    - file: regression-with-automl-databricks-on-aws.md
      start: 33
      end: 37
    - file: regression-with-automl-databricks-on-aws.md
      start: 38
      end: 39
    - file: regression-with-automl-databricks-on-aws.md
      start: 99
      end: 106
    - file: regression-with-automl-databricks-on-aws.md
      start: 108
      end: 113
    - file: regression-with-automl-databricks-on-aws.md
      start: 138
      end: 141
title: AutoML Data Preparation
description: Data preparation features for AutoML including column selection for training, null value imputation, and chronological data splitting
tags:
  - automl
  - data-preparation
  - databricks
timestamp: "2026-06-19T20:12:59.280Z"
---

# AutoML Data Preparation

**AutoML Data Preparation** refers to the configurable settings and preprocessing steps that Databricks AutoML applies to input datasets before training regression, classification, or forecasting models. These settings allow users to control which columns are used for training, how missing values are imputed, and how data is split for validation.

## Column Selection

When configuring an AutoML experiment through the UI, users can specify which columns AutoML should use for training. The prediction target column and the time column used to split the data cannot be removed from the training set. ^[regression-with-automl-databricks-on-aws.md:33-37]

This feature is available in Databricks Runtime 10.3 ML and above. ^[regression-with-automl-databricks-on-aws.md:33-37]

## Missing Value Imputation

Starting in Databricks Runtime 10.4 LTS ML and above, users can specify how null values are imputed for each column. From the **Impute with** dropdown on the configuration page, users select the imputation strategy for a given column. ^[regression-with-automl-databricks-on-aws.md:38-39]

By default, AutoML automatically selects an imputation method based on the column type and content. The system's default choice can be overridden by the user. ^[regression-with-automl-databricks-on-aws.md:38-39]

## Chronological Data Splitting

For classification and regression experiments, users can select a time column to split the data for training, validation, and testing in chronological order. This ensures that the model is evaluated on data that follows the training data in time, which is important for time-dependent predictions. ^[regression-with-automl-databricks-on-aws.md:99-106]

This feature is available in Databricks Runtime 10.4 LTS ML and above. ^[regression-with-automl-databricks-on-aws.md:99-106]

## Data Storage

By default, the dataset is securely stored as an MLflow artifact. Databricks recommends leaving the **Data directory** field empty to trigger this default behavior. A DBFS path can be specified, but the dataset will not inherit the AutoML experiment's access permissions in that case. ^[regression-with-automl-databricks-on-aws.md:108-113]

## Best Practices

- Use chronological splitting when working with time-dependent data to avoid data leakage.
- Review the default imputation strategies to ensure they are appropriate for your specific data types and use cases.
- Rely on the default MLflow artifact storage for dataset security and access control.
- Review AutoML-generated warnings for potential dataset issues, such as unsupported column types or high cardinality columns. ^[regression-with-automl-databricks-on-aws.md:138-141]

## Related Concepts

- [AutoML Regression](/concepts/automl-regress.md)
- [AutoML Classification](/concepts/automl-classification-classify.md)
- [AutoML Forecasting](/concepts/automl-forecast.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Data Profiling](/concepts/data-profiling.md)
- [Feature Store Integration](/concepts/automl-feature-store-integration.md)

## Sources

- regression-with-automl-databricks-on-aws.md

# Citations

1. [regression-with-automl-databricks-on-aws.md:33-37](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
2. [regression-with-automl-databricks-on-aws.md:38-39](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
3. [regression-with-automl-databricks-on-aws.md:99-106](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
4. [regression-with-automl-databricks-on-aws.md:108-113](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
5. [regression-with-automl-databricks-on-aws.md:138-141](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
