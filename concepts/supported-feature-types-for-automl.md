---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 20c4dc5c0e6bcbc7312ba6b49f645bfd486c33cc8ad9f00e0070efdb1afb1f6f
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-feature-types-for-automl
    - SFTFA
    - Feature Types for AutoML
    - Feature types supported by AutoML
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Supported Feature Types for AutoML
description: The set of data types supported by Databricks AutoML including numeric types, Boolean, String, timestamps, ArrayType of Numeric, and DecimalType, with images explicitly unsupported.
tags:
  - automl
  - data-types
  - databricks
timestamp: "2026-06-19T09:44:22.848Z"
---

# Supported Feature Types for AutoML

**Supported Feature Types for AutoML** defines the data types that Databricks AutoML can accept as input features for training regression, classification, and forecasting models. AutoML supports a specific set of Spark and pandas data types, while certain complex types like images are explicitly unsupported.

## Supported Feature Types

AutoML supports the following feature types across all problem types (classification, regression, and forecasting):^[data-preparation-for-regression-databricks-on-aws.md]

| Feature Type | Spark/Pandas Data Types |
|---|---|
| **Numeric** | `ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType` |
| **Boolean** | `BooleanType` |
| **String** | `StringType` (treated as categorical or English text) |
| **Timestamp** | `TimestampType`, `DateType` |
| **Array[Numeric]** | `ArrayType` with numeric element types (Databricks Runtime 10.4 LTS ML and above) |
| **Decimal** | `DecimalType` (Databricks Runtime 11.3 LTS ML and above) |

Image data types are **not** supported as features.^[data-preparation-for-regression-databricks-on-aws.md]

## Semantic Type Detection

Beyond the raw Spark data types listed above, AutoML performs [Semantic Type Detection](/concepts/semantic-type-detection.md) to interpret columns more intelligently. Starting with Databricks Runtime 9.1 LTS ML, AutoML attempts to detect whether columns have a semantic meaning different from their declared data type:^[data-preparation-for-regression-databricks-on-aws.md]

- String and integer columns that represent date or timestamp data are treated as timestamps.
- String columns that represent numeric data are treated as numeric features.

With Databricks Runtime 10.1 ML and above, AutoML additionally detects:^[data-preparation-for-regression-databricks-on-aws.md]

- Numeric columns that contain categorical IDs are treated as categorical features.
- String columns that contain English text are treated as text features.

These detections are best-effort and may sometimes miss the existence of semantic types. You can manually control semantic type assignment using [Semantic Type Annotations](/concepts/semantic-type-annotations.md).^[data-preparation-for-regression-databricks-on-aws.md]

### Semantic Type Annotations

To manually annotate the semantic type of a column, use the following pattern:^[data-preparation-for-regression-databricks-on-aws.md]

```python
metadata_dict = df.schema["<column-name>"].metadata
metadata_dict["spark.contentAnnotation.semanticType"] = "<semantic-type>"
df = df.withMetadata("<column-name>", metadata_dict)
```

The `<semantic-type>` parameter can be one of:^[data-preparation-for-regression-databricks-on-aws.md]

- `categorical` — The column contains categorical values (e.g., numerical IDs).
- `numeric` — The column contains numeric values (e.g., strings that can be parsed as numbers).
- `datetime` — The column contains timestamp values (string, numeric, or date values convertible to timestamps).
- `text` — The string column contains English text.

To disable semantic type detection on a column entirely, use the special keyword annotation `native`.^[data-preparation-for-regression-databricks-on-aws.md]

**Note:** AutoML does not perform semantic type detection on columns that have custom imputation methods specified.^[data-preparation-for-regression-databricks-on-aws.md]

## Limitations

While AutoML supports a wide range of feature types, the following limitations apply:

- Image columns are not supported as features.^[data-preparation-for-regression-databricks-on-aws.md]
- Semantic type detection is best-effort and can be overridden via annotations or disabled entirely.^[data-preparation-for-regression-databricks-on-aws.md]
- Array[Numeric] support requires Databricks Runtime 10.4 LTS ML or above.^[data-preparation-for-regression-databricks-on-aws.md]
- DecimalType support requires Databricks Runtime 11.3 LTS ML or above.^[data-preparation-for-regression-databricks-on-aws.md]

## Related Concepts

- AutoML
- Data Preparation for Regression
- [Impute Missing Values](/concepts/imputation-of-missing-values-in-automl.md)
- [Semantic Type Detection](/concepts/semantic-type-detection.md)
- [Column Selection](/concepts/automl-column-selection.md)
- [Data Splitting Strategies](/concepts/data-splitting-strategies.md)

## Sources

- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
