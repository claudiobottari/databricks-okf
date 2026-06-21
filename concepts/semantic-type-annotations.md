---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5589dfdcfcc795a739527857d1d8ad3fff6e64a36cc39de3aa81e0efe22aac75
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - semantic-type-annotations
    - STA
    - semantic type annotation
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Semantic Type Annotations
description: "A mechanism to manually control semantic type assignment in Databricks AutoML using Python metadata annotations, supporting types: categorical, numeric, datetime, text, and the 'native' keyword to disable detection."
tags:
  - automl
  - feature-engineering
  - databricks
timestamp: "2026-06-19T09:43:52.378Z"
---

# Semantic Type Annotations

**Semantic Type Annotations** are metadata hints applied to DataFrame columns that tell Databricks AutoML how to interpret a column’s data when its semantic meaning differs from its raw Spark or pandas data type. By annotating a column, you can override AutoML’s automatic [Semantic Type Detection](/concepts/semantic-type-detection.md) or disable it entirely for specific columns.^[data-preparation-for-regression-databricks-on-aws.md]

## Purpose

With Databricks Runtime 9.1 LTS ML and above, AutoML attempts to detect whether columns have a semantic type different from the Spark or pandas data type in the table schema. For example, it treats string columns containing numeric data as numeric, and integer columns containing timestamps as datetime. Starting with Databricks Runtime 10.1 ML, AutoML also detects numeric columns that contain categorical IDs as categorical features and string columns that contain English text as text features. These detections are best effort and might occasionally misidentify a column’s intended role. Semantic type annotations let you manually correct or guide these assignments.^[data-preparation-for-regression-databricks-on-aws.md]

## Supported Semantic Types

You can set a column’s semantic type to one of the following values:^[data-preparation-for-regression-databricks-on-aws.md]

| Annotation    | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `categorical` | The column contains categorical values — for example, numerical values that should be treated as IDs. |
| `numeric`     | The column contains numeric values — for example, string values that can be parsed into numbers.     |
| `datetime`    | The column contains timestamp values — string, numerical, or date values that can be converted into timestamps. |
| `text`        | The string column contains English text.                                     |
| `native`      | Disables semantic type detection on the column and keeps the column’s original Spark or pandas data type. |

## How to Apply Annotations

Semantic type annotations are set by modifying the metadata of a DataFrame’s schema column. The annotation key is `spark.contentAnnotation.semanticType` within the column’s metadata dictionary.^[data-preparation-for-regression-databricks-on-aws.md]

```python
metadata_dict = df.schema["<column-name>"].metadata
metadata_dict["spark.contentAnnotation.semanticType"] = "<semantic-type>"
df = df.withMetadata("<column-name>", metadata_dict)
```

Replace `<column-name>` with the actual column name and `<semantic-type>` with one of the supported values listed above.

## Interaction with Custom Imputation

AutoML does not perform semantic type detection for columns that have a custom imputation method specified. If you set a non-default imputation method on a column, AutoML will not attempt to detect or apply a semantic type transformation to that column, regardless of whether you provide an annotation.^[data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- AutoML — The machine learning automation platform that uses these annotations
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — The automatic detection feature that annotations can override
- [Impute Missing Values](/concepts/imputation-of-missing-values-in-automl.md) — Custom imputation which disables semantic type detection
- [Column Selection](/concepts/automl-column-selection.md) — How to include or exclude columns from AutoML training
- Data Preparation for Regression — Regression-specific data preparation and annotation usage

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
