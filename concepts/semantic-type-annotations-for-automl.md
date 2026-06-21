---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0dc07e636947788fce72a7d1a2fbc9d298f121c32692dfc86f088b5fed0aca6d
  pageDirectory: concepts
  sources:
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - semantic-type-annotations-for-automl
    - STAFA
  citations:
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Semantic Type Annotations for AutoML
description: Manual annotations (categorical, numeric, datetime, text, native) that users can apply to columns to override AutoML's automatic semantic type detection.
tags:
  - automl
  - annotations
  - data-types
  - configuration
timestamp: "2026-06-19T18:06:57.334Z"
---

```markdown
---
title: Semantic Type Annotations for AutoML
summary: Manual API-based method to override AutoML's semantic type detection using Spark DataFrame metadata annotations (categorical, numeric, datetime, text, native).
sources:
  - data-preparation-for-regression-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:42:13.911Z"
updatedAt: "2026-06-19T14:42:13.911Z"
tags:
  - machine-learning
  - automl
  - feature-engineering
aliases:
  - semantic-type-annotations-for-automl
  - STAFA
confidence: 0.96
provenanceState: extracted
inferredParagraphs: 0
---

# Semantic Type Annotations for AutoML

**Semantic Type Annotations for AutoML** allow users to manually control how Databricks AutoML interprets the semantic type of a column, overriding the automatic detection that AutoML performs during data preparation. This feature is available starting in Databricks Runtime 10.1 ML and above. ^[data-preparation-for-regression-databricks-on-aws.md]

## Overview

AutoML automatically attempts to detect semantic types that differ from a column's underlying Spark or pandas data type. For example, it treats string and integer columns representing date or timestamp data as timestamps, and string columns containing numeric data as numeric types. With Databricks Runtime 10.1 ML and above, AutoML also treats numeric columns containing categorical IDs as categorical features and string columns containing English text as text features. ^[data-preparation-for-regression-databricks-on-aws.md]

However, these automatic detections are best-effort and may sometimes miss semantic types. Semantic type annotations provide a way to explicitly set or disable the semantic type for any column. ^[data-preparation-for-regression-databricks-on-aws.md]

## Annotation Syntax

To manually annotate the semantic type of a column, modify the column metadata using the `withMetadata` method on the DataFrame. The annotation key is `spark.contentAnnotation.semanticType`. ^[data-preparation-for-regression-databricks-on-aws.md]

```python
metadata_dict = df.schema["<column-name>"].metadata
metadata_dict["spark.contentAnnotation.semanticType"] = "<semantic-type>"
df = df.withMetadata("<column-name>", metadata_dict)
```

Replace `<column-name>` with the actual column name and `<semantic-type>` with one of the supported values. ^[data-preparation-for-regression-databricks-on-aws.md]

## Supported Semantic Types

The following semantic types are supported: ^[data-preparation-for-regression-databricks-on-aws.md]

| Semantic Type | Description | Example Use Case |
|---------------|-------------|------------------|
| `categorical` | The column contains categorical values | Numerical IDs that should not be treated as numeric features |
| `numeric` | The column contains numeric values | String values that can be parsed into numbers |
| `datetime` | The column contains timestamp values | String, numerical, or date values convertible to timestamps |
| `text` | The string column contains English text | Free-text fields for NLP processing |

## Disabling Semantic Type Detection

To disable semantic type detection on a specific column, use the special keyword annotation `native`. This tells AutoML to treat the column according to its original Spark or pandas data type without any semantic reinterpretation. ^[data-preparation-for-regression-databricks-on-aws.md]

```python
metadata_dict["spark.contentAnnotation.semanticType"] = "native"
```

## Important Interactions

Semantic type detection is **not** performed for columns that have custom imputation methods specified. If you specify a non-default imputation method, AutoML skips semantic type detection entirely for that column. ^[data-preparation-for-regression-databricks-on-aws.md]

## Use Cases

Semantic type annotations are useful when:

- AutoML misidentifies a column's semantic type during automatic detection.
- A numeric column contains categorical IDs that should be treated as categories rather than continuous values.
- A string column contains numeric data that should be parsed as numbers.
- You want to override automatic detection to ensure consistent behavior across experiment runs.
- You need to disable semantic detection on a column to preserve its original data type.

## Related Concepts

- [[AutoML Data Preparation]] — The overall data preparation pipeline for AutoML training
- Imputation of Missing Values — Custom imputation methods and their interaction with semantic detection
- [[Supported Feature Types for AutoML|Feature Types for AutoML]] — Supported data types for AutoML training
- [[Column Selection in AutoML|Column Selection for AutoML]] — Specifying which columns to include or exclude
- Time Series Split — Chronological data splitting for time-dependent data

## Sources

- data-preparation-for-regression-databricks-on-aws.md
```

# Citations

1. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
