---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9d1b1db88ade1f32f4edc6e2332af58b79364b770db697129685b99c42cf633
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-imputation-strategies
    - AIS
    - Imputation Strategies
    - Imputation Strategies in AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: AutoML Imputation Strategies
description: How Databricks AutoML handles missing values in classification datasets, including default type-based imputation and custom imputation methods.
tags:
  - databricks
  - automl
  - data-preparation
  - imputation
timestamp: "2026-06-19T09:42:01.084Z"
---

# AutoML Imputation Strategies

**AutoML Imputation Strategies** define how missing values (nulls) are handled in datasets used for AutoML classification and regression training. These strategies determine the replacement method applied to each column with null values before model training begins.^[data-preparation-for-classification-databricks-on-aws.md]

## Default Imputation Behavior

By default, AutoML automatically selects an imputation method for each column based on its data type and content. The system analyzes the column's characteristics to determine the most appropriate strategy without requiring manual configuration.^[data-preparation-for-classification-databricks-on-aws.md]

### Semantic Type Detection Interaction

When AutoML uses its default imputation selection, it also performs [Semantic Type Detection](/concepts/semantic-type-detection.md) on columns. This process identifies whether columns have a semantic meaning different from their underlying Spark or pandas data type — for example, treating string columns containing numeric data as numeric types, or treating numeric columns containing categorical IDs as categorical features.^[data-preparation-for-classification-databricks-on-aws.md]

## Custom Imputation Configuration

### Using the AutoML UI

In Databricks Runtime 10.4 LTS ML and above, you can specify custom imputation methods through the AutoML UI during experiment setup:

1. In the table schema view, locate the **Impute with** column.
2. Select a method from the drop-down for each column you want to configure.^[data-preparation-for-classification-databricks-on-aws.md]

### Using the AutoML API

For programmatic configuration, use the `imputers` parameter in the [AutoML Python API](/concepts/automl-python-api.md). The API reference provides detailed documentation on available options and syntax.^[data-preparation-for-classification-databricks-on-aws.md]

## Important Considerations

### Semantic Type Detection Disabled

If you specify a non-default imputation method for any column, AutoML does **not** perform semantic type detection. This means columns will be treated according to their raw Spark or pandas data types, and adjustments for semantic types (such as treating numeric IDs as categorical or string numbers as numeric) will not be applied.^[data-preparation-for-classification-databricks-on-aws.md]

### Imbalanced Dataset Handling

In Databricks Runtime 11.3 LTS ML and above, when AutoML detects a class imbalance in classification datasets, it applies separate preprocessing strategies for balancing. These strategies (downsampling and class weighting) operate independently from imputation. The imputation step handles missing values first, followed by any imbalance correction applied to the training dataset only. Test and validation datasets are not balanced.^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Data Types

AutoML imputation is available for all supported feature types in classification and regression, including:

- Numeric types (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`)
- Boolean
- String (categorical or English text)
- Timestamps (`TimestampType`, `DateType`)
- `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above)
- `DecimalType` (Databricks Runtime 11.3 LTS ML and above)

^[data-preparation-for-classification-databricks-on-aws.md]

## Best Practices

### When to Use Default Imputation

Default imputation is recommended when:
- You want AutoML to automatically determine the best strategy based on column characteristics.
- You want semantic type detection to remain active.
- You are working with diverse column types and want consistent handling.

### When to Use Custom Imputation

Custom imputation is appropriate when:
- You have domain knowledge about how missing values should be handled for specific columns.
- You require specific imputation values for regulatory or business reasons.
- You accept that semantic type detection will be disabled for the entire dataset.

## Related Concepts

- [AutoML Classification](/concepts/automl-classification-classify.md) — The classification training workflow that applies imputation strategies
- [AutoML Regression](/concepts/automl-regress.md) — The regression training workflow with similar imputation options
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — AutoML's automatic type identification, disabled with custom imputation
- [Data Preparation for Classification](/concepts/automl-data-preparation-for-classification.md) — Broader data preparation workflow including imputation
- Class Imbalance Handling — Separate preprocessing for imbalanced datasets

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
