---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9395b29b84ae8a406aee3442c2efb816777ed4b29d7dfce89bc2cfd05a32f3aa
  pageDirectory: concepts
  sources:
    - forecasting-with-automl-classic-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-dataset-warnings-and-quality-checks
    - Quality Checks and AutoML Dataset Warnings
    - ADWAQC
  citations:
    - file: forecasting-with-automl-classic-compute-databricks-on-aws.md
title: AutoML Dataset Warnings and Quality Checks
description: Feature in Databricks Runtime 10.1 ML+ that displays warnings for potential dataset issues such as unsupported column types or high cardinality columns during AutoML experiments.
tags:
  - automl
  - data-quality
  - databricks
timestamp: "2026-06-19T18:53:43.493Z"
---

# AutoML Dataset Warnings and Quality Checks

**AutoML Dataset Warnings and Quality Checks** are automated diagnostics performed by Databricks AutoML during experiment setup and execution. These checks analyze the input dataset for potential issues that could affect model quality, training performance, or experiment correctness. Warnings are displayed in the **Warnings** tab on the training page and the experiment page after the experiment completes. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Overview

When you configure an AutoML experiment, the system evaluates the provided dataset for common data quality issues. Databricks indicates potential errors or issues to the best of its ability; however, this analysis may not be comprehensive and may not capture all issues you may be searching for. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Types of Warnings

AutoML displays warnings for potential issues with the dataset, including but not limited to:

- **Unsupported column types** — Columns with data types that AutoML cannot process for the selected problem type (classification, regression, or forecasting). ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **High cardinality columns** — Categorical columns with a very large number of unique values, which can lead to overfitting, increased training time, and poor generalization. ^[forecasting-with-automl-classic-compute-databricks-on-aws.md]
- **Missing values** — Datasets with significant null entries that may require imputation or handling before training.
- **Data leakage indicators** — Columns that may inadvertently provide information about the target variable, leading to overly optimistic performance estimates.

## Viewing Warnings

You can access dataset warnings through two locations:

1. **During training** — On the AutoML training page, click the **Warnings** tab to see any issues detected in the dataset.
2. **After experiment completion** — On the experiment page, click the **Warnings** tab to review all warnings generated during the experiment.

^[forecasting-with-automl-classic-compute-databricks-on-aws.md]

## Related Concepts

- [AutoML Experiments](/concepts/automl-forecasting-experiment-stages.md) — The overall workflow for automated machine learning on Databricks.
- [Data Profiling](/concepts/data-profiling.md) — Broader statistical analysis of dataset quality beyond AutoML-specific checks.
- [Forecasting Data Preparation](/concepts/automl-forecasting-data-preparation.md) — Specific data preparation considerations for time series forecasting experiments.
- Classification Data Preparation — Data preparation settings for classification with AutoML.
- Regression Data Preparation — Data preparation settings for regression with AutoML.
- [Feature Store Integration](/concepts/automl-feature-store-integration.md) — Using existing feature tables to augment the original input dataset.

## Sources

- forecasting-with-automl-classic-compute-databricks-on-aws.md

# Citations

1. [forecasting-with-automl-classic-compute-databricks-on-aws.md](/references/forecasting-with-automl-classic-compute-databricks-on-aws-20de86d0.md)
