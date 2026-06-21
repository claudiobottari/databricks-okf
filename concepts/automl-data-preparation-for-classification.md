---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84163f1004c12a63a1a32cc00247a3c64913b8ee231acdde06c0432e1a7c45b1
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-data-preparation-for-classification
    - ADPFC
    - Data Preparation for Classification
    - Data preparation for classification
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: AutoML Data Preparation for Classification
description: Overview of how Databricks AutoML prepares data for classification model training, including configurable settings via UI and API.
tags:
  - machine-learning
  - automl
  - data-preparation
timestamp: "2026-06-19T18:05:13.990Z"
---

# AutoML Data Preparation for Classification

**AutoML Data Preparation for Classification** refers to the series of automated preprocessing steps that Databricks AutoML applies to a dataset when a classification experiment is configured. These steps include type handling, missing value imputation, class balancing, column selection, data splitting, large-dataset sampling, and semantic type detection, all of which can be configured through the AutoML UI or API. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Data Feature Types

AutoML supports numeric types (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`), Boolean, String (categorical or English text), Timestamps (`TimestampType`, `DateType`), `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above), and `DecimalType` (Databricks Runtime 11.3 LTS ML and above). Types such as images are not supported. ^[data-preparation-for-classification-databricks-on-aws.md]

## Imputing Missing Values

Starting with Databricks Runtime 10.4 LTS ML, you can specify a custom imputation method for each column using the **Impute with** dropdown in the UI or the `imputers` parameter in the API. By default, AutoML selects a method based on the column type and content. If a non-default imputation method is selected, AutoML does not perform semantic type detection on that column. ^[data-preparation-for-classification-databricks-on-aws.md]

## Handling Imbalanced Datasets

In Databricks Runtime 11.3 LTS ML and above, when AutoML detects an imbalanced dataset, it reduces the imbalance in the training set by downsampling the majority class(es) and applying class weights. For example, if class A has 95 samples and class B has 5, AutoML downsamples class A to 70 samples (a ratio of 70/95 ≈ 0.736) and scales the class weight for class A by the inverse ratio (1/0.736 ≈ 1.358) while keeping class B weight at 1. Test and validation sets are left unchanged so that model performance is evaluated on the original class distribution. ^[data-preparation-for-classification-databricks-on-aws.md]

## Column Selection

From Databricks Runtime 10.3 ML, you can control which columns are used for training by unchecking them in the UI or by using the `exclude_cols` API parameter. The prediction target column and the time column (if used for splitting) cannot be dropped. By default, all columns are included. ^[data-preparation-for-classification-databricks-on-aws.md]

## Data Splitting

AutoML splits data into training (60%), validation (20%), and test (20%) sets. Three methods are available:

- **Random split** (default): For classification, a stratified random split ensures each class is proportionally represented in each split.
- **Chronological split** (Databricks Runtime 10.4 LTS ML and above): Uses a time column (timestamp, integer, or string) to order data; earliest data is assigned to training, next to validation, latest to test.
- **Manual split** (Databricks Runtime 15.3 ML and above, API only): A split column with values `train`, `validate`, or `test` determines row assignment; rows with other values are ignored and a warning is raised. ^[data-preparation-for-classification-databricks-on-aws.md]

## Sampling Large Datasets

Each AutoML trial trains on a single worker node. If the dataset is too large, AutoML automatically estimates memory requirements and samples the dataset. For classification, it uses PySpark’s `sampleBy` method for stratified sampling, preserving the target label distribution. For regression, it uses PySpark’s `sample` method. ^[data-preparation-for-classification-databricks-on-aws.md]

## Semantic Type Detection

With Databricks Runtime 9.1 LTS ML and above, AutoML attempts to detect semantic types that differ from the raw Spark or pandas data type. String and integer columns representing dates or timestamps are treated as timestamps; string columns that represent numeric data are treated as numeric. With Databricks Runtime 10.1 ML and above, numeric columns that contain categorical IDs are treated as categorical, and string columns containing English text are treated as text features. If a column has a custom imputation method specified, semantic type detection is not performed. ^[data-preparation-for-classification-databricks-on-aws.md]

## Semantic Type Annotations

From Databricks Runtime 10.1 ML and above, you can override or disable semantic type detection by annotating a column’s metadata with the `spark.contentAnnotation.semanticType` key. Valid values are `categorical`, `numeric`, `datetime`, and `text`. To disable detection, use the special value `native`. The annotation is applied using `df.withMetadata()` in PySpark. ^[data-preparation-for-classification-databricks-on-aws.md]

## Related Concepts

- AutoML – Automated machine learning pipeline in Databricks
- [Classification](/concepts/data-classification.md) – The problem type for which this data preparation is optimized
- [Imputation](/concepts/missing-value-imputation.md) – Strategies for handling missing values
- [Data Splitting](/concepts/data-splitting-strategies.md) – Random, chronological, and manual split methods
- [Semantic Type Detection](/concepts/semantic-type-detection.md) – Automatic identification of column meaning beyond raw type
- Stratified Sampling – Preserving class proportions during sampling
- Class Imbalance – Handling skewed class distributions
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime version that enables these features

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
