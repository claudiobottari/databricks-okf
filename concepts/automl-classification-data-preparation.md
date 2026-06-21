---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69cb289511f8309ef39dc94935e68dc0a59925b0a49741969a0aba9edc0be9ad
  pageDirectory: concepts
  sources:
    - data-preparation-for-classification-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-classification-data-preparation
    - ACDP
    - Classification Data Preparation
    - Classification Data Preparation Settings
  citations:
    - file: data-preparation-for-classification-databricks-on-aws.md
title: AutoML Classification Data Preparation
description: How Databricks AutoML prepares datasets for classification model training, including feature type detection, imputation, sampling, and splitting.
tags:
  - automl
  - classification
  - databricks
  - data-preparation
timestamp: "2026-06-19T14:41:16.065Z"
---

---
title: AutoML Classification Data Preparation
summary: How AutoML prepares data for classification, including supported feature types, imputation, imbalanced dataset handling, column selection, data splitting, sampling, and semantic type detection.
sources:
  - data-preparation-for-classification-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:09:26.816Z"
updatedAt: "2026-06-18T08:09:26.816Z"
tags:
  - databricks
  - automl
  - classification
  - data-preparation
aliases:
  - automl-classification-data-preparation
  - ACDP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AutoML Classification Data Preparation

**AutoML Classification Data Preparation** describes how Databricks AutoML prepares tabular data for classification model training. The process includes supported feature types, missing value imputation, handling imbalanced datasets, column selection, data splitting strategies, sampling large datasets, and semantic type detection. Users can adjust these options during experiment setup in the AutoML UI or via the AutoML API. ^[data-preparation-for-classification-databricks-on-aws.md]

## Supported Data Feature Types

AutoML for classification supports only the following feature types: numeric (`ByteType`, `ShortType`, `IntegerType`, `LongType`, `FloatType`, `DoubleType`), Boolean, String (categorical or English text), timestamps (`TimestampType`, `DateType`), `ArrayType[Numeric]` (Databricks Runtime 10.4 LTS ML and above), and `DecimalType` (Databricks Runtime 11.3 LTS ML and above). Images are **not** supported. ^[data-preparation-for-classification-databricks-on-aws.md]

## Impute Missing Values

In Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed. In the UI, select a method from the **Impute with** drop-down in the table schema. In the API, use the `imputers` parameter. By default, AutoML selects an imputation method based on the column type and content. If you specify a non-default imputation method, AutoML does not perform semantic type detection on the column. ^[data-preparation-for-classification-databricks-on-aws.md]

## Imbalanced Dataset Support

In Databricks Runtime 11.3 LTS ML and above, if AutoML detects an imbalanced dataset, it reduces imbalance in the **training** dataset by downsampling the majority class(es) and adding class weights. The test and validation datasets are not balanced, ensuring performance evaluation reflects the true class distribution. ^[data-preparation-for-classification-databricks-on-aws.md]

Class weights are inversely related to the downsampling ratio. For example, if a training dataset has 95 samples of class A and 5 of class B, AutoML downsamples class A to 70 samples (ratio 0.736) while keeping class B at 5 samples. The class weight for class A is scaled up by 1/0.736 ≈ 1.358, while class B weight remains 1. These weights are passed as a parameter during model training. ^[data-preparation-for-classification-databricks-on-aws.md]

## Column Selection

In Databricks Runtime 10.3 ML and above, you can specify which columns AutoML should use for training. In the UI, uncheck the column in the **Include** column. In the API, use the `exclude_cols` parameter. You cannot drop the column selected as the prediction target or the time column used for splitting. By default, all columns are included. ^[data-preparation-for-classification-databricks-on-aws.md]

## Split Data into Train, Validation, and Test Sets

AutoML divides data into three splits for training, validation, and testing. Depending on the ML problem, different split methods are available. ^[data-preparation-for-classification-databricks-on-aws.md]

### Random Split (Default)

If no data split strategy is specified, the dataset is randomly split into 60% train, 20% validate, and 20% test. For classification, a stratified random split ensures each class is adequately represented across all three splits. ^[data-preparation-for-classification-databricks-on-aws.md]

### Chronological Split

In Databricks Runtime 10.4 LTS ML and above, you can select a time column to create chronological splits: earliest data for training, next for validation, latest for testing. The time column can be a timestamp, integer, or string column. ^[data-preparation-for-classification-databricks-on-aws.md]

### Manual Split

In Databricks Runtime 15.3 ML and above, you can use the API to set up a manual split. Specify a split column with values `train`, `validate`, or `test` to identify rows for each dataset. Rows with other values are ignored and a corresponding alert is raised. ^[data-preparation-for-classification-databricks-on-aws.md]

## Sampling Large Datasets

Although AutoML distributes hyperparameter tuning trials across worker nodes, each model is trained on a single worker node. AutoML automatically estimates the memory required to load and train the dataset and samples if necessary. For classification, AutoML uses PySpark’s `sampleBy` method for stratified sampling to preserve the target label distribution. For regression, it uses the PySpark `sample` method. ^[data-preparation-for-classification-databricks-on-aws.md]

## Semantic Type Detection

With Databricks Runtime 9.1 LTS ML and above, AutoML attempts to detect semantic types that differ from the Spark or pandas data type. It treats string and integer columns representing dates/timestamps as timestamp types, and string columns representing numeric data as numeric types. With Databricks Runtime 10.1 ML and above, it also treats numeric columns containing categorical IDs as categorical features, and string columns containing English text as text features. These detections are best-effort and may miss some semantic types. ^[data-preparation-for-classification-databricks-on-aws.md]

### Semantic Type Annotations

With Databricks Runtime 10.1 ML and above, you can manually control the assigned semantic type by placing an annotation on a column using `df.withMetadata()`. The `spark.contentAnnotation.semanticType` can be set to `categorical`, `numeric`, `datetime`, or `text`. To disable semantic type detection on a column, use the special keyword `native`. ^[data-preparation-for-classification-databricks-on-aws.md]

> **Note:** AutoML does not perform semantic type detection for columns that have custom imputation methods specified.

## Sources

- data-preparation-for-classification-databricks-on-aws.md

# Citations

1. [data-preparation-for-classification-databricks-on-aws.md](/references/data-preparation-for-classification-databricks-on-aws-23ffa2ac.md)
