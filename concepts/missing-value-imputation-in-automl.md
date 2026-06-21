---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e2840004d1e6e1305d64a8352fec3785d3ea6014f93e518bd2662f7b34033dc
  pageDirectory: concepts
  sources:
    - data-preparation-for-forecasting-databricks-on-aws.md
    - data-preparation-for-regression-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - missing-value-imputation-in-automl
    - MVIIA
    - Data Imputation in AutoML
    - Imputation in AutoML
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
    - file: data-preparation-for-forecasting-databricks-on-aws.md
    - file: data-preparation-for-regression-databricks-on-aws.md
title: Missing Value Imputation in AutoML
description: Configurable strategies for handling null values in forecasting data, including default automatic selection based on column type and content.
tags:
  - data-cleaning
  - imputation
  - automl
  - forecasting
timestamp: "2026-06-19T18:05:57.902Z"
---

---  
title: Missing Value Imputation in AutoML  
summary: Configurable handling of null values in Databricks AutoML, where users can specify imputation methods per column or rely on AutoML's default selection based on column type and content.  
sources:  
  - data-preparation-for-classification-databricks-on-aws.md  
  - data-preparation-for-forecasting-databricks-on-aws.md  
  - data-preparation-for-regression-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T11:29:43.524Z"  
updatedAt: "2026-06-18T14:59:35.108Z"  
tags:  
  - machine-learning  
  - automl  
  - data-preprocessing  
  - databricks  
aliases:  
  - missing-value-imputation-in-automl  
  - MVIIA  
confidence: 1  
provenanceState: extracted  
inferredParagraphs: 0  
---  

# Missing Value Imputation in AutoML

**Missing Value Imputation in AutoML** refers to how Databricks AutoML handles null or missing values in training data during automated machine learning runs. AutoML can either apply a default imputation strategy based on column type and content, or use a user-specified custom method. This is applicable to classification, forecasting, and regression experiments. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Default Imputation

By default, AutoML selects an imputation method automatically based on the column's datatype and the distribution of non-null values. The strategy is chosen to preserve the statistical properties of the training data without requiring manual intervention. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

For example, numeric columns may be imputed with the mean or median of the observed values, while categorical columns may use the mode or a placeholder token. The exact algorithms are not user-configurable in the default mode; AutoML determines the best approach per column.

## Custom Imputation

Starting with Databricks Runtime 10.4 LTS ML, you can override AutoML's default imputation by specifying a custom method for selected columns or for all columns. Custom imputation is available both in the AutoML UI (regardless of problem type) and through the API. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

### Configuring in the UI

When setting up a classification, forecasting, or regression experiment in the AutoML UI, navigate to the **table schema** section. For each column, the **Impute with** dropdown lists available imputation methods. Selecting a method applies it to that column for the entire experiment. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

### Configuring via the API

In the AutoML Python API, pass the `imputers` parameter when calling the training function. The exact syntax is described in the [AutoML Python API reference](https://docs.databricks.com/aws/en/machine-learning/automl/automl-api-reference). ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Effect on Semantic Type Detection

If you specify a non-default imputation method for any column, AutoML **does not perform semantic type detection** on that column or on any other column in the dataset. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

[Semantic Type Detection](/concepts/semantic-type-detection.md) is the process by which AutoML attempts to recognize columns that have a semantic meaning different from their raw Spark or pandas data type (for example, a numeric column containing categorical IDs, or a string column containing timestamps). When custom imputation is used, this automatic detection is skipped, and columns are treated according to their native schema type. To apply both custom imputation and semantic type detection, you must manually annotate the semantic type using [Semantic Type Annotations](/concepts/semantic-type-annotations.md) before running the AutoML experiment.

## Supported Data Types for Imputation

Imputation is applied only to columns with supported feature types. These include numeric types (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`), Boolean, String (categorical or English text), timestamps (`TimestampType`, `DateType`), `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML+), and `DecimalType` (Databricks Runtime 11.3 LTS ML+). Columns of unsupported types (e.g., images, structs) are excluded from training regardless of missing value handling. ^[data-preparation-for-classification-databricks-on-aws.md, data-preparation-for-forecasting-databricks-on-aws.md, data-preparation-for-regression-databricks-on-aws.md]

## Best Practices

- Use default imputation unless you have domain-specific knowledge about how to handle missing values (e.g., a fixed value representing "not applicable").  
- If you need both custom imputation and semantic type detection, manually annotate columns with [Semantic Type Annotations](/concepts/semantic-type-annotations.md) before the run.  
- Review the imputation method applied by AutoML in the generated notebook to understand how missing values were treated in the final model.

## Related Concepts

- AutoML — Automated machine learning on Databricks  
- [Semantic Type Detection](/concepts/semantic-type-detection.md) — Automatic recognition of column semantics  
- [Semantic Type Annotations](/concepts/semantic-type-annotations.md) — Manual overrides for column types  
- [Data Preparation for Classification](/concepts/automl-data-preparation-for-classification.md) — Full data preprocessing pipeline  
- Data Preparation for Forecasting — Full data preprocessing pipeline  
- Data Preparation for Regression — Full data preprocessing pipeline  
- [Column Selection in AutoML](/concepts/column-selection-in-automl.md) — Including/excluding columns from training  
- [Train-Validation-Test Split](/concepts/trainvalidationsplit.md) — How data is divided for evaluation  

## Sources

- data-preparation-for-classification-databricks-on-aws.md  
- data-preparation-for-forecasting-databricks-on-aws.md  
- data-preparation-for-regression-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
2. [data-preparation-for-forecasting-databricks-on-aws.md](/references/data-preparation-for-forecasting-databricks-on-aws-d40acbea.md)
3. [data-preparation-for-regression-databricks-on-aws.md](/references/data-preparation-for-regression-databricks-on-aws-5e52b14c.md)
