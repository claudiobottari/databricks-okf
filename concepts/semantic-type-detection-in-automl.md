---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5b68d21499b71f73f127ce1f9b3b479581e99fbf3a7b48e719333c3ec61e2e6
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
    - data-preparation-for-forecasting-databricks-on-aws.md
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - semantic-type-detection-in-automl
    - STDIA
    - AutoML Semantic Type Detection
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
    - file: data-preparation-for-regression-databricks-on-aws.md
    - file: data-preparation-for-forecasting-databricks-on-aws.md
title: Semantic Type Detection in AutoML
description: AutoML's ability to detect semantic types (datetime, numeric, categorical, text) beyond raw Spark/pandas data types, including manual annotation support.
tags:
  - machine-learning
  - automl
  - type-detection
timestamp: "2026-06-19T18:05:41.890Z"
---

```markdown
---
title: Semantic Type Detection in AutoML
summary: A feature in Databricks AutoML that automatically identifies column types, which is disabled when users specify a non-default imputation method for missing values.
sources:
  - data-preparation-for-forecasting-databricks-on-aws.md
  - data-preparation-for-regression-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:28:48.464Z"
updatedAt: "2026-06-19T14:41:55.503Z"
tags:
  - automl
  - data-types
  - databricks
aliases:
  - semantic-type-detection-in-automl
  - STDIA
confidence: 0.9
provenanceState: merged
inferredParagraphs: 1
---

# Semantic Type Detection in AutoML

**Semantic Type Detection** is a feature in [[Databricks AutoML]] that automatically identifies whether a column's logical meaning (semantic type) differs from its underlying Spark or pandas data type. This detection allows AutoML to apply appropriate preprocessing and feature engineering for downstream tasks like classification, regression, and [[Forecast|forecasting]].^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md]

## Overview

Starting with Databricks Runtime 9.1 LTS ML, AutoML attempts to detect semantic types for columns that may have a different interpretation than their raw schema type. These detections are best-effort and may occasionally miss certain semantic types. Users can also manually set semantic types or disable detection entirely using [[semantic type annotations]].^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

### Supported Feature Types

AutoML supports the following data feature types for semantic type detection:

- Numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`)
- Boolean
- String (categorical or English text)
- Timestamps (`TimestampType`, `DateType`)
- `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above)
- `DecimalType` (Databricks Runtime 11.3 LTS ML and above)

Image data types are not supported.^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Detection Adjustments

AutoML makes specific adjustments based on detected semantic types:

**For all Databricks Runtime 9.1 LTS ML and above:**
- String and integer columns representing date or timestamp data are treated as a timestamp type.
- String columns that represent numeric data are treated as a numeric type.^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

**For Databricks Runtime 10.1 ML and above (additional adjustments):**
- Numeric columns that contain categorical IDs are treated as a categorical feature.
- String columns that contain English text are treated as a text feature.^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## When Detection Is Disabled

Semantic type detection is **not** performed in the following scenarios:

- When a custom imputation method is specified for a column (either via the UI or the API `imputers` parameter)
- When a column has a [[Semantic Type Annotations|semantic type annotation]] set to `native` (which disables detection for that specific column)^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Manual Control via Annotations

With Databricks Runtime 10.1 ML and above, users can control semantic type assignment through metadata annotations. The annotation syntax uses `spark.contentAnnotation.semanticType` in the column metadata:

```python
metadata_dict = df.schema["<column-name>"].metadata
metadata_dict["spark.contentAnnotation.semanticType"] = "<semantic-type>"
df = df.withMetadata("<column-name>", metadata_dict)
```

Valid semantic types include:
- `categorical` - For numerical values that should be treated as IDs
- `numeric` - For string values that can be parsed into numbers
- `datetime` - For timestamp-convertible values
- `text` - For string columns containing English text
- `native` - To disable detection (preserve original schema type)^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- [[AutoML Data Preparation]] - How AutoML prepares data for training
- [[Imbalanced Dataset Handling|Imbalanced Dataset Support]] - Handling class imbalance in classification
- [[Column Selection in AutoML]] - Choosing features for model training
- [[Data Splitting Strategies]] - Training, validation, and test set partitioning
- Automated Feature Engineering - Related preprocessing techniques

## Sources

- data-preparation-for-classification-databricks-on-aws.md
- data-preparation-for-regression-databricks-on-aws.md
- data-preparation-for-forecasting-databricks-on-aws.md
```

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
2. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
3. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
