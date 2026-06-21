---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18f8acc3d68c33405bc911f99ebe8d21f10e7f31c4bbbb387601b430cff20447
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - semantic-type-detection
    - STD
    - AutoML Semantic Type Detection
    - semantic-type-detection-in-automl
    - STDIA
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: Semantic Type Detection
description: AutoML's ability to infer semantic types (categorical, numeric, datetime, text) from raw Spark/pandas data types, with support for manual annotations.
tags:
  - automl
  - feature-engineering
  - type-detection
  - databricks
timestamp: "2026-06-19T14:41:17.889Z"
---

```markdown
---
title: Semantic Type Detection
summary: AutoML automatically detects and adjusts column types beyond their raw Spark or pandas data types, treating string date columns as timestamps, numeric ID columns as categorical, or English text columns as text features.
sources:
  - data-preparation-for-classification-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:59:58.742Z"
tags:
  - automl
  - feature-engineering
  - databricks
aliases:
  - semantic-type-detection
  - STD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Semantic Type Detection

**Semantic Type Detection** is a feature in [[Databricks AutoML]] that attempts to infer whether a column's meaningful (semantic) type differs from its raw Spark or pandas data type. This detection informs how the column is treated during training – for example, treating a string column that contains numbers as a numeric feature rather than a categorical one. These detections are best effort and may occasionally miss the existence of a semantic type.^[data-preparation-for-classification-databricks-on-aws.md]

## Adjustments Made by AutoML

Starting with Databricks Runtime 9.1 LTS ML, AutoML makes the following adjustments:

- String and integer columns that represent date or timestamp data are treated as a timestamp type.
- String columns that represent numeric data are treated as a numeric type.^[data-preparation-for-classification-databricks-on-aws.md]

With Databricks Runtime 10.1 ML and above, AutoML also makes these adjustments:

- Numeric columns that contain categorical IDs are treated as a categorical feature.
- String columns that contain English text are treated as a text feature.^[data-preparation-for-classification-databricks-on-aws.md]

## Semantic Type Annotations

Available since Databricks Runtime 10.1 ML, you can manually control the semantic type assigned to a column by placing a **semantic type annotation** on the column’s metadata. This overrides AutoML's automatic detection. To annotate a column, use the `withMetadata` method on the DataFrame’s schema:^[data-preparation-for-classification-databricks-on-aws.md]

```python
metadata_dict = df.schema["<column-name>"].metadata
metadata_dict["spark.contentAnnotation.semanticType"] = "<semantic-type>"
df = df.withMetadata("<column-name>", metadata_dict)
```

The `<semantic-type>` value can be one of the following:

- `categorical` – The column contains categorical values (e.g., numerical values that should be treated as IDs).
- `numeric` – The column contains numeric values (e.g., string values that can be parsed into numbers).
- `datetime` – The column contains timestamp values (string, numerical, or date values that can be converted into timestamps).
- `text` – The string column contains English text.^[data-preparation-for-classification-databricks-on-aws.md]

To disable semantic type detection entirely for a column, use the special keyword annotation `native`.^[data-preparation-for-classification-databricks-on-aws.md]

## Interaction with Custom Imputation

AutoML does **not** perform semantic type detection for columns that have Imputation|custom imputation methods specified. If you set a non-default imputation method on a column, AutoML skips any semantic type adjustments for that column.^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Feature Types

Semantic type detection operates only on the [[Supported Data Feature Types in AutoML|supported data feature types]], which include numeric, boolean, string, timestamp, array, and decimal types. Image data is not supported.^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- [[Databricks AutoML]]
- [[AutoML Data Preparation for Classification|Data Preparation for Classification]]
- [[Missing Value Imputation|Imputation]]
- [[FeatureSpec|Feature Types]]
- [[Semantic Type Annotations]]

## Sources

- data-preparation-for-classification-databricks-on-aws.md
```

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
