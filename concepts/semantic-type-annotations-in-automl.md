---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fce57b3ca827c3b2d49e39d632a23b648b67f6826f21cd4200ee6dda091fc61a
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - semantic-type-annotations-in-automl
    - STAIA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Semantic Type Annotations in AutoML
description: How users can manually assign semantic types (categorical, numeric, datetime, text, or native) to columns using metadata annotations to override or disable automatic detection.
tags:
  - machine-learning
  - automl
  - type-detection
  - annotations
timestamp: "2026-06-19T18:05:30.452Z"
---

# Semantic Type Annotations in AutoML

**Semantic Type Annotations** are a mechanism that lets you manually override the automatic semantic type detection performed by AutoML. By attaching an annotation to a column, you can force AutoML to treat that column as categorical, numeric, datetime, text, or native (i.e., no semantic conversion), regardless of its underlying Spark or pandas data type.

## Overview

Starting with Databricks Runtime 10.1 LTS ML, AutoML automatically attempts to detect the semantic type of each column — for example, it treats string columns that contain numeric data as numeric types, and numeric columns containing categorical IDs as categorical features. However, these detections are best-effort and may sometimes miss the correct type. Semantic type annotations give you a way to correct or enforce the intended treatment. ^[data-preparation-for-classification-databricks-on-aws.md]

When a custom [imputation](/concepts/missing-value-imputation.md) method is specified for a column, AutoML does **not** perform semantic type detection at all for that column. In that case, annotations are not needed because detection is skipped entirely. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Annotation Types

The following values can be used as the `<semantic-type>` in an annotation: ^[data-preparation-for-classification-databricks-on-aws.md]

| Annotation    | Description                                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------|
| `categorical` | The column contains categorical values (e.g., numeric IDs that should not be treated as numbers).              |
| `numeric`     | The column contains numeric values (e.g., string-encoded numbers that can be parsed).                          |
| `datetime`    | The column contains timestamp values (string, numerical, or date values that can be converted into timestamps).|
| `text`        | The string column contains English text.                                                                       |
| `native`      | Disables semantic type detection for the column, keeping the original Spark/pandas data type.                  |

## How to Apply a Semantic Type Annotation

To annotate a column, you use the `withMetadata` method on the DataFrame. The annotation is stored under the metadata key `spark.contentAnnotation.semanticType`. ^[data-preparation-for-classification-databricks-on-aws.md]

The syntax is:

```python
metadata_dict = df.schema["<column-name>"].metadata
metadata_dict["spark.contentAnnotation.semanticType"] = "<semantic-type>"
df = df.withMetadata("<column-name>", metadata_dict)
```

After this annotation is set, AutoML will treat the column according to the specified semantic type during training, overriding its automatic detection logic.

## Interaction with Automatic Detection

If no annotation is provided, AutoML applies its own automatic detection rules. With Databricks Runtime 10.1 ML and above, those rules include: ^[data-preparation-for-classification-databricks-on-aws.md]

- String and integer columns representing date or timestamp data → treated as `datetime`.
- String columns representing numeric data → treated as `numeric`.
- Numeric columns containing categorical IDs → treated as `categorical`.
- String columns containing English text → treated as `text`.

If you apply an annotation, it takes precedence over these automatic rules. To entirely disable semantic type detection for a column, use the `native` annotation. ^[data-preparation-for-classification-databricks-on-aws.md]

## When to Use Annotations

- **Correct misclassification** — when AutoML incorrectly guesses the type (e.g., a categorical ID column treated as numeric).
- **Enforce a specific treatment** — when you want to force a column to be treated as text or datetime even if its raw type suggests otherwise.
- **Disable detection** — when you want to keep the column exactly as its native Spark type (`native` annotation) to avoid any transformation.

## Related Concepts

- [AutoML Data Preparation](/concepts/automl-data-preparation.md)
- [Impute Missing Values in AutoML](/concepts/imputation-of-missing-values-in-automl.md)
- Classification with AutoML
- [Feature Types in AutoML](/concepts/supported-feature-types-in-automl.md)

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
