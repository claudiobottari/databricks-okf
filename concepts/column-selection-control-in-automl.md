---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: afd19b25298780a9a11e63619caf26fb9d05840162a13c0cc76b787781676e77
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-selection-control-in-automl
    - CSCIA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Column Selection Control in AutoML
description: Ability to specify which columns to include or exclude from training in Databricks AutoML via UI checkboxes or the exclude_cols API parameter.
tags:
  - databricks
  - automl
  - feature-selection
  - column-selection
timestamp: "2026-06-19T09:43:22.377Z"
---

# Column Selection Control in AutoML

**Column Selection Control in AutoML** refers to the ability to specify which columns in your dataset are included or excluded from automated machine learning training. This feature, available in Databricks Runtime 10.3 ML and above, allows you to control the input features used by AutoML experiments when building classification, regression, and other models. ^[data-preparation-for-classification-databricks-on-aws.md]

## Overview

By default, AutoML includes all columns in the training dataset. However, you may want to exclude certain columns — for example, those containing irrelevant information, identifiers that should not influence predictions, or features that introduce data leakage. Column selection control gives you this flexibility both through the AutoML UI and the API. ^[data-preparation-for-classification-databricks-on-aws.md]

## Excluding Columns

### In the UI

To exclude a column from training in the AutoML UI, locate the column in the schema table and uncheck the **Include** checkbox. This removes the column from the training dataset. ^[data-preparation-for-classification-databricks-on-aws.md]

### Using the API

In the [AutoML Python API](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference), use the `exclude_cols` parameter to specify which columns to exclude. For example:

```python
from databricks import automl

automl.classify(
    dataset=df,
    target_col="label",
    exclude_cols=["id_column", "timestamp_column"]
)
```

This parameter accepts a list of column names as strings. ^[data-preparation-for-classification-databricks-on-aws.md]

## Important Restrictions

You cannot exclude:

- The column selected as the **prediction target** (the label or outcome variable). ^[data-preparation-for-classification-databricks-on-aws.md]
- The **time column** used to create chronological train/validation/test splits. ^[data-preparation-for-classification-databricks-on-aws.md]

If you attempt to exclude these required columns, AutoML will raise an error.

## Use Cases

Common scenarios for excluding columns include:

- **Identifier columns** (e.g., row IDs, user IDs, record numbers) that should not be treated as features. ^[data-preparation-for-classification-databricks-on-aws.md]
- **Derived or redundant columns** that duplicate information already present in other features.
- **Columns with data leakage risk** (e.g., post-target data or time-dependent information that would not be available at inference time).
- **High-cardinality columns** with limited predictive value that may increase training time without improving model quality.

## Related Concepts

- [Supported Data Feature Types in AutoML](/concepts/supported-data-feature-types-in-automl.md) — describes which data types AutoML can process.
- [AutoML classification training](/concepts/automl-classification-classify.md) — the classification workflow that uses selected columns.
- [Impute missing values in AutoML](/concepts/imputation-of-missing-values-in-automl.md) — handling null values in included columns.
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — how AutoML infers column meaning and how to override it.
- [Data Splitting Strategies](/concepts/data-splitting-strategies.md) — controlling how data is split into train/validation/test sets.

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
